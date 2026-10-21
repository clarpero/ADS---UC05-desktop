from PySide6.QtWidgets import(QWidget, QVBoxLayout, 
                              QLabel, QLineEdit, QPushButton, 
                              QComboBox, QFormLayout, QListWidget)


class JanelaPrincipal(QWidget):
    def __init__(self, layout, label, campo_nome, botao_cadastrar, botao_limpar, mensagem, contador, formulario, campo_destino, lista, limpar_campos):
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

        #Os eventos de clique dos botões serão conectados aos métodos correspondentes
        self.botao_cadastrar.clicked.connect(self.cadastrar_visita)
        self.botao_limpar.clicked.connect(self.limpar_campos)

        
    def cadastrar_visita(self):
        nome = self.campo_nome.text().strip()
        destino = self.campo_destino.currentText()

        if not nome:
            self.mensagem.setText('Informe o nome do visitante.')
            self.campo_nome.setFocus()
            return

        if self.campo_destino.currentIndex() == 0:
            self.mensagem.setText('Selecione o setor de destino.')
            self.campo_destino.setFocus()
            return

        registro = {"nome": nome, "destino": destino}
        self.registros.append(registro)
        self.lista.addItem(f"{nome} - {destino}")
        self.contador.setText(f'Visitas nesta sessão: {len(self.registros)}')
        self.mensagem.setText('Visita registrada com sucesso!')
        self.limpar_campos()

        
    def limpar_campos(self):
            self.campo_nome.clear()
            self.campo_destino.setCurrentIndex(0)
            self.mensagem.setText('Campos limpos. Preencha novamente.')
            self.campo_nome.setFocus()

        