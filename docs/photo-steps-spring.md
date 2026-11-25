# Spring photo-step assets

Four original AI-generated photo-style contact sheets for active activities SPR-06 through SPR-09. These depict sequential craft actions from the current `content/activities.json`; they are not photographs from a recorded physical demonstration and do not establish that the guides have been physically tested. The existing finished-project galleries were not altered.

## Files and exact crop contract

Source PNGs: `assets/source/photo-steps/SPR-06.png`, `SPR-07.png`, `SPR-08.png`, `SPR-09.png`.

Browser sheets: `public/assets/photo-steps/SPR-06.webp`, `SPR-07.webp`, `SPR-08.webp`, `SPR-09.webp`.

All four sheets are natively **1881 × 836 pixels**, an exact **3-column × 2-row** grid of **627 × 418** landscape panels. Read left to right across the top row, then left to right across the bottom row. There are no gutters or borders. Crop origins are `(0,0)`, `(627,0)`, `(1254,0)`, `(0,418)`, `(627,418)`, `(1254,418)`. Each crop is 627 × 418. The requested prompt resolution was 2304 × 1024, but the built-in tool returned 1881 × 836; native detail was preserved rather than enlarged merely to meet the 640px target. The video renderer can contain each full panel.

PNGs were copied intact from built-in image-generation results. WebPs were mechanically encoded with ImageMagick quality 88, without visual retouching, resizing, crops or compositing. Temporary close-up crops were used only for inspection. All creation used the built-in tool, not the fallback API/CLI.

## Panel mapping and visual review

| Activity | Setup (panel 1) | Step 1 (panel 2) | Step 2 (panel 3) | Step 3 (panel 4) | Step 4 (panel 5) | Step 5 (panel 6) |
| --- | --- | --- | --- | --- | --- | --- |
| SPR-06 Meet the mud creatures | Soil, bowl, water, tray, sticks, stones | Choose and sort features | Add water and mix mud | Shape plain low oval | Press short twig spines into mud body with stone features | Meet the same finished hedgehog |
| SPR-07 Dandelion Crown | Long-stem yellow dandelions on tray | Select two flexible stems | Cross new stem underneath the first | One visible loop, then long tail lies alongside | Repeat into an open curving chain | Overlap ends and tuck stems to join circle |
| SPR-08 Muddy Faces | Bowl/soil/water and natural face pieces by tree | Choose clear bark patch | Mix thick sticky mud | Press a plain flat oval | Add eyes, nose, smile and leafy hair | Change eyebrow expression on same face |
| SPR-09 Spring Fairy Garden | Sorted sticks, bark, stones, leaves and flowers | Mark doorway/path at tree base | Lean sticks against trunk with stone braces | Overlap light bark/leaf roof | Arrange pebble path and flowers | Completed garden plus optional low rock shelter |

All 24 panels were visually inspected. Each sequence keeps the same work surface/location and recognizable materials. Hands appear natural, objects are supported, and no face, text, label, watermark or impossible floating join was found. SPR-06 preserves the low oval through decoration; SPR-08 keeps the same small bark patch and avoids scraping. SPR-09 shows tree/ground contact for the leaning sticks, supported light roofing, an open doorway and the optional stable rock shelter at the end.

The SPR-07 crossing and wrap panels were also inspected as enlarged crops: the second stem crosses beneath the first and hangs down, then a single visible loop brings the tail alongside the first stem. Later panels show an open repeated chain and an overlapping/tucked ring join. These are still generated images, so the written instructions and adult guidance remain the source for the precise technique.

## SPR-06 prompt

Selected original generation: `/workspace/scratch/3f0f3f3c1b5a/generated_images/exec-cec07b1f-b30b-40b1-846c-6932a1f0842a.png`

```text
Use case: photorealistic-natural. Create a PHOTO INSTRUCTION CONTACT SHEET for a nature craft. EXACT canvas 2304×1024 pixels: THREE columns and TWO rows of equal LANDSCAPE photographs, each panel 768×512 pixels (3:2). Six panels edge-to-edge with NO borders, gutters, frames, labels, numbers, writing, arrows or watermarks. Read order is top-left, top-middle, top-right, bottom-left, bottom-middle, bottom-right. First panel is materials; remaining five panels show one continuous genuine construction sequence. Every panel must use the SAME background, work surface, craft, material colours and natural daylight, like photographs from one real session. Close enough that the physical action is clear. Real handmade textures, achievable simple construction, adult hands allowed but NO faces/bodies; anatomically normal hands, at most two hands per panel. No floating objects, impossible joins, magically finished work in early steps, illustrations or CGI.
Activity: Meet the mud creatures. Show building ONE low oval mud hedgehog on the SAME pale blue washable tray on a light weathered garden table. Same stainless bowl, same spoon, same cup, same chunky smooth stones and blunt short sticks across the sequence. The mud is dark earthy clay-rich soil, with rough fingerprints, not polished ceramic.
Panel1 top-left MATERIALS: neat real loose setup of bowl containing dry brown clay-rich soil, a small water cup, spoon, empty pale blue tray, two smooth light stones for eyes, one darker broad nose stone, about15 short blunt fallen twigs, and a couple loose green leaves at the edge. Nothing assembled.
Panel2 top-middle STEP1 gather: adult hands choosing the two eye stones and sorting short blunt sticks beside the empty tray; same dry soil bowl and water cup nearby. No creature yet.
Panel3 top-right STEP2 mix: one hand adds a small splash of water from cup into the bowl while the other stirs with spoon; show thick lumpy damp mud that holds together rather than runny soup. Tray still empty; selected sticks and stones remain beside it.
Panel4 bottom-left STEP3 shape: two muddy hands press a LOW OVAL mound of the same mud onto the blue tray, tapering one end slightly into a hedgehog snout and flattening the base. No eyes or spines yet. Mixing bowl sits behind tray.
Panel5 bottom-middle STEP4 decorate: same low oval body now has the light stone eyes and dark nose. One hand carefully presses a short BLUNT twig into the back among several already added short twig spines; remaining loose sticks sit at tray edge. Show gentle placement, not stabbing fingers.
Panel6 bottom-right STEP5 meet the friend: completed same little hedgehog on same tray, short twig spines over its back, two light eye stones and dark nose, low broad stable muddy body. A hand gently points beside the finished friend as if telling its story, not changing it. Bowl/spoon and a few leftover materials still visible in background. Do not substitute a different animal between panels.
```

## SPR-07 prompt

Selected original generation: `/workspace/scratch/3f0f3f3c1b5a/generated_images/exec-9bd6e7ee-df77-47e6-933d-b3088d4266d6.png`

```text
Use case: photorealistic-natural. Create a PHOTO INSTRUCTION CONTACT SHEET for a nature craft. EXACT canvas 2304×1024 pixels: THREE columns and TWO rows of equal LANDSCAPE photographs, each panel 768×512 pixels (3:2). Six panels edge-to-edge with NO borders, gutters, frames, labels, numbers, writing, arrows or watermarks. Read order is top-left, top-middle, top-right, bottom-left, bottom-middle, bottom-right. First panel is materials; remaining five panels show one continuous genuine construction sequence. Every panel must use the SAME background, work surface, craft, material colours and natural daylight, like photographs from one real session. Close enough that the physical action is clear. Real handmade textures, achievable simple construction, adult hands allowed but NO faces/bodies; anatomically normal hands, at most two hands per panel. No floating objects, impossible joins, magically finished work in early steps, illustrations or CGI.
Activity: Dandelion Crown. Close photographic construction details of a REAL crown made by looping long fresh dandelion stems, not wire or glue. Same pale weathered wooden tabletop and shallow cream tray in every panel. Only yellow DANDELIONS with many fine petals and long flexible green stems. No daffodils, daisies, wire, elastic, glue or purchased hoop. Use progressively closer camera views for the crossing/loop, but maintain same natural daylight and work surface. Two adult hands demonstrate without hiding the important stem connection.
Panel1 top-left MATERIALS: about30 yellow dandelions with 15–20cm intact long green stems spread on the cream tray, untouched flowers, no crown or chain yet.
Panel2 top-middle STEP1 choose: two hands select exactly TWO fresh long-stem dandelions from the same tray and lay them on table, flowers at left and long stems extending right. Show stem lengths clearly.
Panel3 top-right STEP2 cross: tight close-up of exactly TWO flower heads side by side at left. The first flower's stem runs horizontally to the RIGHT. The second flower is just beside it; its stem crosses UNDER the first near the heads and hangs DOWN toward bottom edge. Thumb and finger lightly pinch the crossing while leaving it visible. This is a single simple crossed pair, NOT a knot, not a woven bundle, no extra flowers.
Panel4 bottom-left STEP3 wrap: very clear close-up of that SAME pair. The second stem has made exactly ONE full loop up and around the first horizontal stem immediately below the heads, passing between the two heads; its LONG TAIL is now folded to the RIGHT alongside the first stem. Show one visible green stem loop hugging the horizontal first stem and two parallel long stem tails exiting right. One hand pinches under the heads; the other gently lays the new tail alongside. The loop is physically continuous and snug, without breaking a stem. No string, no detached stem pieces, no decorative random braid.
Panel5 bottom-middle STEP4 repeat: same pair has grown into an OPEN gently curving chain of about10 yellow dandelion heads, not a closed ring. Parallel gathered long stems lie to the right underneath the heads. Two hands add just ONE new flower at the open end by the same simple loop-around-bundle method. Show one fresh long stem being wrapped, all heads close together and a loose chain curving on the tabletop.
Panel6 bottom-right STEP5 join: the same chain is now longer, about25 flowers, curved into a loose CIRCLE. Hands hold the overlapping two ends and tuck the long leftover stems through nearby existing loops to close the join. Show the join clearly at the front, with two ends overlapping and a green tail being tucked, not tied into a big knot. The rest of the complete yellow flower crown rests on the same cream tray with a clear empty centre. No face wearing it, no neck tie.
```

## SPR-08 prompt

Selected original generation: `/workspace/scratch/3f0f3f3c1b5a/generated_images/exec-45f32cab-5669-4551-b576-a04782b8f198.png`

```text
Use case: photorealistic-natural. Create a PHOTO INSTRUCTION CONTACT SHEET for a nature craft. EXACT canvas 2304×1024 pixels: THREE columns and TWO rows of equal LANDSCAPE photographs, each panel 768×512 pixels (3:2). Six panels edge-to-edge with NO borders, gutters, frames, labels, numbers, writing, arrows or watermarks. Read order is top-left, top-middle, top-right, bottom-left, bottom-middle, bottom-right. First panel is materials; remaining five panels show one continuous genuine construction sequence. Every panel must use the SAME background, work surface, craft, material colours and natural daylight, like photographs from one real session. Close enough that the physical action is clear. Real handmade textures, achievable simple construction, adult hands allowed but NO faces/bodies; anatomically normal hands, at most two hands per panel. No floating objects, impossible joins, magically finished work in early steps, illustrations or CGI.
Activity: Muddy Faces. Build ONE flat mud face on the SAME rough grey-brown tree trunk at a low reachable spot, on a small patch of bare sturdy bark with no moss or lichen. Same bowl, cup, soil, spoon, two cream eye stones, one grey nose stone, curved twig mouth and green leafy hair. Ground and trunk consistent through all photographs; no carving or scraping bark.
Panel1 top-left MATERIALS: at the base of the tree, a reusable bowl of dry clean clay-rich soil, small water cup, spoon, two large cream smooth stones, one grey nose stone, short curved twig and loose green leaves neatly spread on a small light cloth. Tree trunk visible behind.
Panel2 top-middle STEP1 find place: adult hand gently points to a clear reachable palm-sized patch of rough tree bark where the face will go, with untouched bark and no mud yet. Material cloth and bowl below in view; no tool touching tree.
Panel3 top-right STEP2 mix: close-up beside same tree; hands add a little water to the bowl and stir thick clay-rich mud with spoon, showing a squeezed dollop holding its shape. Selected stones/leaves on cloth remain nearby. No face on tree yet.
Panel4 bottom-left STEP3 press: muddy palm gently presses a SMALL FLAT OVAL mud pad onto the chosen bark patch, smoothing its edge. All bark outside the palm-sized pad untouched. Pad is plain, no decorations or facial features yet.
Panel5 bottom-middle STEP4 decorate: same mud oval now has two cream stones as eyes, one grey nose stone, a curved twig smile and loose green leaves along top for hair. A hand is adding the last leafy hair piece into the MUD only. The face looks homemade, cheerful and flat against trunk.
Panel6 bottom-right STEP5 new expression: the SAME complete face in same position. A hand turns one short twig eyebrow to a playful raised angle to change its expression; other features and hair unchanged. Show the entire small mud face and surrounding bark clearly. No extra sculpture or second different tree. Materials and bowl still at base.
```

## SPR-09 prompt

Selected original generation: `/workspace/scratch/3f0f3f3c1b5a/generated_images/exec-44d3a903-d6b7-47fd-b094-d06fee9c5be1.png`

```text
Use case: photorealistic-natural. Create a PHOTO INSTRUCTION CONTACT SHEET for a nature craft. EXACT canvas 2304×1024 pixels: THREE columns and TWO rows of equal LANDSCAPE photographs, each panel 768×512 pixels (3:2). Six panels edge-to-edge with NO borders, gutters, frames, labels, numbers, writing, arrows or watermarks. Read order is top-left, top-middle, top-right, bottom-left, bottom-middle, bottom-right. First panel is materials; remaining five panels show one continuous genuine construction sequence. Every panel must use the SAME background, work surface, craft, material colours and natural daylight, like photographs from one real session. Close enough that the physical action is clear. Real handmade textures, achievable simple construction, adult hands allowed but NO faces/bodies; anatomically normal hands, at most two hands per panel. No floating objects, impossible joins, magically finished work in early steps, illustrations or CGI.
Activity: Spring Fairy Garden. Build ONE tiny natural LEAN-TO against the SAME broad rough tree trunk on a bare clear patch of earth. Same location, low angle, natural daylight throughout. Every stick touches ground and leans on tree; no floating unsupported roof, glue, nails, manufactured fairy doors or lifted living moss. Same short blunt twigs, light bark pieces, broad leaves, pale stones, a few small fallen white/lavender flowers.
Panel1 top-left MATERIALS: on bare earth beside the tree, sort 8–12 short blunt fallen twigs, 3–4 light loose bark pieces, broad loose leaves, about12 smooth stones and a few fallen flowers. No construction yet. Tree and clear patch visible.
Panel2 top-middle STEP1 plan: a hand lays two loose twigs flat on earth to mark doorway and short path at tree base. Same materials gathered to side; nothing upright yet, no digging, roots untouched.
Panel3 top-right STEP2 lean: several short twigs lean diagonally against the tree, their feet spread on ground and braced by small stable stones. An adult hand gently adds a last support twig to the sloping row. Leave a visible front opening. Show actual contact at trunk and ground; NO roof covering yet.
Panel4 bottom-left STEP3 roof: same twig supports stay in place. A hand lays a LIGHT fallen bark piece over the lower supports, overlapping another piece above like shingles, with a broad leaf filling a gap. Keep roof low, clear open doorway, all bark supported on sticks. No heavy roof rock and no cutting living bark.
Panel5 bottom-middle STEP4 garden: same now-complete twig/bark lean-to. Hand arranges small smooth pebbles into a winding path to the entrance and places a fallen lavender flower beside it. A few loose leaves and white flowers decorate roof; no living moss is dug up.
Panel6 bottom-right STEP5 explore: finished SAME garden with shelter and winding pebble path fully visible. To one side there is now an optional VERY SMALL low rock shelter made from two broad stable support stones and one small flat roof stone, with a visible little gap underneath; an adult hand gently points beside it to compare shelters. Main tree lean-to unchanged. Natural handmade results, modest scale, no professional miniature architecture.
```

