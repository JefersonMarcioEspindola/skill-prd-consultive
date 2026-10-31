# PRD.html

The HTML is the version for reading, presenting and sharing. It adds no content: everything in it is in `PRD.md`. What it adds is form, meaning the right component for each kind of information, and the board's verdict with faces.

## How to build it

1. Copy `assets/skeleton.html` in full. Don't write CSS from scratch: the skeleton already handles themes, phones and printing, and rewriting it creates inconsistency between documents.
2. Set `<html lang="...">` to the session's language and write every visible text in that language, including the skeleton's fixed labels ("In this document", "Acceptance criteria", "Main objection", "Approved by the board", the signal labels...).
3. Set the theme in `<html data-theme="...">` according to the profile:
   - `light` (default): change nothing.
   - `dark`: change the attribute, the variables are ready.
   - `brand`: change the attribute, uncomment the `html[data-theme="brand"]` block and fill it with the profile's colors. If the profile names Google Fonts, add their `<link>` in `<head>` and set `--display` and `--sans`. Check that text on the accent (`--accent-fg`) is still readable. If the brand background is dark, first copy every variable from the `dark` block into the `brand` block (translucent header, signals and tags already tuned for dark backgrounds) and only then override the brand colors.
4. Fill in the header (brand on the left, "PRD · type" in the middle, status on the right), the hero and one `<section>` per PRD.md section, with the same numbering.
5. Delete the example blocks you don't use and **every** comment.
6. Add the photos (see "How to add the photos", below).

## Hero

- Tags: `PRD` and the mode (`Consultative mode` or `Fast mode`, translated).
- `h1`: product name.
- `.positioning`: the confirmed positioning statement.
- `p.lede`: the summary paragraph.
- `.scoreboard`: one item per persona who evaluated, with the final signal (not Téo).
- Meta: version and date.
- TOC: one entry per section, same order, with `<ol start="2">` so the numbering matches the section tags.
- IDs (FR-01, D-02, R-01, E-03) always inside `<code>`, including in tables, so they don't break mid-ID.

## Which component to use

| PRD.md section | Component |
|---|---|
| 1. Summary | Becomes the hero itself (positioning + lede). The following sections keep the MD numbering, starting at 02 |
| 2. Problem and context | `.mod` with the rows Pain, How it's solved today, Why now |
| 3. Audience | Running text; several user profiles become `.entity-grid` |
| 4. Goals and metrics | `table.tbl` inside `.tbl-wrap`; non-goals as a list |
| 5. MVP scope | `.scope` with `.col.in` and `.col.out` |
| 6. Main flows | `.flow` per flow (up to about 6 steps; with more, use a numbered list) |
| 7. Functional requirements | One `.req` per FR, criteria in `ol.acceptance` (numbered, no checkboxes) |
| 8. Non-functional requirements | List, or `table.tbl` if there are many |
| 9. Data model | `.entity-grid`; an entity's states in `.states` |
| 10. Stack and architecture | `table.tbl` (layer, choice, why) |
| 11. Decisions | `.dec-list` |
| 12. Accepted risks | `table.tbl`; the most serious risk also in `.callout.warn` |
| 13. Board verdict | `.board` with one `.persona` per member |
| 14. Build order | `.phase-list` |
| Extra sections (impact, migration) | `.mod` or `.phase-list`, depending on the content |

If some content doesn't fit any component, use running text. Don't invent new components.

## Board cards

One `article.persona` per persona who evaluated the idea, in the order Helena, Caio, ideal customer (Bia or Lucas, whoever took part) and Lúcia. Téo isn't in the verdict because he doesn't evaluate.

```html
<article class="persona" style="--p:#1D2B53">
  <div class="avatar" data-persona="helena" data-signal="green"><span>H</span></div>
  <div>
    <div class="p-head"><h4>Helena</h4><span class="p-role">Investor</span><span class="signal signal-green">Would go</span></div>
    <blockquote>Her final line, in her voice, in 1 to 3 sentences.</blockquote>
    <div class="row"><span class="lbl">Main objection</span><p>...</p></div>
    <div class="row"><span class="lbl">How it was handled</span><p>Decided in D-02 / became risk R-01 / changed the scope.</p></div>
  </div>
</article>
```

- `--p`, initials and `data-persona`: see the visual identity table in `references/board.md`.
- `data-signal`: `green`, `yellow` or `red`. Badge class: `signal-green` ("Would go"), `signal-yellow` ("Would go with conditions") or `signal-red` ("Wouldn't go now"), with the label translated into the session's language.
- The ideal customer changes profile with each idea; adjust `.p-role` (for example, "Ideal customer · personal trainer").
- The same `data-persona` and `data-signal` apply to the small avatars in the hero's `.scoreboard`.

## How to add the photos

Use the first path the environment allows:

1. **Can run Python and has the skill's files:** save the HTML and run `python3 <skill folder>/scripts/embed_avatars.py <path to PRD.html>`. The file becomes self-contained and opens even offline.
2. **Can't run Python** (most chat apps): write the image directly into the avatar, pointing to the published photos:

```html
<div class="avatar" data-persona="helena" data-signal="green"><img src="https://raw.githubusercontent.com/JefersonMarcioEspindola/skill-prd-consultive/main/plugins/prd-consultive/skills/prd-consultive/assets/board/helena-green.webp" alt="Helena"></div>
```

   The file name is `<persona>-<signal>.webp`, with the same values as `data-persona` and `data-signal`; Téo always uses `teo-neutral.webp`. The photos show up when the file is opened online.
3. **Neither:** keep the initials (`<span>H</span>`), which are already in the persona's color.

### What the script does

`scripts/embed_avatars.py` looks for every element with `data-persona` and `data-signal`, finds the image in `assets/board/` (first `<persona>-<signal>`, then `<persona>-neutral`, as webp, png or jpg) and puts it inside the avatar as a data URI. The HTML stays a single file that opens anywhere. If it doesn't find the image, it keeps the initials. Running it twice doesn't duplicate anything.

## Before delivering

- [ ] Every visible text is in the session's language, and `<html lang>` matches it.
- [ ] Sections and numbering match PRD.md.
- [ ] No leftover comments or example blocks.
- [ ] The `<title>` follows the format `<Product> · PRD`.
- [ ] The signals in the scoreboard and the cards match section 13 of PRD.md.
- [ ] The photos were added by one of the three paths (and, if they stayed as initials, you said so).
