------ CLIENTE ------
“Na recepção, precisamos registrar quem chegou e para qual setor irá. Quero ver os visitantes cadastrados durante o expediente e 
evitar formulários incompletos. Não precisamos de banco de dados nesta primeira demonstração.”

------ Requisitos iniciais ------
RF01: abrir janela gráfica com título.
RF02: informar nome e selecionar setor.
RF03: registrar e listar visitantes válidos.
RF04: rejeitar nome vazio ou setor não escolhido.
RF05: limpar formulário sem apagar a lista.
RF06: exibir contagem de visitantes da sessão.


------ Restrições do protótipo ------
Aplicação local usando Python e PySide6.
Sem login, banco de dados ou rede.
Dados fictícios e temporários.
O protótipo deve ser executável em outra máquina com instalação documentada.


# Registro de visitantes - Desktop
Aplicação didática de registro de visitantes com Python e PySide6
Armazena registros somente em memoria durante a execução

# Requisitos
- Python 3
- PySide6

# Executar
1. criar ambiente: 'python -m venv .venv'
2. Ativar o ambiente virtual
3. Instalar: 'python -m pip install -r requirements,txt'
4.Executar: 'python main.py'

# Funcionalidades
- Registrar nome e setor
- Validar campos obrigatórios
- Listar visitas da sessão
- Limpar formulário e exigir contador

# Limitação
Sem banco de dados; os registros são perdidos ao encerrar.