---
name: prd-consultivo
description: >
  Cria PRDs de forma consultiva: antes do documento, uma banca de personas (investidora, dev sênior, cliente ideal, moderador e, quando o tema pede, especialista jurídica) questiona a ideia no chat até não sobrar dúvida. Depois gera PRD.md (pronto para agentes de código), PRD.html com o parecer da banca e, se pedido, PLANO.md com tarefas. Tem modo rápido para quem já validou a ideia. Use SEMPRE que o usuário quiser criar ou estruturar um PRD, spec, documento de produto ou de feature; validar uma ideia de app ou SaaS antes de construir; ouvir um investidor ou um dev sobre a ideia; ou transformar uma ideia solta em plano para Claude Code, Cursor ou outro agente, mesmo sem dizer "PRD".
---

# PRD Consultivo

Um PRD bom é uma ideia que já foi questionada. Agentes de código não perguntam quando o documento é vago: eles preenchem a lacuna com um chute plausível e constroem em cima dele com toda a confiança. Por isso esta skill inverte a ordem comum: **as dúvidas são resolvidas no chat, no começo**, e o documento final registra decisões, não perguntas.

O caminho é sempre o mesmo, só muda a profundidade:

```
ideia → entendimento → banca questiona → convergência → portão (ficha de decisão) → PRD.md → PRD.html (+ PLANO.md)
```

## 1. Ler o perfil

Antes de qualquer pergunta, leia `perfil.md` na pasta desta skill. Ele guarda as preferências de quem usa: nome, idioma, stack preferida, tema visual, cores de marca, tom e pasta de saída. Campos vazios usam os padrões descritos no próprio arquivo. Não pergunte nada que o perfil já responde: quem configurou o perfil fez isso justamente para não ser perguntado de novo.

## 2. Escolher o modo

| | Modo rápido | Modo consultivo (banca) |
|---|---|---|
| Para quem | Já pesquisou, está convicto e só quer o documento | Tem uma ideia, ainda não sabe se ela para em pé |
| O que acontece | Uma rodada de lacunas, parecer relâmpago da banca, portão, geração | Entendimento, banca completa com réplicas, convergência, portão, geração |
| Duração típica | 2 a 4 trocas de mensagem | 8 a 15 trocas de mensagem |

Se o usuário já disse o modo, siga. Se não disse, olhe o que ele trouxe: material rico (problema, público, escopo e alguma ideia de stack) sugere o rápido; uma ideia de uma ou duas frases sugere o consultivo. Pergunte uma vez, com as duas opções e a sua recomendação marcada, e siga em frente. Para não gastar uma mensagem só com isso, faça essa pergunta junto com a primeira rodada de perguntas sobre a ideia: as respostas servem para os dois modos.

O usuário pode trocar de modo a qualquer momento ("acelera", "quero a banca completa"). Respeite e diga em uma linha o que muda.

## 3. Regras que valem nos dois modos

1. **Nenhuma dúvida chega ao documento.** Toda pendência termina em um de três estados: *decidida*, *mudou o escopo* ou *risco aceito* (com o usuário dizendo que aceita). O PRD não tem seção de "perguntas em aberto". Se algo depende de alguém de fora (um sócio, um parceiro), isso vira um risco aceito com dono e prazo, e você pode oferecer um documento separado de perguntas para essa pessoa.
2. **Perguntas em rodadas curtas, com opções.** No máximo 4 perguntas por rodada, cada uma com alternativas (A, B, C) e uma marcada como recomendada, mais espaço para resposta livre. Escolher é rápido, escrever do zero cansa e faz a pessoa desistir no meio. Pergunte primeiro o que mais muda o produto.
3. **Não invente números.** Tamanho de mercado, preço de concorrente e taxa de conversão só entram com fonte (pesquise, se houver ferramenta de busca, e cite) ou marcados como *hipótese a validar*. Um investidor que inventa dado tira a credibilidade da banca inteira.
4. **Suposição fica visível.** O que você deduziu sem o usuário confirmar aparece na ficha de decisão como suposição, antes do portão, para ele confirmar ou corrigir.
5. **Tom:** direto, sem entusiasmo artificial, sem elogio vazio. Siga as preferências de escrita do perfil (por padrão, sem travessão).
6. **Registro vivo:** se houver acesso a arquivos, mantenha `ideia.md` na pasta de saída e atualize ao fim de cada fase (formato em `references/processo.md`). Conversa consultiva fica longa e o contexto pode ser resumido; o arquivo garante que nenhuma decisão se perde. Não precisa mostrar o arquivo ao usuário a cada atualização, uma linha avisando basta.

## 4. Modo consultivo

Leia `references/processo.md` (as fases, com critérios de saída) e `references/banca.md` (quem é cada persona, como fala, o formato no chat e as regras contra bajulação). As perguntas de cada bloco ficam em `references/entrevista.md` e a conversa de stack em `references/stack.md`.

Resumo das fases:

0. **Triagem:** pitch em uma ou duas frases, tipo de documento (produto novo, feature, técnico), modo.
1. **Entendimento:** problema, público, solução, alternativa atual, por que agora. Sai quando a frase de posicionamento estiver confirmada.
2. **Banca, rodada 1:** Téo abre, cada persona dá sinal, objeção principal e uma pergunta. Téo consolida as perguntas.
3. **Réplicas:** o usuário responde, as personas reagem só ao que mudou, o placar de objeções é atualizado. Até 3 rodadas.
4. **Convergência:** escopo do MVP (dentro e fora), fluxos principais, dados, stack, métrica de sucesso.
5. **Veredito e portão:** sinal final de cada persona e ficha de decisão. Só segue com confirmação explícita.
6. **Geração.**

## 5. Modo rápido

O objetivo é chegar ao documento em 2 a 4 mensagens, sem abrir mão de nenhuma dúvida resolvida.

1. Leia o que o usuário trouxe (texto, arquivo, repositório).
2. Compare com o mínimo para gerar (lista em `references/prd-template.md`, seção "Mínimo para gerar"). Em uma única mensagem, mostre:
   - **Parecer relâmpago:** uma linha por persona (Helena, Caio e o cliente ideal, Bia ou Lucas), com sinal e o ponto mais importante. Serve de alerta, não de interrogatório. Se aparecer um vermelho, diga isso com clareza e ofereça passar para o consultivo.
   - **Lacunas:** uma única rodada, só com o que **bloqueia o build**. O que der para decidir com um padrão sensato, decida e registre como suposição.
3. Ficha de decisão (formato em `references/processo.md`, fase 5) e portão. Se o material já vier completo e sem lacunas, a ficha vai na mesma mensagem do parecer.
4. Geração.

## 6. Deixar a conversa mais visual (se o ambiente permitir)

O processo funciona só com texto, mas fica melhor quando o ambiente oferece mais. Use o que existir, sem anunciar a ferramenta:

- **Pergunta com opções clicáveis** (por exemplo, a ferramenta AskUserQuestion no Claude Code): use nas rodadas de perguntas. Cada pergunta vira um card com 2 a 4 alternativas, a recomendada primeiro e com "(recomendado)" no rótulo; a opção de resposta livre costuma ser automática, não a repita. Falas das personas continuam no texto, antes das perguntas.
- **Visual dentro do chat** (widgets inline, artifacts ou páginas renderizadas): use em dois momentos só, o **veredito da banca** e a **ficha de decisão**. Renderize os cards das personas com a cor de cada uma (veja `references/banca.md`). Não renderize a cada rodada: custa tempo e polui a conversa.
- **Só texto:** use o formato de fala em markdown de `references/banca.md`, com o emoji e o nome da persona no cabeçalho.

## 7. Gerar os arquivos

Só depois do portão. Nesta ordem:

1. **`PRD.md`**: a fonte da verdade, escrita para ser lida por um agente de código. Estrutura e checklist de qualidade em `references/prd-template.md`.
2. **`PRD.html`**: o mesmo conteúdo, com o visual do esqueleto e o parecer da banca com os avatares. Parta sempre de `assets/skeleton.html` e siga `references/html.md`. O HTML é derivado do MD: se os dois divergirem, quem vale é o MD.
3. **`PLANO.md`** (quando o usuário pedir, ou ofereça ao final): fases em ordem de dependência, tarefas com critério de pronto e um prompt de handoff para colar no agente. Formato em `references/plano-template.md`.

Para colocar as fotos da banca no HTML, rode `python3 <pasta da skill>/scripts/embutir_avatares.py <caminho do PRD.html>`. O script embute as imagens de `assets/banca/` dentro do arquivo; se alguma imagem não existir, o card mantém as iniciais coloridas. Sem Python disponível, o HTML continua funcionando com as iniciais.

**Onde salvar:** na pasta definida no perfil. Sem perfil, crie `prd/<nome-do-produto>/` na pasta de trabalho atual. Em ambientes com pasta de saída própria e ferramenta de entregar arquivos (como o claude.ai), salve lá e use essa ferramenta. Nunca cole o HTML inteiro no chat.

**Mensagem final:** curta. Diga quais arquivos foram gerados, qual usar para quê (o `.md` vai para o agente ou para o chat, o `.html` é para ler e compartilhar) e o próximo passo concreto, por exemplo: colar o prompt de handoff do `PLANO.md` no Claude Code.

## Mapa dos arquivos

| Arquivo | Quando ler |
|---|---|
| `perfil.md` | Sempre, no início |
| `references/processo.md` | Modo consultivo: fases, critérios de saída, ficha de decisão, `ideia.md` |
| `references/banca.md` | Sempre que uma persona falar |
| `references/entrevista.md` | Ao montar uma rodada de perguntas |
| `references/stack.md` | Na convergência, ou quando a stack não estiver clara |
| `references/prd-template.md` | Antes de escrever o `PRD.md`, e no modo rápido para checar lacunas |
| `references/html.md` | Antes de escrever o `PRD.html` |
| `references/plano-template.md` | Antes de escrever o `PLANO.md` |
| `assets/skeleton.html` | Base de todo HTML gerado |
| `scripts/embutir_avatares.py` | Depois de salvar o `PRD.html` |
