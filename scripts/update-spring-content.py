"""Apply the four requested spring guides, preserving old IDs for saved projects."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def material(name, quantity, kind='nature', optional=False):
    return dict(name=name, quantity=quantity, kind=kind, optional=optional)

def step(title, text, littleTask='', youngTask='', adultTask=''):
    return dict(title=title, text=text, littleTask=littleTask, youngTask=youngTask, adultTask=adultTask)

spring = [
 dict(
  id='SPR-06', title='Meet the mud creatures', subtitle='A tiny friend, a silly beast, or a monster of your own.',
  description='Shape a handful of mud into a cute friend or a wonderfully scary monster. Bring it to life with stones, twigs, leaves and flowers. A simple round creature is just as special as one with lots of little details.',
  ages=['little','young'], together=True, minutes=30, prepMinutes=5,
  setting='Outside or at a washable table', difficulty='Make it simple or detailed', tags=['mud','soil','stones','twigs','leaves','flowers','creatures','spring'],
  materials=[material('Clean, clay-rich soil approved by a grown-up','About 2 cups'),material('Water, added slowly','A small cup','home'),material('Reusable bowl, spoon and washable tray','1 of each','home'),material('Smooth stones too large to swallow, for eyes or noses','2–6','nature',True),material('Blunt fallen twigs, loose leaves or grass','A small handful','nature',True),material('Flowers identified and approved by a grown-up','2–4, optional','nature',True)],
  adultNote='Choose clean soil away from animal waste, sprayed areas and roads. Check flowers and loose pieces; skip unknown berries and sharp twigs. Keep mud away from mouths and eyes. Choose large features for younger makers and wash hands afterwards.',
  littleRole='Roll a simple body and choose eyes, ears and a funny face.', youngRole='Shape several joined pieces and add a tail, patterned spines or an unusual expression.',
  togetherPlan='A Little Maker shapes the body and chooses the face. A Young Creator helps attach ears or limbs and adds details. Give the creature a name together.',
  steps=[
   step('Gather a creature collection','Set out your bowl and tray. With a grown-up, gather clean soil, smooth stones and a few blunt fallen twigs, leaves or approved flowers. Decide which pieces could become eyes, ears, hair or spines.', 'Choose two eyes and some ears or hair.', 'Sort pieces by the features they could make.', 'Approve the soil and decorations before children handle them.'),
   step('Mix mud that holds its shape','Spoon soil into the bowl. Add a little water and stir, then squeeze a small handful. It should hold a ball without dripping. Add more soil if it is runny. If sandy soil keeps crumbling, try clean clay-rich soil or make a flat creature.', 'Squeeze a little mud into a ball.', 'Adjust the mix with small amounts of soil or water.', 'Help check the texture; ordinary mud will not behave like modelling clay.'),
   step('Shape a body and a head','Press a mud ball onto the tray so it has a wide, steady base. Keep it as one round creature, or add a smaller head. Press joined pieces firmly together and smooth the seam with a damp finger. A low oval makes a good hedgehog.', 'Make one round or oval body.', 'Add a head, small feet or a short tail and smooth the joins.'),
   step('Bring your creature to life','Gently push suitable stones into the mud for eyes or a nose. Add leaf ears, short twig spines, or grass and flowers for hair. Keep decorations light. Make a friendly smile, a silly frown or a monster face that makes you laugh.', 'Add the eyes and your favourite decoration.', 'Try leaf wings, twig whiskers or a row of small mud teeth.', 'Help press pieces in without poking hands; remove any sharp or unstable parts.'),
   step('Meet your new mud friend','Give your creature a name and show what it can do in an imaginary story. Try a second creature with a different shape or mood. Take a picture on the tray before it dries; cracks and crumbles are part of temporary mud art.', 'Name your friend and invent its favourite game.', 'Compare a simple creature with one that has more details.', 'Help photograph the creation, tidy the space and wash hands.')
  ],
  keep='Enjoy on the tray during play. Mud may crack or crumble as it dries; this is a temporary creation, not a waterproof toy.',
  cleanup='Remove decorations, return loose natural pieces only where permitted, and wipe mud into a bin or approved soil area before washing tools. Wash hands with soap and water.',
  extension='Invent a whole family: a shy leaf-eared friend, a prickly hedgehog and a cheerful grass-haired monster.',
  examples=['A leaf-eared mud bunny','A twig-spined hedgehog','A silly mud monster'], waitLabel='No drying needed for play. Mud changes as it dries.'
 ),
 dict(
  id='SPR-07', title='Dandelion Crown', subtitle='Cross, wrap, and grow a circle of sunshine.',
  description='Weave long-stemmed yellow dandelions into a flower crown using a repeating wrap-and-fold technique. Add one flower at a time, then join the chain into a loose circle. This takes patient fingers and a little practice.',
  ages=['young'], together=False, minutes=40, prepMinutes=10,
  setting='Outside or at a table', difficulty='A bigger challenge', tags=['flowers','dandelions','crown','weaving','spring'],
  materials=[material('Fresh dandelions with flexible stems about 15–20 cm long','About 25–40; size will vary'),material('Flat work surface or a reusable tray','1','home'),material('Short piece of soft cotton string, only if the final join needs help','1 small piece','home',True),material('Child-safe scissors for an adult-assisted string trim','1 pair','home',True)],
  adultNote='Use dandelions, not daffodils. A grown-up identifies the flowers, checks for sensitivities, and chooses an unsprayed place where picking is allowed. Leave plenty for insects. Keep sap away from eyes and mouths; stop if skin feels irritated. Help with the join and any scissors. The crown should sit loosely, without ties under the chin.',
  littleRole='', youngRole='Hold the growing bundle, repeat the stem wrap and make a comfortable circular join.', togetherPlan='',
  steps=[
   step('Choose long, flexible stems','Ask a grown-up to identify dandelions and approve a place to pick a few. Keep the long stems attached and set the flowers on a tray. Choose fresh stems that bend gently. Leave plenty of flowers growing for insects.', '', 'Choose flexible stems and set out two flowers to practise.', 'These yellow fluffy flowers are dandelions. Do not substitute daffodils or unidentified flowers.'),
   step('Cross two flowers','Hold the first flower with its head on the left and its stem pointing right. Put the second flower just beside the first, with its stem crossing underneath the first stem and hanging down. Pinch the crossing close to the flower heads.', '', 'Keep the heads close and hold the crossing with your thumb and finger.', 'Demonstrate the crossing slowly, with both hands visible.'),
   step('Wrap, then lay the stem alongside','Keep pinching the crossing. Bring the hanging stem up and around the first stem, passing it between the two flower heads. Fold its long tail back to the right, alongside the first stem. Gently snug the loop under the heads without pulling it tight enough to snap.', '', 'Follow the close-up: cross underneath, wrap up and around, then lay the tail to the right.', 'Pause after each movement. If a stem breaks, remove that flower and try a fresher, more flexible one.'),
   step('Add one flower and repeat','Place a new flower beside the last one, with its stem underneath the growing bundle. Repeat the same wrap, then lay the tail alongside the other stems. Keep the heads close and curve the chain gently as it grows. Pause often to check its length around the top of the head.', '', 'Repeat the same motion, adding only one flower each time.', 'Help hold the bundle if it gets slippery. Keep the chain loose enough to fit comfortably.'),
   step('Join your sunshine circle','Overlap the two ends to make a loose crown. Hold the overlap and thread the long remaining stems through nearby stem loops, wrapping and tucking them back two or three times. Ask a grown-up to secure a slipping join with a short cotton tie if needed. Try it on gently or display it on the tray.', '', 'Tuck the ends neatly and check that the crown rests comfortably.', 'Check the join and fit. Trim any optional string ends; never add a tie around the neck.')
  ],
  keep='Enjoy the crown while the flowers are fresh. It will wilt naturally; a photo keeps the memory. A tray display is a good choice if you prefer not to wear flowers.',
  cleanup='Remove and take home any string. Compost flowers where appropriate, clear the making space, and wash hands after handling sap.',
  extension='Make a tiny practice chain before a full crown, or create a smaller ring to decorate a nature table.',
  examples=['A woven circle of sunshine','A fuller flower crown','A small dandelion crown'], waitLabel='Practise one wrap before making a full crown.'
 ),
 dict(
  id='SPR-08', title='Muddy Faces', subtitle='Give a tree a grin—or make a face on the ground.',
  description='Press a soft mud face against a tree or lay one flat on the ground. Add silly features and leafy, twiggy or flowery hair. Make it sleepy, surprised, fierce or funny, then change it as often as you like.',
  ages=['little','young'], together=True, minutes=25, prepMinutes=5,
  setting='Outside at a permitted tree or flat patch of ground', difficulty='Easy does it', tags=['mud','soil','faces','trees','stones','leaves','flowers','spring'],
  materials=[material('Clean, clay-rich soil approved by a grown-up','About 2 cups'),material('Water, added a little at a time','A small cup','home'),material('Reusable bowl and spoon','1 of each','home'),material('Smooth stones too large to swallow','2–5'),material('Blunt fallen twigs and loose leaves or grass','A small handful'),material('Flowers identified and approved by a grown-up','A few, optional','nature',True)],
  adultNote='Ask permission before putting mud on a tree. Choose a small patch of sturdy, rough bark within easy reach; avoid young trees, damaged bark, moss and lichens. Never scrape bark or push twigs into it. Use the ground if mud will not stay. Check soil and decorations, keep mud away from mouths and eyes, and wash hands afterwards.',
  littleRole='Press a flat face and choose a mouth and some funny hair.', youngRole='Change eyebrows, eyes and mouths to show different feelings.',
  togetherPlan='A Little Maker presses the mud shape and picks the hair. A Young Creator adds features and helps show a new expression. Tell a story about the face together.',
  steps=[
   step('Find a place for a face','With a grown-up, choose an approved tree with rough, sturdy bark at a comfortable height, or a flat patch of ground. Leave living moss, lichens and roots alone. Set your decorations nearby and imagine the expression you want to make.', 'Choose a place you can reach easily.', 'Plan where the eyes, nose, mouth and hair will go.', 'Approve the tree and location. Use the ground if the bark is unsuitable or permission is unavailable.'),
   step('Mix thick, sticky mud','Put soil in the bowl and add water a little at a time. Stir until a handful holds together without dripping. If it slides off your hand, add more soil. Clay-rich soil usually holds better; you can always make the face flat if your mix is crumbly.', 'Squeeze a small ball of mud.', 'Adjust the mix until it holds a flattened shape.', 'Check that the soil is clean and the mix is comfortable to handle.'),
   step('Press a flat face shape','Gently press a small, thick oval of mud onto the approved bark, or flatten it on the ground. Smooth the edges with your fingers. Keep it low and fairly flat so it stays in place. If it slips, move your face to the ground instead of forcing it onto the tree.', 'Pat the mud into a round or oval face.', 'Shape cheeks or add a small mud nose.', 'Do not scrape bark, hammer anything in or cover a large area of the trunk.'),
   step('Add a face and wild hair','Press smooth stones lightly into the mud for eyes and a nose. A curved twig can make a smile. Arrange loose leaves, grass or approved flowers above the face for hair. Push decorations into the mud only, never into the bark.', 'Choose a smile and add leafy hair.', 'Tilt eyebrows or change the mouth to create a different mood.', 'Help place suitable large features and remove any sharp pieces.'),
   step('Try a new expression','Step back and meet your muddy character. Move one eyebrow or turn the mouth to make a new expression. Take a picture of your favourite face, then gently remove the mud and decorations when play is finished.', 'Show how your face is feeling.', 'Make two expressions by moving only a few pieces.', 'Remove mud gently without scraping the tree; rinse lightly with plain water only if needed and permitted.')
  ],
  keep='This is temporary art for your making session. Photograph it, then remove the mud and decorations gently.',
  cleanup='Clear the face without scraping bark or disturbing plants. Take away anything you brought, clean tools, and wash hands with soap and water.',
  extension='Create a happy face and a surprised face, or make a small family on the ground with different leafy hairstyles.',
  examples=['A leafy grin on a tree','A flower-haired ground face','A wild-haired woodland face'], waitLabel='If mud slips from bark, make the face flat on the ground.'
 ),
 dict(
  id='SPR-09', title='Spring Fairy Garden', subtitle='A flower-filled hideaway tucked beside a tree.',
  description='Build a tiny spring garden with a shelter leaning against a tree, a stone path and a few colourful natural details. You can also use a stable rock for support or build a low shelter from stones. Let the examples spark your own little world.',
  ages=['young'], together=False, minutes=50, prepMinutes=10,
  setting='Outside beside a permitted tree or stable rock', difficulty='A bigger challenge', tags=['fairy garden','twigs','stones','leaves','flowers','building','spring'],
  materials=[material('Short, sturdy, blunt fallen twigs about 10–20 cm long','8–12'),material('Loose fallen bark pieces or broad fallen leaves','3–6 small pieces'),material('Small stable stones, too large to swallow','8–15'),material('Loose fallen greenery and adult-approved flowers','A small handful'),material('Permitted clear space at a tree base or beside a stable rock','About 40 × 40 cm','home'),material('Additional flat stones for an optional low rock shelter','3–5','nature',True)],
  adultNote='Build a miniature garden for imaginary visitors, not a shelter for a child or animal. Use loose fallen materials and leave living moss, bark, roots and habitats untouched. Keep the structure low; no digging into roots, nails, glue or cutting the tree. A grown-up checks all supports and handles any stone roof.',
  littleRole='', youngRole='Plan a supported lean-to, test its balance and add a path and spring garden.', togetherPlan='',
  steps=[
   step('Choose a tree-side corner','With a grown-up, find a permitted clear spot at the base of a tree. Use the trunk as the back of your tiny garden without digging or moving roots. Mark out a doorway and a path with loose twigs. A stable rock can be an alternative support.', '', 'Plan where the shelter, doorway, path and flowers will sit.', 'Choose an existing clear patch, leaving living plants and small habitats alone.'),
   step('Lean a little twig shelter','Rest short twigs diagonally against the trunk so their feet spread out on the ground. Brace the feet with small stable stones and leave an opening at the front. Add a few more leaning twigs close together to support the roof. Test gently and lower any pieces that wobble.', '', 'Keep each twig touching the tree and the ground, with a clear doorway.', 'Check that the low lean-to is steady. Do not push twigs into bark or roots.'),
   step('Add a light roof','Lay small pieces of loose fallen bark or broad leaves across the leaning twigs. Work from the bottom upwards so each layer overlaps the one below. Keep the doorway open and the roof light. Use a light twig to hold a slipping leaf instead of adding heavy pieces.', '', 'Overlap the covering while keeping its twig supports in place.', 'Use only bark already on the ground. Never peel bark from a living tree.'),
   step('Grow a tiny spring garden','Arrange stones into a winding path leading to the doorway. Add loose greenery, approved flowers, a leaf rug or a tiny twig bench beside the shelter. Keep the entrance clear. Change the colours and shapes until the garden feels like your own.', '', 'Make a path and one special detail for an imaginary visitor.', 'Use fallen greenery rather than lifting living moss. Approve any flowers before use.'),
   step('Explore your fairy hideaway','Imagine who might visit and give your garden a name. Try a small rock shelter beside it if you like: use a broad, stable base and ask a grown-up to place a small flat roof stone. Photograph your garden, then take the structure down after play.', '', 'Tell a story about the garden and compare twig and stone supports.', 'Keep stone builds low and stable. Handle roof stones and help return the space to how it was.')
  ],
  keep='Enjoy during the making session. Flowers wilt and loose roofs shift, so photograph your little world and take it down afterwards.',
  cleanup='Gently dismantle the shelter and clear the path. Return loose pieces only where permitted, leave roots and habitats untouched, and wash hands.',
  extension='Build a tiny stone resting place, change the garden path, or tell a story about a spring visitor. Your garden does not need to copy the examples.',
  examples=['A tree-side spring hideaway','A tiny stone shelter','A flower-filled twig garden'], waitLabel='A tree or stable rock helps support a low shelter.'
 )
]

for a in spring:
    a['natureNote']='Pick only a few flowers identified by a grown-up, where picking is allowed. Leave plenty for insects and keep roots and habitats undisturbed.' if a['id']=='SPR-07' else 'Choose loose, fallen materials where collecting is allowed. Ask a grown-up before gathering flowers, leave plenty for insects, and protect roots and tiny habitats.'
    a.update(season='spring', showInstructions=True, reviewStatus='Draft guide — not yet physically tested or reviewed.')
    for i,s in enumerate(a['steps'],1):
        s['diagram']=f"/assets/steps/{a['id']}-{i}.svg"

path=ROOT/'content/activities.json'
existing=json.loads(path.read_text())
for a in existing:
    if a['id'] in {f'SPR-0{i}' for i in range(1,6)}:
        a['archived']=True
new_ids={a['id'] for a in spring}
existing=[a for a in existing if a['id'] not in new_ids]
summer_index=next(i for i,a in enumerate(existing) if a['season']=='summer')
existing[summer_index:summer_index]=spring
path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
print('Added four spring guides; five earlier spring guides retained for saved projects.')
