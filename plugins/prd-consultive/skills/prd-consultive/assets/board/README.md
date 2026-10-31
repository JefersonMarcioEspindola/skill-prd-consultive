# Board images

Put the personas' photos here. Without them the skill works just the same: the cards show the initials in each persona's color.

## File names

`<persona>-<state>.webp` (`.png` and `.jpg` also work)

| Persona | Files |
|---|---|
| Helena | `helena-neutral`, `helena-green`, `helena-yellow`, `helena-red` |
| Caio | `caio-neutral`, `caio-green`, `caio-yellow`, `caio-red` |
| Bia | `bia-neutral`, `bia-green`, `bia-yellow`, `bia-red` |
| Lucas | `lucas-neutral`, `lucas-green`, `lucas-yellow`, `lucas-red` |
| Téo | `teo-neutral` (the other expressions are optional, Téo gives no signal) |
| Lúcia | `lucia-neutral`, `lucia-green`, `lucia-yellow`, `lucia-red` |

If only the `neutral` version exists, it's used for every signal. Ideal size: square, 256 to 512 px, up to about 100 KB each (webp helps). If Pillow is installed, the script shrinks larger images on its own.

## Want to make your own board?

Generate the images in any generator (Gemini, Google Flow, Midjourney, ChatGPT), keeping:

- the same illustration style in all of them;
- a flat background in the persona's color: Helena `#1D2B53`, Caio `#0A6E4A`, Bia and Lucas `#E07A2E`, Téo `#5B4B8A`, Lúcia `#8A5A00`;
- chest-up framing, no text or logos;
- expressions: neutral; green (convinced, smiling); yellow (thoughtful, hand on chin); red (arms crossed, skeptical).

Tip: generate Helena neutral first, approve the style, and ask for the others "in the same style as the previous image", in the same conversation.
