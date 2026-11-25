"""Apply four summer replacements while preserving earlier saved-project IDs."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def material(name,quantity,kind='nature',optional=False):
    return dict(name=name,quantity=quantity.replace(', optional','') if optional else quantity,kind=kind,optional=optional)
def step(title,text,littleTask='',youngTask='',adultTask=''):
    return dict(title=title,text=text,littleTask=littleTask,youngTask=youngTask,adultTask=adultTask)

summer=[
 dict(
  id='SUM-06',title='A summer nature mandala',subtitle='Little treasures, growing circles, and your own summer pattern.',
  description='Arrange leaves, stones, twigs and colourful flowers into a circular summer pattern. Start with one special piece in the middle and add a new ring around it. Make a tiny design or a bigger shared mandala, using what you find.',
  ages=['little','young'],together=True,minutes=30,prepMinutes=5,
  setting='Outside on flat ground or a reusable tray',difficulty='Make it simple or detailed',tags=['mandala','patterns','leaves','stones','twigs','flowers','summer'],
  materials=[material('Loose leaves in different shapes','A few handfuls'),material('Smooth stones too large to swallow','6–15'),material('Short blunt fallen twigs','6–12','nature',True),material('Loose petals or flowers approved by a grown-up','A small handful','nature',True),material('Flat ground or a reusable tray','1 clear space','home')],
  adultNote='Check collected pieces and choose sizes suitable for the children. Use loose materials where gathering is allowed. A grown-up identifies any flowers; leave plenty for insects. No glue or scissors are needed.',
  littleRole='Choose the centre and repeat a simple ring of leaves or stones.',youngRole='Build new repeating patterns, alternate colours and balance the outer rings.',
  togetherPlan='A Little Maker chooses the centre and first ring. A Young Creator adds another pattern around it. Take turns choosing the next colour or shape.',
  steps=[
   step('Gather and sort your treasures','With a grown-up, collect loose leaves, smooth stones and any approved twigs, flowers or petals. Sort them into little piles by colour, shape or size. Choose a flat place with enough space for your circles to grow.','Sort leaves and stones into piles.','Look for several pieces that can repeat in a pattern.','Check the materials and approve the making space.'),
   step('Choose a special centre','Put one favourite stone, leaf or flower in the middle of your space. Leave room around it for several rings. Turn it until it looks right to you; your mandala can be big, small or a little wonky.','Place your favourite piece in the middle.','Plan the size and direction of the first ring.'),
   step('Make a repeating first ring','Place a circle of leaves or stones around your centre. Repeat one kind of piece, or alternate two colours or shapes. Keep going until the ring meets itself. Leave little gaps so each piece is easy to see.','Repeat a leaf or a stone all the way around.','Try an alternating broad-leaf, narrow-leaf pattern.'),
   step('Grow another summer pattern','Add a new ring outside the first. Try stones between leaves, twigs like sun rays, or approved petals for splashes of colour. Change the repeating rule with each ring and use the materials you have. Stop whenever the design feels complete.','Add a piece in each outside gap.','Build an outer ring with a different colour or repeating rule.'),
   step('Make the pattern your own','Step back and look at your summer mandala. Move any pieces you like, add a border, or leave it beautifully simple. Show someone your repeating pattern and take a picture before the breeze changes it.','Point out your favourite colour or shape.','Explain the repeating rule in each ring.','Help photograph the design and restore the space afterwards.')
  ],
  keep='This is temporary outdoor art. A photograph keeps the pattern after wind, footsteps or weather changes it.',
  cleanup='Clear paths and play spaces. Return loose natural pieces only where permitted, take home anything you brought, and leave living plants and habitats undisturbed.',
  extension='Make a tiny mandala beside a large one, try only two colours, or let a friend choose the rule for the next ring.',
  examples=['A leafy summer circle','A flower-and-stone pattern','A bright petal mandala'],waitLabel=''
 ),
 dict(
  id='SUM-07',title='Rocky friends',subtitle='A few stones can become a whole new friend.',
  description='Turn smooth stones into a turtle, frog, dragonfly or an animal only you could imagine. Lay the pieces flat and move them around until your rocky friend appears. Start with a simple shape, then add as many details as you like.',
  ages=['little','young'],together=True,minutes=25,prepMinutes=5,
  setting='Outside or on a flat tray',difficulty='Make it simple or detailed',tags=['rocks','stones','pebbles','animals','friends','summer'],
  materials=[material('Smooth flat stones in several shapes, all suitable for the children','6–15'),material('Flat ground or a reusable tray','1 space','home'),material('Short blunt fallen twigs for whiskers, legs or antennae','2–6','nature',True),material('Crayon for optional eyes on stones you own','1','home',True)],
  adultNote='Choose stones children can handle easily and sizes too large to swallow. Keep the artwork flat; no heavy stones or tall stacks are needed. Do not lift habitat stones or take stones where collecting is restricted. Draw only on stones you own and take marked stones home.',
  littleRole='Choose a big body stone, then add a head and feet.',youngRole='Build wings, a long tail or a detailed creature using different stone shapes.',
  togetherPlan='A Little Maker chooses and places the body. A Young Creator helps arrange the legs, wings or tail. Decide together what your friend is called.',
  steps=[
   step('Find interesting stone shapes','Set out smooth stones checked by a grown-up. Look for broad, narrow, round and oval shapes. Arrange them on a flat tray or clear ground and imagine what each one could become. You can use just a few pieces.','Choose a big body stone and a smaller head.','Sort stones that could become wings, feet or a tail.','Choose manageable stones and a place where using them is allowed.'),
   step('Lay out a body and a head','Put your largest flat stone down for the body and a smaller one beside it for the head. Turn the pieces to try different shapes. Keep both on the ground or tray, rather than balancing the head on top.','Place the body and head next to each other.','Try a turtle shell, a round frog or a long insect body.'),
   step('Give your friend feet or wings','Arrange smaller flat stones around the body. Four oval stones can make turtle feet; long stones can become dragonfly wings or frog legs. Add a tail if you want. Move the pieces until your creature looks ready for an adventure.','Add feet on each side of the body.','Use matching shapes for wings or a curved row for a tail.'),
   step('Add a little personality','Choose suitable stones for features or add crayon eyes to a stone you own. Lay short twigs flat for whiskers or antennae. Your creature can also have an imaginary face. Leave the pieces loose so you can change its expression or pose.','Choose where the eyes should go.','Add a face, antennae or another special detail.','Use only suitable large features. Keep marked stones with your own craft supplies.'),
   step('Meet your rocky friend','Give your friend a name and make up a story. Can the same stones become a different animal? Try a turtle, frog or dragonfly, then photograph your favourite arrangement before you move the pieces.','Name your friend and show its feet or wings.','Rearrange the stones into a second creature.','Help photograph the flat artwork and put the stones away safely.')
  ],
  keep='Loose stone art stays flat. Photograph it or keep the stones in a tray to make a new friend another day.',
  cleanup='Take marked stones and your own supplies home. Return unmarked loose stones only where permitted and leave paths clear.',
  extension='Make a family of different-sized friends or turn the same collection into a completely new animal.',
  examples=['A flat stone turtle','A pebble frog friend','A stone dragonfly'],waitLabel='Keep the stones flat. No glue or stacking needed.'
 ),
 dict(
  id='SUM-08',title='Our wilderness creatures',subtitle='Mossy hair, leafy wings, and a friend nobody has met before.',
  description='Combine bark, loose moss, twigs, leaves and stones into a woodland creature of your own. Make a simple mossy friend or a more detailed animal, insect or fairy. This older-maker activity invites patient arranging, experimenting and lots of imagination.',
  ages=['young'],together=False,minutes=40,prepMinutes=10,
  setting='Outside or at a table',difficulty='A bigger challenge',tags=['creatures','moss','bark','twigs','leaves','stones','summer'],
  materials=[material('Loose fallen bark, broad leaves or flat stones for a body and head','2–4 pieces; choose what you have'),material('Short blunt fallen twigs','4–8'),material('Loose leaves for wings, clothes or ears','4–10'),material('Already-detached loose moss or fallen dry grass for hair','A little, optional','nature',True),material('Smooth stones too large to swallow for features','2–4','nature',True),material('Flat ground, a reusable tray or a sheet of reused card','1 work space','home'),material('Crayon for optional details on your own card','1','home',True)],
  adultNote='Gather only loose materials with permission. Never peel living moss or bark from trees, logs or rocks, and do not disturb habitats. Loose grass or leaves can replace moss. Check twigs and stones before use. Keep the creature flat or very low; glue and sharp tools are not required.',
  littleRole='',youngRole='Plan the creature, tuck and overlap its pieces, then add details that give it a personality.',togetherPlan='',
  steps=[
   step('Imagine a wilderness friend','Look at your approved collection of bark, leaves, twigs, stones and loose moss or grass. Choose a simple mossy character or plan a creature with wings, legs or leafy clothes. Sort the pieces by the jobs they could do.','','Choose the body, head and one special feature before building.','Use only moss that is already detached and permitted to collect; otherwise choose loose grass or leaves.'),
   step('Start with the biggest shapes','Lay a broad piece of fallen bark, a leaf or a flat stone down for the body. It can be the face too, or you can add a smaller head beside it. Turn the pieces until you find a shape you like. Keep the design flat so it does not need to balance.','','Try the body and head in a few positions before adding details.'),
   step('Add limbs, wings or a tail','Lay short twigs for arms and legs. Slide their ends under the body to help keep them in place. Overlap leaves for ears, wings or a tail. A pair of broad leaves can make butterfly wings, while thin twigs can make a bird’s legs.','','Tuck the ends under larger pieces and adjust the outline of your creature.'),
   step('Give your creature a personality','Arrange a little already-loose moss or grass for hair, layer leaf clothes, and add suitable stone features. You can draw a face on your own card instead. Keep everything loose and try different expressions. A simple friend is just as good as a detailed one.','','Use texture, colour and shape to invent one detail nobody else has.','Do not pull moss from living surfaces. Keep any marked card with your own supplies.'),
   step('Introduce your new friend','Give your creature a name, a home and an imaginary favourite food. Make a mossy bark friend, a leafy insect or a stone-and-leaf bird, then try your own idea. Photograph the finished arrangement while it is still flat.','','Tell a short story about your creature and explain one clever material choice.','Help photograph the work, take home card and tidy the space.')
  ],
  keep='This is loose, temporary art. Leave it flat on a tray for the making session and photograph it before putting the pieces away.',
  cleanup='Take all card and other supplies home. Return loose natural materials only where permitted without disturbing plants or habitats. Wash hands after making.',
  extension='Make two creatures from the same pieces, or give a mossy friend a leaf-winged companion and invent a shared adventure.',
  examples=['A mossy bark friend','A leaf-winged butterfly','A stone-and-leaf bird'],waitLabel='Moss is optional. Use loose grass or leaves instead.'
 ),
 dict(
  id='SUM-09',title='Sandy Explorer',subtitle='Little paths, shell borders, and a splash of discovery.',
  description='Make a small sand maze with winding paths, low walls, shells and pebbles. Add a flower, build a rock-lined route, or trickle a little water into a shallow channel. Keep it playful and a little wonky—this is a maze made by you.',
  ages=['little','young'],together=True,minutes=35,prepMinutes=5,
  setting='A shallow sand tray or a permitted sandy patch',difficulty='Make it simple or detailed',tags=['sand','maze','shells','pebbles','water','patterns','summer'],
  materials=[material('Clean, slightly damp sand approved by a grown-up','Enough for a shallow tray or small patch'),material('Smooth pebbles, all too large to swallow','8–20'),material('Empty shells with smooth, unbroken edges','A few, optional','nature',True),material('A flower or loose petals approved by a grown-up','1–3, optional','nature',True),material('Blunt stick or small reusable scoop','1','home'),material('Small cup of water for optional channels','1 small cup','home',True),material('Shallow reusable tray if making at home','1, optional','home',True)],
  adultNote='Choose clean sand in a shallow tray or a permitted place away from waves and moving water. Check shells are empty, unbroken and allowed to collect. Use small manageable stones and keep walls and channels low. A grown-up stays beside the makers when water is used. Fill channels and level the sand after play.',
  littleRole='Make a simple winding path and decorate its edges with shells or pebbles.',youngRole='Design branching paths, test a clear route and compare dry and watered channels.',
  togetherPlan='A Little Maker draws the main path and chooses the border. A Young Creator adds turns or short dead ends. Trace the route together before trying a little water.',
  steps=[
   step('Choose your sandy patch','Ask a grown-up to approve a shallow sand tray or small sandy place away from the water’s edge. Pat slightly damp sand into a flat base. Set smooth pebbles, empty shells and any approved flowers beside your work space.','Pat the sand into a flat base.','Choose a space with room for a start and a centre.','Check the sand, shells and stones, and choose a place away from waves or moving water.'),
   step('Draw a winding path','Use a finger or blunt stick to draw an open path from one edge to a special place in the middle. Try a loose spiral or a route with several turns. Older makers can add short dead ends. Trace your main route to check that the entrance really reaches the finish.','Draw one curving path from the edge to the middle.','Add branches while keeping at least one clear route to the finish.'),
   step('Build low sand walls','Push a little damp sand to either side of your line to make low walls and a shallow channel between them. Leave the entrance and turns open. If a wall crumbles, add a little damp sand and pat gently. Uneven walls are part of the fun.','Pat a low wall beside the path.','Check the route again and fix any blocked turns.','Keep all digging shallow and within the approved making area.'),
   step('Decorate the edges','Line parts of the walls with smooth pebbles or empty shells. Add an approved flower or a few petals near the finish. Try a shell-pebble-shell pattern, or make a mostly rock-lined route. Keep decorations beside the path so a finger can still follow it.','Choose a shell or pebble border.','Repeat a border pattern and keep every turn clear.','Keep shells and stones low and remove sharp or broken pieces.'),
   step('Explore with a little water','Follow the route from start to finish with your finger or blunt stick. If you want, slowly pour a little water into one shallow channel and watch where it goes. Sand may soak it up quickly; that is part of exploring. Compare it with a dry path and photograph your maze.','Trace the path and watch a small trickle of water.','Notice where water travels or soaks in, and adjust the route.','Help pour a small amount. When finished, remove decorations, fill channels and level the sand.')
  ],
  keep='Enjoy the maze during play. Drying, water and footsteps will change it; take a picture before levelling the sand.',
  cleanup='Remove shells, stones, flowers and supplies. Fill every channel, flatten the walls, leave the area clear, and wash hands before eating.',
  extension='Make a spiral, a branching maze and a rock-lined path. Compare which turns are easiest to follow, or try decorating the same route in a new pattern.',
  examples=['A shell-and-pebble spiral','A maze with a little water','A winding rock-lined route'],waitLabel='Water may soak into sand quickly. Keep channels shallow.'
 )
]
for a in summer:
    a.update(season='summer',showInstructions=True,reviewStatus='Draft guide — not yet physically tested or reviewed.')
    a['natureNote']='Use loose materials only where collecting is allowed. Ask a grown-up about flowers and empty shells, leave living plants and animals alone, and take your supplies home.'
    for i,s in enumerate(a['steps'],1):s['diagram']=f"/assets/steps/{a['id']}-{i}.svg"
p=ROOT/'content/activities.json'
existing=json.loads(p.read_text())
for a in existing:
    if a['id'] in {f'SUM-0{i}' for i in range(1,6)}:a['archived']=True
ids={a['id'] for a in summer}
existing=[a for a in existing if a['id'] not in ids]
i=next(i for i,a in enumerate(existing) if a['season']=='fall')
existing[i:i]=summer
p.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
print('Added four summer guides; five earlier summer guides retained for saved projects.')
