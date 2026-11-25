"""Apply the four fall activities requested on November 22, 2026.

Previous IDs are retained as archived guides so saved projects keep their meaning.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def material(name, quantity, kind='nature', optional=False):
    return dict(name=name, quantity=quantity, kind=kind, optional=optional)

def step(title, text, littleTask, youngTask, adultTask=''):
    return dict(title=title, text=text, littleTask=littleTask, youngTask=youngTask, adultTask=adultTask)

fall = [
 dict(
  id='FAL-06', title='Make a Leafy Friend', subtitle='A fox, an owl, or someone only you could imagine.',
  description='Turn colourful fallen leaves into a friendly animal. Layer a body, ears, wings and a face on the ground or on card. Make it cute, funny or wonderfully unusual.',
  ages=['little','young'], together=True, minutes=25, prepMinutes=5,
  setting='Outside or at a table', difficulty='Easy does it', tags=['leaves','animals','leaf art','all ages','fall'],
  materials=[material('Fallen leaves in different colours, sizes and shapes','10–30'),material('Smooth short fallen twigs','2–6'),material('Flat ground, a reusable tray or a sheet of card','1 work space','home'),material('Paper eye circles and a crayon for other animal variations','2 circles + 1 crayon','home',True),material('Flat smooth pebbles too large to swallow, for owl eyes','2–3','nature',True),material('Child-safe water-based craft glue, for a card-backed version only','A few small dabs, optional','home',True)],
  adultNote='Check leaves and twigs before use. A grown-up chooses smooth flat pebbles too large to swallow for owl eyes. Avoid tiny loose craft eyes. Glue is optional and chosen by a grown-up. Keep glued artwork on card and take it indoors.',
  littleRole='Choose the colours, place a big body leaf and give your friend a face.',
  youngRole='Layer smaller leaves to make patterned feathers, fur, wings or a tail.',
  togetherPlan='A Little Maker chooses the creature and places the big shapes. A Young Creator layers the details. Decide on its name together.',
  steps=[
   step('Find your fall colours','Collect loose fallen leaves where picking them up is allowed. Sort them by colour and shape beside a flat work space. Choose a few smooth twigs for legs or whiskers.', 'Pick your favourite colours.', 'Sort broad body leaves and smaller detail leaves.', 'Check the materials and choose suitable large flat pebbles for the owl eyes.'),
   step('Give your friend a body','Lay a large leaf flat for the body. Try a smaller leaf above or beside it for the head. Turn the leaves around until you see a fox, owl, bird or an invented creature.', 'Place the body and head.', 'Experiment with the direction and shape of the head.'),
   step('Layer ears, wings and tails','Overlap smaller leaves to build ears, wings, a tail or fluffy-looking fur. A row of yellow leaves can become owl feathers. Keep moving the pieces until your friend feels like yours.', 'Add two ears or wings.', 'Build a repeating layered pattern across the body.'),
   step('Add a friendly face','For the owl, lay two smooth flat pebbles on the leaf face for eyes and add a small leaf beak. Lay twigs flat for legs. Other creatures can use paper eyes or features drawn on the backing. Leave everything loose, or ask a grown-up to help glue leaves onto card; keep the pebble eyes loose.', 'Choose a happy, sleepy or silly face.', 'Add balanced details and small leaf eyebrows.', 'Use only small dabs of approved glue on card if chosen; follow its drying directions.'),
   step('Meet your leafy friend','Give your creation a name and a personality. Add a leaf hat or a little leafy home if you like. Take a picture before moving it; the loose version is meant to stay flat.', 'Tell us your friend’s name.', 'Invent a short story or a second leafy friend.', 'Photograph the project without identifying details, then help tidy up.')
  ],
  keep='Loose leaf art is temporary. Display a card-backed version flat indoors; leaves may curl and change colour as they dry.',
  cleanup='Take all paper, glue and craft pieces home. Reuse the tray and return loose natural pieces only where permitted. Wash hands after making.',
  extension='Make the same animal again with different leaf shapes, or invent a whole family with different expressions.',
  examples=['A golden leaf owl','An olive-green leaf rabbit','A red-and-orange leaf fish'], waitLabel='Optional glue: allow the drying time on its label.'
 ),
 dict(
  id='FAL-07', title='Fall Fairy Garden', subtitle='A leafy little world, with a story all your own.',
  description='Build a small twig shelter with an overlapping leaf roof, then add paths and a garden. A rock or tree can help support your design. Paper fairies are optional; imagination is the main ingredient.',
  ages=['young'], together=False, minutes=50, prepMinutes=10,
  setting='Outside on permitted soft soil', difficulty='A bigger challenge', tags=['leaves','twigs','soil','fairy garden','building','fall'],
  materials=[material('Sturdy, blunt forked fallen twigs for uprights, about 10–20 cm long','4'),material('Smooth short fallen twigs for roof crosspieces and sides','8–14'),material('Broad fallen leaves for a roof and garden','10–15'),material('Flat stones for a path, too large to swallow','8–12'),material('Clean soil from a grown-up-approved place; clay-rich soil may hold better','About 1 cup'),material('Water, added a little at a time','A small cup','home'),material('Small reusable bowl and spoon or mixing stick','1 of each','home'),material('Permitted patch of soft ground beside a stable rock or tree','About 40 × 40 cm','home'),material('Paper scraps, crayons and child-safe scissors for optional fairies','A few scraps + 1 set','home',True)],
  adultNote='This is a miniature garden for play, not a shelter for a child or animal. Choose clean soil and a place where collecting and building are allowed. Keep twigs blunt and low. Do not cut into roots, damage bark, take living moss or disturb habitats. Supervise optional scissors.',
  littleRole='', youngRole='Plan a stable low shelter, overlap the roof leaves and design a path and garden.', togetherPlan='',
  steps=[
   step('Choose a little corner','With a grown-up, choose a small patch of soft ground beside a stable rock or tree. Leave roots and living plants untouched. Point out where your shelter, door, path and garden will go.', '', 'Sketch the layout with a twig or point out each area.', 'Approve a clean, permitted spot away from roots and small habitats.'),
   step('Build a steady twig frame','Press four blunt forked twigs a short way into soft soil. Nest roof crosspieces in the forks, beside the rock or tree. Add a few side twigs, leaving a doorway. Keep it low and test that the pieces stay in place.', '', 'Adjust the supports until the low roof frame feels steady.', 'Help place supports; stop if you meet a root or need force. Do not lean on loose rocks.'),
   step('Mix a little mud paste','Put a few spoonfuls of soil in the bowl. Add water a little at a time and stir until it is thick, not runny. Try a small dab on two leaves. Some soil will not stick well; twigs will still support the roof.', '', 'Add water slowly and compare a thick dab with a runny one.', 'Use clean soil, keep mud away from mouths and eyes, and help judge the consistency.'),
   step('Make an overlapping leaf roof','Lay broad leaves over the twig crosspieces, starting at the low edge and overlapping toward the top. Add small dabs of mud paste where leaves overlap. If they slide, add a light twig to hold them in place.', '', 'Overlap leaves like roof tiles and check the support underneath.', 'Mud is a temporary paste, not strong glue. Help lower or support any unstable parts.'),
   step('Let your garden tell a story','Arrange a winding stone path, a leaf garden or a tiny twig bench. Add paper fairies if you want, or leave space for imagined visitors. Use the examples for ideas, then add your own colours and details.', '', 'Create one detail that makes the garden your own.', 'Help cut optional paper fairies, keep them loose, and bring paper indoors after play.')
  ],
  keep='Enjoy the garden for the making session and photograph it. Mud and leaves will change as they dry or get wet, so the roof is not permanent or weatherproof.',
  cleanup='Remove paper and all added craft materials. Take down the twig frame when play ends, leave roots and habitats undisturbed, and wash hands and tools.',
  extension='Invent who lives in the garden, add a second tiny resting place, or redesign the path without copying an example exactly.',
  examples=['A rock-side leaf cottage','A tiny garden with a paper fairy','A tree-side twig hideaway'], waitLabel='Mud paste is temporary and may not hold every kind of leaf.'
 ),
 dict(
  id='FAL-08', title='Fall Mandalas', subtitle='One little centre. Endless ways to grow.',
  description='Start in the middle and grow a circular pattern with fallen leaves, twigs, stones and pinecones. Add a new pattern with each ring. Make it cute, fierce, colourful or beautifully simple.',
  ages=['little','young'], together=True, minutes=30, prepMinutes=5,
  setting='Outside on a flat surface', difficulty='Make it simple or detailed', tags=['leaves','twigs','pebbles','pinecones','patterns','mandala','fall'],
  materials=[material('Fallen leaves in a few colours and shapes','A few handfuls'),material('Smooth short fallen twigs','6–12, or what you find','nature',True),material('Smooth stones too large to swallow','6–12, or what you find','nature',True),material('Fallen pinecones','3–8, or what you find','nature',True),material('Flat ground or a reusable tray','1 clear space','home')],
  adultNote='Use loose, fallen pieces where collecting is allowed. An adult checks materials and chooses sizes suitable for the children. Skip unknown berries, sharp shells and tiny loose pieces. No glue or scissors are needed.',
  littleRole='Choose the centre and place a simple repeated ring of leaves.',
  youngRole='Add new repeating patterns, colour changes and balanced spacing in each outer ring.',
  togetherPlan='Little Makers build the centre and first leaf ring. Young Creators add outer patterns. Take turns choosing what the next circle will look like.',
  steps=[
   step('Gather a pattern collection','Look for loose leaves, smooth twigs, suitable stones and pinecones. You can make a mandala with leaves alone. Sort what you find into little piles and choose a flat, clear place to work.', 'Sort leaves into colour piles.', 'Look for several pieces with similar sizes and shapes.', 'Check collected pieces and approve the work space.'),
   step('Choose your centre','Place one favourite leaf, stone or pinecone in the middle. Leave room around it for the pattern to grow. Turn your centre piece until it looks the way you want.', 'Choose and place the centre.', 'Plan how wide the first ring will be.'),
   step('Make your first circle','Arrange leaves around the centre, pointing inward or outward. Repeat a colour or alternate two shapes all the way around. Leave gaps if you like; the circle does not need to be perfect.', 'Repeat your favourite leaf colour.', 'Try an alternating red-yellow or broad-narrow pattern.'),
   step('Grow a new pattern each ring','Add an outer ring with a different repeated pattern: twig, stone, twig, stone, or leaves between pinecones. Build another loop if there is room. Use the materials you have, and stop at any size.', 'Place a leaf or stone in each gap.', 'Change the repeating rule for each new ring.'),
   step('Give it your own character','Look at the whole design. Make the leaves look like sun rays, soft petals or fierce spikes, or keep a calm repeating pattern. Change any pieces you want and take a picture of your finished mandala.', 'Choose whether it feels cute, fierce or beautiful.', 'Adjust spacing, add a final border, and explain your pattern.', 'Photograph the design, then help restore the space without disturbing living things.')
  ],
  keep='This is temporary outdoor art. Take a picture before wind or weather changes the pattern.',
  cleanup='Clear paths and play areas when finished. Return loose natural materials only where permitted and leave living plants and small habitats as you found them.',
  extension='Make a tiny mandala beside a larger one, try only two colours, or let a different person design each new ring.',
  examples=['A glowing leaf sun','A woodland ring of cones and stones','A colourful layered fall circle'], waitLabel=''
 ),
 dict(
  id='FAL-09', title='Meet your fall friends', subtitle='Leaf dresses, twig arms and a little woodland personality.',
  description='Make leaf fairies and woodland characters with twig limbs, leafy clothes and expressive faces. Keep them loose on the ground or make a flat picture on card. Extra cutting and tiny details are optional.',
  ages=['young'], together=False, minutes=40, prepMinutes=10,
  setting='Outside or at a table', difficulty='A bigger challenge', tags=['leaves','twigs','fairies','characters','paper','fall'],
  materials=[material('Fallen leaves for clothes, hair and wings','6–12 per friend'),material('Smooth, blunt fallen twigs for a body and limbs','4–6 per friend'),material('Flat ground, a reusable tray or card backing','1 work space','home'),material('Paper face circle prepared by a grown-up and a crayon','1 circle + 1 crayon','home',True),material('Child-safe scissors for optional leaf or paper details','1 pair with supervision','home',True),material('Child-safe water-based craft glue, chosen by a grown-up','A few small dabs for card only','home',True),material('Clean soil and a little water for optional temporary mud paste','A few spoonfuls','nature',True),material('Small reusable bowl and spoon if mixing mud','1 of each','home',True)],
  adultNote='Supervise scissors and prepare small paper shapes if needed. Use naturally shaped leaves for a no-cut version. A grown-up chooses any glue; keep it on card and take the artwork indoors. Mud can hold some flat pieces briefly but will not make a strong upright puppet.',
  littleRole='', youngRole='Design the character, layer leaf clothes and add a face, wings or a leafy hairstyle.', togetherPlan='',
  steps=[
   step('Choose who you will meet','Spread your leaves and twigs on a tray beside a flat work space. Imagine a fairy, forest explorer or funny leaf person. Choose broad leaves for clothes and smaller leaves for hair or wings.', '', 'Pick colours and shapes that match your character.', 'Check materials and prepare a paper face circle if wanted.'),
   step('Lay out the body and face','Lay a short twig flat for the body. Add twig arms and legs around it. Place a paper circle or small leaf above the body for the face. Try a waving pose or a dancing pose before adding clothes.', '', 'Arrange the limbs and head so the character is easy to recognise.', 'Help keep twig ends blunt and all pieces lying flat.'),
   step('Dress your fall friend','Overlap leaves over the body to make a dress, coat or tunic. Add leaf wings, a hat or colourful hair. Use each leaf’s natural shape, or ask a grown-up before making small cuts with child-safe scissors.', '', 'Layer leaves from the bottom up and try different costumes.', 'Supervise any cutting; offer the no-cut version as an equally good choice.'),
   step('Add details your way','Draw a face on the paper or place leaf features. Leave the friend loose, or use a tiny dab of mud under flat pieces. For a card picture, a grown-up may help with approved glue. Keep it flat while it sets.', '', 'Add an expression and choose whether to keep the pieces loose.', 'Mud is temporary. Use glue only on backing and follow its drying instructions; do not promise a standing puppet.'),
   step('Introduce your fall friends','Give each friend a name and a story. Arrange a little scene on the ground or beside your fairy garden. Photograph the finished friends. Your colours, clothes and characters can look completely different from the examples.', '', 'Create a companion or tell a story about your character.', 'Bring paper and glued artwork indoors after play, and help tidy the work space.')
  ],
  keep='Keep the characters flat. Photograph loose or mud-held friends; display a glued card picture indoors once it has dried.',
  cleanup='Take all paper and glued materials home. Reuse tools and trays, clear the play space and wash hands after using soil.',
  extension='Make friends with different moods, add a leafy pet, or introduce your characters to the Fall Fairy Garden.',
  examples=['A winged leaf fairy','A colourful leaf-dress friend','A playful twig-and-leaf character'], waitLabel='Optional glue: follow its drying instructions. Mud holds only temporarily.'
 )
]

for a in fall:
    a['season']='fall'
    a['showInstructions']=True
    a['reviewStatus']='Draft guide — not yet physically tested or reviewed.'
    for i,s in enumerate(a['steps'],1):
        s['diagram']=f"/assets/steps/{a['id']}-{i}.svg"

path=ROOT/'content/activities.json'
existing=json.loads(path.read_text())
for a in existing:
    if a['id'] in {'FAL-01','FAL-02','FAL-03','FAL-04','FAL-05'}:
        a['archived']=True
new_ids={a['id'] for a in fall}
existing=[a for a in existing if a['id'] not in new_ids]
winter_index=next(i for i,a in enumerate(existing) if a['season']=='winter')
existing[winter_index:winter_index]=fall
path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
print('Added four fall guides; five earlier fall guides retained for saved projects.')
