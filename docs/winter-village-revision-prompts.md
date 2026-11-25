# Winter village gallery revision

Created November 23, 2026 with the built-in image-generation tool, using an image edit with two local reference inputs. These AI-generated examples illustrate possible craft outcomes and are not photographs of physically tested projects.

## Inputs and delivery

- Edit target: the previous `assets/source/WIN-07.png` gallery.
- Composition reference: the user-supplied `Screenshot 2026-11-22 at 6.42.33 PM.png` (the source filename contains a narrow non-breaking space before PM).
- Selected generated output: `/workspace/scratch/3f0f3f3c1b5a/generated_images/exec-e842b80b-b168-4d55-9ba8-895e341b1c52.png`.
- Final source: `assets/source/WIN-07.png`.
- Browser asset: `public/assets/activities/WIN-07.webp`.

The gallery is 2172 × 724 pixels, with three equal square panels. The first panel was mechanically packed from the original gallery into the generated composition so its original PNG pixels remain identical. The middle and right panels are the generated edit, without artistic retouching. The WebP was mechanically encoded at quality 84.

| Panel | Example |
| --- | --- |
| Left | Original twig-roof cottage and pebble path, preserved exactly |
| Middle | Three round, flat-topped sprig-roof snow houses, arranged like the supplied reference, with a branching twig-edged path |
| Right | Three flat-topped snow-block cottages, chunky snow steps, pebble courtyard and a low forked-twig gateway |

Visual review confirms different building shapes in all three examples, white shallow door impressions, natural materials, small solid snow forms, and stones kept at ground level. The middle example closely follows the supplied composition and roof decorations. It is a generated reconstruction, not a direct copy of the reference pixels.

## Final generation prompt

```text
Use case: compositing. Edit target image 1 is an existing original website gallery; image 2 is the user's composition reference for the NEW middle panel. Deliver one photorealistic landscape triptych, exactly THREE equal SQUARE panels edge-to-edge, 3:1 total aspect ratio, target 2172×724 pixels. Each panel independent photograph, no text, no gutters, no border.

LEFT THIRD: PRESERVE the first square panel of image 1 unchanged: one small white solid snow cottage with short twig pitched roof, shallow door arch pressed in white snow, flat pebbles at ground-level threshold and curved pebble path, same snowy background, camera, light, scale, and texture. Do not replace or redraw this first example if possible.

MIDDLE THIRD: replace image 1's middle panel entirely with a very close reconstruction of image 2's snowy village composition. Three squat ROUND flat-topped snow mounds/cottages arranged in a triangle: largest at back center, smaller front left, medium front right. Top edges softly rounded, no pitched roofs or roof twigs. Each has a shallow arched white recessed door impression, white snow inside, not a dark hollow. Back center roof a small cedar-like evergreen sprig laid along the top; front-left roof a short fallen pine sprig; front-right roof a tiny dried branching flower/seed stem. A broad curved snow path starts at foreground center and branches toward each door; its edges have rows of irregular SHORT VERTICAL twig posts. A tiny evergreen sprig beside left edge and one front right. Snow-covered dark boulder in upper-right background, bare stems and softly snowy woodland. Recreate image 2's house proportions, relative positions, natural shadows, textures and visible route closely. Natural miniature handmade snowcraft, not houses with gables.

RIGHT THIRD: a completely DIFFERENT child-made small SNOW-BLOCK HAMLET/castle-like courtyard. Three low squat rectangular solid snow blocks/cottages with flat tops, unequal heights and clearly visible handmade packed-snow edges. One slightly taller rectangular central block and two smaller cuboid blocks beside it, tiny chunky snow steps on one side. Shallow arched door outlines pressed into solid white fronts. A little irregular flat-pebble courtyard and short pebble approach. A simple low twig gateway made of two short blunt vertical twigs with one horizontal twig nestled across forked tops at the entrance. No pitched roof, no round dome houses, no pointed tall towers, no elaborate professional castle sculpture. Snow blocks remain small, low and solid. Soft winter garden backdrop, clearly different composition from middle panel.

All panels: realistic granular hand-packed imperfect snow, natural soft winter daylight and pale blue shadows, small achievable outdoor craft made from snow and found natural materials. All pebbles remain on the ground, no stones on walls or roofs. No people, toys, fairy figurines, lights, plastic ornaments, watermarks, words, hollow tunnels or enterable structures. The three examples must read instantly as twig-roof cottage / round sprig-roof village / flat-top block hamlet.
```
