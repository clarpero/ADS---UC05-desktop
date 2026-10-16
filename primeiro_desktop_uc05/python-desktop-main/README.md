# UC 05 — Meu primeiro aplicativo desktop

**Projeto didático:** aplicação de cadastro de produtos com Python, PySide6 (Qt Widgets) e SQLite. O SQL é escrito explicitamente: **não utilizamos ORM nesta etapa**. O ORM será estudado depois, comparando as abordagens.

## 1. Pré-requisitos

- Python **3.11 ou superior**, em uma versão suportada pelo PySide6 instalado;
- Windows 10/11 ou Linux com ambiente gráfico;
- Terminal (PowerShell, bash ou outro);
- Conexão à internet **apenas para instalar dependências**;
- Editor ou IDE à escolha (VS Code, PyCharm etc.).

> Não há necessidade de instalar servidor MySQL ou PostgreSQL: o SQLite integra a biblioteca padrão Python.

## 2. Instalação no Windows (PowerShell)

1. Instale Python em <https://www.python.org/downloads/>. Confira se `py -3 --version` responde.
2. Extraia o ZIP e abra o terminal **dentro da pasta `primeiro_desktop_uc05`**.
3. Execute:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run.py
```

Se a política do PowerShell impedir a ativação, **não é necessário modificar permanentemente a política do sistema**: execute diretamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

## 3. Instalação no Linux (Ubuntu/Debian)

No terminal dentro da pasta do projeto:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run.py
```

Se a interface Qt reclamar de bibliotecas do sistema, verifique os pacotes gráficos e bibliotecas XCB exigidos pela versão do Qt no ambiente; verifique a mensagem específica antes de instalar pacotes extras.

## 4. Instalação no Arch Linux

```bash
sudo pacman -Syu python python-pip
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run.py
```

> **Importante:** não instale PySide6 globalmente via `sudo pip`. Use sempre o ambiente virtual `.venv`. A disponibilidade de bibliotecas de interface Qt depende do ambiente gráfico configurado.

## 5. O que testar (roteiro de validação)

1. Abrir o aplicativo e localizar a janela **Controle de produtos**.
2. Cadastrar `Teclado`, quantidade `3`.
3. Cadastrar `Mouse`, quantidade `5`.
4. Selecionar `Teclado`, alterar quantidade para `4` e atualizar.
5. Fechar e reabrir: os registros devem permanecer no banco.
6. Selecionar `Mouse`, excluir e confirmar.
7. Tentar cadastrar nome vazio: deve surgir uma mensagem de validação.
8. Verificar que os nomes aparecem ordenados na tabela.

**Onde ficam os dados?** Por padrão, em `~/.uc05_primeiro_desktop/estoque.db` na pasta do usuário. Não compartilhe dados pessoais neste projeto didático.

## 6. Executar testes sem instalar outras dependências

```bash
python -m unittest discover -s tests -v
```

No PowerShell sem ativação, use `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`.

## 7. Compreendendo as peças do projeto

| Arquivo | Responsabilidade |
|---|---|
| `run.py` | Ponto de entrada |
| `app/main.py` | Interface PySide6, componentes e eventos |
| `app/database.py` | SQLite, SQL explícito e validações simples |
| `tests/test_database.py` | Testes do banco sem precisar abrir uma janela |
| `docs/ROTEIRO_DA_AULA.md` | Condução e atividades para estudantes |

**O fluxo:** clique no botão → sinal `clicked` → método `salvar` → função `db.inserir` → `INSERT` SQL parametrizado → atualização da tabela.

## 8. Primeiro contato com Git (opcional na primeira aula)

```bash
git init
git add .
git commit -m "feat: primeiro aplicativo desktop"
```

Configure previamente `git config user.name` e `git config user.email` se o Git solicitar. `.gitignore` já evita versionar o ambiente `.venv` e bancos de dados locais.

## 9. Solução de problemas

- `No module named PySide6`: confirme que instalou as dependências **no mesmo Python** usado para executar `run.py`.
- `python` não encontrado: use `py -3` no Windows ou `python3` no Linux para criar o ambiente virtual.
- Janela não aparece: execute em sessão gráfica local, não em terminal remoto sem display.
- Erro de plugin `xcb` no Linux: confira bibliotecas gráficas da distribuição e configuração da sessão X11/Wayland; não copie correções genéricas indiscriminadamente.
- Dados antigos: localize `~/.uc05_primeiro_desktop/estoque.db`. Faça backup e só apague se desejar reiniciar os exercícios.
- Dependência indisponível: confira versão do Python e acesso ao repositório PyPI.

## 10. Próximas etapas

- Adicionar campo de **preço** com tratamento adequado de valores monetários.
- Implementar busca por nome com SQL parametrizado.
- Acrescentar tabela de movimentações e discutir transações.
- Comparar acesso SQL explícito com SQLAlchemy ORM, **sem migrar tudo de uma só vez**.

## Documentação oficial

- Python e ambientes virtuais: <https://docs.python.org/3/library/venv.html>
- Qt for Python: <https://doc.qt.io/qtforpython-6/>
- SQLite em Python: <https://docs.python.org/3/library/sqlite3.html>
- Git: <https://git-scm.com/doc>
