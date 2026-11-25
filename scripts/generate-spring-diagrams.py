#!/usr/bin/env python3
"""Generate twenty precise original pastel spring craft diagrams.
Run: python3 scripts/generate-spring-diagrams.py
Reads the catalogue for accessibility metadata; never edits it.
Crown method traced from the user-provided reference frames: cross under, wrap up, lay alongside.
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

# Spring additions: soft lilac, mint and peach; accurate illustrated material forms.
CURRENT_STEP=1
MUD='#ad805c'; MUDLIGHT='#c69d75'; STEM='#81a363'; TEAL='#58a89d'
def header(t,sub=''):
 return circle(45,49,22,'#dce9ce',INK,2)+text(45,58,CURRENT_STEP,25,weight=700)+text(493,58,t,32,weight=700)+(text(480,98,sub,23,c='#6c705a',weight=500) if sub else '')
def movement(d,c=RED):return path(d,stroke=c,sw=4,attrs='stroke-dasharray="8 7" marker-end="url(#arrow)"')
def stem(d,c=STEM,w=10):return path(d,stroke='#476543',sw=w+3)+path(d,stroke=c,sw=w)+path(d,stroke='#ffffff33',sw=2,attrs='transform="translate(-1 -1)"')
def tray(x=480,y=457,w=710,h=115):return ellipse(x,y,w/2,h/2,'#c0d1b1','#60765b',3)+ellipse(x,y-7,w/2-16,h/2-12,'#edf1dc','#8ba07c',2)
def bowl(x,y,s=1):
 a=path('M-106 0 Q-94 95 0 103 Q94 95 106 0 Z','#b3c5b2',INK,4)+ellipse(0,0,106,31,MUD,INK,3)
 for xx,yy in [(-62,-6),(-21,8),(26,-3),(65,4)]:a+=ellipse(xx,yy,13,5,MUDLIGHT,'none',0)
 return grp(a,f'translate({x} {y}) scale({s})')
def spoon(x,y,ang=0,s=1):
 a=path('M-10 0 L-7 -99 Q0 -116 7 -99 L10 0 Z','#bf956d',INK,3)+ellipse(0,22,27,40,'#cba67b',INK,3)+ellipse(0,22,19,28,'#a17c55','none',0)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def drop(x,y,s=1):return grp(path('M0 -30 C-10 -9 -20 7 -16 19 Q0 40 16 19 C20 7 10 -9 0 -30 Z','#b1d7da','#73999f',3),f'translate({x} {y}) scale({s})')
def dandelion(x,y,r=30,ang=0):
 a=''
 # Narrow yellow ray florets distinguish dandelions from daffodils or daisies.
 for layer,(scale,count,col) in enumerate([(1,24,'#efc957'),(.76,19,'#f7de79'),(.46,13,'#f4cc58')]):
  for i in range(count):
   t=i*360/count+layer*7
   a+=grp(ellipse(0,-r*.58*scale,r*.1*scale,r*.47*scale,col,'#c99c43',1),f'rotate({t})')
 a+=circle(0,0,r*.2,'#e7b746','#c99c43',1)
 return grp(a,f'translate({x} {y}) rotate({ang})')
def spring_flower(x,y,s=1,col='#eac5d4'):
 a=''
 for i in range(6):
  t=i*math.pi/3;a+=ellipse(math.sin(t)*17,-math.cos(t)*17,12,18,col,'#9d7e8c',2,attrs=f'transform="rotate({i*60} {math.sin(t)*17} {-math.cos(t)*17})"')
 a+=circle(0,0,10,'#f0d17a',INK,2)
 return grp(a,f'translate({x} {y}) scale({s})')
def grass(x,y,s=1,spread=1):
 a=''
 for i in range(7):
  endx=(i-3)*17*spread;endy=-55-22*(1-abs(i-3)/3)
  a+=path(f'M0 15 Q{endx*.24} {-30} {endx} {endy}',stroke=['#71966b','#8bad78','#a0b780'][i%3],sw=5)
 return grp(a,f'translate({x} {y}) scale({s})')
def mudball(x,y,rx,ry):
 a=path(f'M{-rx} 0 C{-rx} {-ry*.68} {-rx*.48} {-ry*1.04} 0 {-ry} C{rx*.6} {-ry*.96} {rx*1.06} {-ry*.48} {rx} 5 C{rx} {ry*.75} {rx*.55} {ry} 0 {ry} C{-rx*.62} {ry*.96} {-rx*1.04} {ry*.57} {-rx} 0 Z',MUD,INK,3.5)
 a+=path(f'M{-rx*.65} {-ry*.3} Q{-rx*.42} {-ry*.75} {-rx*.04} {-ry*.72}',stroke=MUDLIGHT,sw=8)
 for xx,yy in [(-.5,.3),(.4,-.4),(.65,.2),(-.15,.5)]:a+=circle(xx*rx,yy*ry,2.5,'#8f6749','none',0)
 return grp(a,f'translate({x} {y})')
def stoneeye(x,y,s=1):
 return stone(x,y,.30*s,0,'#6d7565')+ellipse(x-3*s,y-4*s,4*s,2.5*s,'#dee3ce','none',0)
def mudfriend(x,y,s=1,kind='bunny',finished=True):
 a=''
 if kind=='hedgehog':
  if finished:
   for i in range(9):
    t=i/8;a+=twig(-100+t*195,-25-22*math.sin(t*math.pi),-122+t*222,-85-42*math.sin(t*math.pi),8)
  a+=mudball(0,30,126,66)+mudball(104,57,44,33)
  if finished:a+=stoneeye(89,42,.9)+stone(144,57,.26,0,'#747b69')+smile(118,69,10)
 else:
  a+=mudball(0,46,93,74)
  if kind=='bunny':
   a+=mudball(0,-37,66,57)
   if finished:a+=leaf(-28,-114,.48,-17,'green','oval')+leaf(28,-114,.48,17,'green','oval')
  else:
   if finished:a+=grass(0,-34,1.2,1.1)+spring_flower(37,-93,.5)+leaf(-58,-37,.32,-35,'green','oval')
  if finished:
   fy=-44 if kind=='bunny' else 11
   a+=stoneeye(-24,fy,1.1)+stoneeye(24,fy,1.1)+stone(0,fy+27,.25,0,'#8b775d')
   if kind=='monster':a+=path(f'M-24 {fy+48} Q0 {fy+26} 24 {fy+48}',stroke=INK,sw=4)
   else:a+=smile(0,fy+45,19)
 return grp(a,f'translate({x} {y}) scale({s})')
def supply_leaf(x,y,s=1):return leaf(x,y,s,-20,'green','oval')+spring_flower(x+34*s,y-55*s,.45*s)

def mud_creatures(n):
 titles=['Gather bits for a muddy friend','Mix until it holds a shape','Give your creature a steady body','Add a face, ears or spines','Meet your muddy characters']
 subs=['Clean soil, a little water and safe natural details.','Add water slowly. Stop before it gets drippy.','Keep it low. Smooth joins with a damp finger.','Press decorations gently into the mud.','One leaf-ear bunny, a hedgehog or a silly monster.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=tray(480,454,775,155)+bowl(215,321,.82)+drop(356,304,1)+spoon(319,312,26,.65)
  a+=twig(445,244,494,421,12)+twig(500,278,456,410,10)+leaf(609,308,.62,15,'green','oval')+grass(657,409,.72)
  for x,y in [(766,328),(722,391),(811,407)]:a+=stone(x,y,.48)
  a+=note(221,545,'Soil + water',size=25)+note(613,545,'Ears, eyes, hair or spines',size=25)
 elif n==2:
  a+=bowl(351,346,1.35)+spoon(387,248,-26,.95)+drop(192,208,.9)+arrow(214,245,258,321,-15)
  a+=mudball(747,337,78,68)+hand(644,351,.62,70)+note(745,463,'Holds a ball',size=26)+note(278,492,'A spoonful at a time',size=26)
 elif n==3:
  a+=tray(480,474,755,110)+mudfriend(303,333,1.1,'bunny',False)+mudfriend(678,372,.92,'hedgehog',False)
  a+=hand(425,292,.55,-50)+arrow(438,297,344,347,15)+drop(456,236,.35)
  a+=note(282,546,'Round body + head',size=25)+note(688,546,'Low oval',size=25)
 elif n==4:
  a+=tray(483,480,680,100)+mudfriend(481,351,1.18,'bunny',True)
  a+=stone(186,300,.48,0,'#6d7565')+arrow(238,296,427,300,-12)+note(186,373,'Stone features',size=25)
  a+=leaf(773,247,.41,15,'green','oval')+arrow(725,266,536,227,20)+note(774,367,'Leaf ears',size=25)
 else:
  a+=tray(480,476,848,107)+mudfriend(218,368,.9,'bunny',True)+mudfriend(488,407,.83,'hedgehog',True)+mudfriend(768,393,.95,'monster',True)
  a+=camera(851,187,.54)+sparkle(331,258,.6)+sparkle(673,263,.55)
 a+=footer(['Use only pieces a grown-up has checked.','Too runny? Add soil. Crumbly? Make a flat creature.','Press joined pieces together and smooth the seam.','Use light pieces and keep the base broad.','Photograph your temporary art before it dries.'][n-1])
 return a

# Dandelion crown: exact loop method, not a braid or slit-threaded flower chain.
def wrap_diagram(phase,x,y,s=1):
 a=''
 # New flower's first segment goes UNDER the existing horizontal stem.
 lower='M-9 -46 L-9 135' if phase==1 else 'M-9 -46 L-9 27' if phase==2 else 'M-9 -46 L-9 -7'
 a+=stem(lower,TEAL,9)
 a+=stem('M-76 -36 Q-67 -19 -46 -20 L137 -20',STEM,11)
 if phase==2:
  a+=stem('M-9 27 Q-11 53 -35 51 Q-60 49 -57 18 L-56 -31 Q-55 -55 -37 -72 L-37 -131',TEAL,9)
  a+=movement('M27 107 Q-89 112 -86 16 Q-87 -69 -52 -104')
 elif phase==3:
  a+=stem('M-9 -7 Q-11 11 -32 10 Q-54 9 -53 -12 L-53 -31 Q-53 -61 -30 -55 Q-2 -34 24 -33 L137 -33',TEAL,9)
  a+=movement('M29 -68 L127 -68')
 # Flowers are shown after stems so calyces visibly connect under the heads.
 a+=dandelion(-78,-65,31)+dandelion(-9,-78,31)
 a+=path('M-89 -38 Q-76 -27 -63 -38 M-19 -51 Q-9 -40 1 -51',stroke='#58734a',sw=5)
 return grp(a,f'translate({x} {y}) scale({s})')
def crown_ring(x,y,s=1):
 a=ellipse(0,0,151,88,'none','#476543',16)+ellipse(0,-2,151,88,'none','#8aa86c',10)+ellipse(0,4,142,82,'none','#a1b67f',6)
 for i in range(15):
  t=i*2*math.pi/15;xx=math.sin(t)*151;yy=-math.cos(t)*88
  # Visible little stem wraps under each flower head.
  a+=grp(ellipse(0,0,12,20,'none','#5d7e4e',4),f'translate({xx} {yy+10}) rotate({i*24})')
 for i in range(15):
  t=i*2*math.pi/15;a+=dandelion(math.sin(t)*151,-math.cos(t)*88-19,25, i*24)
 return grp(a,f'translate({x} {y}) scale({s})')
def stem_chain(x,y,s=1,count=5,new=True):
 a=stem(f'M{-120+count*48} 9 L{-120+count*48} 114',TEAL,8) if new else ''
 a+=stem('M-130 32 Q15 46 199 22',STEM,16)+stem('M-130 41 Q10 56 200 31','#a0b781',5)
 for i in range(count):
  xx=-120+i*48;yy=17+10*math.sin(i*.6)
  a+=stem(f'M{xx} {yy-18} Q{xx+21} {yy+7} {xx+4} {yy+28} Q{xx-17} {yy+31} {xx-12} {yy+7} Q{xx-10} {yy-5} {xx+17} {yy+15}',STEM,6)
  a+=dandelion(xx,yy-23,24)
 if new:
  xx=-120+count*48;a+=dandelion(xx,-15,24)+movement(f'M{xx+33} 105 Q{xx-31} 113 {xx-28} 45')
 return grp(a,f'translate({x} {y}) scale({s})')
def crown_join(x,y,s=1):
 a=stem('M-132 -6 Q0 -26 142 -8',STEM,15)+stem('M-132 10 Q0 -8 142 8','#a6ba81',7)
 # Three pre-existing loops, with the free tail visibly threaded beneath them.
 for xx in [-58,12,80]:a+=ellipse(xx,-3,13,30,'none','#527b4a',7)
 a+=stem('M-145 85 Q-111 89 -92 57 Q-74 25 -59 11 Q-40 -7 -17 5 Q8 15 33 5 Q58 -7 88 0 Q112 7 142 -2',TEAL,8)
 for xx in [-58,12,80]:a+=path(f'M{xx-10} -19 Q{xx-16} 5 {xx-7} 24',stroke='#527b4a',sw=8)
 a+=movement('M-120 55 Q-76 37 -44 4')+movement('M-20 49 L92 38')
 return grp(a,f'translate({x} {y}) scale({s})')
def dandelion_crown(n):
 titles=['Choose long-stemmed dandelions','Cross the new stem underneath','Wrap up, then lay the tail alongside','Add another flower the same way','Curve, overlap and tuck the ends']
 subs=['A grown-up identifies the flowers and approves the spot.','First flower on the left; its stem points right.','Follow the teal stem through one complete loop.','One new flower, one wrap, then its tail joins the bundle.','Make a loose ring and ask a grown-up to check the fit.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=tray(480,468,760,107)
  for i,(x,y,ang) in enumerate([(255,224,-13),(414,212,5),(556,244,15),(694,219,-7)]):
   stemart=stem('M0 22 Q18 105 0 225',STEM,9)+dandelion(0,0,37)
   a+=grp(stemart,f'translate({x} {y}) rotate({ang})')
  a+=line(145,245,145,445,'#7f9677',3)+line(135,245,155,245,'#7f9677',3)+line(135,445,155,445,'#7f9677',3)+note(100,338,'15–20',size=23)+note(100,367,'cm',size=23)
 elif n==2:
  a+=wrap_diagram(1,415,285,1.55)+arrow(733,376,418,257,-17)+note(763,340,'New stem',size=27)+note(763,371,'goes UNDER',size=27)+note(763,404,'then hangs down',size=23)
  a+=note(290,487,'Pinch close to the flower heads',size=25)
 elif n==3:
  for phase,xc,label,sub in [(1,180,'Cross','New stem underneath'),(2,480,'Wrap','Up between the heads'),(3,780,'Lay alongside','Long tail points right')]:
   panel=rect(xc-138,140,276,328,['#eef2e4','#edf3ee','#f5ece7'][phase-1],'none',0,20)
   panel+=wrap_diagram(phase,xc,306,.94)+text(xc,491,label,27,weight=700)+text(xc,520,sub,20,weight=500)
   a+=grp(panel,attrs=f'id="wrap-phase-{phase}" data-wrap-phase="{phase}"')
  a+=line(180,550,227,550,STEM,9)+text(239,558,'Existing stems',19,'start',DARK,600)
  a+=line(559,550,606,550,TEAL,9)+text(618,558,'New flower',19,'start',DARK,600)
 elif n==4:
  a+=stem_chain(390,220,1.45,5,True)+note(479,422,'Keep each new stem underneath first',size=27)
  a+=wrap_diagram(3,791,456,.43)+arrow(679,396,746,432,-10)+note(217,501,'Wrap, lay alongside, repeat',size=26)
 elif n==5:
  a+=crown_ring(272,326,1.16)+crown_join(737,322,.97)+note(740,220,'Overlap the ends',size=27)+note(734,460,'Tuck through nearby loops',size=23)+note(734,490,'Repeat 2–3 times',size=25)
  a+=sparkle(92,204,.7)+sparkle(438,442,.7)
 a+=footer(['Leave plenty of growing flowers for insects.','Hold both stems gently at the crossing.','Snug the loop gently. Do not snap the stem.','Curve the chain gently and check its length often.','A grown-up can add a short cotton tie if it slips.'][n-1])
 return a

def tree(x,y,w=230,h=385):
 a=path(f'M{-w*.42} {-h} Q{-w*.48} {-h*.65} {-w*.45} {-h*.23} L{-w*.69} 19 Q{-w*.37} 6 {-w*.16} 10 Q0 27 {w*.18} 8 L{w*.66} 22 L{w*.46} {-h*.19} Q{w*.45} {-h*.68} {w*.42} {-h} Z','#c5a382','#7f6953',3)
 for k in range(7):
  xx=-w*.34+k*w*.115
  a+=path(f'M{xx} {-h+9} Q{xx-13} {-h*.76} {xx+7} {-h*.57} Q{xx-14} {-h*.34} {xx-4} {-h*.04}',stroke=['#997a60','#ad8b6b','#d8ba96'][k%3],sw=4)
 a+=path(f'M{-w*.13} {-h*.62} Q{-w*.02} {-h*.75} {w*.07} {-h*.62} Q{w*.04} {-h*.48} {-w*.13} {-h*.62} Z',stroke='#8c7158',sw=3)
 return grp(a,f'translate({x} {y})')
def curved_twig(x,y,w=70,h=18,up=False):
 yy=-h if up else h
 return path(f'M{-w/2} 0 Q0 {yy} {w/2} 0',stroke=INK,sw=10)+path(f'M{-w/2} 0 Q0 {yy} {w/2} 0',stroke='#ac7d54',sw=6)
def mud_face(x,y,s=1,finished=True,mood='happy',hair='leaves'):
 a=mudball(0,8,97,115)
 if finished:
  if hair=='leaves':
   for xx,ang,c in [(-60,-40,'green'),(-23,-15,'gold'),(23,15,'green'),(61,40,'green')]:a+=leaf(xx,-105,.42,ang,c,'oval')
   a+=spring_flower(50,-128,.57,'#dbc5e6')
  elif hair=='grass':a+=grass(0,-100,1.3,1.1)+dandelion(50,-145,20)
  else:
   for i in range(7):a+=twig(-68+i*22,-77,-82+i*27,-142-15*math.sin(i),8)
  a+=stoneeye(-35,-21,1.35)+stoneeye(35,-21,1.35)+stone(0,20,.46,90,'#a49a81')
  a+=grp(curved_twig(0,0,86,22,mood=='frown'),'translate(0 68)')
  if mood=='surprise':a+=ellipse(0,68,21,23,'none',INK,6)
  a+=leaf(-40,-50,.18,-70,'green','point')+leaf(40,-50,.18,70 if mood!='frown' else 110,'green','point')
 return grp(a,f'translate({x} {y}) scale({s})')
def muddy_faces(n):
 titles=['Choose bark or a flat ground spot','Make thick, mouldable mud','Press on a flat oval pad','Give the face its own expression','Meet a wonderfully muddy character']
 subs=['Ask a grown-up. Leave moss, lichens and roots alone.','A handful should hold together without dripping.','If it slips on bark, make the face on the ground.','All decorations go into the mud, never into the bark.','Move a brow or turn the mouth to change its mood.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=soil(275,465,175,35)+tree(278,450,225,310)+dash('M200 268 C204 181 350 180 357 268 C363 368 201 373 200 268','#725c48',3)
  a+=soil(690,368,171,109)+dash('M586 370 C586 267 796 264 797 370 C798 469 584 469 586 370','#96704f',3)
  a+=note(277,538,'Approved rough bark',size=25)+note(689,538,'Or a flat ground patch',size=25)
 elif n==2:
  a+=bowl(345,360,1.32)+spoon(393,260,-23,.9)+drop(191,219,.85)+arrow(218,249,254,327,-15)
  a+=mudball(736,344,85,62)+hand(646,357,.57,75)+note(737,466,'Holds together',size=26)+note(297,513,'More soil if it is runny',size=25)
 elif n==3:
  a+=soil(294,475,184,29)+tree(296,455,245,320)+mud_face(295,310,.88,False)
  a+=hand(157,295,.65,58)+arrow(188,289,227,307,-20)
  a+=soil(698,386,163,108)+grp(mud_face(0,0,.78,False),'translate(701 370) rotate(18)')
  a+=note(300,534,'Press gently; smooth the edges',size=23)+note(716,534,'Ground works too',size=23)
 elif n==4:
  a+=tree(480,496,297,370)+mud_face(481,343,1.05,True,'happy','leaves')
  a+=stone(183,261,.5,0,'#6d7565')+arrow(232,269,408,320,-15)+note(186,330,'Stone features',size=25)
  a+=grass(776,298,.85)+arrow(731,268,568,229,15)+note(788,369,'Leafy hair',size=25)
 else:
  a+=soil(274,470,200,28)+tree(276,450,246,320)+mud_face(276,335,.93,True,'happy','leaves')
  a+=soil(686,408,185,104)+grp(mud_face(0,0,.82,True,'frown','grass'),'translate(686 370) rotate(9)')
  a+=camera(840,198,.52)+sparkle(476,256,.6)+note(277,535,'A friendly smile',size=24)+note(688,548,'A silly frown',size=24)
 a+=footer(['Set safe decorations nearby before you begin.','Try a flatter face if your soil keeps crumbling.','Keep it small, low and fairly flat.','Use a naturally curved twig for the mouth.','Take a photo, then gently remove mud and decorations.'][n-1])
 return a

# Tree-side lean-to: every pole visibly touches the trunk and is braced at its foot.
def bark_tile(points):
 d='M'+' L'.join(f'{x} {y}' for x,y in points)+' Z';a=path(d,'#c7a98d','#806f59',3)
 (x1,y1),(x2,y2),(x3,y3),(x4,y4)=points
 for t in [.24,.51,.76]:
  sx=x1+(x2-x1)*t;sy=y1+(y2-y1)*t;ex=x4+(x3-x4)*t;ey=y4+(y3-y4)*t
  a+=path(f'M{sx} {sy+4} Q{(sx+ex)/2-4} {(sy+ey)/2} {ex} {ey-4}',stroke='#9b856d',sw=3)
 return a

def roofpoint(u,v):return (415+3*u+170*v+112*u*v,300-85*u+200*v+25*u*v)
def lean_to(n,decor=True):
 a=soil(526,490,346,70)+tree(334,485,242,360)
 if n>=2:
  # The open triangular side is the doorway. Nothing is fastened to the bark.
  a+=path('M415 300 L585 500 L415 500 Z','#8a77542b','none',0)
  for j in range(7):
   u=j/6;top=roofpoint(u,0);foot=roofpoint(u,1)
   a+=twig(*foot,*top,12)
   a+=stone(foot[0]+8,foot[1]+8,.38,(-1)**j*9)
 if n>=3:
  # Short overlapping bark tiles lie across the close-spaced leaning poles.
  for v0,v1 in [(.62,1.0),(.31,.7),(0,.4)]:
   for u0,u1 in [(0,.48),(.44,1)]:
    a+=bark_tile([roofpoint(u0,v0),roofpoint(u1,v0),roofpoint(u1,v1),roofpoint(u0,v1)])
  leaves=leaf(486,362,.64,50,'green','oval')+leaf(592,415,.67,65,'green','oak')+leaf(424,293,.5,65,'gold','oval')
  a+=grp(leaves,attrs='clip-path="url(#leanclip)"')
  a+=twig(*roofpoint(0,.48),*roofpoint(1,.48),10)
 if n>=4:
  for i in range(6):a+=stone(490-i*22,499+i*6,.35+(i%2)*.06,i*11)
  a+=leaf(652,506,.36,60,'green','oak')+leaf(689,501,.34,10,'green','oval')
  a+=spring_flower(675,474,.57,'#dbc5e6')+spring_flower(729,491,.54,'#ebbdc9')+dandelion(624,499,17)
  a+=spring_flower(454,323,.48,'#dbc5e6')+spring_flower(531,374,.45,'#e8bfcc')+dandelion(583,412,16)
  a+=leaf(376,463,.34,70,'green','oval')
 return a

def rock_shelter(x,y,s=1):
 a=soil(0,90,135,35)
 # Separate low supports leave an unmistakable opening beneath a thin roof slab.
 a+=path('M-47 20 L46 20 L50 83 L-50 83 Z','#59634f','#59634f',1)
 a+=stone(-78,48,.85,-5,'#a9ad99')+stone(78,48,.85,5,'#a9ad99')
 a+=path('M-113 0 Q-65 -11 7 -8 L94 -5 L114 7 L109 23 Q0 28 -114 21 Z','#bcc2ad','#71806a',3)
 a+=path('M-94 4 Q-14 -3 79 5 M-103 17 Q-11 22 99 16',stroke='#e0e3cf',sw=3)
 for xx,yy in [(-20,83),(-30,106),(-45,127)]:a+=stone(xx,yy,.25)
 a+=spring_flower(91,71,.55)+leaf(107,88,.25,20,'green','oval')
 return grp(a,f'translate({x} {y}) scale({s})')
def spring_garden(n):
 titles=['Find a little spot beside a tree','Lean twigs against the trunk','Overlap a light roof','Make a path and a spring garden','Give your tiny garden a story']
 subs=['Keep roots and living plants just as they are.','Brace each foot with a small, stable stone.','Loose fallen bark or broad leaves rest on the twigs.','A flower here, a leaf there: make it yours.','Photograph your creation, then take it down after play.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=lean_to(1)+dash('M401 398 Q620 378 755 477 Q661 545 430 509 Z','#8e9a72',3)
  a+=twig(416,484,496,481,8)+twig(393,507,378,533,8)+note(676,282,'Plan a door',size=27)+note(676,317,'and a path',size=27)+arrow(658,341,503,462,14)
 elif n==2:
  a+=lean_to(2)+arrow(763,190,425,255,25)+note(747,157,'Rest against bark',size=25)
  a+=arrow(816,407,698,449,-12)+note(800,371,'Brace the feet',size=24)+note(211,423,'Doorway',size=25)+arrow(223,435,479,458,8)
 elif n==3:
  a+=lean_to(3)+arrow(772,190,585,415,22)+note(749,158,'Work bottom to top',size=25)
  a+=note(175,409,'Keep the door',size=24)+note(175,438,'open',size=24)+arrow(234,444,479,458,8)
 elif n==4:
  a+=lean_to(4)+sparkle(767,267,.65)+arrow(171,435,401,524,12)+note(173,398,'Winding path',size=25)+note(758,235,'Spring colour',size=25)
 else:
  a+=grp(lean_to(4),'translate(100 20) scale(.92)')
  a+=rock_shelter(145,378,.69)+note(153,257,'Another idea',size=25)+note(152,287,'Low rock shelter',size=21)
  a+=camera(821,196,.53)+sparkle(713,165,.65)
 a+=footer(['A grown-up approves the place. No digging or nails.','Use short, low poles and test them gently.','A light twig can hold a slipping leaf in place.','Use only loose or approved collected decorations.','A grown-up places any flat roof stone.'][n-1])
 return a

DEFS=DEFS.replace('</defs>','<clipPath id="leanclip"><path d="M415 300 L418 215 L700 440 L585 500 Z"/></clipPath></defs>')
CATALOGUE={x['id']:x for x in json.loads((ROOT/'content/activities.json').read_text())}
TASKS={'SPR-06':mud_creatures,'SPR-07':dandelion_crown,'SPR-08':muddy_faces,'SPR-09':spring_garden}
OUT.mkdir(parents=True,exist_ok=True)
for aid,draw in TASKS.items():
 activity=CATALOGUE[aid]
 for n,step in enumerate(activity['steps'],1):
  CURRENT_STEP=n
  title=f'{activity["title"]} — step {n}: {step["title"]}'
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="630" viewBox="0 0 960 630" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(step["text"])}</desc>{DEFS}{background()}{draw(n)}</svg>'
  (OUT/f'{aid}-{n}.svg').write_text(svg)
print('Generated 20 precise pastel spring panels, SPR-06–09. Crown phase groups: 1, 2, 3.')
