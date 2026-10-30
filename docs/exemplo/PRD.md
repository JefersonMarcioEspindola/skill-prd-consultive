# TreinoCerto: PRD

> **Status:** aprovado na banca em 30/10/2026 · **Modo:** consultivo · **Tipo:** produto novo · **Versão:** 1.0

## 1. Resumo

**Para personal trainers autônomos que perdem tempo montando treinos no WhatsApp e cobrando aluno por aluno, o TreinoCerto é um app de gestão de alunos que centraliza treino e cobrança. Diferente de planilhas e do próprio WhatsApp, o aluno recebe o treino no celular e a mensalidade é cobrada sozinha por Pix.**

O MVP foca em um único ciclo: o personal cadastra o aluno, envia o treino, o aluno marca o que fez e a cobrança mensal sai automaticamente. Agenda compartilhada, avaliação física e marketplace de personais ficam para depois.

## 2. Problema e contexto

- **Dor:** o personal com 15 a 40 alunos gasta de 4 a 6 horas por semana montando treino em PDF ou mensagem e cobrando mensalidade atrasada um por um.
- **Como resolvem hoje:** WhatsApp para treino e lembretes, planilha para controle de pagamento, Pix manual. Nada avisa quando o aluno some ou atrasa.
- **Por que agora:** Pix Automático (cobrança recorrente via Pix) tornou viável a cobrança recorrente sem cartão, que é o meio de pagamento que esse público mais rejeita.

## 3. Público

Personal trainer autônomo, de 25 a 40 anos, com 15 a 40 alunos, que atende em academia ou em domicílio. Usa o celular o dia todo, entre um atendimento e outro; o computador é raro. Quem paga o TreinoCerto é o personal; o aluno usa de graça.

- **Aluno:** recebe o treino, marca exercícios feitos, paga a mensalidade.

## 4. Objetivos e métricas

| Métrica | Meta | Prazo | Como medir |
|---|---|---|---|
| Personais pagantes ativos | 30 | 90 dias após lançamento | Assinaturas ativas no provedor de pagamento |
| Alunos com treino aberto na semana | 60% | Por personal, a partir da 4ª semana | Eventos de abertura de treino |
| Mensalidades pagas sem lembrete manual | 70% | 60 dias | Cobranças pagas até o vencimento |

**Não-objetivos:** não é app de academia (sem gestão de catraca ou turma), não monta treino com IA no MVP, não é rede social de fitness.

## 5. Escopo do MVP

**Dentro:**
- Cadastro do personal e convite de alunos por link (RF-01, RF-02)
- Montagem e envio de treino com biblioteca de exercícios (RF-03)
- Aluno marca o treino como feito (RF-04)
- Cobrança mensal recorrente por Pix (RF-05)
- Painel do personal com alertas de aluno sumido ou inadimplente (RF-06)

**Fora (e por quê):**
- Agenda de horários: personal resolve no WhatsApp hoje sem dor grande; reavaliar com 30 pagantes.
- Avaliação física e fotos de evolução: dados de saúde aumentam a exigência de LGPD; reavaliar na v2 com a Dra. Lúcia.
- Treino gerado por IA: diferencial incerto e custo variável; reavaliar se a retenção estiver acima de 60%.
- App nativo nas lojas: PWA cobre o uso no celular e evita a revisão das lojas.

## 6. Fluxos principais

### F1. Personal convida aluno
1. Personal toca em "Novo aluno", informa nome, WhatsApp e valor da mensalidade.
2. O app gera um link de convite e abre o WhatsApp com a mensagem pronta.
3. Aluno abre o link, cria acesso com o número de telefone e aceita a cobrança recorrente.

**Resultado:** aluno ativo, cobrança programada.

### F2. Personal envia treino
1. Personal escolhe o aluno e toca em "Novo treino".
2. Adiciona exercícios da biblioteca, com séries, repetições e observação.
3. Publica; o aluno recebe uma notificação.

**Resultado:** treino visível no app do aluno.

### F3. Aluno faz o treino
1. Aluno abre o treino do dia.
2. Marca cada exercício como feito.
3. Ao terminar, o treino fica registrado no histórico.

**Resultado:** personal vê a frequência atualizada.

## 7. Requisitos funcionais

### RF-01. Cadastro do personal
O sistema deve permitir que o personal crie conta com telefone e código por SMS e assine o plano mensal.
**Critérios de aceite:**
1. Conta criada em menos de 2 minutos, sem e-mail obrigatório.
2. Código SMS inválido mostra erro e permite reenviar após 30 s.
3. Sem assinatura ativa, o personal só acessa a tela de assinatura.
**Prioridade:** essencial · **Fluxo:** F1

### RF-02. Convite de aluno
O sistema deve gerar um link único de convite por aluno, válido por 7 dias.
**Critérios de aceite:**
1. O link abre o cadastro do aluno já vinculado ao personal.
2. Link expirado mostra mensagem e opção de pedir novo convite.
3. O personal vê o status do convite (enviado, aceito, expirado).
**Prioridade:** essencial · **Fluxo:** F1

### RF-03. Montagem de treino
O sistema deve permitir montar treinos a partir de uma biblioteca de pelo menos 150 exercícios, com séries, repetições, carga e observação.
**Critérios de aceite:**
1. Busca por nome do exercício retorna resultados enquanto o personal digita.
2. O personal pode duplicar um treino de um aluno para outro.
3. Treino sem nenhum exercício não pode ser publicado.
**Prioridade:** essencial · **Fluxo:** F2

### RF-04. Execução do treino pelo aluno
O sistema deve permitir que o aluno marque exercícios como feitos, inclusive sem internet, sincronizando quando a conexão voltar.
**Critérios de aceite:**
1. Marcação offline aparece como pendente e sincroniza sozinha.
2. O treino concluído aparece no histórico do aluno e no painel do personal.
**Prioridade:** essencial · **Fluxo:** F3

### RF-05. Cobrança recorrente
O sistema deve cobrar a mensalidade do aluno por Pix Automático na data definida pelo personal, repassando o valor ao personal pelo provedor de pagamento.
**Critérios de aceite:**
1. O aluno autoriza a recorrência uma única vez, no convite.
2. Falha de cobrança gera nova tentativa em 3 dias e alerta ao personal.
3. O sistema nunca armazena dados bancários do aluno, só o identificador do provedor.
**Prioridade:** essencial · **Fluxo:** F1

### RF-06. Painel do personal
O sistema deve mostrar ao personal a lista de alunos com última atividade e status de pagamento, destacando quem está há mais de 7 dias sem treinar ou com cobrança em atraso.
**Critérios de aceite:**
1. Os alertas aparecem no topo do painel, ordenados por gravidade.
2. Um toque no aluno em alerta abre o WhatsApp com mensagem sugerida.
**Prioridade:** importante · **Fluxo:** F3

## 8. Requisitos não funcionais

- **RNF-01 Celular primeiro:** todas as telas usáveis com uma mão em telas a partir de 360 px.
- **RNF-02 Privacidade/LGPD:** termo de uso e política de privacidade aceitos no cadastro; aluno pode pedir exclusão dos dados pelo app.
- **RNF-03 Desempenho:** painel do personal carrega em menos de 1,5 s em 4G com 40 alunos.
- **RNF-04 Instalação:** PWA instalável na tela inicial, com ícone e funcionamento offline do treino do dia.

## 9. Modelo de dados

| Entidade | Campos principais | Relações |
|---|---|---|
| `E-01 Personal` | nome, telefone, status da assinatura | tem muitos Alunos |
| `E-02 Aluno` | nome, telefone, valor da mensalidade, dia de vencimento, status | pertence a Personal; tem muitos Treinos e Cobranças |
| `E-03 Exercicio` | nome, grupo muscular, vídeo | usado em muitos Treinos |
| `E-04 Treino` | título, itens (exercício, séries, reps, carga), publicado em | pertence a Aluno; tem muitas Execuções |
| `E-05 Execucao` | data, itens concluídos, sincronizado | pertence a Treino |
| `E-06 Cobranca` | competência, valor, status, id no provedor | pertence a Aluno |

Estados da cobrança: `agendada → paga` ou `agendada → falhou → nova tentativa → paga | atrasada`.

## 10. Stack e arquitetura

| Camada | Escolha | Por quê |
|---|---|---|
| Front e back | Next.js + TypeScript (PWA) | Um repositório só; perfil prefere Next; PWA evita as lojas |
| Banco | Postgres no Neon, Drizzle ORM | Dados relacionais; plano gratuito cobre o MVP |
| Auth | Login por telefone (SMS) via provedor gerenciado | Público não usa e-mail no dia a dia |
| Pagamentos | Asaas (Pix Automático e repasse) | Suporta recorrência por Pix e split para o personal |
| Hospedagem | Vercel | Deploy simples, integra com Next |
| Offline | Service worker com fila de sincronização | Academia costuma ter sinal ruim |

Os webhooks do provedor de pagamento atualizam o status da cobrança; um job diário gera os alertas do painel.

## 11. Decisões

- **D-01:** Cobrança por Pix Automático em vez de cartão. Porque o público rejeita cartão em mensalidade de serviço pessoal. Descartado: cartão recorrente.
- **D-02:** Preço por faixa de alunos (até 15, até 40) em vez de preço fixo. Porque alinha o custo com a receita do personal (objeção da Helena). Descartado: preço único.
- **D-03:** PWA em vez de app nativo. Porque publica no mesmo dia e cada atualização vai direto ao aluno, sem esperar a revisão das lojas (objeção do Caio). Descartado: Expo nas lojas.
- **D-04:** Aluno não paga nem cria senha. Porque cada passo a mais no convite derruba a adesão (objeção da Bia). Descartado: cadastro com e-mail e senha.

## 12. Riscos aceitos

| ID | Risco | Levantado por | Mitigação | Revisar quando |
|---|---|---|---|---|
| R-01 | Cancelamento alto de personais nos meses de baixa (dezembro e janeiro) | Helena | Plano anual com desconto a partir do 3º mês | Churn mensal acima de 8% |
| R-02 | Liberação do Pix Automático pelo provedor demorar (depende de aprovação da conta, não de código) | Caio | Pedir a liberação no primeiro dia (T-00); plano B: Pix mensal com lembrete automático | Ainda não liberado quando o resto do MVP estiver pronto |
| R-03 | Aluno não instalar o PWA e continuar pedindo treino no WhatsApp | Bia | Link do treino também funciona sem instalar | Menos de 40% de abertura na 4ª semana |

## 13. Parecer da banca

| Persona | Sinal | Ponto principal | Como foi tratado |
|---|---|---|---|
| Helena · Investidora | 🟢 | Público autônomo cancela fácil quando o mês aperta | D-02 e risco aceito R-01 |
| Caio · Dev sênior | 🟡 | O código sai em um ou dois dias; quem define o lançamento é a liberação do Pix Automático pelo provedor | D-03 e risco aceito R-02 |
| Bia · Cliente ideal (personal trainer) | 🟢 | Aluno não vai criar senha nem instalar app só para ver treino | D-04 e risco aceito R-03 |

## 14. Ordem de construção

1. **Fundação:** projeto, banco, auth por telefone e assinatura do personal (RF-01). Em paralelo, no primeiro dia: abrir a conta no Asaas e pedir a liberação do Pix Automático.
2. **Alunos e treinos:** convite, biblioteca e montagem de treino (RF-02, RF-03).
3. **Execução:** treino do aluno com offline (RF-04).
4. **Cobrança:** Pix Automático, autorização dentro do convite (completa o F1) e webhooks (RF-05).
5. **Painel e alertas:** (RF-06), depois deploy e teste com 5 personais.
