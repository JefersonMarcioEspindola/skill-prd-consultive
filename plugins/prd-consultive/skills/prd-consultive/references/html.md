# PRD.html

O HTML é a versão para ler, apresentar e compartilhar. Ele não acrescenta conteúdo: tudo que está nele está no `PRD.md`. O que ele acrescenta é forma, ou seja, o componente certo para cada tipo de informação, e o parecer da banca com rosto.

## Como montar

1. Copie `assets/skeleton.html` inteiro. Não escreva CSS do zero: o esqueleto já resolve tema, celular e impressão, e reescrever gera inconsistência entre documentos.
2. Defina o tema em `<html data-tema="...">` conforme o perfil:
   - `claro` (padrão): não mexa em nada.
   - `escuro`: troque o atributo, as variáveis já estão prontas.
   - `marca`: troque o atributo, descomente o bloco `html[data-tema="marca"]` e preencha com as cores do perfil. Se o perfil indicar fontes do Google Fonts, adicione o `<link>` delas no `<head>` e ajuste `--display` e `--sans`. Confira se o texto sobre o acento (`--accent-fg`) continua legível. Se o fundo da marca for escuro, copie primeiro todas as variáveis do bloco `escuro` para o bloco `marca` (header translúcido, sinais e tags já ajustados para fundo escuro) e só depois sobrescreva as cores da marca.
3. Preencha o header (marca à esquerda, "PRD · tipo" no meio, status à direita), o hero e uma `<section>` por seção do PRD.md, com a numeração igual.
4. Apague os blocos de exemplo que não usar e **todos** os comentários.
5. Coloque as fotos (veja "Como colocar as fotos", abaixo).

## Hero

- Tags: `PRD` e o modo (`Modo consultivo` ou `Modo rápido`).
- `h1`: nome do produto.
- `.posicionamento`: a frase de posicionamento confirmada.
- `p.lede`: o parágrafo de resumo.
- `.placar`: um item por persona que avaliou, com o sinal final (sem o Téo).
- Meta: versão e data.
- TOC: uma entrada por seção, mesma ordem, com `<ol start="2">` para a numeração bater com as tags das seções.
- IDs (RF-01, D-02, R-01, E-03) sempre dentro de `<code>`, inclusive em tabelas, para não quebrarem no meio.

## Qual componente usar

| Seção do PRD.md | Componente |
|---|---|
| 1. Resumo | Vira o próprio hero (posicionamento + lede). As seções seguintes mantêm a numeração do MD, começando em 02 |
| 2. Problema e contexto | `.mod` com as linhas Dor, Como resolvem hoje, Por que agora |
| 3. Público | Texto corrido; vários perfis de usuário viram `.entity-grid` |
| 4. Objetivos e métricas | `table.tbl` dentro de `.tbl-wrap`; não-objetivos em lista |
| 5. Escopo do MVP | `.escopo` com `.col.dentro` e `.col.fora` |
| 6. Fluxos principais | `.flow` por fluxo (até uns 6 passos; com mais que isso, use lista numerada) |
| 7. Requisitos funcionais | Um `.req` por RF, critérios em `ol.aceite` (numerados, sem checkbox) |
| 8. Requisitos não funcionais | Lista, ou `table.tbl` se forem muitos |
| 9. Modelo de dados | `.entity-grid`; estados de uma entidade em `.states` |
| 10. Stack e arquitetura | `table.tbl` (camada, escolha, porquê) |
| 11. Decisões | `.dec-list` |
| 12. Riscos aceitos | `table.tbl`; o risco mais sério também em `.callout.warn` |
| 13. Parecer da banca | `.banca` com um `.persona` por membro |
| 14. Ordem de construção | `.phase-list` |
| Seções extras (impacto, migração) | `.mod` ou `.phase-list`, conforme o conteúdo |

Se um conteúdo não encaixar em nenhum componente, use texto corrido. Não invente componentes novos.

## Cards da banca

Um `article.persona` por persona que avaliou a ideia, na ordem Helena, Caio, cliente ideal (Bia ou Lucas, o que participou da sessão) e Lúcia. O Téo não entra no parecer porque não avalia.

```html
<article class="persona" style="--p:#1D2B53">
  <div class="avatar" data-persona="helena" data-sinal="verde"><span>H</span></div>
  <div>
    <div class="p-head"><h4>Helena</h4><span class="p-role">Investidora</span><span class="sinal sinal-verde">Seguiria</span></div>
    <blockquote>Fala final dela, na voz dela, em 1 a 3 frases.</blockquote>
    <div class="row"><span class="lbl">Objeção principal</span><p>...</p></div>
    <div class="row"><span class="lbl">Como foi tratada</span><p>Decidida em D-02 / virou o risco R-01 / mudou o escopo.</p></div>
  </div>
</article>
```

- `--p`, iniciais e `data-persona`: veja a tabela de identidade visual em `references/banca.md`.
- `data-sinal`: `verde`, `amarelo` ou `vermelho`. Classe do selo: `sinal-verde` ("Seguiria"), `sinal-amarelo` ("Seguiria com condições") ou `sinal-vermelho` ("Não seguiria agora").
- O cliente ideal muda de perfil a cada ideia; ajuste o `.p-role` (por exemplo, "Cliente ideal · personal trainer").
- O mesmo `data-persona` e `data-sinal` vale para os avatares pequenos do `.placar` no hero.

## Como colocar as fotos

Use o primeiro caminho que o ambiente permitir:

1. **Executa Python e tem os arquivos da skill:** salve o HTML e rode `python3 <pasta da skill>/scripts/embutir_avatares.py <caminho do PRD.html>`. O arquivo fica autocontido, abre até sem internet.
2. **Não executa Python** (a maioria dos apps de chat): escreva a imagem direto no avatar, apontando para as fotos publicadas:

```html
<div class="avatar" data-persona="helena" data-sinal="verde"><img src="https://raw.githubusercontent.com/JefersonMarcioEspindola/skill-prd-consultive/main/plugins/prd-consultive/skills/prd-consultive/assets/banca/helena-verde.webp" alt="Helena"></div>
```

   O nome do arquivo é `<persona>-<sinal>.webp`, com os mesmos valores de `data-persona` e `data-sinal`; o Téo usa sempre `teo-neutro.webp`. As fotos aparecem quando o arquivo é aberto com internet.
3. **Nenhum dos dois:** deixe as iniciais (`<span>H</span>`), que já ficam na cor da persona.

### O que o script faz

`scripts/embutir_avatares.py` procura todo elemento com `data-persona` e `data-sinal`, encontra a imagem em `assets/banca/` (primeiro `<persona>-<sinal>`, depois `<persona>-neutro`, em webp, png ou jpg) e coloca a imagem dentro do avatar como data URI. O HTML continua sendo um arquivo único, que abre em qualquer lugar. Se não achar a imagem, mantém as iniciais. Rodar o script duas vezes não duplica nada.

## Antes de entregar

- [ ] As seções e a numeração batem com o PRD.md.
- [ ] Nenhum comentário ou bloco de exemplo sobrando.
- [ ] O `<title>` está no formato `<Produto> · PRD`.
- [ ] Os sinais do placar e dos cards batem com a seção 13 do PRD.md.
- [ ] As fotos foram colocadas por um dos três caminhos (e, se ficaram como iniciais, você avisou).
