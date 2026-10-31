# Perfil

Preencha uma vez e a skill para de perguntar o que já está aqui. Se instalou como plugin, copie este arquivo para `~/.claude/prd-consultive/perfil.md` e edite a cópia: a pasta do plugin é substituída a cada atualização. Pode deixar campos em branco: cada um tem um padrão, indicado entre parênteses.

## Quem usa

- **Nome:** (em branco: a skill não usa nome)
- **Idioma dos documentos:** (o idioma em que você escrever na conversa)
- **País:** (Brasil). Muda as leis, os meios de pagamento e a moeda que a banca usa como referência.
- **Experiência com PRD:** (em branco: a skill pergunta o modo. Se escrever "experiente", ela sugere o modo rápido quando o material vier completo)

## Banca

- **Cliente ideal:** (automático: Lucas quando o público é predominantemente masculino, Bia nos outros casos). Opções: automático, Bia, Lucas.

## Stack preferida

Usada como recomendação padrão quando a ideia não define a stack. A banca ainda pode sugerir outra coisa se a ideia pedir, e diz o porquê.

- **Web / SaaS:** (Next.js + TypeScript + Postgres)
- **Backend / API:** (Node.js + TypeScript)
- **Mobile:** (Expo / React Native)
- **Hospedagem:** (Vercel para o front, Postgres gerenciado como Neon ou Supabase)
- **Outras preferências ou restrições:** (nenhuma)

## Visual do PRD.html

- **Tema:** (claro). Opções: claro, escuro, marca.
- **Cores de marca** (só para o tema "marca"):
  - fundo: 
  - painel: 
  - texto: 
  - acento: 
  - texto sobre o acento: 
- **Fonte de títulos:** (do sistema). Se usar uma do Google Fonts, escreva o nome exato.
- **Fonte do corpo:** (do sistema)
- **Nome que aparece no header:** (nome do produto)

## Escrita

- **Tom:** (direto, sem entusiasmo artificial)
- **Evitar travessão:** (sim)
- **Outras regras de escrita:** (nenhuma)

## Saída

- **Pasta onde salvar:** (prd/<nome-do-produto>/ na pasta de trabalho atual)
- **Gerar PLANO.md por padrão:** (não, a skill oferece no final)
