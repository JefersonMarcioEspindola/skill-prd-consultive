# Stack

Quem conduz é o Caio. O objetivo é sair com decisões justificadas, não com uma lista de tecnologias da moda. Stack boa é a que quem vai construir consegue entregar e manter.

## 1. Descobrir antes de perguntar

Se houver acesso a um repositório ou pasta de projeto, olhe antes de fazer qualquer pergunta de stack:

| Arquivo | O que revela |
|---|---|
| `package.json` | Framework (next, react, vue, express, nest), ORM (prisma, drizzle), auth, testes |
| `requirements.txt`, `pyproject.toml` | Python: django, fastapi, flask |
| `composer.json`, `Gemfile`, `go.mod`, `Cargo.toml` | PHP, Ruby, Go, Rust |
| `app.json`, `eas.json`, `pubspec.yaml` | Mobile: Expo/React Native, Flutter |
| `docker-compose.yml`, `.env.example` | Banco, filas, serviços externos |
| `vercel.json`, `netlify.toml`, `fly.toml`, `Dockerfile` | Hospedagem |
| `CLAUDE.md`, `AGENTS.md`, `README.md` | Convenções e decisões já tomadas |

Mostre o que encontrou em uma linha ("Vi que o projeto já usa Next 15 com Prisma e Postgres") e pergunte só o que falta.

Depois, olhe o `perfil.md`. Se tiver stack preferida, ela é a recomendação padrão.

## 2. Perguntar só o que muda a escolha

Se nem o repositório nem o perfil respondem, pergunte em uma rodada:

1. **Tipo de aplicação:** web / mobile / web e mobile / só API / automação ou bot
2. **Quem constrói e com que experiência:** (isso pesa mais que qualquer outro fator)
3. **Restrições:** algo já decidido, orçamento de hospedagem, exigência de cliente

## 3. Recomendar com motivo

Recomende uma stack completa, com o porquê de cada escolha ligado à ideia, e deixe o usuário trocar qualquer peça. Pontos de partida quando não há preferência:

| Tipo | Recomendação inicial | Por quê |
|---|---|---|
| SaaS web | Next.js + TypeScript, Postgres (Neon ou Supabase), Drizzle ou Prisma, auth gerenciada, deploy na Vercel | Um repositório só, muita documentação, agentes de IA conhecem bem |
| Mobile | Expo (React Native) + TypeScript, backend como serviço ou API Node | Um código para iOS e Android, publicação simples |
| API ou backend isolado | Node.js + TypeScript (Fastify ou Nest) ou Python (FastAPI), Postgres | Escolha pela linguagem que o time já domina |
| Automação ou bot | Script em Node ou Python, agendado, ou ferramenta no-code se ninguém programa | Menor coisa que funciona |
| Site de conteúdo | Next.js ou Astro, CMS se não-dev edita | Desempenho e SEO sem servidor |

Decisões que quase sempre aparecem e precisam de resposta explícita:

- **Auth:** gerenciada (Clerk, Auth.js, Supabase Auth) ou própria? Gerenciada, salvo motivo forte.
- **Pagamentos:** Stripe, Mercado Pago ou Asaas (Pix e boleto no Brasil). Nunca guardar dados de cartão.
- **Arquivos:** storage de objetos (S3, R2, Supabase Storage), nunca no banco.
- **E-mail transacional e notificações:** qual serviço, se o MVP precisa.
- **IA:** qual modelo, onde roda a chamada (sempre no servidor) e qual o custo estimado por uso.

## 4. Registrar como decisão

Cada escolha entra no `ideia.md` e depois no PRD como decisão, no formato:

> D3: Postgres no Neon, porque o perfil prefere Postgres e o plano gratuito cobre o MVP. Descartado: Firebase (modelo de dados relacional pesa a favor de SQL).

Se o usuário não sabe e não quer decidir, use a recomendação e registre como suposição para ele confirmar na ficha de decisão.
