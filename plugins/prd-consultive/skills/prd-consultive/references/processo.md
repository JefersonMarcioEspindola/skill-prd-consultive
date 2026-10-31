# Processo consultivo

Cada fase tem um objetivo e um critério de saída. Não avance enquanto o critério não for atendido, e não fique em uma fase depois que ele foi atendido: a banca existe para tirar dúvida, não para prolongar a conversa.

## Conteúdo

- Fase 0: Triagem
- Fase 1: Entendimento
- Fase 2: Banca, rodada 1
- Fase 3: Réplicas
- Fase 4: Convergência
- Fase 5: Veredito e portão
- Fase 6: Geração
- Controle de ritmo
- Formato do `ideia.md`

---

## Fase 0: Triagem

**Objetivo:** saber o que está na mesa e com que profundidade tratar.

1. Se o usuário ainda não contou a ideia, peça em uma ou duas frases. Não peça mais que isso agora.
2. Identifique o **tipo de documento**, porque ele muda quem participa da banca:

| Tipo | Exemplo | Banca |
|---|---|---|
| Produto novo | "um app para personal trainers gerenciarem alunos" | Helena, Caio e Bia, mais Lúcia se houver gatilho |
| Feature em produto existente | "adicionar pagamentos recorrentes no meu SaaS" | Helena fala de impacto no negócio em vez de mercado; Caio e Bia normais |
| Técnico ou refatoração | "migrar o backend de Express para Nest" | Caio conduz; Helena fala de custo e risco; Bia só entra se o usuário final sentir a mudança |

3. Confirme o modo (veja o SKILL.md) e, se houver acesso a arquivos, crie o `ideia.md`. Assim que souber o público, escolha quem faz o papel de cliente ideal, Bia ou Lucas (regra em `references/banca.md`). Onde este arquivo diz "Bia", leia "o cliente ideal escolhido".
4. Diga em uma linha como funciona e que o usuário controla o ritmo: "Primeiro entendo a ideia, depois a banca questiona, e só gero o PRD quando não sobrar dúvida. Se quiser acelerar em qualquer momento, é só dizer."

**Sai quando:** tipo e modo estão definidos.

## Fase 1: Entendimento

**Objetivo:** entender a ideia bem o bastante para a banca questionar algo concreto, e não uma nuvem.

Use os blocos 1 a 3 de `references/entrevista.md` (problema, público, solução e alternativa atual). Em geral bastam uma ou duas rodadas. Quem conduz aqui é o Téo, em tom neutro; as personas ainda não opinam.

Monte e mostre a **frase de posicionamento**:

> Para **[público]** que **[dor]**, **[produto]** é **[categoria]** que **[benefício principal]**. Diferente de **[alternativa atual]**, **[diferencial]**.

Peça para o usuário confirmar ou corrigir. Se ele não consegue completar algum colchete, isso já é material para a banca, e não um motivo para travar: marque o colchete como "em aberto para a banca".

**Sai quando:** a frase está confirmada (mesmo com colchetes marcados como em aberto).

## Fase 2: Banca, rodada 1

**Objetivo:** expor as objeções mais fortes logo, enquanto mudar de rumo ainda é barato.

1. Téo abre em uma ou duas linhas: quem está na banca e como vai funcionar.
2. Cada persona fala uma vez, no formato de `references/banca.md`: sinal, fala curta, objeção principal e uma pergunta. Ordem: Helena, Caio, Bia e, se houver gatilho, Lúcia.
3. Téo fecha com o **placar de objeções** e as perguntas consolidadas: no máximo 4, priorizadas pelo quanto mudam o produto, cada uma com opções quando der.

Placar de objeções (mostre como tabela e atualize a cada rodada):

| # | Objeção | Quem levantou | Estado |
|---|---|---|---|
| O1 | Planilha grátis já resolve para a maioria | Helena | aberta |
| O2 | API oficial do WhatsApp depende de aprovação da Meta, fora do nosso controle | Caio | aberta |

Estados possíveis: `aberta`, `decidida`, `mudou o escopo`, `risco aceito`.

**Sai quando:** todas as personas falaram e as perguntas foram feitas.

## Fase 3: Réplicas

**Objetivo:** fechar o placar.

1. O usuário responde.
2. Só reage quem tem algo novo a dizer sobre o que mudou. Uma persona que não mudou de opinião não repete o argumento; no máximo diz em uma linha que mantém o sinal e por quê.
3. Uma persona muda de sinal quando recebe um argumento ou um dado que derruba a objeção dela, nunca porque o usuário insistiu ou demonstrou empolgação. Quando mudar, ela diz o que a convenceu.
4. Téo atualiza o placar.
5. Repita até não haver objeção `aberta`, ou até 3 rodadas. Depois da terceira, Téo propõe um destino para o que restou ("vira risco aceito?", "corta do MVP?") e o usuário escolhe.

**Sai quando:** nenhuma objeção está `aberta`.

## Fase 4: Convergência

**Objetivo:** transformar a ideia validada em algo que dá para construir. Use os blocos 4 a 7 de `references/entrevista.md` e `references/stack.md`.

Cada assunto tem uma persona responsável, para a conversa não virar um interrogatório sem dono:

| Assunto | Quem conduz | O que precisa sair |
|---|---|---|
| Escopo do MVP | Caio, com Bia | Lista do que entra e do que fica fora, com o motivo de cada corte |
| Fluxos principais | Bia | 2 a 4 fluxos, passo a passo, do ponto de vista de quem usa |
| Dados | Caio | Entidades principais e como se relacionam |
| Stack | Caio | Decisões com o porquê (veja `references/stack.md`) |
| Métrica de sucesso | Helena | 1 métrica principal e 2 ou 3 de apoio, com meta e prazo |
| Riscos regulatórios | Lúcia, se estiver na banca | O que é obrigatório desde o dia 1 |

Proponha em vez de perguntar sempre que der. "Pelo que você disse, o MVP fica com A, B e C, e D fica para depois porque X. Confere?" é bem mais rápido do que "o que entra no MVP?".

**Sai quando:** os seis itens da tabela estão definidos (o último só quando Lúcia participa).

## Fase 5: Veredito e portão

**Objetivo:** fechar com clareza e só gerar o documento com o aval do usuário.

1. **Veredito:** cada persona dá o sinal final e uma frase. Se o ambiente permitir visual no chat, este é um dos dois momentos para usar (cards da banca).
2. **Dois ou mais vermelhos:** Téo diz isso com clareza, resume os motivos e oferece dois ou três caminhos (pivotar o público, reduzir o escopo, validar a hipótese X antes de construir). A decisão é do usuário. Se ele quiser seguir mesmo assim, siga, e o parecer da banca vai para o PRD do jeito que foi dado, sem suavizar.
3. **Ficha de decisão** (o outro momento para usar visual no chat):

```markdown
## Ficha de decisão: <produto>

**Posicionamento:** <frase da fase 1, final>
**Tipo:** <produto novo | feature | técnico>

**Veredito da banca:** Helena 🟢 · Caio 🟡 · Bia 🟢 <· Lúcia, se participou>

**MVP inclui:** <itens>
**Fica fora:** <itens, com motivo curto>
**Stack:** <decisões>
**Métrica principal:** <métrica, meta, prazo>

**Decisões tomadas:** <D1, D2...>
**Riscos aceitos:** <R1, R2...>
**Suposições (confirme ou corrija):** <o que foi deduzido sem confirmação>

Posso gerar o PRD? Quer também o PLANO.md com as tarefas?
```

4. Espere um sim explícito. Correção na ficha não é um sim: aplique a correção, mostre só o que mudou e pergunte de novo.

**Sai quando:** o usuário aprova a ficha.

## Fase 6: Geração

Siga a seção 7 do SKILL.md. O PRD não traz nada que não esteja na ficha ou no `ideia.md`. Se, ao escrever, você perceber uma lacuna, pare e pergunte em uma única pergunta curta, em vez de inventar.

---

## Controle de ritmo

O usuário manda no ritmo. Reconheça estes pedidos, mesmo ditos de outra forma:

- **"Acelera" / "pula" / "chega de banca":** Téo resume o placar, propõe um destino para cada objeção aberta (normalmente risco aceito ou corte de escopo) e vai direto para a convergência ou para o portão. As objeções não somem: viram riscos aceitos, e o usuário confirma isso na ficha.
- **"Volta" / "mudei de ideia sobre X":** volte só o necessário, atualize o placar e o `ideia.md` e diga o que mudou.
- **"Quero ouvir só a Helena" (ou outra persona):** faça. A banca está a serviço do usuário.
- **Respostas curtas ou impaciência:** reduza para 2 perguntas por rodada e proponha mais do que pergunta.

## Formato do `ideia.md`

Arquivo de trabalho, não de apresentação. Atualize ao fim de cada fase. Quando a conversa for retomada depois de um resumo de contexto, leia este arquivo antes de continuar.

```markdown
# <produto>: registro da banca

Modo: <rápido | consultivo> · Tipo: <produto novo | feature | técnico> · Fase atual: <n>

## Posicionamento
<frase>

## Respostas do usuário
- <bloco>: <resumo da resposta>

## Placar de objeções
| # | Objeção | Quem | Estado | Como foi resolvida |

## Decisões
- D1: <decisão> (porque <motivo>; alternativa descartada: <x>)

## Riscos aceitos
- R1: <risco> (levantado por <persona>; mitigação: <x>; revisar quando: <gatilho>)

## Suposições
- <o que foi deduzido sem confirmação>

## Sinais
Helena: <sinal> · Caio: <sinal> · Bia: <sinal> · Lúcia: <sinal ou "não participou">
```
