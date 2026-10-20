from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QFormLayout, QListWidget
class JanelaPrincipal(QWidget):
    def __init__(self, layout:QVBoxLayout, label:QLabel, campo_nome:QLineEdit, 
                botao_cadastrar:QPushButton, botao_limpar:QPushButton, mensagem:QLabel,
                contador:QLabel, formulario:QFormLayout, campo_destino:QComboBox,
                lista:QListWidget):
        super().__init__()
        self.setWindowTitle("Cadastro de Visitantes")
        self.resize(520, 400)
        self.registros = []

        self.titulo = QLabel('Recepção - Registro de Visitantes')
        self.campo_nome = QLineEdit()
        self.campo_nome.setPlaceholderText("Nome Completo")

        self.campo_destino = QComboBox()
        self.campo_destino.addItems(["Selecione um setor","Secretaria", "Cordenação", "Laboratório"])

        self.botao_cadastrar = QPushButton("Registrar Visita")
        self.botao_limpar = QPushButton("Limpar Campos")
        self.mensagem = QLabel("Preencha os campos")
        self.lista = QListWidget()
        self.lista.addItem("Nenhum visitante registrado.")
        self.contador = QLabel("Visitantes nessa sessão: 0")
        formulario = QFormLayout()
        formulario.addRow("Nome:", self.campo_nome)
        formulario.addRow("Destino:", self.campo_destino)

        layout = QVBoxLayout()
        layout.addWidget(self.titulo)
        layout.addLayout(formulario)
        layout.addWidget(self.botao_cadastrar)
        layout.addWidget(self.botao_limpar)
        layout.addWidget(self.mensagem)
        layout.addWidget(QLabel("Visitantes registrados:"))
        layout.addWidget(self.lista)
        layout.addWidget(self.contador)
        self.setLayout(layout)

    def limpar(self):
        self.campo_nome.clear()
        self.mensagem.setText("Campo limpo.")

    def cadastrar(self):
        nome = self.campo_nome.text()
        self.mensagem.setText(f"Cliente cadastrado: {nome}")

