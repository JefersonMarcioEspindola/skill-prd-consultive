# Profile

Fill it in once and the skill stops asking what's already here. You can leave fields blank: each one has a default, shown in parentheses.

If you installed it as a Claude Code plugin, copy this file to `~/.claude/prd-consultive/profile.md` and edit the copy: the plugin folder is replaced on every update. In chat apps (claude.ai, ChatGPT, Gemini), edit this file before uploading the skill, or simply tell it your preferences in the conversation.

You can fill it in any language.

## Who uses it

- **Name:** (blank: the skill doesn't use a name)
- **Language:** (the language of your first message in the conversation)
- **Country:** (inferred from the conversation). Changes the laws, payment methods and currency the board uses as references.
- **PRD experience:** (blank: the skill asks for the mode. If you write "experienced", it suggests fast mode when the material comes complete)

## Board

- **Usual purpose:** (blank: the skill infers it from the first message, or asks). Options: personal, internal, for sale. Only a default: what you say in the conversation wins.
- **Ideal customer:** (automatic: Lucas when the audience is predominantly male, Bia otherwise). Options: automatic, Bia, Lucas.

## Preferred stack

Used as the default recommendation when the idea doesn't define the stack. The board can still suggest something else if the idea calls for it, and says why.

- **Web / SaaS:** (Next.js + TypeScript + Postgres)
- **Backend / API:** (Node.js + TypeScript)
- **Mobile:** (Expo / React Native)
- **Hosting:** (Vercel for the front end, managed Postgres like Neon or Supabase)
- **Other preferences or constraints:** (none)

## PRD.html look

- **Theme:** (light). Options: light, dark, brand.
- **Brand colors** (only for the "brand" theme):
  - background: 
  - panel: 
  - text: 
  - accent: 
  - text on accent: 
- **Heading font:** (system). If you use one from Google Fonts, write the exact name.
- **Body font:** (system)
- **Name shown in the header:** (product name)

## Writing

- **Tone:** (direct, no artificial enthusiasm)
- **Avoid em dashes:** (yes)
- **Other writing rules:** (none)

## Output

- **Folder to save in:** (prd/<product-name>/ in the current working folder)
- **Create PLAN.md by default:** (no, the skill offers it at the end)
