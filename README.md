# prd-consultivo

**Uma skill do Claude que cria PRDs do jeito consultivo: antes de escrever o documento, uma banca questiona a sua ideia no chat.** Quando não sobra nenhuma dúvida, ela gera o PRD em Markdown (pronto para o Claude Code, Cursor ou outro agente) e em HTML (para ler e compartilhar).

> Versão inicial (0.1.0). Funciona, mas ainda está em evolução.

## A banca

<p>
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/helena-neutro.webp" width="88" alt="Helena">
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/caio-neutro.webp" width="88" alt="Caio">
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/bia-neutro.webp" width="88" alt="Bia">
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/lucas-neutro.webp" width="88" alt="Lucas">
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/teo-neutro.webp" width="88" alt="Téo">
  <img src="plugins/prd-consultivo/skills/prd-consultivo/assets/banca/lucia-neutro.webp" width="88" alt="Dra. Lúcia">
</p>

| Quem | O que quer saber |
|---|---|
| **Helena**, investidora | Quem paga, quanto, e o que te protege de ser copiado |
| **Caio**, dev sênior | Qual a parte mais arriscada, o que corta do MVP, o que depende de terceiros |
| **Bia** ou **Lucas**, cliente ideal | Eu usaria? Por que trocaria o que uso hoje? |
| **Téo**, moderador | Conduz, resume e registra as decisões |
| **Dra. Lúcia**, especialista | Entra quando a ideia mexe com dados sensíveis, dinheiro ou setor regulado |

Cada persona dá um sinal (🟢 seguiria, 🟡 com condições, 🔴 não seguiria), a objeção mais forte e uma pergunta. Ninguém diz só "ótima ideia".

## Dois modos

- **Rápido:** você já pesquisou e só quer o documento. Uma rodada de lacunas, um parecer relâmpago da banca e pronto.
- **Consultivo:** você tem uma ideia e quer saber se ela para em pé. Entendimento, banca com réplicas, escopo, stack e veredito.

Nos dois, as dúvidas são resolvidas **no começo, no chat**. O PRD final não tem "perguntas em aberto": cada ponto vira decisão, mudança de escopo ou risco aceito.

## O que você recebe

- `PRD.md`: a fonte da verdade, com requisitos e critérios de aceite numerados, decisões com o porquê e o que fica fora do MVP.
- `PRD.html`: o mesmo conteúdo com visual de documento e o parecer da banca com as fotos.
- `PLANO.md` (se pedir): fases e tarefas em ordem, mais um prompt pronto para colar no agente.

Veja um exemplo em [`docs/exemplo`](docs/exemplo) (ideia fictícia).

## Instalação

### Plugin do Claude Code

```text
/plugin marketplace add JefersonMarcioEspindola/skill-prd-consultivo
/plugin install prd-consultivo@prd-consultivo
```

### Manual

```bash
git clone https://github.com/JefersonMarcioEspindola/skill-prd-consultivo.git
mkdir -p ~/.claude/skills
cp -R skill-prd-consultivo/plugins/prd-consultivo/skills/prd-consultivo ~/.claude/skills/
```

### claude.ai

Compacte a pasta `plugins/prd-consultivo/skills/prd-consultivo` em um `.zip` e envie em Configurações → Capacidades → Skills.

## Como usar

Preencha `perfil.md` (opcional) com a sua stack, o tema do HTML e o tom de escrita. Depois é só falar com o Claude:

> Quero criar um PRD para um app de agendamento para barbearias.

> Coloca essa ideia na banca: um SaaS que gera contratos de freelancer com IA.

Você controla o ritmo: "acelera", "quero ouvir só a Helena", "volta, mudei de ideia sobre o preço".

## Licença

MIT
