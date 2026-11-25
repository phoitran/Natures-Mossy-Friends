#!/usr/bin/env python3
"""Generate fifteen precise original pastel winter craft diagrams.
Run: python3 scripts/generate-winter-diagrams.py
Reads catalogue metadata and writes only WIN-06–08 instruction SVGs.
"""
from pathlib import Path
import math, json, html, random

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/assets/steps'
W,H=960,630
INK='#61483a'; DARK='#3c5240'; RED='#c76f5b'; GOLD='#ecae3c'; GREEN='#879b4e'; CREAM='#fff7e6'; PINK='#f1b198'; BLUE='#8eb6bd'
def esc(v):return html.escape(str(v))
def grp(s,t='',attrs=''):return f'<g'+(f' transform="{t}"' if t else '')+f' {attrs}>{s}</g>'
def path(d,fill='none',stroke=INK,sw=4,attrs=''):return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {attrs}/>'
def line(x,y,X,Y,c=INK,w=4,attrs=''):return f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" {attrs}/>'
def ellipse(x,y,rx,ry,c=CREAM,stroke=INK,sw=3,attrs=''):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" stroke="{stroke}" stroke-width="{sw}" {attrs}/>'
def circle(x,y,r,c=CREAM,stroke=INK,sw=3,attrs=''):return ellipse(x,y,r,r,c,stroke,sw,attrs)
def rect(x,y,w,h,c=CREAM,stroke=INK,sw=3,r=12,attrs=''):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}" stroke="{stroke}" stroke-width="{sw}" {attrs}/>'
def text(x,y,t,size=28,anchor='middle',c=DARK,weight=600):return f'<text x="{x}" y="{y}" font-family="Trebuchet MS, DejaVu Sans, Arial, sans-serif" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{c}">{esc(t)}</text>'
def arrow(x,y,X,Y,bend=0):
 return path(f'M{x} {y} Q{(x+X)/2+bend} {(y+Y)/2-bend} {X} {Y}',stroke=RED,sw=5,attrs='marker-end="url(#arrow)"')
def note(x,y,t,anchor='middle',size=27):return text(x,y,t,size,anchor,DARK,600)
def dash(d,c='#c5a67b',w=3):return path(d,stroke=c,sw=w,attrs='stroke-dasharray="8 10"')
def header(t,sub=''):
 return text(480,58,t,34,weight=700)+(text(480,98,sub,24,c='#7e7760',weight=500) if sub else '')
def footer(t):return text(480,588,t,28 if len(t)<50 else 25,weight=700)
def sparkle(x,y,s=1,c=GOLD):return path('M0 -13 Q3 -3 13 0 Q3 3 0 13 Q-3 3 -13 0 Q-3 -3 0 -13 Z',c,c,1).replace('<path',f'<path transform="translate({x} {y}) scale({s})"',1)
def background():return '<rect width="960" height="630" fill="#fffaf3"/>'+path('M0 495 Q130 450 223 505 Q360 550 493 505 Q720 455 960 502 L960 630 L0 630 Z','#eee7f2','none',0)+ellipse(800,170,130,70,'#f9e3db','none',0)+ellipse(130,280,120,85,'#e6f0df','none',0)
def paper(x,y,w,h,ang=0):
 s=path(f'M{-w/2} {-h/2+8} L{w/2-9} {-h/2} L{w/2} {h/2-5} L{-w/2+6} {h/2} Z','#fff8e8','#d5c4a4',3)
 for i in range(16):
  rx=(-.43+(i*17%31)/36)*w;ry=(-.43+(i*13%29)/34)*h
  s+=line(rx,ry,rx+4,ry+1,'#e8dbc4',1.4)
 return grp(s,f'translate({x} {y}) rotate({ang})')
LEAFPATH={
 'round':'M0 -94 C75 -87 80 65 0 94 C-80 65 -75 -87 0 -94 Z',
 'oval':'M0 -100 C52 -83 69 -34 48 17 C35 49 9 78 0 100 C-26 81 -57 47 -59 10 C-65 -42 -40 -82 0 -100 Z',
 'oak':'M0 -100 C24 -87 6 -65 30 -68 C59 -67 50 -38 35 -31 C73 -43 78 -9 51 6 C83 17 63 48 38 43 C57 77 20 81 0 100 C-20 81 -57 77 -38 43 C-63 48 -83 17 -51 6 C-78 -9 -73 -43 -35 -31 C-50 -38 -59 -67 -30 -68 C-6 -65 -24 -87 0 -100 Z',
 'maple':'M0 -105 L22 -63 L46 -77 L42 -29 L89 -44 L74 -7 L100 7 L49 35 L58 62 L18 65 L0 105 L-18 65 L-58 62 L-49 35 L-100 7 L-74 -7 L-89 -44 L-42 -29 L-46 -77 L-22 -63 Z',
 'point':'M0 -112 C10 -76 55 -61 49 -16 L62 4 L40 23 L43 49 L20 64 L0 105 L-20 64 L-43 49 L-40 23 L-62 4 L-49 -16 C-55 -61 -10 -76 0 -112 Z'
}
def leaf(x,y,s=1,angle=0,col='gold',kind='oval',shadow=True):
 d=LEAFPATH[kind];a=''
 if shadow:a+=path(d,'#9b825a22','none',0,attrs='transform="translate(4 7)"')
 a+=path(d,f'url(#{col})',INK,3.7)
 a+=path('M0 -86 Q-5 -28 0 27 Q4 75 0 119',stroke='#76533c',sw=3)
 for yy,l in [(-55,19),(-30,34),(-3,39),(25,30),(50,18)]:
  a+=path(f'M0 {yy+12} Q{-l*.6} {yy} {-l} {yy-12} M0 {yy+12} Q{l*.6} {yy} {l} {yy-12}',stroke='#8c643c',sw=2)
 a+=path('M-17 -69 Q-37 -37 -31 -14',stroke='#fff6bd77',sw=5)
 return grp(a,f'translate({x} {y}) rotate({angle}) scale({s})')
def twig(x1,y1,x2,y2,w=15):
 d=f'M{x1} {y1} Q{(x1+x2)/2+3} {(y1+y2)/2-3} {x2} {y2}'
 a=path(d,stroke=INK,sw=w+4)+path(d,stroke='#ac7a4e',sw=w)+path(d,stroke='#d5a26b',sw=max(2,w*.22),attrs='transform="translate(-1 -2)"')
 for t in [.23,.61,.82]:
  x=x1+(x2-x1)*t;y=y1+(y2-y1)*t
  a+=line(x-3,y-3,x+3,y+3,'#855737',2)
 return a

def stone(x,y,s=1,ang=0,col='#b1b4a4'):
 a=path('M-45 0 C-46 -25 -24 -39 6 -33 C34 -34 51 -16 45 6 C41 28 11 37 -19 28 C-37 26 -49 15 -45 0 Z',col,'#6e7b6d',3)
 a+=path('M-29 -9 Q-13 -27 15 -23',stroke='#e2e2cc',sw=5)+circle(25,10,2,'#8d9386','none',0)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def pine(x,y,s=1,ang=0):
 a=path('M0 -82 C36 -59 47 -18 41 34 C36 68 17 83 0 86 C-27 78 -44 57 -43 26 C-49 -19 -31 -62 0 -82 Z','#886041',INK,3)
 for row in range(5):
  yy=-55+row*27
  for xx in ([-13,13] if row%2==0 else [-24,0,24]):
   a+=path(f'M{xx-15} {yy-2} Q{xx} {yy-14} {xx+15} {yy-2} Q{xx+12} {yy+18} {xx} {yy+24} Q{xx-12} {yy+18} {xx-15} {yy-2} Z','#bf8952',INK,2)
   a+=path(f'M{xx-9} {yy+1} Q{xx} {yy-4} {xx+8} {yy+1}',stroke='#e8b371',sw=2)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def eye(x,y,r=20,look=0):
 return circle(x,y,r,'#fffdf4',INK,2.5)+circle(x+look,y+3,r*.42,'#35433b','none',0)+circle(x+look-r*.12,y-r*.08,r*.13,'#fff','none',0)
def smile(x,y,w=25):return path(f'M{x-w} {y} Q{x} {y+w*.8} {x+w} {y}',stroke=INK,sw=3.5)
def cheek(x,y,s=1):return ellipse(x,y,11*s,6*s,'#ed927a99','none',0)
def hand(x,y,s=1,ang=0):
 # Gentle pointing adult hand: broad finger and cuff, not a tool.
 a=path('M-43 39 L-43 2 Q-43 -11 -30 -10 L-12 -3 L-12 -56 Q-12 -74 2 -73 Q15 -72 15 -55 L15 -14 Q24 -27 35 -17 Q44 -28 53 -16 Q66 -20 70 -6 L73 38 Q68 65 42 72 L-15 72 Q-36 64 -43 39 Z','#e8b88f',INK,3)
 a+=line(15,-14,15,21,'#b77e59',2)+line(35,-13,35,22,'#b77e59',2)+line(53,-11,53,20,'#b77e59',2)+rect(-19,68,66,29,'#91a56c',INK,3,4)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def camera(x,y,s=1):
 a=rect(-54,-34,108,76,'#a4b99d',INK,3,15)+rect(-35,-47,30,17,'#a4b99d',INK,3,5)+circle(0,4,26,CREAM,INK,3)+circle(0,4,17,BLUE,INK,3)+circle(34,-17,5,GOLD,INK,2)
 return grp(a,f'translate({x} {y}) scale({s})')
def soil(x,y,rx,ry):
 a=ellipse(x,y,rx,ry,'#cfa676','#97704d',3)
 rng=random.Random(41)
 for _ in range(25):
  px=x+rng.uniform(-.87,.87)*rx;py=y+rng.uniform(-.75,.75)*ry
  if ((px-x)/rx)**2+((py-y)/ry)**2<.9:a+=circle(px,py,rng.uniform(2,4),'#b58a60','none',0)
 return a

def leaf_owl(x,y,s=1,stage=5,facekind='paper'):
 a=leaf(0,70,.85,0,'gold','oak')+leaf(0,-67,.62,0,'orange','maple')
 if stage>=3:
  a+=leaf(-73,50,.65,-24,'red','point')+leaf(73,50,.65,24,'red','point')
  a+=leaf(-39,-125,.34,-25,'green','point')+leaf(39,-125,.34,25,'green','point')
 if stage>=4:
  if facekind=='paper':a+=eye(-27,-63,24,-1)+eye(27,-63,24,-1)
  else:a+=stone(-25,-62,.32,0,'#e0dec9')+stone(25,-62,.32,0,'#e0dec9')
  a+=path('M-9 -35 L9 -35 L0 -18 Z',GOLD,INK,2)
  a+=twig(-27,142,-38,176,7)+twig(27,142,38,176,7)+twig(-38,176,-56,178,6)+twig(38,176,56,178,6)
  a+=cheek(-51,-29,.9)+cheek(51,-29,.9)
 if stage>=5:a+=leaf(0,-141,.26,30,'gold','oval')+sparkle(-116,-60,.6)+sparkle(120,70,.7)
 return grp(a,f'translate({x} {y}) scale({s})')


DEFS='<defs>\n<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f8e29a"/><stop offset=".55" stop-color="#ebca72"/><stop offset="1" stop-color="#d6a959"/></linearGradient>\n<linearGradient id="red" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f0b3a1"/><stop offset=".5" stop-color="#dd9583"/><stop offset="1" stop-color="#c97467"/></linearGradient>\n<linearGradient id="orange" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f6d2a1"/><stop offset=".55" stop-color="#edb181"/><stop offset="1" stop-color="#d98f67"/></linearGradient>\n<linearGradient id="green" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c4d8ac"/><stop offset=".6" stop-color="#a6bf8a"/><stop offset="1" stop-color="#7fa16c"/></linearGradient>\n<marker id="arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="7" markerHeight="7" orient="auto"><path d="M2 2 L10 6 L2 10" fill="none" stroke="#d75b38" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></marker>\n<clipPath id="roofclip"><path d="M-165 -35 L149 -35 L218 -151 L-84 -151 Z"/></clipPath>\n</defs>'

CURRENT_STEP=1
SNOW='#fffef9'; SNOWLINE='#8b9fa7'; ICE='#dce9ed'
def header(t,sub=''):
 return circle(45,49,22,'#dce9ef',INK,2)+text(45,58,CURRENT_STEP,25,weight=700)+text(493,58,t,32,weight=700)+(text(480,98,sub,23,c='#647665',weight=500) if sub else '')
def winter_background():
 return '<rect width="960" height="630" fill="#fcfbf6"/>'+path('M0 485 Q146 452 264 486 Q453 526 623 477 Q794 452 960 486 L960 630 L0 630 Z','#e8e6f3','none',0)+ellipse(786,189,130,73,'#f6e4de','none',0)+ellipse(137,287,116,83,'#e5efdf','none',0)
def snowflake(x,y,s=1):
 a=''
 for i in range(3):
  t=i*math.pi/3;a+=line(math.cos(t)*-22,math.sin(t)*-22,math.cos(t)*22,math.sin(t)*22,'#a8c4cc',3)
 return grp(a,f'translate({x} {y}) scale({s})')
def ground(x=480,y=479,rx=362,ry=67):
 a=ellipse(x,y,rx,ry,'#eef4f3','#b5c8ca',2.5)
 for xx,yy in [(-.7,.1),(-.45,-.42),(.12,.39),(.42,-.3),(.72,.21)]:a+=path(f'M{x+xx*rx-13} {y+yy*ry} Q{x+xx*rx} {y+yy*ry+4} {x+xx*rx+13} {y+yy*ry}',stroke='#d0e0e0',sw=3)
 return a

def snowball(x,y,rx,ry=None):
 if ry is None:ry=rx
 a=path(f'M{-rx} 0 C{-rx*1.03} {-ry*.56} {-rx*.5} {-ry*1.03} 0 {-ry} C{rx*.6} {-ry*1.03} {rx*1.02} {-ry*.45} {rx} 0 C{rx*.98} {ry*.61} {rx*.5} {ry*.96} 0 {ry} C{-rx*.58} {ry*.96} {-rx*1.04} {ry*.58} {-rx} 0 Z',SNOW,SNOWLINE,3)
 a+=path(f'M{-rx*.74} {ry*.08} Q{-rx*.56} {ry*.7} {-rx*.02} {ry*.76}',stroke='#dce9ed',sw=7)
 for xx,yy in [(-.38,-.55),(.3,-.41),(.54,.14),(-.12,.48)]:a+=circle(xx*rx,yy*ry,2,'#b7cbd1','none',0)
 return grp(a,f'translate({x} {y})')
def mitten(x,y,s=1,ang=0,col='#e5bbad'):
 a=path('M-32 51 L-36 -6 Q-40 -52 -6 -65 Q30 -75 40 -38 L43 -9 Q57 -30 73 -16 Q82 -6 67 19 L44 47 L36 70 L-25 70 Z',col,INK,3)
 a+=rect(-29,60,68,30,'#a3b58e',INK,3,7)+line(-15,63,-15,88,'#d1dec0',2)+line(1,63,1,88,'#d1dec0',2)+line(17,63,17,88,'#d1dec0',2)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def snow_eye(x,y,s=1):return stone(x,y,.17*s,0,'#69756b')+ellipse(x-2*s,y-2*s,2.5*s,1.5*s,'#e1e6d8','none',0)
def twig_smile(x,y,w=35):
 return grp(path(f'M{-w/2} 0 Q0 {w*.45} {w/2} 0',stroke=INK,sw=6)+path(f'M{-w/2} 0 Q0 {w*.45} {w/2} 0',stroke='#ad855e',sw=3),f'translate({x} {y})')
def snowperson(x,y,s=1,stage=5,balls=2,lean=0):
 a=''
 if stage>=4:
  shoulder_y=12 if balls==2 else 2
  a+=twig(-48,shoulder_y,-119,shoulder_y-34,8)+twig(49,shoulder_y,119,shoulder_y-39,8)
  a+=twig(-111,shoulder_y-30,-125,shoulder_y-57,5)+twig(110,shoulder_y-34,128,shoulder_y-53,5)
 a+=snowball(0,65,89,77)
 if stage>=3:
  if balls==3:a+=snowball(0,-35,60,53)+snowball(lean,-111,41,38);fy=-111
  else:a+=snowball(lean,-42,57,53);fy=-42
  # Little packed-snow seam makes the two joined forms visibly continuous.
  a+=path(f'M-28 {-6 if balls==2 else -73} Q0 {3 if balls==2 else -65} 28 {-6 if balls==2 else -73}',stroke='#cfdee1',sw=4)
  if stage>=4:
   a+=snow_eye(lean-18,fy-7,1.1)+snow_eye(lean+18,fy-7,1.1)+twig_smile(lean,fy+16,36)
   if stage>=5:a+=leaf(lean+2,fy-54,.28,74,'green','oval')
 return grp(a,f'translate({x} {y}) scale({s})')

def carrot(x,y,s=1,ang=0):
 a=path('M-10 -10 Q0 -17 10 -9 L0 31 Z','#e9a36b',INK,2)+line(-5,0,4,2,'#c47c4d',2)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def boot(x,y,s=1,flip=False):
 a=path('M-19 22 L-19 -47 Q-19 -56 -30 -57 L-44 -57 Q-58 -58 -58 -70 Q-57 -80 -41 -81 L19 -81 L19 22 Z','#d8897e',INK,3)
 a+=rect(-61,-88,83,12,'#a85454',INK,2,4)+line(-7,-51,-7,15,'#eab76a',7)+line(5,-51,5,15,'#91af9a',7)
 return grp(a,f'translate({x} {y}) scale({-s if flip else s} {s})')
def reference_snowman(x,y,s=1,kind='pine'):
 if kind=='upside':
  a=twig(-43,-22,-124,26,7)+twig(43,-22,124,30,7)
  a+=snowball(0,82,73,66)+snowball(0,-24,63,57)+snowball(0,-152,90,84)
  a+=snow_eye(-23,75,1)+snow_eye(23,75,1)+carrot(0,91,.8)+twig_smile(0,57,43)
  a+=path('M-52 30 Q0 43 52 30 L51 45 Q0 58 -51 45 Z','#657168',INK,2)+path('M-25 46 L-43 90 L-28 97 L-9 49 Z','#657168',INK,2)
  for yy in [-50,-22,6]:a+=snow_eye(0,yy,.9)
  a+=boot(-43,-250,.8)+boot(43,-250,.8,True)
 elif kind=='classic':
  a=snowperson(0,0,1,4,3)+carrot(0,-105,.68,-63)
  for yy in [-46,-17,20,62]:a+=snow_eye(0,yy,.8)
 else:
  a=twig(-56,50,-125,91,8)+twig(53,48,123,67,8)
  a+=path('M-103 142 Q-99 62 -57 -9 Q-43 -53 0 -56 Q46 -55 59 -8 Q97 61 103 142 Z',SNOW,SNOWLINE,3)+snowball(0,-40,54,53)
  a+=snow_eye(-17,-47,1)+snow_eye(17,-47,1)+twig_smile(0,-23,35)+pine(0,-107,.22,5)
  for xx,yy in [(-63,77),(21,30),(55,101)]:a+=circle(xx,yy,2,'#b7cbd1','none',0)
 return grp(a,f'translate({x} {y}) scale({s})')

def little_snowman(n):
 titles=['Find snow that sticks together','Pat a sturdy little base','Add a smaller head','Give your snow person a face','Meet your little snow friend']
 subs=['Dress warmly and test clean snow with a grown-up.','A hand-sized friend starts with a broad, steady base.','Pack a little snow around the join to steady it.','Pebble eyes, a twig smile and two short arms.','A pine-cone hat, a carrot nose or a funny upside-down pose.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=ground(480,483,298,47)+snowball(481,311,80,75)+mitten(325,340,.87,33)+mitten(639,340,.87,-35)
  a+=arrow(320,234,392,281,-10)+arrow(651,238,569,280,10)+note(480,486,'Does a handful hold together?',size=26)+snowflake(216,173,.65)+snowflake(756,198,.6)
 elif n==2:
  a+=ground(480,477,318,60)+snowperson(480,338,1.08,2)+mitten(312,363,.68,57)+arrow(334,302,412,373,10)
  a+=note(763,290,'Keep it small',size=25)+note(762,325,'and steady',size=25)+arrow(714,350,574,448,-12)
 elif n==3:
  a+=ground(476,491,342,52)+snowperson(408,344,1.04,3,2)+arrow(402,172,402,225,0)+mitten(526,242,.53,-56)
  a+=snowperson(757,386,.65,3,3)+note(751,524,'Optional third ball',size=23)+note(240,257,'Small head',size=25)+arrow(263,275,347,292,10)
 elif n==4:
  a+=ground(480,491,347,49)+snowperson(430,342,1.06,4,2)
  a+=pine(177,233,.36)+arrow(222,270,426,235,-16)+note(171,333,'Pine-cone hat',size=24)
  a+=carrot(664,245,1,-55)+arrow(624,265,451,310,12)+note(684,313,'Carrot nose',size=23)
  a+=reference_snowman(767,428,.31,'upside')+note(765,511,'Or upside down!',size=22)
 else:
  a+=ground(480,488,411,44)+reference_snowman(211,343,.87,'pine')+reference_snowman(478,346,.88,'classic')+reference_snowman(757,379,.65,'upside')
  a+=note(211,521,'Pine-cone hat',size=24)+note(478,521,'Carrot nose',size=24)+note(757,521,'Upside-down boots',size=24)+camera(850,171,.4)
 a+=footer(['Powdery snow can wait for a stickier day.','Flatten the bottom so it sits on the ground.','Keep the whole stack low. Ask for help if needed.','Try a hat or carrot; ask for help with upside-down friends.','Take a picture, gather loose pieces and warm up inside.'][n-1])
 return a

# The cottage is a solid snow shape. Its door is only a shallow surface line.
def cottage(x,y,s=1,stage=5):
 a=path('M-110 -10 L65 -10 L65 135 Q-24 144 -110 135 Z',SNOW,SNOWLINE,3)
 a+=path('M65 -10 L155 -45 L155 99 L65 135 Z','#eef5f3',SNOWLINE,3)
 a+=path('M-110 -10 L-20 -80 L65 -10 Z',SNOW,SNOWLINE,3)
 a+=path('M-110 -10 L-20 -80 L70 -115 L-20 -45 Z','#f8fcf7',SNOWLINE,3)
 a+=path('M-20 -80 L70 -115 L155 -45 L65 -10 Z','#e4eff0',SNOWLINE,3)
 a+=path('M-96 117 Q-25 126 52 117',stroke='#dae8e9',sw=5)
 for xx,yy in [(-76,28),(-24,9),(28,41),(99,38),(121,74)]:a+=circle(xx,yy,2,'#b7cbd1','none',0)
 if stage>=3:
  # Each stick is physically supported by the solid sloping snow beneath it.
  for j in range(5,-1,-1):
   t=j/5;ridge=(-20+90*t,-80-35*t)
   left=(-110+90*t,-10-35*t);right=(65+90*t,-10-35*t)
   a+=twig(*ridge,*left,8)+twig(*ridge,*right,8)
   for end in [left,right]:
    p=(ridge[0]+(end[0]-ridge[0])*.34,ridge[1]+(end[1]-ridge[1])*.34);q=(ridge[0]+(end[0]-ridge[0])*.56,ridge[1]+(end[1]-ridge[1])*.56)
    a+=line(*p,*q,SNOW,5)
 if stage>=4:
  a+=path('M-52 132 L-52 88 Q-26 62 0 88 L0 132',stroke='#9aadb3',sw=3)
  a+=stone(-63,139,.23)+stone(-43,148,.21)+stone(-12,148,.2)+stone(11,138,.23)
 return grp(a,f'translate({x} {y}) scale({s})')
def snowy_path(points,stones=True):
 d='M'+' '.join(f'{x} {y}' if i==0 else f'L{x} {y}' for i,(x,y) in enumerate(points))
 a=path(d,stroke='#b4c8cc',sw=7)+path(d,stroke='#e3eef0',sw=3)
 if stones:
  for i,(x,y) in enumerate(points[1:-1]):a+=stone(x+(14 if i%2 else -14),y+10,.19,i*12)
 return a

def sprig(x,y,s=1,dry=False):
 col='#a18a63' if dry else '#799766';a=line(0,10,0,-67,col,5)
 for yy,wide in [(-14,35),(-34,28),(-53,18)]:
  a+=line(0,yy,-wide,yy-25,col,4)+line(0,yy,wide,yy-26,col,4)
  if dry:a+=circle(-wide,yy-25,6,'#c4aa6d',col,2)+circle(wide,yy-26,6,'#c4aa6d',col,2)
  else:
   for side in [-1,1]:a+=line(side*wide*.5,yy-12,side*wide*.8,yy-7,col,3)+line(side*wide*.7,yy-18,side*wide*.6,yy-30,col,3)
 return grp(a,f'translate({x} {y}) scale({s})')
def round_house(x,y,s=1,stage=5,dry=False):
 a=path('M-100 70 Q-104 2 -82 -36 Q-69 -61 0 -63 Q73 -60 86 -31 Q103 13 100 70 Q0 100 -100 70 Z',SNOW,SNOWLINE,3)
 a+=ellipse(0,-48,74,19,'#f6faf9','#d0dfe0',2)+path('M-81 61 Q-11 82 72 66',stroke='#dae8e9',sw=5)
 if stage>=3:a+=sprig(0,-61,.8,dry)
 if stage>=4:a+=path('M-26 83 L-26 43 Q0 12 26 43 L26 83',stroke='#a6bac0',sw=3)
 return grp(a,f'translate({x} {y}) scale({s})')
def snow_castle(x,y,s=1,stage=5):
 a=''
 # Low snow blocks and two broad towers, with surface door lines.
 for xx,yy,w,h in [(-112,-1,76,108),(35,-26,76,132),(-38,25,75,82)]:
  a+=rect(xx,yy,w,h,SNOW,SNOWLINE,3,7)
  if stage>=3:
   for u in [0,28,56]:a+=rect(xx+u,yy-19,20,24,SNOW,SNOWLINE,2,3)
 if stage>=4:
  a+=path('M-20 107 L-20 65 Q0 42 20 65 L20 107',stroke='#a6bac0',sw=3)
  a+=stone(-41,122,.25)+stone(0,133,.27)+stone(40,122,.25)
 return grp(a,f'translate({x} {y}) scale({s})')
def twig_path(points):
 a=snowy_path(points,False)
 for i,(x,y) in enumerate(points):
  for sign in [-1,1]:a+=twig(x+sign*16,y,x+sign*16+2,y-22,4)
 return a

def village(n):
 titles=['Plan a tiny winter village','Try three snowy house shapes','Give each roof its character','Mark doors and connect the houses','Tell a little snowy village story']
 subs=['Choose flat, packable snow and room for a few paths.','A peaked cottage, rounded houses or a low snow castle.','Twigs, sprigs or snow turrets: choose a different look.','Doors are surface marks; paths connect the little homes.','Make every tiny winter world different.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=ground(480,374,363,160)
  for x,y in [(311,331),(617,303),(588,446)]:a+=dash(f'M{x-67} {y-29} Q{x-73} {y-55} {x} {y-57} Q{x+72} {y-54} {x+65} {y-24} Q{x+62} {y+32} {x} {y+33} Q{x-68} {y+30} {x-67} {y-29}', '#9cb2b9',3)
  a+=snowy_path([(334,383),(398,412),(491,400),(562,346)],False)+twig(754,217,800,338,9)+stone(167,367,.4)+stone(195,412,.36)+note(477,532,'Leave space between the houses',size=25)
 elif n==2:
  a+=ground(480,468,397,57)+cottage(203,350,.66,2)+round_house(493,374,.83,2)+snow_castle(773,357,.8,2)
  a+=note(213,203,'Pinch a roof ridge',size=24)+arrow(215,222,203,282,0)
  a+=note(496,242,'Round and flat-topped',size=23)+arrow(493,260,493,320,0)
  a+=note(774,224,'Low blocks',size=24)+arrow(773,242,773,350,0)
  a+=note(480,522,'Pack a cup or container, then turn it out.',size=24)
 elif n==3:
  a+=ground(480,462,402,50)+cottage(202,344,.7,3)+round_house(491,365,.88,3)+snow_castle(778,344,.79,3)
  a+=note(215,194,'Twig slopes',size=24)+arrow(213,211,209,267,0)
  a+=note(489,195,'Loose sprigs',size=24)+arrow(488,212,489,260,0)
  a+=note(778,225,'Snow turrets',size=24)+arrow(776,242,767,302,0)
  a+=note(480,522,'Solid snow supports the roof details.',size=25)
 elif n==4:
  a+=ground(480,469,397,78)+round_house(277,335,.9,4)+round_house(674,367,.8,4,True)
  a+=twig_path([(278,418),(336,452),(400,479),(463,489),(534,470),(590,452),(674,443)])
  a+=note(480,200,'A shallow door mark',size=24)+arrow(450,221,279,386,14)
  a+=stone(399,507,.24)+stone(427,513,.23)+note(742,509,'Twigs or stones',size=22)
 else:
  a+=ground(480,458,420,72)+cottage(153,350,.61,5)
  a+=round_house(440,343,.57,5)+round_house(371,407,.48,5)+round_house(526,407,.47,5,True)
  a+=twig_path([(438,398),(440,435),(420,469),(396,495)])+twig_path([(440,435),(491,451),(526,446)])
  a+=snow_castle(770,352,.61,5)
  a+=snowy_path([(757,429),(725,469),(771,489),(822,470)],True)
  a+=twig(713,447,715,403,5)+twig(741,446,743,402,5)+twig(714,404,744,404,5)
  a+=note(170,529,'Twig-roof cottage',size=22)+note(456,529,'Round snowy homes',size=22)+note(773,529,'Snow-block village',size=22)+camera(851,184,.43)
 a+=footer(['Two or three hand-sized houses are plenty.','Keep the bases broad and every building solid.','Use loose natural pieces and keep rocks on the ground.','Mark the route with short twigs or smooth stones.','Photograph the village, gather decorations and warm up.'][n-1])
 return a

# Snow animals remain low: mouse snout, broad rabbit joints, flat turtle flippers.
def snow_mouse(x,y,s=1,stage=5):
 a=snowball(0,40,115,70)
 if stage>=3:a+=snowball(107,61,43,31)+path('M82 48 Q92 43 103 39',stroke='#dce9ed',sw=4)
 if stage>=4:
  a+=stone(55,-20,.5,72,'#929ba0')+stone(92,-16,.48,104,'#929ba0')
  a+=snow_eye(97,47,1)+stone(142,64,.18,0,'#69756b')
  for yy in [65,72]:a+=line(132,yy,165,yy-8,'#91a375',2.5)+line(125,yy,150,yy+11,'#91a375',2.5)
  a+=path('M-104 57 Q-157 92 -178 67',stroke='#a3b385',sw=4)
 return grp(a,f'translate({x} {y}) scale({s})')
def snow_rabbit(x,y,s=1,stage=5):
 a=snowball(0,57,83,79)+snowball(-71,96,34,26)
 if stage>=3:a+=snowball(42,-28,57,48)+path('M13 12 Q42 26 66 10',stroke='#dce9ed',sw=4)
 if stage>=4:
  a+=snowball(20,-107,20,65)+snowball(63,-100,21,62)+path('M20 -152 L20 -85 M63 -143 L63 -80',stroke='#ead3ce',sw=6)
  a+=snow_eye(52,-29,1)+stone(93,-14,.18,0,'#69756b')+twig_smile(70,5,22)
 return grp(a,f'translate({x} {y}) scale({s})')
def snow_turtle(x,y,s=1,stage=5):
 a=''
 if stage>=3:
  for xx,yy in [(-77,19),(76,16),(-70,92),(75,89)]:a+=snowball(xx,yy,34,17)
  a+=snowball(3,-27,32,26)
 a+=snowball(0,50,84,65)
 if stage>=4:
  a+=snow_eye(-8,-33,.85)+snow_eye(13,-33,.85)
  a+=path('M-30 28 Q0 8 30 28 L26 73 Q0 92 -26 73 Z M0 17 L0 -9 M-28 48 L-77 45 M28 48 L77 45 M-16 81 L-37 104 M16 81 L37 104',stroke='#a4bdc4',sw=3)
 return grp(a,f'translate({x} {y}) scale({s})')
def snow_cat(x,y,s=1,carved=False,stage=5):
 a=path('M-55 83 Q-102 57 -90 8 Q-82 -17 -67 -3 Q-57 4 -60 19 Q-81 54 -45 64',SNOW,SNOWLINE,10)
 a+=snowball(0,49,66,83)
 if stage>=3:
  a+=snowball(0,-48,57,50)+snowball(-38,115,30,17)+snowball(36,115,30,17)
  a+=path('M-46 -78 L-42 -118 L-9 -88 M9 -88 L43 -117 L48 -76',SNOW,SNOWLINE,3)
 if stage>=4:
  if carved:
   a+=path('M-34 -47 Q-22 -58 -10 -46 M10 -46 Q22 -58 34 -47 M-10 -28 L0 -19 L10 -28 M0 -19 L0 -5 M-21 -8 Q0 6 21 -8',stroke='#a4bdc4',sw=3)
   for v in [-1,1]:a+=path(f'M{v*11} -17 L{v*42} -25 M{v*12} -7 L{v*43} -8',stroke='#a4bdc4',sw=2.5)
  else:
   a+=leaf(-37,-96,.2,-31,'gold','oval')+leaf(36,-96,.2,28,'gold','oval')+snow_eye(-20,-49,1)+snow_eye(20,-49,1)+stone(0,-29,.15,0,'#69756b')
   for v in [-1,1]:a+=line(v*10,-17,v*58,-32,'#a8876a',3)+line(v*10,-12,v*60,-12,'#a8876a',3)
  a+=path('M-23 31 L-23 108 M23 31 L23 108',stroke='#c1d3d7',sw=3)
 return grp(a,f'translate({x} {y}) scale({s})')
def snow_bear(x,y,s=1,stage=5):
 a=snowball(0,46,73,83)+snowball(-61,26,30,44)+snowball(61,26,30,44)+snowball(-39,111,32,23)+snowball(39,111,32,23)
 if stage>=3:a+=snowball(-37,-95,24,23)+snowball(37,-95,24,23)+snowball(0,-54,60,53)
 if stage>=4:
  a+=snowball(0,-34,29,23)+snow_eye(-23,-68,1)+snow_eye(23,-68,1)+stone(0,-42,.19,0,'#69756b')+twig_smile(0,-22,23)
  for yy in [12,44,77]:a+=snow_eye(0,yy,.85)
 return grp(a,f'translate({x} {y}) scale({s})')

def snowy_friends(n):
 titles=['Choose a snowy creature','Build one low body','Shape the small parts and join them','Add ears, a face and gentle details','Introduce your snowy friends']
 subs=['Think about the biggest shape first.','A broad base helps a small snow shape stay steady.','Blend joins with extra snow. Shorten wobbly parts.','Long, pointed or round ears can give each friend its character.','Mice, rabbits, cats, a bear or a turtle: try your own.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=ground(480,474,394,54)+snow_mouse(223,354,.72,2)+snow_cat(491,347,.69,True,2)+snow_turtle(749,360,.73,2)
  a+=note(219,493,'Oval mouse',size=25)+note(490,493,'Seated animal',size=25)+note(748,493,'Low shell',size=25)+snowflake(165,190,.6)
 elif n==2:
  a+=ground(480,477,324,53)+snow_mouse(469,366,1.13,2)+mitten(290,371,.57,59)+mitten(660,364,.57,-62)
  a+=note(479,218,'Low and broad',size=28)+arrow(477,244,477,293,0)
 elif n==3:
  a+=ground(480,491,391,43)+snow_mouse(294,375,.93,3)+snow_turtle(704,378,.85,3)
  a+=mitten(444,337,.48,-65)+arrow(462,277,388,392,13)+note(270,244,'Pinch a snout',size=25)+note(727,242,'Flat flippers',size=25)+arrow(744,266,754,370,-10)
 elif n==4:
  a+=ground(480,478,404,60)+snow_mouse(176,379,.74,4)+snow_rabbit(457,369,.72,4)+snow_cat(765,371,.72,True,4)
  a+=note(177,208,'Small pebble ears',size=22)+arrow(213,228,225,352,-12)
  a+=note(477,182,'Long rabbit ears',size=22)+arrow(478,198,481,238,0)
  a+=note(774,235,'Carve a cat face',size=22)+arrow(772,252,767,333,0)+note(480,524,'A bear can have round ears; a turtle can have shell lines.',size=23)
 else:
  a+=ground(480,499,419,46)
  a+=snow_mouse(134,231,.42,5)+snow_mouse(234,258,.31,5)+note(182,326,'Little snow mice',size=22)
  a+=snow_rabbit(452,232,.48,5)+snow_rabbit(539,272,.28,5)+carrot(462,250,.55,-12)+note(486,326,'Rabbit friends',size=22)
  a+=snow_cat(738,240,.51,False,5)+snow_mouse(822,288,.18,5)+note(779,326,'Cat and mouse',size=22)
  a+=snow_cat(182,425,.57,True,5)+note(182,536,'Seated snow cat',size=22)
  a+=snow_bear(487,422,.59,5)+note(487,536,'Round-eared bear',size=22)
  a+=snow_turtle(782,436,.73,5)+note(782,536,'Flat snow turtle',size=22)
 a+=footer(['Dress warmly. Powdery snow can wait for another day.','Use handfuls of snow rather than lifting heavy pieces.','Keep heads and limbs close to the main body.','Ask a grown-up to help with taller ears and seated shapes.','Name them, photograph them and warm up inside.'][n-1])
 return a

CATALOGUE={a['id']:a for a in json.loads((ROOT/'content/activities.json').read_text())}
TASKS={'WIN-06':little_snowman,'WIN-07':village,'WIN-08':snowy_friends}
OUT.mkdir(parents=True,exist_ok=True)
for aid,draw in TASKS.items():
 activity=CATALOGUE[aid]
 for n,step in enumerate(activity['steps'],1):
  CURRENT_STEP=n;title=f'{activity["title"]} — step {n}: {step["title"]}'
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="630" viewBox="0 0 960 630" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(step["text"])}</desc>{DEFS}{winter_background()}{draw(n)}</svg>'
  (OUT/f'{aid}-{n}.svg').write_text(svg)
print('Generated fifteen pastel winter direction panels, WIN-06–08.')
