# Template do PRD.md

O `PRD.md` é a fonte da verdade e é escrito para dois leitores: uma pessoa que vai decidir e um agente de código que vai construir. Para o agente, o que importa é não haver ambiguidade: IDs estáveis, requisitos testáveis, decisões com o porquê e limites claros do que **não** fazer.

## Conteúdo

- Mínimo para gerar
- Princípios de escrita
- Estrutura
- Variações por tipo de documento
- Checklist antes de salvar

---

## Mínimo para gerar

Sem estes itens o PRD sai vago. No modo rápido, é com esta lista que você confere as lacunas:

1. Público principal, específico
2. Problema e alternativa atual
3. O que entra no MVP **e o que fica fora**
4. Fluxo principal, passo a passo
5. Entidades de dados principais
6. Stack (ou recomendação aceita)
7. Métrica principal de sucesso

## Princípios de escrita

- **Seção que não muda o build ou uma decisão de produto não entra.** Melhor um PRD de 4 páginas preciso do que um de 15 genérico.
- **Requisitos usam "deve"** e têm critério de aceite verificável. "Deve ser rápido" não é critério; "a lista de alunos carrega em menos de 1 s com 500 registros" é.
- **IDs estáveis** (RF-01, RNF-01, D-01, R-01, E-01) para o PLANO.md e o agente poderem referenciar.
- **Critérios de aceite em lista numerada, nunca checkbox.** O PRD é especificação, não lista de tarefas: quem lê é um agente, e ele precisa citar o critério ("RF-03, critério 2"), não marcar. Checkbox só existe no PLANO.md, onde o agente marca o que concluiu.
- **Cada decisão traz o porquê e a alternativa descartada.** É isso que impede o agente (ou você daqui a três meses) de "melhorar" algo que foi decidido de propósito.
- **Prazo realista para quem constrói com IA.** A ordem de construção é em fases, não em semanas. Se o documento falar em tempo, separe o tempo de construir (horas ou dias com agente) do tempo de esperar terceiros (aprovações, revisões, liberações), que é o que costuma definir a data.
- **Fora de escopo é tão importante quanto o escopo.** Agentes adoram adicionar coisas; a lista de "fora" é o freio.
- **Sem perguntas em aberto.** Tudo o que ficou pendente aparece como risco aceito, com dono e gatilho de revisão.
- Siga o tom e as regras de escrita do perfil.

## Estrutura

Use estes títulos, nesta ordem. Os números ajudam a referenciar ("ver seção 7").

```markdown
# <Produto>: PRD

> **Status:** aprovado na banca em <data> · **Modo:** <rápido | consultivo> · **Tipo:** <produto novo | feature | técnico> · **Versão:** 1.0

## 1. Resumo
<Frase de posicionamento, em negrito.>
<Um parágrafo: o que é, para quem, o que resolve e o que torna diferente.>

## 2. Problema e contexto
- **Dor:** <a dor, do ponto de vista de quem sofre>
- **Como resolvem hoje:** <alternativa atual e o que tem de ruim>
- **Por que agora:** <o que mudou>

## 3. Público
<Usuário principal, com contexto de uso (dispositivo, momento, familiaridade com tecnologia). Se quem paga for diferente de quem usa, diga.>
<Outros perfis de usuário (admin etc.) em lista curta.>

## 4. Objetivos e métricas
| Métrica | Meta | Prazo | Como medir |
|---|---|---|---|
| <principal> | | | |

**Não-objetivos:** <o que o produto deliberadamente não tenta ser ou resolver>

## 5. Escopo do MVP
**Dentro:**
- <item> (RF-xx)

**Fora (e por quê):**
- <item>: <motivo curto; quando reavaliar>

## 6. Fluxos principais
### F1. <nome do fluxo>
1. <passo, do ponto de vista do usuário>
2. ...
**Resultado:** <estado final>

## 7. Requisitos funcionais
### RF-01. <nome curto>
<O sistema deve...>
**Critérios de aceite:**
1. <comportamento verificável>
2. <caso de erro ou borda>
**Prioridade:** <essencial | importante> · **Fluxo:** F1

## 8. Requisitos não funcionais
- **RNF-01 Segurança:** <...>
- **RNF-02 Privacidade/LGPD:** <...>
- **RNF-03 Desempenho:** <...>
- **RNF-04 Acessibilidade:** <...>
<Só os que se aplicam, cada um verificável.>

## 9. Modelo de dados
| Entidade | Campos principais | Relações |
|---|---|---|
| `E-01 Nome` | <campos> | <pertence a / tem muitos> |

## 10. Stack e arquitetura
| Camada | Escolha | Por quê |
|---|---|---|
<Um parágrafo curto de arquitetura, se houver algo além do óbvio (filas, jobs, integrações).>

## 11. Decisões
- **D-01:** <decisão>. Porque <motivo>. Descartado: <alternativa>.

## 12. Riscos aceitos
| ID | Risco | Levantado por | Mitigação | Revisar quando |
|---|---|---|---|---|

## 13. Parecer da banca
| Persona | Sinal | Ponto principal | Como foi tratado |
|---|---|---|---|
| Helena · Investidora | 🟢 | | |
| Caio · Dev sênior | 🟡 | | |
| Bia · Cliente ideal | 🟢 | | |

## 14. Ordem de construção
1. <fase>: <o que entrega> (RF-xx, RF-yy)
<Mesma sequência do PLANO.md, se ele existir.>
```

## Variações por tipo de documento

- **Feature em produto existente:** a seção 3 vira "Quem é afetado" (pode ser curta); a seção 9 mostra só as entidades novas ou alteradas; acrescente "Impacto no que já existe" depois da seção 6 (telas, APIs e dados que mudam e como migrar).
- **Técnico ou refatoração:** a seção 2 vira "Situação atual e problema técnico"; as seções 3 e 6 podem sair; acrescente "Plano de migração e rollback" depois da seção 10; as métricas são técnicas (tempo de build, custo, erros), mas pelo menos uma precisa ligar a mudança ao negócio.
- **Modo rápido:** a seção 13 traz o parecer relâmpago (uma linha por persona). Diga isso na própria seção.

## Checklist antes de salvar

Releia o PRD contra esta lista. Se algo falhar, corrija antes de entregar.

- [ ] Nenhuma pergunta em aberto, nenhum "a definir", nenhum "TBD".
- [ ] Todo RF tem pelo menos um critério de aceite verificável e um caso de erro quando houver entrada do usuário.
- [ ] Todo item de "Dentro" do escopo aponta para um RF, e todo RF está no escopo.
- [ ] A lista de "Fora" existe e tem motivo em cada item, e nada do que está fora aparece prometido em outro lugar (resumo, posicionamento, fluxos).
- [ ] Toda decisão tem o porquê.
- [ ] A ordem de construção não contradiz dependências (não se constrói o pagamento antes do cadastro que ele usa).
- [ ] O parecer da banca é o que ela disse de fato, sem suavizar sinais vermelhos.
- [ ] Nenhum número de mercado sem fonte ou sem a marcação de hipótese.
- [ ] Nenhuma estimativa de código em semanas ou meses; quando há espera de terceiros, ela aparece separada e com o pedido começando na Fase 1.
- [ ] Nada no documento que não esteja na ficha de decisão ou no `ideia.md`.
