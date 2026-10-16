from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

lista_de_visitantes = []
lista_de_setores = ['Diretoria', 'Refeitório','Administração','Recepção','Júridico','Ensino']

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Visitantes")
        self.layout = QVBoxLayout()
        self.label = QLabel("Nome do cliente")
        self.campo_nome = QLineEdit()
        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_limpar = QPushButton("Limpar")
        self.mensagem = QLabel("")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.campo_nome)
        self.layout.addWidget(self.botao_cadastrar)
        self.layout.addWidget(self.botao_limpar)
        self.layout.addWidget(self.mensagem)
        self.setLayout(self.layout)
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_limpar.clicked.connect(self.limpar)

    def limpar(self):
        self.campo_nome.clear()
        self.mensagem.setText("Campo limpo.")

    def cadastrar(self):
        nome = self.campo_nome.text()
        self.mensagem.setText(f"Cliente cadastrado: {nome}")
