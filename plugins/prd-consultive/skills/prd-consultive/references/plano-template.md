# Template do PLANO.md

O plano transforma o PRD em trabalho executável, em pedaços que um agente de código (ou uma pessoa) consegue pegar um de cada vez. Cada tarefa precisa ser pequena o bastante para caber em uma sessão e clara o bastante para dizer quando terminou.

## Regras

- **Ordem por dependência:** uma tarefa só vem depois daquilo que ela usa. A fundação (projeto, banco, auth) vem antes das funcionalidades.
- **Toda fase termina com algo que dá para ver funcionando.** Evite fases só de "infraestrutura" sem nada para testar.
- **Toda tarefa referencia os RF do PRD** e tem critério de pronto. Uma tarefa sem RF precisa justificar por que existe (setup, deploy).
- **Tamanho:** de 3 a 8 tarefas por fase. Cada tarefa cabe em uma sessão de agente (pedir, construir e testar em até 1 ou 2 horas); se parecer maior, divida. Um MVP inteiro costuma levar de um a três dias de trabalho com agente. Nunca estime código em semanas.
- **Dependências externas primeiro:** o que depende de terceiros (abrir conta no provedor de pagamento, pedir liberação de API, comprar domínio, enviar app para revisão) vira a tarefa `T-00` da Fase 1, marcada como "em paralelo", porque corre enquanto o código é feito e normalmente é o que define a data de lançamento.
- **Mesma sequência da seção 14 do PRD.** Se divergir, um dos dois está errado: corrija.

## Estrutura

```markdown
# <Produto>: plano de desenvolvimento

> Baseado em PRD.md v<versão>. Stack: <resumo de uma linha>.

## Como usar este plano
Execute uma fase por vez. Ao terminar cada tarefa, marque [x] e confira os critérios de pronto. Não comece uma fase antes de a anterior estar funcionando.

## Fase 1: <nome> · entrega: <o que dá para ver funcionando no fim>

### T-01. <nome da tarefa>
- **Requisitos:** RF-01, RF-02
- **Depende de:** nenhuma
- **O que fazer:** <2 a 4 linhas objetivas>
- **Pronto quando:**
  - [ ] <critério verificável>
  - [ ] <teste ou verificação manual>

### T-02. ...

## Fase 2: ...

## Prompt de handoff

Cole no seu agente de código (Claude Code, Codex, Cursor etc.) dentro da pasta do projeto:

> Leia `docs/PRD.md` e `docs/PLANO.md` antes de qualquer coisa. O PRD é a fonte da verdade: respeite a seção 5 (o que fica fora do MVP) e a seção 11 (decisões, com o porquê de cada uma) e não mude nada disso sem me perguntar. Execute só a Fase 1 do plano, uma tarefa por vez, na ordem. Ao terminar cada tarefa, confira os critérios de "Pronto quando", marque a tarefa no PLANO.md e me diga em duas linhas o que foi feito. Se encontrar algo que o PRD não responde, pare e pergunte em vez de decidir sozinho.
```

Ao entregar, sugira copiar `PRD.md` e `PLANO.md` para uma pasta `docs/` do projeto, que é onde o prompt de handoff procura.
