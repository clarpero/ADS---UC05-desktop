# Portaria Digital

Aplicação desktop educacional de controle de visitantes, construída com Python e PySide6
para praticar programação orientada a eventos, SQL, transações, regras de negócio,
testes e empacotamento.

Projeto da UC05 (Técnico em Desenvolvimento de Sistemas, Senac PI).

## Contexto

O pedido original da recepção era registrar quem chegou e para qual setor vai, ver quem
está no prédio durante o expediente e evitar formulários incompletos. O protótipo
começou só em memória e evoluiu para esta versão com banco SQLite, histórico, lotação
por setor e testes.

## Recursos
- entrada e saída com crachá automático;
- lista de presentes com filtro e lotação por setor;
- histórico com permanência e resumo por setor;
- gestão de setores com exclusão protegida;
- tema claro e escuro, lembrado entre execuções (Ctrl+T);
- dados fictícios e testes automatizados.

## Requisitos
- Python 3.10 ou superior

## Executar
```bash
python -m venv .venv
```
Ative o ambiente virtual (Windows: `.venv\Scripts\activate`; Linux/macOS:
`source .venv/bin/activate`) e:
```bash
python -m pip install -r requirements.txt
python main.py
```
O banco `portaria.db` e o registro técnico `portaria.log` são criados na pasta de onde o
programa é aberto. Apagar o `portaria.db` faz a aplicação criar um banco novo, com os
setores e os crachás iniciais.

## Dados de demonstração
```bash
python dados_ficticios.py --semente 7
```

## Testes
```bash
python -m pytest -q
```
Resultado esperado: `37 passed`.

## Arquitetura
interface (portaria/ui) → serviços (regras e transações) → repositório (SQL) → SQLite

```txt
main.py                    abre o banco, aplica o tema e mostra a janela
portaria/
├── schema.sql             tabelas, chaves estrangeiras e índices parciais
├── db.py                  conexão (row_factory, foreign_keys) e dados iniciais
├── validacao.py           funções puras: CPF, normalização e máscara
├── erros.py               RegraNegocioError (erro previsto, vai para a tela)
├── repositorio.py         SQL parametrizado, sem commit
├── servicos.py            regras RN01 a RN07 e transações
├── orm.py                 mapeamento SQLAlchemy, só para estudo
└── ui/
    ├── janela_principal.py   abas Portaria, Histórico e Setores
    ├── dialogo_setor.py      diálogo de cadastro e edição de setor
    ├── tema.py, estilo.qss   tokens de tema e folha de estilo
    └── icones/               setas SVG dos temas claro e escuro
tests/                     suíte pytest (banco em memória)
```

## Arquivos de estudo
`explorar.py`, `comparar_orm.py`, `estudo_sessao.py`, `integridade.py`,
`trava_banco.py` e `laboratorio_estilo.py` são experimentos das etapas do roteiro
(SQL à mão, ORM e N+1, chave estrangeira, banco travado e estilo). Ficam na raiz para
serem executados com `python nome.py` a partir da pasta do projeto, sem mudar o caminho
de importação do pacote `portaria`, e não são usados pela aplicação.
`integridade.py` e `estudo_sessao.py` alteram dados: rode-os num banco de teste.

## Limitações conhecidas
- um computador por vez acessando o banco;
- o banco é criado na pasta de onde o programa é aberto (um atalho com outra pasta de
  trabalho cria outro banco);
- CPFs dos dados fictícios podem coincidir com CPFs reais por acaso.

## Licenças
Código sob a licença MIT do arquivo [LICENSE](LICENSE).

PySide6 (Qt for Python) é distribuído sob LGPLv3. Para quem distribuir o programa
empacotado, isso significa, em resumo:
- informar que o produto usa software sob LGPL e entregar uma cópia da licença;
- disponibilizar o código-fonte do Qt/PySide6 usado (ou uma oferta escrita de fornecê-lo);
- permitir que o usuário troque as bibliotecas do Qt por outra versão (o modo de pasta
  do PyInstaller mantém as bibliotecas como arquivos separados);
- não usar módulos do Qt disponíveis só sob GPL e não acrescentar restrições.

Fonte: [Obrigações da GPL e da LGPL, The Qt Company](https://www.qt.io/licensing/open-source-lgpl-obligations).
Este resumo é didático e não substitui a leitura da licença.
