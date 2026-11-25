#!/usr/bin/env python3
"""Generate twenty precise original pastel summer craft diagrams.
Run: python3 scripts/generate-summer-diagrams.py
Reads catalogue metadata; writes only SUM-06–09 step SVGs.
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
SAND='#e3c596'; SANDDARK='#b89262'; PEBBLE='#b8bca9'
def header(t,sub=''):
 return circle(45,49,22,'#dce9ce',INK,2)+text(45,58,CURRENT_STEP,25,weight=700)+text(493,58,t,32,weight=700)+(text(480,98,sub,23,c='#6c705a',weight=500) if sub else '')
def flower(x,y,s=1,col='#ebbbcc'):
 a=''
 for i in range(6):
  t=i*math.pi/3;xx=math.sin(t)*17;yy=-math.cos(t)*17
  a+=ellipse(xx,yy,12,18,col,'#a17b88',2,attrs=f'transform="rotate({i*60} {xx} {yy})"')
 a+=circle(0,0,10,'#efd07b',INK,2)
 return grp(a,f'translate({x} {y}) scale({s})')
def grass(x,y,s=1):
 a=''
 for i in range(7):
  xx=(i-3)*16;yy=-56-23*(1-abs(i-3)/3)
  a+=path(f'M0 15 Q{xx*.3} -31 {xx} {yy}',stroke=['#7e9d72','#9bb583','#b3c794'][i%3],sw=5)
 return grp(a,f'translate({x} {y}) scale({s})')
def moss(x,y,s=1):
 a=path('M-68 25 Q-89 0 -65 -19 Q-72 -46 -42 -48 Q-32 -77 -5 -58 Q17 -78 36 -52 Q71 -60 70 -29 Q95 -12 74 12 Q72 45 43 39 Q20 64 0 42 Q-27 62 -46 38 Q-65 50 -68 25 Z','#91ad77','#627c57',3)
 for xx,yy in [(-43,-17),(-15,-36),(20,-28),(50,-4),(-24,12),(14,23)]:a+=path(f'M{xx-8} {yy+5} L{xx} {yy-6} L{xx+7} {yy+5}',stroke='#c1d3a6',sw=3)
 return grp(a,f'translate({x} {y}) scale({s})')
def pebble_eye(x,y,r=5):return circle(x,y,r,DARK,'none',0)+circle(x-r*.25,y-r*.3,r*.22,CREAM,'none',0)
def bigstone(x,y,rx=75,ry=60,col=PEBBLE):
 a=path(f'M{-rx} 0 C{-rx*1.05} {-ry*.63} {-rx*.6} {-ry*1.05} 0 {-ry} C{rx*.65} {-ry*1.05} {rx*1.03} {-ry*.52} {rx} 5 C{rx*.97} {ry*.74} {rx*.42} {ry} {-rx*.12} {ry*.95} C{-rx*.7} {ry} {-rx*1.04} {ry*.54} {-rx} 0 Z',col,'#73816c',3)
 a+=path(f'M{-rx*.63} {-ry*.16} Q{-rx*.4} {-ry*.7} {rx*.16} {-ry*.7}',stroke='#e2e3ce',sw=5)
 for xx,yy in [(.4,.28),(-.4,.44),(.64,-.08)]:a+=circle(xx*rx,yy*ry,2,'#929d88','none',0)
 return grp(a,f'translate({x} {y})')
def summer_pattern(x,y,s=1,stage=5):
 a=''
 # Small irregularities make the repeated pattern deliberately child-made.
 if stage>=4:
  for i in range(12):
   t=i*math.pi/6+.025*math.sin(i*2);r=178+6*math.sin(i*1.3)
   if i%3==0:a+=flower(math.sin(t)*r,-math.cos(t)*r,.48,['#e8bfd4','#ddd0e8'][i%2])
   else:a+=stone(math.sin(t)*r,-math.cos(t)*r,.32,(i%3-1)*13,'#b7bfaa')
  for i in range(6):
   t=i*math.pi/3+.2;a+=twig(math.sin(t)*207,-math.cos(t)*207,math.sin(t+.035)*238,-math.cos(t+.035)*238,7)
 if stage>=3:
  for i in range(8):
   t=i*math.pi/4+.03*math.sin(i);r=104+5*math.cos(i*2)
   a+=leaf(math.sin(t)*r,-math.cos(t)*r,.46+(i%3)*.015,i*45+(i%2)*5,['green','gold','green','orange'][i%4],'oval')
 a+=bigstone(0,0,40,34,'#c1c5ac')
 if stage>=5:a+=flower(0,0,.57,'#e8bfd4')
 return grp(a,f'translate({x} {y}) scale({s})')
def summer_mandala(n):
 titles=['Sort a little collection of summer','Choose a favourite centre','Make a repeating ring','Try a different outer ring','A pattern that is all your own']
 subs=['Loose leaves and stones; twigs and flowers are optional.','Leave room for the pattern to grow around it.','Repeat a shape or alternate a pair of colours.','Leaves, flowers or stones can change the rhythm.','A little uneven can be a lovely part of making.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  for x,y,s,ang,c in [(182,263,.61,-22,'green'),(271,333,.55,17,'gold'),(345,253,.47,35,'green')]:a+=leaf(x,y,s,ang,c,'oval')
  for x,y,s in [(488,269,.66),(553,349,.5),(456,391,.41)]:a+=stone(x,y,s)
  a+=twig(684,240,725,427,12)+twig(742,279,683,411,10)+flower(806,291,.9)+flower(813,402,.67,'#d9c6e5')
  a+=note(257,507,'Leaves')+note(506,507,'Stones')+note(746,507,'Optional extras',size=25)
 elif n==2:
  a+=dash('M275 336 A205 165 0 1 1 685 336 A205 165 0 1 1 275 336','#d5d8bd',3)+bigstone(480,328,84,66)
  a+=arrow(235,227,393,300,12)+note(190,198,'Start here',size=26)+leaf(787,337,.6,17,'green','oval')+note(789,461,'Or a leaf',size=24)
 elif n==3:
  a+=summer_pattern(480,335,1.12,3)+leaf(800,259,.43,42,'green','oval')+arrow(750,279,625,252,14)+note(792,409,'Repeat around',size=25)
 elif n==4:
  a+=summer_pattern(480,335,.88,4)+arrow(166,226,307,231,15)+note(145,185,'A new ring',size=25)+arrow(810,426,684,416,-12)+note(812,472,'Keep the spaces',size=24)
 else:
  a+=summer_pattern(466,333,.89,5)+camera(805,244,.62)+sparkle(799,362,.7)+leaf(176,448,.32,-33,'green','oval')+note(809,437,'Remember it',size=25)
 a+=footer(['Use permitted loose pieces; leave growing plants alone.','One centre piece is enough to begin.','Turn leaf tips inward or outward.','Build one ring at a time and stop at any size.','Take a photo, then gather your natural materials.'][n-1])
 return a

def rocky_turtle(x,y,s=1,stage=5):
 a=''
 if stage>=3:
  for xx,yy,ang in [(-75,-46,-35),(75,-46,35),(-74,70,25),(74,70,-25)]:a+=stone(xx,yy,.47,ang,'#a8b29e')
  a+=stone(0,116,.27,90,'#a8b29e')
 a+=bigstone(0,25,76,84,'#b4c0a4')+bigstone(0,-92,36,30,'#bcc4ad')
 if stage>=4:
  a+=pebble_eye(-12,-96,4.6)+pebble_eye(12,-96,4.6)+smile(0,-81,10)
  a+=path('M-35 11 Q0 -19 35 11 L28 60 Q0 82 -28 60 Z',stroke='#7b8e6d',sw=2.4)+line(0,-4,0,-46,'#7b8e6d',2.4)+line(-32,35,-68,35,'#7b8e6d',2.4)+line(32,35,68,35,'#7b8e6d',2.4)
 return grp(a,f'translate({x} {y}) rotate(-4) scale({s})')
def rocky_frog(x,y,s=1):
 a=''
 for xx,yy,ang in [(-70,66,-35),(70,66,35),(-70,-22,35),(70,-22,-35)]:a+=stone(xx,yy,.52,ang,'#9fac90')
 a+=bigstone(0,36,62,66,'#a6b394')+bigstone(0,-49,68,37,'#b7c1a5')
 a+=pebble_eye(-29,-56,7)+pebble_eye(29,-56,7)+smile(0,-33,25)
 return grp(a,f'translate({x} {y}) scale({s})')
def rocky_dragonfly(x,y,s=1):
 a=''
 for xx,yy,ang in [(-66,-45,24),(66,-45,-24),(-62,22,-23),(62,22,23)]:a+=grp(stone(0,0,1,0,'#b9c5b0'),f'translate({xx} {yy}) rotate({ang}) scale(1.1 .65)')
 for j in range(5):a+=stone(0,-57+j*35,.29-j*.015,90,'#96a78d')
 a+=bigstone(0,-98,27,23,'#acb89f')+pebble_eye(-9,-101,3.7)+pebble_eye(9,-101,3.7)
 a+=twig(-10,-118,-24,-145,5)+twig(10,-118,24,-145,5)
 return grp(a,f'translate({x} {y}) scale({s})')
def rocky_friends(n):
 titles=['Find broad, smooth stones','Start with a body and a head','Add feet, wings or a little tail','Give your friend a face','Meet the rocky friends']
 subs=['Choose stones that sit steadily on their flat sides.','Lay the stones beside one another, not in a tall stack.','Try the smaller shapes around the bigger ones.','A few crayon marks or suitable large stones can work.','A turtle, a frog or a dragonfly: invent your own.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=paper(480,331,742,370,-1)
  for x,y,rx,ry,c in [(236,269,71,48,'#bdc3b0'),(414,330,64,83,'#b0bca3'),(604,262,85,43,'#c4c6b2'),(728,390,45,36,'#a7b59c')]:a+=bigstone(x,y,rx,ry,c)
  a+=stone(229,420,.53)+stone(597,422,.6)+note(487,513,'Flat sides down',size=26)
 elif n==2:
  a+=paper(480,331,535,371,-1)+rocky_turtle(478,337,1.06,2)
  a+=arrow(226,274,432,253,-15)+note(174,229,'Head',size=27)+arrow(769,392,569,380,18)+note(797,354,'Body',size=27)
 elif n==3:
  a+=paper(480,330,535,373,-1)+rocky_turtle(478,337,1.06,3)
  a+=stone(186,296,.48,-35)+arrow(229,304,384,291,-12)+note(184,378,'Four flat feet',size=25)+note(792,430,'A small tail',size=25)+arrow(737,447,506,469,-12)
 elif n==4:
  a+=paper(480,330,535,373,-1)+rocky_turtle(478,337,1.06,4)
  a+=grp(rect(-53,-11,106,22,'#95ad7c',INK,3,4)+path('M53 -11 L78 0 L53 11 Z','#dbc5a0',INK,2),'translate(764 233) rotate(24)')
  a+=arrow(709,249,525,240,-10)+note(788,335,'Optional crayon',size=23)+note(787,366,'eyes and details',size=23)
  a+=twig(173,371,213,423,8)+note(180,471,'Or twig details',size=23)
 else:
  a+=paper(480,334,834,377,-1)+rocky_turtle(212,332,.89,5)+rocky_frog(486,343,.94)+rocky_dragonfly(764,345,.87)
  a+=note(213,510,'Turtle',size=25)+note(486,510,'Frog',size=25)+note(765,510,'Dragonfly',size=25)+camera(838,180,.42)
 a+=footer(['A grown-up checks each stone before you begin.','Build the picture flat on a tray or the ground.','Turn stones until the shapes feel right.','Keep every piece flat. No glue or tall stacking.','Take a picture before rearranging the loose stones.'][n-1])
 return a

def bark_body(x,y,s=1):
 a=path('M-63 -106 L-39 -126 L-11 -116 L12 -132 L54 -111 L69 -36 L57 27 L76 116 L43 137 L8 127 L-24 139 L-66 117 L-56 47 L-73 -12 Z','#ac855d',INK,3)
 for xx in [-42,-20,4,25,46]:a+=path(f'M{xx} -100 Q{xx-9} -45 {xx+4} 0 Q{xx-8} 61 {xx+3} 113',stroke=['#cfab7b','#846448'][int(abs(xx))%2],sw=4)
 return grp(a,f'translate({x} {y}) scale({s})')
def bark_friend(x,y,s=1,stage=5):
 a=''
 if stage>=3:
  a+=twig(-45,0,-126,-37,9)+twig(-126,-37,-142,-70,7)+twig(-126,-37,-158,-42,6)+twig(45,0,127,-30,9)+twig(127,-30,148,-65,7)+twig(-26,106,-52,174,10)+twig(26,106,52,174,10)
 a+=bark_body(0,0,1)
 if stage>=4:
  a+=moss(0,-95,.86)+moss(-52,-40,.42)+moss(51,-28,.4)+leaf(0,61,.55,10,'green','oak')
  a+=stone(-24,-23,.22,0,'#e0ddc7')+stone(24,-23,.22,0,'#e0ddc7')+pebble_eye(-24,-23,3.7)+pebble_eye(24,-23,3.7)+smile(0,5,20)
 if stage>=5:a+=flower(33,-130,.4,'#e0cae6')+sparkle(102,-91,.45)
 return grp(a,f'translate({x} {y}) scale({s})')
def leaf_butterfly(x,y,s=1):
 a=''
 for xx,yy,ang,c,k in [(-66,-53,-47,'green','oval'),(66,-53,47,'gold','oval'),(-52,42,-130,'green','point'),(52,42,130,'gold','point')]:a+=leaf(xx,yy,.62,ang,c,k)
 a+=twig(0,-93,0,105,10)+twig(-3,-94,-24,-125,5)+twig(3,-94,24,-125,5)+stone(0,-101,.23)+pebble_eye(-7,-104,2.8)+pebble_eye(7,-104,2.8)
 return grp(a,f'translate({x} {y}) scale({s})')
def stone_fairy(x,y,s=1):
 a=twig(-35,12,-100,-21,8)+twig(35,12,100,-21,8)+twig(-20,80,-43,153,8)+twig(20,80,43,153,8)
 a+=leaf(-58,-25,.59,-44,'green','oval')+leaf(58,-25,.59,44,'gold','oval')+bigstone(0,42,43,65,'#c4c8b3')+bigstone(0,-58,30,27,'#d4d6bf')
 a+=leaf(-11,-90,.29,-60,'green','oval')+flower(16,-101,.42)+pebble_eye(-10,-63,3.6)+pebble_eye(10,-63,3.6)+smile(0,-47,10)
 return grp(a,f'translate({x} {y}) scale({s})')
def wilderness(n):
 titles=['Imagine a woodland character','Choose a flat body','Tuck in limbs or leaf wings','Add hair, clothes and a face','Our wilderness creatures']
 subs=['Sort loose pieces by the parts they might become.','Bark, a broad leaf or a stone can start the idea.','Lay ends under the body to hold the arrangement.','Use already-loose moss or grass; leave living moss alone.','A mossy friend, a butterfly or a stone-and-leaf fairy.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=paper(480,330,786,373,-1)+bark_body(231,318,.87)+leaf(385,275,.6,22,'green','oak')+grass(410,417,.67)+moss(556,265,.71)+stone(576,411,.49)
  a+=twig(713,233,748,435,11)+twig(763,260,700,414,9)+flower(815,276,.55)
  a+=note(251,518,'Body shapes',size=25)+note(614,518,'Arms, wings, hair and faces',size=24)
 elif n==2:
  a+=paper(475,329,500,375,-1)+bark_friend(475,314,1.08,2)+leaf(173,306,.58,-15,'green','oak')+bigstone(790,320,56,73)
  a+=note(179,443,'Or a large leaf',size=24)+note(789,443,'Or a stone',size=24)
 elif n==3:
  a+=paper(475,330,560,376,-1)+bark_friend(475,311,1.06,3)
  a+=twig(171,268,230,310,9)+arrow(238,290,405,312,18)+note(185,386,'Tuck ends under',size=23)
  a+=leaf(792,308,.45,30,'green','oval')+note(789,432,'Try leaf wings',size=24)
 elif n==4:
  a+=paper(475,330,560,376,-1)+bark_friend(475,310,1.06,4)+moss(176,244,.58)+arrow(238,248,415,210,15)+note(174,341,'Already-loose moss',size=22)
  a+=stone(788,272,.36,0,'#d9dbc4')+arrow(741,282,530,284,15)+note(790,370,'Stone features',size=24)
 else:
  a+=paper(480,330,843,385,-1)+bark_friend(212,315,.89,5)+leaf_butterfly(490,335,.86)+stone_fairy(767,325,.87)
  a+=note(208,518,'Mossy friend',size=24)+note(493,518,'Leaf butterfly',size=24)+note(767,518,'Stone fairy',size=24)
 a+=footer(['A made-up creature can look any way you like.','Keep the entire creation flat on its backing.','Try each pose before adding more pieces.','Decorate with loose materials; never strip a tree.','Name your friends, photograph them and tidy up.'][n-1])
 return a

def shell(x,y,s=1,ang=0):
 a=path('M-28 25 L-43 -5 Q-40 -29 -23 -28 Q-11 -43 0 -29 Q13 -41 25 -26 Q43 -26 44 -4 L28 25 Q0 14 -28 25 Z','#f2dec6','#ac9279',2.5)
 for xx in [-30,-15,0,15,30]:a+=path(f'M0 19 Q{xx*.36} -2 {xx} -24',stroke='#d3b79b',sw=2)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def sand_patch():
 a=ellipse(0,0,330,200,SAND,'#b99b72',3)
 rng=random.Random(92)
 for _ in range(75):
  x=rng.uniform(-310,310);y=rng.uniform(-180,180)
  if (x/330)**2+(y/200)**2<.89:a+=circle(x,y,rng.uniform(.8,2.1),'#c4a776','none',0)
 return a

def spiral_points():
 pts=[(0,202),(0,180)]
 for i in range(241):
  t=i/240;th=math.pi/2+t*4*math.pi;r=220-200*t+4*math.sin(th*3)+3*math.sin(th*7)
  pts.append((r*math.cos(th),.7*r*math.sin(th)))
 return pts
ROUTE=spiral_points()
def distance_to_route(x,y):
 distance=float('inf')
 for a,b in zip(ROUTE,ROUTE[1:]):
  dx=b[0]-a[0];dy=b[1]-a[1]
  t=max(0,min(1,((x-a[0])*dx+(y-a[1])*dy)/(dx*dx+dy*dy or 1)))
  distance=min(distance,math.hypot(x-a[0]-t*dx,y-a[1]-t*dy))
 return distance
def safe_edge_position(i,side,radius):
 px,py=ROUTE[i];p0=ROUTE[i-1];p1=ROUTE[i+1];dx=p1[0]-p0[0];dy=p1[1]-p0[1];length=math.hypot(dx,dy)
 nx=-dy/length;ny=dx/length
 for offset in [32*side,-32*side,40*side,-40*side]:
  xx=px+nx*offset;yy=py+ny*offset
  if distance_to_route(xx,yy)>=radius+13.5+5:return xx,yy
 return None
def routepath(points):return 'M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in points)
def stroke_path(points,col,w,cap='butt',attrs=''):
 return f'<path d="{routepath(points)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round" {attrs}/>'
def maze_art(x,y,s=1,stage=5,water=False,rocky=False):
 a=sand_patch();route=''
 if stage>=2:
  if stage>=3:
   route+=stroke_path(ROUTE,'#ba9668',51)+stroke_path(ROUTE,'#efd5a1',43)
  route+=stroke_path(ROUTE,'#c39e6f',27 if stage>=3 else 15)+stroke_path(ROUTE,'#d4b17f',21 if stage>=3 else 10)
  # An open entrance reaches the centre. Butt caps never close it with a wall.
  end=ROUTE[-1];route+=circle(end[0],end[1],14,'#d4b17f','none',0)
  if stage>=4:
   for j,i in enumerate(range(13,220,13)):
    side=1 if j%3 else -1
    radius=45*(.23+(j%2)*.035) if rocky or j%3 else 44*.28
    position=safe_edge_position(i,side,radius)
    if position is None:continue
    xx,yy=position
    if rocky or j%3:route+=stone(xx,yy,.23+(j%2)*.035,(j%5-2)*12,'#b5bba6')
    else:route+=shell(xx,yy,.28,(j%5-2)*13)
   route+=flower(-30,-10,.43,'#e2bed0')
  if water:
   route+=stroke_path(ROUTE[:23],'#a8ced0',15)+stroke_path(ROUTE[3:18],'#d9ece6',3)
 a+=grp(route,attrs='clip-path="url(#sandclip)"')
 return grp(a,f'translate({x} {y}) scale({s})')
def watercup(x,y,s=1,ang=0):
 a=path('M-38 -35 L38 -35 L28 45 Q0 57 -28 45 Z','#b2ccd0',INK,3)+ellipse(0,-35,38,10,'#d7e9e4',INK,3)+path('M38 -18 Q70 -21 67 12 Q65 32 32 29',stroke=INK,sw=4)
 a+=path('M-23 -1 Q0 -8 25 -1 L20 31 Q0 38 -20 31 Z','#85b8c4','none',0)
 return grp(a,f'translate({x} {y}) rotate({ang}) scale({s})')
def waterdrop(x,y,s=1):return grp(path('M0 -20 Q-21 8 -10 20 Q0 30 10 20 Q21 8 0 -20 Z','#9bc8ce','#729a9e',2),f'translate({x} {y}) scale({s})')
def sandy(n):
 titles=['Choose a safe little sandy place','Draw an open route to the centre','Build low walls beside the line','Decorate the edges, not the route','Explore a little water, or keep it dry']
 subs=['Slightly damp sand in a shallow tray or away from the shore.','A finger or blunt stick makes a lovely wiggly line.','Keep the entrance and every turn open.','Smooth pebbles and empty shells stay outside the path.','Sand may soak up the water. That is part of exploring.']
 a=header(titles[n-1],subs[n-1])
 if n==1:
  a+=maze_art(453,343,.93,1)+hand(216,248,.58,35)+arrow(247,237,349,286,-12)
  a+=watercup(799,385,.78,0)+shell(770,228,.62,-10)+stone(840,271,.48)+flower(826,180,.65)+twig(192,420,258,465,10)
  a+=note(189,180,'Pat it flat',size=25)+note(800,508,'Set details beside it',size=22)
 elif n==2:
  a+=maze_art(480,330,1,2)+twig(774,173,637,255,11)+arrow(748,265,645,274,-10)
  a+=note(785,160,'Finger or blunt stick',size=22)+note(791,487,'Open entrance',size=23)+arrow(741,501,498,531,-8)
  a+=note(777,369,'Trace to the centre',size=23)
 elif n==3:
  a+=maze_art(480,330,1,3)+hand(170,285,.55,45)+arrow(225,275,287,306,-12)+note(171,204,'Low walls',size=25)
  a+=note(795,466,'Leave turns clear',size=23)+arrow(744,435,663,416,-13)
 elif n==4:
  a+=maze_art(480,330,1,4)+shell(807,213,.58,20)+arrow(773,245,656,249,18)+note(805,176,'Beside the path',size=23)
  a+=note(173,457,'A clear route',size=24)+arrow(226,465,371,468,-10)
 else:
  a+=maze_art(337,327,.86,5,True)+maze_art(766,244,.41,3)+maze_art(766,441,.41,4,False,True)
  a+=watercup(438,458,.52,-35)+waterdrop(388,483,.28)+waterdrop(367,494,.22)
  a+=twig(108,455,213,407,9)+note(176,176,'Test with a finger or stick',size=23)
  a+=note(765,351,'Dry spiral',size=24)+note(765,549,'Rock-lined route',size=24)+note(327,551,'One shallow channel',size=24)
 a+=footer(['A grown-up approves the place and the materials.','Follow the line from the outside all the way in.','Uneven, crumbly edges are part of the fun.','Keep enough room to follow it with one finger.','Try a small trickle, then photograph your maze.'][n-1])
 return a

# Revised third wilderness variation matches the generated gallery: a flat bird.
def stone_bird(x,y,s=1):
 a=twig(-22,59,-37,126,8)+twig(18,60,27,126,8)+twig(-37,126,-57,130,6)+twig(27,126,49,130,6)
 a+=leaf(76,22,.55,50,'green','point')+leaf(82,48,.44,80,'gold','oval')+bigstone(0,20,67,55,'#bec5ad')+bigstone(-50,-46,31,27,'#ced0b8')
 a+=leaf(13,19,.53,100,'green','oak')+twig(-80,-47,-105,-42,7)+pebble_eye(-56,-50,5)+leaf(-41,-76,.21,32,'gold','oval')
 return grp(a,f'translate({x} {y}) scale({s})')
# Function lookup occurs at render time; reuse the drawing slot without altering other panels.
stone_fairy=stone_bird
DEFS=DEFS.replace('</defs>','<clipPath id="sandclip"><ellipse cx="0" cy="0" rx="330" ry="200"/></clipPath></defs>')
CATALOGUE={a['id']:a for a in json.loads((ROOT/'content/activities.json').read_text())}
TASKS={'SUM-06':summer_mandala,'SUM-07':rocky_friends,'SUM-08':wilderness,'SUM-09':sandy}
OUT.mkdir(parents=True,exist_ok=True)
for aid,draw in TASKS.items():
 activity=CATALOGUE[aid]
 for n,step in enumerate(activity['steps'],1):
  CURRENT_STEP=n;title=f'{activity["title"]} — step {n}: {step["title"]}'
  body=draw(n)
  if aid=='SUM-08':body=body.replace('stone-and-leaf fairy','stone-and-leaf bird').replace('Stone fairy','Leafy bird')
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="630" viewBox="0 0 960 630" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(step["text"])}</desc>{DEFS}{background()}{body}</svg>'
  (OUT/f'{aid}-{n}.svg').write_text(svg)
print('Generated twenty SUM-06–09 pastel cartoon instruction panels.')
