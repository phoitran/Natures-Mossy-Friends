"""Apply three winter replacements while retaining earlier saved-project guides."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def material(name,quantity,kind='nature',optional=False):
    return dict(name=name,quantity=quantity,kind=kind,optional=optional)
def step(title,text,littleTask='',youngTask='',adultTask=''):
    return dict(title=title,text=text,littleTask=littleTask,youngTask=youngTask,adultTask=adultTask)

winter=[
 dict(
  id='WIN-06',title='Make a little snow man',subtitle='A handful of snow, a twiggy smile and a new winter friend.',
  description='Build a snow person with its own character: a lumpy friend with a pine-cone hat, a classic carrot-nose snowman, or a funny upside-down one with boots. Start small, shape two or three snowballs, and make its face and pose your own.',
  ages=['little','young'],together=True,minutes=25,prepMinutes=5,
  setting='Outside on a flat snowy patch',difficulty='A simple snowy start',tags=['snow','snowman','winter','twigs','stones'],
  materials=[material('Clean snow that packs when squeezed','Several handfuls'),material('Short blunt fallen twigs','2–4'),material('Smooth stones suitable for the children','A few'),material('Fallen leaf or small pine cone','1–2','nature',True),material('Carrot for a nose','1','nature',True),material('Scarf and small boots for an upside-down variation','1 set','home',True),material('Warm outdoor clothes and waterproof mittens','For each maker','home')],
  adultNote='Choose a flat patch away from roads, water and overhead snow or ice. Check loose materials and choose stone sizes suitable for the children. Keep the snow person small and low, with no heavy lifting. Take warm-up breaks and stop if anyone feels cold or wet.',
  littleRole='Pat the snowballs and choose the face and twig arms.',youngRole='Help flatten the joining surfaces and give the snow person its own character.',
  togetherPlan='A Little Maker shapes the base and picks the face. A Young Creator helps join the smaller snowball and add details. Work side by side and let the youngest maker choose the smile.',
  steps=[
   step('Find snow that sticks together','Dress warmly and choose a flat snowy patch with a grown-up. Squeeze a handful of clean snow in your mittens. If it holds together, you are ready. If it stays powdery, save this build for stickier snow rather than adding water that may freeze.','Squeeze a handful of snow.','Check whether the snow holds its shape.','Approve the place and check everyone is warm and dry.'),
   step('Pat a sturdy little base','Press several handfuls into one round snowball. Set it on the ground and flatten the bottom so it sits steadily. Keep it small enough to shape with your hands; this friend does not need giant rolled snowballs.','Pat a round base.','Flatten the bottom and check it sits steadily.'),
   step('Add a smaller snowball','Make a smaller ball for the head. Flatten the top of the base a little, set the head on it and gently press loose snow around the join. You can add a small middle ball first for a three-ball friend. Keep the whole stack low and steady.','Shape the little head.','Help flatten and join the snowballs.','Help with joining if the snowballs wobble; make them smaller if needed.'),
   step('Give your snow person a face','Gently press suitable smooth stones into the head for eyes. Make a smile with a curved twig or marks in the snow and add two twig arms. Try a pine cone for a hat or a carrot for a nose. For an upside-down version, a grown-up can help put the face on the bottom ball and small boots on top of a low, stable stack.','Choose the eyes and smile.','Add arms and a hat or extra snow details.','Check twig ends and help with the upside-down variation; keep the stack low and steady.'),
   step('Meet your little snow man','Name your new friend and take a picture. Give it a snowball neighbour, a pine-cone hat or a different expression. Try a traditional snowman or an upside-down joke with a grown-up helping. Make each friend different, then head inside for a warm-up break.','Choose a name and say hello.','Make a neighbour with a different expression.','Collect loose decorations when play is finished, before the snow melts.')
  ],
  keep='Snow changes with the weather. Enjoy your little friend outside during play and take a picture before it melts.',
  cleanup='Gather every stone, twig, carrot and extra decoration when finished. Take any scarf and boots indoors, leave the snowy patch clear and dry your mittens.',
  extension='Make a tiny family with different shapes and expressions, or give each snow person a name and a winter story.',
  examples=['A pine-cone-hat snow man','A classic carrot-nose snow man','An upside-down snow man with boots'],waitLabel='Snow needs to pack together. Warm-up breaks are part of making.'
 ),
 dict(
  id='WIN-07',title='A pocket-sized snow village',subtitle='Twig-roof cottages, rounded snow houses or a tiny snow castle.',
  description='Build a miniature village from snow, rocks and twigs. Try a twig-roof cottage, rounded snow houses with sprigs on top and twig-lined paths, or a tiny block-shaped snow castle. Mix different shapes and make a little winter world of your own.',
  ages=['young'],together=False,minutes=40,prepMinutes=5,
  setting='Outside on a flat snowy patch',difficulty='More detailed building',tags=['snow','village','houses','rocks','twigs','winter'],
  materials=[material('Clean snow that packs when squeezed','Enough for 2–3 small mounds'),material('Short blunt fallen twigs','A small handful'),material('Small manageable smooth stones','A small handful'),material('Small reusable cups or containers for shaping','2–3','home',True),material('Already-loose evergreen sprigs or dry stems','A few','nature',True),material('Warm outdoor clothes and waterproof mittens','For each maker','home')],
  adultNote='Choose a flat place away from roads, water and overhead snow or ice. Keep every cottage hand-sized, solid and low; these are models, not shelters to enter. Use small stones at ground level and short blunt twigs. Take warm-up breaks and stop if anyone feels cold or wet.',
  littleRole='',youngRole='Choose the house shapes, decorate their roofs and connect the village with paths.',togetherPlan='',
  steps=[
   step('Plan a tiny winter village','Dress warmly and find a flat snowy patch with a grown-up. Test that a handful of snow holds together. Set out a few stones and short blunt twigs, then mark places for two or three hand-sized houses with room for paths between them.','','Choose where the cottages and paths will go.','Check the place, materials and weather; use snow that already packs together.'),
   step('Shape solid snowy cottages','Pat snow into two or three small solid mounds. Shape a cottage with a peaked roof, round houses with flat tops, or low rectangular castle blocks. You can pack snow into a cup or container and turn it out first. Keep each base broad and the inside solid.','','Try a peaked cottage, rounded house or block-shaped castle.'),
   step('Give each roof its character','For a cottage, lay short twigs on the snowy roof slopes and dust them lightly with snow. For round houses, tuck an already-loose evergreen sprig or dry stem into each top. For a castle, shape low snow turrets. Let the solid snow support the details and keep rocks at ground level.','','Choose twig slopes, sprig-topped roofs or little snow turrets.','Check roof pieces and keep all the miniature buildings low and solid.'),
   step('Add doors and village paths','Press a shallow door shape into the front of each cottage without hollowing it out. Arrange a few stones at ground level around the doorway. Connect the houses with a finger-drawn path and use small stones or short twigs to mark its edges.','','Make door outlines and connect the cottages with paths.'),
   step('Tell a snowy village story','Look around your tiny village. Try one twig-roof cottage, a group of round sprig-topped houses, or a snow castle with a pebble courtyard. Connect their doors with branching paths. Imagine who lives there, photograph the scene and gather your decorations before warming up inside.','','Give the cottages names and invent a village story.','Help collect all roof twigs and stones before leaving the making place.')
  ],
  keep='The village is temporary outdoor play. Photograph the twig roofs and winding paths before snow and weather change them.',
  cleanup='Gather all stones, twigs, sprigs, dry stems, containers and supplies. Leave the making place clear and bring outdoor clothes inside to dry.',
  extension='Add a tiny snowy meeting place, draw a new route through the village, or tell a story about a visitor arriving at the smallest cottage.',
  examples=['A tiny twig-roof snow cottage','Round snow houses with twig paths','A tiny snow-block castle village'],waitLabel='Hand-sized solid models only. Keep rocks at ground level.'
 ),
 dict(
  id='WIN-08',title='Snowy Friends',subtitle='Mice, rabbits, cats, a bear or a turtle: choose your snowy friend.',
  description='Turn snow into mice, rabbits, cats, a bear or a turtle. Try tiny creatures, a seated animal or a flat shape on the ground. Older makers can practise shaping and joining snow, then add ears, whiskers and faces to create a friend with its own personality.',
  ages=['young'],together=False,minutes=40,prepMinutes=5,
  setting='Outside on a flat snowy patch',difficulty='A step beyond a snow person',tags=['snow','animals','sculpture','winter','creatures'],
  materials=[material('Clean snow that packs when squeezed','Several generous handfuls'),material('Smooth stones for eyes and a nose','A few'),material('Short blunt twigs or loose dry grass','A few','nature',True),material('Small flat smooth pebbles for mouse ears; fallen leaves for cat ears','2–4','nature',True),material('Small carrot or carrot pieces for noses','1','nature',True),material('Warm outdoor clothes and waterproof mittens','For each maker','home')],
  adultNote='For older makers practising more detailed shaping. Choose a flat place away from roads, water and overhead snow or ice. Start with a low body and broad joins. A grown-up can help with taller ears or seated animals; no hidden sticks are needed inside the snow. Check natural pieces, take warm-up breaks and stop if anyone feels cold or wet.',
  littleRole='',youngRole='Plan the animal shape, blend the joins and add recognisable details.',togetherPlan='',
  steps=[
   step('Choose a snowy creature','Dress warmly and test a handful of snow with a grown-up. Choose mice, a rabbit, cat, bear, turtle or an invented creature. Think about its biggest shape first: an oval mouse, a seated animal or a low turtle shell. Snow that will not pack can wait for another day.','','Choose one creature and picture its main body shape.','Check the place and materials, and make sure everyone stays warm and dry.'),
   step('Build one low body','Press snow into a mound with a broad base. Smooth an oval mouse, a seated rabbit, cat or bear, or a wide dome for a turtle. Begin with a small body. A grown-up can help you build up a larger seated shape without lifting heavy snow.','','Build and smooth the main body before adding small parts.'),
   step('Shape and join the small parts','Pinch a mouse snout from the front, or join a head and paws to a seated animal. Give a turtle a head and four flat flippers. A cat can have a curved tail supported along its body. Press extra snow around each join and blend it in; shorten parts that keep falling off.','','Add the head and limbs, then blend each join with loose snow.'),
   step('Add ears, a face and texture','Shape long rabbit ears, pointed cat ears or round bear ears with broad bases and grown-up help. Mice can have small flat pebble ears, a carrot-tip nose and grass whiskers. Press each pebble partly into the snow so it stays steady. Fallen leaves can make pointed cat ears. Use stone eyes or shallow carved features. A blunt twig can mark a turtle shell or a cat face.','','Add the details that make your creature recognisable.','Check twig ends and natural pieces; keep the snow sculpture low and stable.'),
   step('Introduce your snowy friend','Look at your creature from a few sides and reshape any part you want. Name it, photograph it and try a small companion. Different-sized ears, a crooked smile or an uneven shell can make your friend special. Gather loose details and head inside for a warm-up break.','','Name your creature and decide what makes it special.','Help collect all stones, leaves and twig details before leaving.')
  ],
  keep='Enjoy the sculpture outside during play. Take a picture to remember the details as the snow softens or melts.',
  cleanup='Collect stones, leaves, grass, twigs, carrot pieces and pebble ears from the sculpture. Leave the snowy patch clear and dry your mittens indoors.',
  extension='Make a whole snowy animal family, try both carved and pebble faces, or invent a creature by changing its body shape, ears or tail.',
  examples=['A pair of little snow mice','A rabbit and its little friend','A snow cat meets a tiny mouse','A seated snow cat','A round-eared snow bear','A flat snow turtle'],waitLabel='Broad joins and short details are easier to keep in place.'
 )
]
for a in winter:
    a.update(season='winter',showInstructions=True,reviewStatus='Draft guide — not yet physically tested or reviewed.')
    a['natureNote']='Use fallen or already-loose materials where collecting is allowed. Leave living plants and animals alone, and gather every decoration before the snow melts.'
    for i,s in enumerate(a['steps'],1):s['diagram']=f"/assets/steps/{a['id']}-{i}.svg"
p=ROOT/'content/activities.json'
existing=json.loads(p.read_text())
for a in existing:
    if a['id'] in {f'WIN-0{i}' for i in range(1,6)}:a['archived']=True
ids={a['id'] for a in winter}
existing=[a for a in existing if a['id'] not in ids]+winter
p.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
print('Added three winter guides; five earlier winter guides retained for saved projects.')
