# Features and catalogue

This describes the version 21 source exported November 24, 2026. Implementation is distinct from production acceptance; see the README status table.

## Active activities

Little Makers covers ages 4–6 and Young Creators covers ages 7–12. A grown-up supervises both. Complexity and age estimates are provisional until hands-on trials.

| ID | Activity | Age pathways |
| --- | --- | --- |
| SPR-06 | Meet the mud creatures | 4–6 and 7–12 |
| SPR-07 | Dandelion Crown | 7–12 |
| SPR-08 | Muddy Faces | 4–6 and 7–12 |
| SPR-09 | Spring Fairy Garden | 7–12 |
| SUM-06 | A summer nature mandala | 4–6 and 7–12 |
| SUM-07 | Rocky friends | 4–6 and 7–12 |
| SUM-08 | Our wilderness creatures | 7–12 |
| SUM-09 | Sandy Explorer | 4–6 and 7–12 |
| FAL-06 | Make a Leafy Friend | 4–6 and 7–12 |
| FAL-07 | Fall Fairy Garden | 7–12 |
| FAL-08 | Fall Mandalas | 4–6 and 7–12 |
| FAL-09 | Meet your fall friends | 7–12 |
| WIN-06 | Make a little snow man | 4–6 and 7–12 |
| WIN-07 | A pocket-sized snow village | 7–12 |
| WIN-08 | Snowy Friends | 7–12 |

Twenty earlier records are archived, not deleted. They stay in the JSON and retain diagrams/videos for older saved projects. The dedicated Make Together area is removed, while eligible legacy `together` variants remain valid.

## User journeys

1. **Discover:** browse without an account; filter/search or use Surprise me; open an eligible guide.
2. **Prepare and make:** inspect materials and grown-up notes, then follow five illustrated steps. Use photo examples, the 75-second video, read-aloud, enlarged text/diagrams or printing.
3. **Save privately:** favourite an idea or start a project. Guests save locally; adult account holders can synchronize progress and attach private photos. JSON backups exclude photo bytes.
4. **Share deliberately:** use the activity gallery's separate upload and public-sharing confirmation. The private project photo is never automatically published. Owners can withdraw/delete; another adult can report.
5. **Suggest improvements:** open the corner feedback form, write an idea/change/bug and optionally supply a reply address; remain on the same page.

## Design requirements reflected in code

- Four-second hero advance interval across all active activities; smooth crossfade, pause below the image and reduced-motion support.
- Cream/green base, restrained dusty-rose details and pink butterfly accents; seasonal filter colours.
- Seasonal cartoons on relevant entry/empty states; motion stays decorative rather than covering controls.
- Header, catalogue, activity, My projects, about and privacy journeys; no hardcoded project-count marketing claim.
- Winter variations include three snow-person examples, three snow-village examples and six Snowy Friends examples. Generated mouse ears and leaf-owl eyes follow the requested pebble treatment.

## Accessibility and content support

Instructions remain text-based and available without sound. Videos have burned-in captions plus shipped WebVTT files; read-aloud is user initiated. Larger-text, enlarged diagrams, native dialogs and motion preferences are implemented. These controls are not a claim of a completed accessibility audit. Generated photo panels show intended progress and inspiration; they do not prove a child can reproduce the result.

## Not yet delivered

Independent email signup is not live; the existing site uses ChatGPT identity. Feedback inbox receipt remains unverified. Recorded Shelley audio covers only SUM-06. Public reporting lacks a moderator dashboard. There are no payments, advertising subscriptions or physical-activity trial results. See [ROADMAP.md](ROADMAP.md).
