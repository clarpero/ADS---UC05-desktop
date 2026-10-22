from PySide6.QtWidgets import(QHBoxLayout, QWidget, QVBoxLayout, 
                              QLabel, QLineEdit, QPushButton, 
                              QComboBox, QFormLayout, QListWidget)

setores = ['Secretaria', 'Coordenação', 'Laboratório']

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Portaria Digital")
        self.resize(820, 520)
        
        # --- widgets ---
        self.titulo = QLabel('Recepção - Registro de Visitantes')
        self.campo_cpf = QLineEdit()
        self.campo_cpf.setPlaceholderText('Somente Números')
        self.campo_cpf.setMaxLength(14)
        self.campo_nome = QLineEdit()
        self.campo_setor = QComboBox()
        self.campo_setor.addItem('Selecione um setor')
        self.campo_setor.addItems(setores)
        self.botao_entrada = QPushButton('Registrar entrada')
        self.botao_limpar = QPushButton('Limpar campos')
        self.mensagem = QLabel('Informe o CPF do visitante')

        # ---- Layouts ----
        formulario = QFormLayout()
        formulario.addRow('CPF:', self.campo_cpf)
        formulario.addRow('Nome:', self.campo_nome)
        formulario.addRow('Setor:', self.campo_setor)

        botoes = QHBoxLayout()
        botoes.addWidget(self.botao_entrada)
        botoes.addWidget(self.botao_limpar)

        layout = QVBoxLayout()
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.mensagem)
        layout.addStretch()
        self.setLayout(layout)
   
        self.botao_entrada.setStyleSheet(
             "background-color: #0b5ed7; color: white; border-radius: 8px; padding: 8x 16px;")
        self.botao_limpar.setStyleSheet(
                     "background-color: #0b5ed7; color: white; border-radius: 8px; padding: 8x 16px;")
        self.botao_entrada.clicked.connect(self.registrar_entrada)        
        self.botao_limpar.clicked.connect(self.limpar_campos)


    def registrar_entrada(self):
        cpf = " ".join(c for c in self.campo_cpf.text() if c.isdigit())
        nome = " ".join(self.campo_nome.text().split())

        if len(cpf) != 11:
            self.mensagem.setText('O CPF precisa ter 11 digitos.')
            self.campo_cpf.setFocus()
            return
        if not nome:
            self.mensagem.setText('Informe o nome do visitante.')
            self.campo_nome.setFocus()
            return
        if self.campo_setor.currentIndex() == 0: 
            self.mensagem.setText('Selecone o setor de destino.')
            return 

        setor = self.campo_setor.currentText()
        self.mensagem.setText(f'Dados válidos: {nome} para {setor}. Ainda não gravamos nada')

    def limpar_campos(self):
        self.campo_cpf.clear()
        self.campo_nome.clear()
        self.setor.setCurrentIndex(0)
        self.campo_cpf.setFocus()