#!/usr/bin/env python3
"""Build 20 original, deterministic cartoon instruction panels for FAL-06–09.

Usage: python3 scripts/generate-fall-diagrams.py
Uses the activity catalogue only for accessible titles/descriptions; never edits it.
All art is native SVG, deliberately drawn to explain the actual physical steps.
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

def leaf_owl(x,y,s=1,stage=5,facekind='pebble'):
 a=leaf(0,70,.85,0,'gold','oak')+leaf(0,-67,.62,0,'orange','maple')
 if stage>=3:
  a+=leaf(-73,50,.65,-24,'red','point')+leaf(73,50,.65,24,'red','point')
  a+=leaf(-39,-125,.34,-25,'green','point')+leaf(39,-125,.34,25,'green','point')
 if stage>=4:
  if facekind=='paper':a+=eye(-27,-63,24,-1)+eye(27,-63,24,-1)
  else:a+=stone(-25,-62,.48,0,'#727a7c')+stone(25,-62,.48,0,'#727a7c')
  a+=path('M-9 -35 L9 -35 L0 -18 Z',GOLD,INK,2)
  a+=twig(-27,142,-38,176,7)+twig(27,142,38,176,7)+twig(-38,176,-56,178,6)+twig(38,176,56,178,6)
  a+=cheek(-51,-29,.9)+cheek(51,-29,.9)
 if stage>=5:a+=leaf(0,-141,.26,30,'gold','oval')+sparkle(-116,-60,.6)+sparkle(120,70,.7)
 return grp(a,f'translate({x} {y}) scale({s})')

# FAL-06: a clearly flat leaf animal, with additional layers appearing at each step.
def leafy(n):
 titles=['Sort a rainbow of fallen leaves','Start with a body and a head','Layer on a little personality','Add eyes and twig legs','Make this friend your own']
 subs=['Big leaves, small leaves, a few simple details.','Try the pieces before you attach anything.','Ears, wings or a tail: you choose.','Everything stays flat on its backing.','Name it. Change it. Remember it.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=paper(475,326,720,360,-1)
  for x,y,s,ang,c,k in [(220,267,.64,-18,'gold','oak'),(294,311,.7,15,'red','maple'),(395,260,.58,8,'green','oval'),(474,337,.48,-20,'orange','point')]:a+=leaf(x,y,s,ang,c,k)
  for x,y,ang,c in [(590,236,-30,'red'),(643,292,20,'gold'),(588,362,-14,'green')]:a+=leaf(x,y,.31,ang,c,'oval')
  a+=twig(710,239,741,337,10)+twig(754,265,727,397,10)+stone(680,411,.45,0,'#727a7c')+stone(575,441,.45,0,'#727a7c')
  a+=note(315,499,'Big shapes')+note(654,499,'Little details')
 elif n==2:
  a+=paper(480,325,485,374,-1)+leaf_owl(480,300,1.1,2)
  a+=leaf(178,337,.49,15,'gold','oak')+arrow(232,331,366,353,25)+note(167,444,'Body')
  a+=leaf(770,227,.4,-15,'orange','maple')+arrow(710,244,577,245,-25)+note(787,345,'Head')
 elif n==3:
  a+=paper(475,326,490,375,-1)+leaf_owl(475,305,1.05,3)
  a+=leaf(778,305,.4,35,'red','point')+arrow(728,324,598,356,25)+note(783,418,'Layer leaves')
  a+=hand(168,306,.55,32)+arrow(216,267,367,189,-25)+note(166,440,'Try ears, too')
 elif n==4:
  a+=paper(475,325,490,380,-1)+leaf_owl(475,307,1.03,4)
  a+=stone(161,226,.6,0,'#727a7c')+stone(228,226,.6,0,'#727a7c')+note(195,288,'Pebble eyes')+arrow(256,228,404,248,20)
  a+=twig(746,325,770,406,9)+twig(770,406,798,411,8)+arrow(730,393,555,481,-15)+note(782,465,'Twig legs')
 else:
  a+=paper(425,326,560,383,-2)+leaf_owl(425,300,1.13,5)
  a+=path('M655 172 Q727 146 818 177 Q844 216 803 248 L728 245 L690 272 L699 238 Q635 226 655 172 Z','#f5dda8','#c5a16a',3)+note(742,207,'Hello, friend!',size=25)
  a+=camera(781,382,.8)+sparkle(698,399,.6)+sparkle(838,324,.7)
 a+=footer(['Arrange everything on a flat base.','A large leaf makes a great body.','Overlap the pieces to build your animal.','No glue needed. An adult can help if you use it.','Take a photo, then tidy your natural treasures.'][n-1])
 return a

# FAL-07: supported twig shelter; the roof load sits on crosspieces, not floating mud.
def rock(x,y,s=1):
 a=path('M-110 69 L-91 -25 L-35 -77 L52 -65 L113 9 L122 76 Z','#b6b7a6','#778071',3)
 a+=path('M-91 -25 L-17 -4 L52 -65 M-17 -4 L31 75 M-17 -4 L113 9',stroke='#8e9685',sw=3)+path('M-74 -25 L-37 -55 L5 -50',stroke='#d4d5bd',sw=7)
 return grp(a,f'translate({x} {y}) scale({s})')
def hut(x,y,s=1,roof=False,pathway=False):
 a=''
 # Four blunt posts, two front/back supporting rails, and five roof crosspieces.
 A=(-150,170);B=(140,170);C=(210,60);D=(-80,60)
 tops=[(-150,-40),(140,-40),(210,-145),(-80,-145)]
 # A low side row is pressed into soil; the front doorway remains open.
 for fx,fy in [(-96,83),(-113,110),(-131,138)]:a+=twig(fx,fy,fx,fy-82,11)
 for foot,top in zip([D,C,A,B],[tops[3],tops[2],tops[0],tops[1]]):
  tx,ty=top
  # The continuous Y shape is a naturally forked upright. Rails sit between its arms.
  a+=twig(*foot,tx,ty+22,17)
  a+=twig(tx,ty+22,tx-22,ty-23,13)+twig(tx,ty+22,tx+22,ty-23,13)
 a+=twig(*tops[3],*tops[2],17)+twig(*tops[0],*tops[1],17)
 for j in range(5):
  t=j/4;a+=twig(-80+290*t,-145,-150+290*t,-40,12)
 if roof:
  # Eight overlapping broad leaf tiles, flattened into the sloping roof plane.
  leaves=''
  for j in range(4):leaves+=leaf(-103+j*68,-67,.55,65,['gold','orange','red','green'][j],'oval')
  for j in range(4):leaves+=leaf(-55+j*68,-118,.54,65,['red','gold','green','orange'][j],'oak')
  a+=grp(leaves,'','clip-path="url(#roofclip)"')
  a+=twig(-115,-77,170,-78,11)
  for px,py in [(-104,-60),(-31,-84),(71,-90)]:a+=ellipse(px,py,8,4,'#815e40','none',0)
 if pathway:
  for j in range(6):a+=stone(10-j*13,191+j*17,.36+j*.015,(-1)**j*8)
  a+=leaf(-225,133,.43,-65,'green','oak')+leaf(-255,153,.3,-40,'gold','oval')
 return grp(a,f'translate({x} {y}) scale({s})')
def fairy(x,y,s=1):
 a=leaf(-28,10,.3,-45,'gold','oval')+leaf(28,10,.3,45,'gold','oval')+path('M0 -5 L-25 66 L25 66 Z','#e7b89a',INK,2.5)+circle(0,-22,20,'#f4d9ae',INK,2.5)+eye(-7,-24,3.5)+eye(7,-24,3.5)+smile(0,-15,5)
 return grp(a,f'translate({x} {y}) rotate(-12) scale({s})')
def mud_bowl(x,y,s=1):
 a=path('M-100 0 Q-90 87 0 97 Q90 87 100 0 Z','#a4b1a0',INK,4)+ellipse(0,0,100,30,'#9b704a',INK,3)
 for xx,yy in [(-53,-7),(20,3),(54,-5),(-15,9)]:a+=ellipse(xx,yy,11,5,'#b58a5c','none',0)
 return grp(a,f'translate({x} {y}) scale({s})')
def spoon(x,y,angle=0,s=1):
 a=path('M-12 5 L-8 -108 Q0 -125 8 -108 L12 5 Z','#b88d60',INK,3)+ellipse(0,18,28,40,'#c9a374',INK,3)+ellipse(0,18,21,28,'#9c744b','none',0)
 return grp(a,f'translate({x} {y}) rotate({angle}) scale({s})')
def garden(n):
 titles=['Find a little place to build','Give the roof real support','Mix a little mud paste','Overlap leaves across the roof','Grow your own tiny world']
 subs=['A permitted patch of soft soil, away from roots.','Four forked twigs cradle the roof crosspieces.','Add water a spoonful at a time.','Mud is temporary; a twig can hold leaves down.','A path, a garden and a story of your own.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=soil(465,387,350,126)+rock(757,264,.85)
  a+=dash('M245 344 Q390 260 613 321 L655 421 Q429 498 236 420 Z')
  a+=leaf(150,440,.37,-25,'gold','oak')+leaf(703,453,.35,45,'orange','maple')
  a+=hand(147,234,.65,35)+arrow(211,238,340,324,-20)+note(251,165,'Permission first',size=25)
  a+=note(461,470,'Plan a small patch',size=25)
 elif n==2:
  a+=soil(487,445,348,88)+rock(802,277,.7)+hut(460,300,.83)
  a+=arrow(279,283,279,403)+note(165,237,'Press into soil',size=24)+note(171,267,'not tree roots',size=24)
  a+=arrow(718,171,564,201,15)+note(752,150,'Roof crosspieces',size=24)
 elif n==3:
  a+=mud_bowl(321,369,1.25)+spoon(358,272,-24,.9)
  a+=path('M149 207 Q168 236 161 250 Q147 267 134 249 Q129 234 149 207 Z',BLUE,'#577f87',3)
  a+=arrow(183,233,235,327,-15)+note(172,180,'A little water',size=25)
  a+=leaf(678,389,.78,58,'green','oval')+leaf(699,352,.88,58,'gold','oak')+ellipse(694,366,35,20,'#886141',INK,2.5)+spoon(749,276,25,.55)
  a+=note(701,500,'A dab on a leaf',size=25)+note(321,515,'Thick, not runny',size=25)
 elif n==4:
  a+=soil(469,451,352,83)+rock(803,281,.7)+hut(468,312,.9,True)
  a+=leaf(194,190,.45,60,'orange','oval')+arrow(247,203,378,239,-20)+note(177,145,'Overlap leaves',size=24)
  a+=arrow(761,163,605,242,10)+note(774,142,'Twig on top',size=24)
 else:
  a+=soil(479,416,380,122)+rock(801,270,.72)+hut(460,293,.89,True,True)
  a+=fairy(230,415,.65)+note(178,493,'Paper fairy',size=23)
  a+=camera(798,465,.6)+sparkle(722,200,.65)+sparkle(326,210,.55)
 a+=footer(['Keep the project small and leave habitats alone.','Nest crosspieces in the forks. Ask a grown-up to check.','Try the paste before using it on the roof.','Start low and overlap toward the top.','Photograph it, then remove every added craft piece.'][n-1])
 return a

# FAL-08: visible concentric construction; all objects are loose and removable.
def mandala_art(x,y,s=1,stage=5,mode='beautiful'):
 a=''
 if stage>=4:
  for i in range(12):
   t=i*math.pi/6
   if stage>=5 and mode=='cute':a+=stone(math.sin(t)*191,-math.cos(t)*191,.38,i*30,'#b2b69d')
   else:a+=twig(math.sin(t)*178,-math.cos(t)*178,math.sin(t)*217,-math.cos(t)*217,8)
  for i in range(8):
   t=i*math.pi/4+math.pi/8;a+=stone(math.sin(t)*153,-math.cos(t)*153,.35,i*45,'#b2b69d')
  for i in range(4):
   t=i*math.pi/2+math.pi/4
   if not (stage>=5 and mode=='cute'):a+=pine(math.sin(t)*235,-math.cos(t)*235,.32,i*90)
 if stage>=3:
  count=12 if stage>=5 and mode=='fierce' else 8
  for i in range(count):
   t=i*2*math.pi/count
   kind='point' if stage>=5 and mode=='fierce' else 'round' if stage>=5 and mode=='cute' else 'oval'
   colours=['orange','red'] if mode=='fierce' else ['red','gold','green','orange']
   a+=leaf(math.sin(t)*111,-math.cos(t)*111,.52,i*360/count,colours[i%len(colours)],kind)
 if mode=='beautiful':
  if stage>=5:
   for j in range(12):
    t=j*math.pi/6;a+=stone(math.sin(t)*50,-math.cos(t)*50,.12,j*30,'#a6ad96')
   a+=leaf(0,0,.27,0,'gold','maple')
  else:a+=leaf(0,0,.52,0,'gold','maple')
 else:
  a+=leaf(0,0,.59,0,'gold','round' if mode=='cute' else 'maple')
  a+=stone(-18,-5,.15,0,'#747c66')+stone(18,-5,.15,0,'#747c66')
  if mode=='cute':a+=twig(-13,25,0,31,4)+twig(0,31,13,25,4)
  else:a+=leaf(-17,-22,.13,-48,'red','point')+leaf(17,-22,.13,48,'red','point')+twig(-13,30,13,30,4)
 return grp(a,f'translate({x} {y}) scale({s})')
def mandala(n):
 titles=['Sort your autumn treasures','Choose a centre','Make the first repeating ring','Repeat in a new material','Let your pattern have a personality']
 subs=['Leaves, twigs, pebbles and pinecones.','One leaf or pinecone is enough to begin.','Turn the leaf tips out and fill the gaps.','Try a ring of stones, then twigs or cones.','Cute, fierce or simply beautiful: all yours.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  for x,y,ang,c,k in [(220,251,-15,'red','maple'),(277,305,22,'gold','oak'),(168,329,-30,'green','oval')]:a+=leaf(x,y,.48,ang,c,k)
  a+=twig(401,219,439,390,13)+twig(447,229,413,396,11)+twig(483,248,490,393,10)
  for x,y,s,ang in [(593,270,.55,-10),(650,334,.6,10),(567,373,.4,30)]:a+=stone(x,y,s,ang)
  a+=pine(782,278,.65,-15)+pine(821,381,.5,20)
  for x,t in [(223,'Leaves'),(447,'Twigs'),(611,'Pebbles'),(801,'Pinecones')]:a+=note(x,488,t, size=26)
 elif n==2:
  a+=dash('M270 340 A210 155 0 1 1 690 340 A210 155 0 1 1 270 340', '#e0cba4',3)
  a+=leaf(480,330,1.05,0,'gold','maple')+arrow(253,219,394,291,-20)+note(201,193,'Start here',size=27)
  a+=pine(792,329,.6,0)+note(792,442,'Or a pinecone',size=24)
 elif n==3:
  a+=mandala_art(480,334,.88,3)+leaf(789,270,.43,45,'red','oval')+arrow(737,286,627,244,25)+note(788,406,'Repeat a shape',size=24)
 elif n==4:
  a+=mandala_art(480,332,.84,4)+arrow(153,187,303,208,-15)+note(139,158,'New ring',size=25)+arrow(808,417,681,420,-15)+note(819,469,'Same spacing',size=24)
 else:
  for x,mode in [(190,'cute'),(480,'fierce'),(770,'beautiful')]:a+=mandala_art(x,315,.5,5,mode)
  for x,t in [(190,'Cute'),(480,'Fierce'),(770,'Beautiful')]:a+=note(x,493,t,size=28)
  a+=camera(865,527,.35)
 a+=footer(['Use permitted fallen pieces and keep them loose.','Leave room around the middle for more rings.','A repeated colour or shape makes a pattern.','Build outward, one ring at a time.','Take a photo, then leave the habitat clear.'][n-1])
 return a

# FAL-09: a top-down leaf character, never drawn as a standing unsupported sculpture.
def leaf_friend(x,y,s=1,stage=5,col='red',wings=True,pose=0):
 a=''
 a+=twig(0,-55,0,65,10)+twig(-70,-10,70,-10+pose,9)+twig(0,58,-48,156,9)+twig(0,58,48,156,9)
 a+=circle(0,-98,42,'#f4dfb9',INK,3)
 if stage>=3:
  if wings:a+=leaf(-66,-4,.48,-58,'green','point')+leaf(66,-4,.48,58,'green','point')
  a+=leaf(-24,58,.61,18,col,'oak')+leaf(24,58,.61,-18,'gold' if col=='red' else 'orange','oak')+leaf(0,29,.5,0,col,'maple')
  a+=leaf(-22,-131,.27,-60,'gold','oval')+leaf(20,-134,.27,55,'orange','oval')
 if stage>=4:
  a+=eye(-13,-104,5.8)+eye(13,-104,5.8)+smile(0,-87,12)+cheek(-25,-86,.65)+cheek(25,-86,.65)
  a+=leaf(1,-13,.2,90,'green','oval')
 if stage>=5:a+=sparkle(-106,-90,.5)+sparkle(108,57,.45)
 return grp(a,f'translate({x} {y}) rotate({pose/7}) scale({s})')
def glue(x,y,s=1):
 a=rect(-29,-25,58,90,'#f3ead2',INK,3,10)+path('M-17 -25 L-10 -58 L10 -58 L17 -25 Z','#d39b60',INK,3)+rect(-9,-73,18,17,RED,INK,3,4)+rect(-23,-4,46,39,'#8ca474',INK,2,4)+text(0,21,'glue',14,c=CREAM,weight=700)
 return grp(a,f'translate({x} {y}) scale({s})')
def friends(n):
 titles=['Pick leaves for a little friend','Lay out the twig body','Layer a leafy outfit','Draw the face and add details','Meet your fall friends']
 subs=['A dress, wings, hair: follow the shapes you find.','Arms, legs and a round paper face, all flat.','Try a skirt, a dress, wings or a colourful hairstyle.','Let each friend have a different expression.','Make a scene and give everyone a name.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=paper(479,323,770,382,-1)
  for x,y,s,ang,c,k in [(206,289,.7,-14,'red','oak'),(319,339,.58,20,'gold','maple'),(372,228,.4,48,'green','point')]:a+=leaf(x,y,s,ang,c,k)
  for x,y,X,Y in [(539,218,539,408),(591,246,665,308),(642,223,579,408)]:a+=twig(x,y,X,Y,11)
  a+=circle(753,267,47,'#f4dfb9',INK,3)+circle(765,381,40,'#f4dfb9',INK,3)
  a+=note(284,495,'Leaf outfits')+note(653,495,'Twigs + paper faces')
 elif n==2:
  a+=paper(475,324,530,384,-1)+leaf_friend(475,312,1.1,2)
  a+=arrow(748,215,542,199,-18)+note(782,182,'Paper face',size=25)+arrow(182,371,427,434,18)+note(162,331,'Twig limbs',size=25)
 elif n==3:
  a+=paper(472,326,530,384,-1)+leaf_friend(472,308,1.07,3)
  a+=leaf(776,307,.52,18,'red','oak')+arrow(726,315,575,362,-15)+note(778,436,'Overlap leaves',size=25)
  a+=hand(150,268,.52,32)+arrow(203,234,379,204,-15)+note(158,404,'Try leafy hair',size=24)
 elif n==4:
  a+=paper(471,326,530,384,-1)+leaf_friend(471,307,1.08,4)
  a+=path('M708 170 L773 220 L761 235 L697 185 Z','#d6a66b',INK,3)+path('M697 185 L691 163 L708 170 Z','#f0d7ac',INK,2)+arrow(688,204,535,198,15)+note(787,158,'Draw a face',size=25)
  a+=glue(178,372,.68)+note(177,464,'Optional adult help',size=23)
  a+=note(789,416,'Keep it flat',size=25)
 else:
  a+=paper(480,329,778,390,-1)+leaf_friend(324,314,.99,5,'red',True,-3)+leaf_friend(644,314,.99,5,'green',False,4)
  a+=leaf(164,455,.24,-38,'gold','oval')+leaf(796,452,.25,45,'red','maple')+camera(811,191,.46)
  a+=note(324,516,'One of a kind',size=25)+note(644,516,'Made by you',size=25)
 a+=footer(['Work on flat ground or a paper backing.','Rearrange the pieces until the pose feels right.','A grown-up handles any optional cutting.','No glue needed; grown-ups can help attach to backing.','Photograph your scene and gather added materials.'][n-1])
 return a

DEFS='''<defs>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f8e29a"/><stop offset=".55" stop-color="#ebca72"/><stop offset="1" stop-color="#d6a959"/></linearGradient>
<linearGradient id="red" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f0b3a1"/><stop offset=".5" stop-color="#dd9583"/><stop offset="1" stop-color="#c97467"/></linearGradient>
<linearGradient id="orange" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f6d2a1"/><stop offset=".55" stop-color="#edb181"/><stop offset="1" stop-color="#d98f67"/></linearGradient>
<linearGradient id="green" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c4d8ac"/><stop offset=".6" stop-color="#a6bf8a"/><stop offset="1" stop-color="#7fa16c"/></linearGradient>
<marker id="arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="7" markerHeight="7" orient="auto"><path d="M2 2 L10 6 L2 10" fill="none" stroke="#d75b38" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></marker>
<clipPath id="roofclip"><path d="M-165 -35 L149 -35 L218 -151 L-84 -151 Z"/></clipPath>
</defs>'''

CATALOGUE={}
try:CATALOGUE={x['id']:x for x in json.loads((ROOT/'content/activities.json').read_text())}
except (FileNotFoundError,json.JSONDecodeError):pass
TASKS={'FAL-06':('Leafy Friend',leafy),'FAL-07':('Fall Fairy Garden',garden),'FAL-08':('Autumn Nature Mandalas',mandala),'FAL-09':('Meet Fall Friends',friends)}
OUT.mkdir(parents=True,exist_ok=True)
for aid,(name,draw) in TASKS.items():
 for n in range(1,6):
  entry=CATALOGUE.get(aid,{});steps=entry.get('steps',[]);st=steps[n-1] if len(steps)>=n else {}
  title=f'{entry.get("title",name)} — step {n}: {st.get("title", "illustrated instructions")}'
  desc=st.get('text',f'Cartoon construction diagram for {name}, step {n}. Natural materials are loose or supported as shown; adult assistance is indicated where needed.')
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(desc)}</desc>{DEFS}{background()}{draw(n)}</svg>'
  (OUT/f'{aid}-{n}.svg').write_text(svg)
print('Generated 20 original cartoon instruction SVGs: FAL-06 through FAL-09.')
