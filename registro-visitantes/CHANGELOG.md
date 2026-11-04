# Changelog

## [1.0.0] - 2026-11-04

### Adicionado
- Janela PySide6 com formulário de entrada (CPF, nome e setor) e atalhos de teclado.
- Validação de CPF pelos dígitos verificadores e exibição do CPF mascarado.
- Persistência em SQLite com esquema próprio: setor, visitante, crachá e visita.
- Entrada e saída atômicas: a visita e a situação do crachá mudam na mesma transação.
- Índices parciais que impedem duas visitas abertas para o mesmo visitante ou crachá.
- Repositório com SQL parametrizado e camada de serviços com as regras RN01 a RN07.
- Lotação máxima por setor, com a ocupação exibida no combo.
- Aba de histórico com período, busca, permanência em minutos e resumo por setor.
- Aba de setores com criação, edição, desativação e exclusão protegida.
- Tratamento central de falhas: mensagens claras na tela e traceback em `portaria.log`,
  sem dados pessoais.
- Tema claro e escuro com tokens, variantes de botão, ícones SVG e componentes do Qt
  em português; o tema escolhido é lembrado.
- Gerador de dados fictícios com semente.
- Suíte pytest com 37 testes.
- Módulo ORM (SQLAlchemy) e scripts de estudo para comparação com SQL explícito.

### Corrigido
- Comandos SQL de criação das tabelas com erros de digitação, que deixavam a chave
  estrangeira desligada sem aviso.
- Validação de CPF, visitante já presente e seleção da tabela antes de registrar saída.
- Arquivo `requirements.tx` criado por engano em UTF-16, substituído pelo
  `requirements.txt`.
- Nomes de setor duplicados com acento ou maiúsculas diferentes passam a ser recusados.

### Limitações conhecidas
- Um computador por vez acessando o banco.
- O banco é criado na pasta de onde o programa é aberto.
- CPFs dos dados fictícios podem coincidir com CPFs reais por acaso.
- O executável gerado só roda no sistema operacional em que foi empacotado.
