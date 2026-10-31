# Stack

Caio leads. The goal is to come out with justified decisions, not a list of trendy technologies. A good stack is one the builder can ship and maintain.

## 1. Discover before asking

If you have access to a repository or project folder, look before asking any stack question:

| File | What it reveals |
|---|---|
| `package.json` | Framework (next, react, vue, express, nest), ORM (prisma, drizzle), auth, tests |
| `requirements.txt`, `pyproject.toml` | Python: django, fastapi, flask |
| `composer.json`, `Gemfile`, `go.mod`, `Cargo.toml` | PHP, Ruby, Go, Rust |
| `app.json`, `eas.json`, `pubspec.yaml` | Mobile: Expo/React Native, Flutter |
| `docker-compose.yml`, `.env.example` | Database, queues, external services |
| `vercel.json`, `netlify.toml`, `fly.toml`, `Dockerfile` | Hosting |
| `CLAUDE.md`, `AGENTS.md`, `README.md` | Conventions and decisions already made |

Show what you found in one line ("I see the project already uses Next 15 with Prisma and Postgres") and ask only what's missing.

Then look at the profile. If it has a preferred stack, that's the default recommendation.

## 2. Ask only what changes the choice

If neither the repository nor the profile answers, ask in one round:

1. **Type of application:** web / mobile / web and mobile / API only / automation or bot
2. **Who builds it and with what experience:** (this weighs more than any other factor)
3. **Constraints:** anything already decided, hosting budget, client requirements

## 3. Recommend with a reason

Recommend a complete stack, with the why of each choice tied to the idea, and let the user swap any piece. Starting points when there's no preference:

| Type | Initial recommendation | Why |
|---|---|---|
| Web SaaS | Next.js + TypeScript, Postgres (Neon or Supabase), Drizzle or Prisma, managed auth, deploy on Vercel | One repository, lots of documentation, AI agents know it well |
| Mobile | Expo (React Native) + TypeScript, backend as a service or a Node API | One codebase for iOS and Android, simple publishing |
| Standalone API or backend | Node.js + TypeScript (Fastify or Nest) or Python (FastAPI), Postgres | Pick the language the team already knows |
| Automation or bot | A scheduled Node or Python script, or a no-code tool if nobody codes | The smallest thing that works |
| Content site | Next.js or Astro, a CMS if non-developers edit | Performance and SEO without a server |

Decisions that almost always come up and need an explicit answer:

- **Auth:** managed (Clerk, Auth.js, Supabase Auth) or custom? Managed, unless there's a strong reason.
- **Payments:** a provider that works in the user's country (Stripe almost everywhere; in Brazil also Mercado Pago or Asaas for Pix and boleto). Never store card data.
- **Files:** object storage (S3, R2, Supabase Storage), never in the database.
- **Transactional email and notifications:** which service, if the MVP needs it.
- **AI:** which model, where the call runs (always on the server) and the estimated cost per use.

## 4. Record as a decision

Each choice goes into `idea.md` and then into the PRD as a decision, in this format:

> D3: Postgres on Neon, because the profile prefers Postgres and the free tier covers the MVP. Rejected: Firebase (the relational data model favors SQL).

If the user doesn't know and doesn't want to decide, use the recommendation and record it as an assumption for them to confirm in the decision sheet.
