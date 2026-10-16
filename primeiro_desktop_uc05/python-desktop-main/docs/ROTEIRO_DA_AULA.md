# Roteiro orientado — Primeiro aplicativo desktop

## Perguntas antes de abrir o código

1. Ao clicar em **Cadastrar**, o que precisa acontecer, em qual sequência?
2. Qual código define a interface? Qual acessa os dados?
3. O que acontece com os produtos se fechar o programa? Como comprovar?
4. Um aplicativo desktop exige internet? Em quais situações?
5. Qual é o papel de Python, PySide6, SQLite e da IDE? São todos frameworks?

## Etapa A — Investigação do projeto (10 min)

Abra `run.py`, `app/main.py` e `app/database.py` e, em dupla, localize: título da janela, widget de entrada, botão, conexão de evento, comando `INSERT` e nome do arquivo de banco. **Não execute ainda:** registre hipóteses sobre o comportamento.

## Etapa B — Instalação e primeira execução (20–30 min)

Siga o README conforme seu sistema. Registre Python usado, biblioteca instalada e problema ocorrido (se houver). Execute o aplicativo.

## Etapa C — Experimentos (15–20 min)

Cadastre dois produtos, altere um, feche/abra, exclua outro e tente cadastrar um nome vazio. Preencha uma tabela de `ação → comportamento esperado → resultado observado`.

## Etapa D — Minha primeira modificação (15 min)

Mude o título da janela e o texto de um botão. Execute novamente. Identifique quais mudanças alteram apenas a interface e quais exigiriam mudança na lógica ou banco.

## Etapa E — Desafio de raciocínio (15–20 min)

Sem copiar código de colegas, explique a diferença entre:

```python
con.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
```

e uma montagem direta da string SQL. Por que o parâmetro `?` é importante? Localize outro exemplo no projeto.

## Etapa F — Síntese e evidência (10 min)

Entregue: print da janela funcional; evidência de persistência após reiniciar; trecho de código alterado; resposta individual explicando `clique → evento → SQL → atualização da tela`.

## Próxima aula / extensão

Adicionar uma busca por nome, começando pelo SQL explícito. Antes da implementação, decidir quem é responsável pelo filtro: o widget, uma regra Python ou o SGBD? Justificar.

## Para o docente

Este kit é demonstração guiada e experimentação; não substitui a pesquisa comparativa de frameworks da Aula 01 nem antecipa a avaliação formal de ORM. Programe apenas um trecho na aula se a investigação e configuração do laboratório consumirem mais tempo que o previsto. Respostas dos estudantes devem ser registradas antes da explicação demonstrativa.
