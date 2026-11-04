# Manual do operador: Portaria Digital

Este manual é para quem trabalha na recepção. Ele explica o uso do programa no dia a
dia, sem detalhes de programação.

## 1. Abrir o programa

Dê dois cliques em **PortariaDigital** (ou no atalho criado pelo suporte). A janela
abre na aba **Portaria**. Use sempre o mesmo atalho: o programa guarda os dados na
pasta de onde é aberto, e abrir por outro caminho mostra uma lista vazia.

A janela tem três abas: **Portaria** (entradas e saídas), **Histórico** (consultas) e
**Setores** (cadastro dos setores).

## 2. Registrar a entrada de um visitante novo

1. Digite o CPF no campo **CPF** (com ou sem pontos e traço) e aperte **Tab**.
2. Digite o nome completo no campo **Nome**.
3. Escolha o setor de destino. Ao lado de cada setor aparece a ocupação, por exemplo
   "Coordenação (2/3)": 2 pessoas lá dentro, de no máximo 3.
4. Clique em **Registrar entrada** (ou **Alt+R**).
5. Entregue ao visitante o crachá mostrado na tabela **No prédio agora**.

## 3. Registrar a entrada de quem já veio antes

Digite o CPF e aperte **Tab**. O nome aparece sozinho e fica bloqueado, com a mensagem
"Visitante já cadastrado. Escolha o setor." Escolha o setor e clique em
**Registrar entrada**.

## 4. Registrar a saída

1. Na tabela **No prédio agora**, clique na linha do visitante. Para achar alguém
   rápido, digite parte do nome ou do setor no campo de filtro acima da tabela.
2. Clique em **Registrar saída da visita selecionada** (ou **Alt+S**).
3. Receba o crachá de volta. Ele fica livre para o próximo visitante.

O rodapé mostra quantas pessoas estão no prédio e quantos crachás estão livres.
Em caso de evacuação, a tabela **No prédio agora** é a lista de quem precisa sair.

## 5. O que fazer em cada mensagem

| Mensagem | O que fazer |
| --- | --- |
| CPF inválido. Confira os 11 dígitos. | Peça o documento de novo e redigite o CPF. |
| Informe o nome do visitante. | Preencha o nome completo. |
| Selecione o setor de destino. | Escolha um setor na lista. |
| (nome) já está no prédio. Registre a saída antes. | A pessoa tem uma entrada aberta. Procure-a na tabela e registre a saída da visita anterior, se ela já tinha saído. |
| (setor) atingiu a lotação de N visitantes. | O setor está cheio. Peça ao visitante que aguarde uma saída ou confirme com o setor. |
| Não há crachá disponível. Aguarde uma devolução. | Todos os crachás estão em uso. Aguarde alguém sair. |
| Selecione uma visita na tabela. | Clique na linha do visitante antes de registrar a saída. |
| Esta visita já foi encerrada. | A saída já tinha sido registrada. Nada a fazer. |
| Entrada não registrada. Corrija os dados e tente de novo. | Leia o aviso que apareceu junto, corrija e tente outra vez. Nada foi gravado pela metade. |

Os avisos também aparecem por alguns segundos na barra inferior da janela.

## 6. Se aparecer "Não foi possível acessar o banco de dados"

A mensagem completa diz que nenhuma alteração parcial foi gravada. Então:

1. Aguarde alguns segundos e tente de novo.
2. Verifique se outro programa está com o arquivo do banco aberto e feche-o.
3. Se o problema continuar, avise o suporte. Não apague nenhum arquivo da pasta do
   programa: o suporte usa o arquivo `portaria.log` para descobrir a causa.

Enquanto isso, anote no papel as entradas e saídas, com horário, para lançar depois.

## 7. Consultar o histórico

1. Abra a aba **Histórico** (**Alt+H**).
2. Escolha as datas em **De** e **Até**.
3. Se quiser, digite parte do nome ou do setor e clique em **Filtrar** (ou aperte
   **Enter**).

A tabela mostra cada visita com entrada, saída e permanência em minutos. Quem ainda
está no prédio aparece como "no prédio". Embaixo, o resumo mostra quantas visitas cada
setor recebeu no período e o tempo médio.

## 8. Cadastrar, alterar e desativar setores

Abra a aba **Setores** (**Alt+T**).

- **Novo setor:** clique em **Novo setor**, informe o nome e a lotação máxima e clique
  em **Salvar**.
- **Alterar:** selecione o setor e clique em **Editar selecionado** (ou dê dois
  cliques na linha). Mude o nome ou a lotação e clique em **Salvar**.
- **Desativar** (setor fechado ou em reforma): em **Editar selecionado**, desmarque
  "Setor ativo" e salve. Ele some da lista de entrada, mas o histórico continua.
- **Excluir:** só é possível para setor que nunca recebeu visita. Setor com histórico
  deve ser desativado.

Mensagens desta aba:

| Mensagem | O que fazer |
| --- | --- |
| Já existe o setor (nome). | Use outro nome ou edite o setor existente. |
| Há N visitante(s) no setor agora. A lotação não pode ficar abaixo disso. | Aguarde as saídas ou escolha uma lotação maior. |
| Não é possível desativar um setor com visitantes no prédio. | Registre a saída de todos do setor antes. |
| Este setor tem histórico de visitas e não pode ser excluído. Desative-o. | Use Editar e desmarque "Setor ativo". |

## 9. Aparência

No menu **Exibir**, a opção **Tema escuro** (**Ctrl+T**) liga ou desliga o modo
escuro. O programa lembra a escolha na próxima vez que for aberto.

## 10. Cuidados com dados pessoais

- A tela mostra só o meio do CPF (***.982.247-**). Não anote CPFs completos em papel
  nem em outros arquivos.
- Não vire o monitor para o visitante nem deixe a janela aberta sem ninguém no balcão.
- Não copie o arquivo `portaria.db` para pen drive, e-mail ou nuvem: ele contém nomes e
  CPFs de todos os visitantes.
- Se um visitante pedir para ter os dados apagados, encaminhe o pedido ao responsável
  pela proteção de dados da instituição.
