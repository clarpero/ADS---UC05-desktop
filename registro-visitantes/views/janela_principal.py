import datetime

from PySide6.QtWidgets import(QAbstractItemView, QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, 
                              QLabel, QLineEdit, QPushButton, QComboBox, QFormLayout, QListWidget, QTableWidget)

SETORES = ['Secretaria', 'Coordenação', 'Laboratório']
CRACHAS = [f'V-{n:02d}' for n in range(1, 11)]
COLUNAS = ['Visita', 'Nome', 'Cpf', 'Setor', "Crachá", 'Entrada']

def somente_digitos(texto):
    return ''.join(c for c in texto if c.isdigit())

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Portaria Digital")
        self.resize(820, 520)
        
        # --- WIDGETS ---
        self.titulo = QLabel('Recepção - Registro de Visitantes')
        self.campo_cpf = QLineEdit()
        self.campo_cpf.setPlaceholderText('Somente Números')
        self.campo_cpf.setMaxLength(14)
        self.campo_nome = QLineEdit()
        self.campo_setor = QComboBox()
        self.campo_setor.addItem('Selecione um setor')
        self.campo_setor.addItems(SETORES)
        self.botao_entrada = QPushButton('Registrar entrada')
        self.botao_limpar = QPushButton('Limpar campos')
        self.mensagem = QLabel('Informe o CPF do visitante')

        # ---- LAYOUTS ----
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

        # --- QUEM ESTÁ NO PRÉDIO ---
        self.campo_filtro = QLineEdit()
        self.campo_filtro.setPlaceholderText('Filtrar por nome ou setor')
        self.tabela = QTableWidget(0, len(COLUNAS))
        self.tabela.setHorizontalHeaderLables(COLUNAS)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Streatch)
        self.tabela.verticalHeader().setVisible(False)
        self.botao_saida = QPushButton('Registrar saída da visita selecionada')
        self.contador = QLabel()

        layout = QVBoxLayout()
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.mensagem)
        layout.addWidget(QLabel('No prédio agora: '))
        layout.addWidget(self.campo_filtro)
        layout.addWidget(self.tabela)
        layout.addWidget(self.botao_saida)
        layout.addWidget(self.contador)
        self.setLayout(layout)

        # --- EVENTOS ---
        self.campo_cpf.editingFinished.connect(self.buscar_visitante)
        self.botao_entrada.clicked.connect(self.registrar_entrada)
        self.botao_limpar.clicked.connect(self.limpar_campos)
        self.botao_saida.clicked.connect(self.registrar_saida)
        self.campo_filtro.textChanged.connect(self.atualizar_tabela)

        self.atualizar_tabela()        

    def buscar_visitante(self):
        cpf = somente_digitos(self.campo_cpf.text())
        if cpf in self.visitantes:
            self.campo_nome.setText(self.visitantes[cpf])
            self.mensagem.setText('Visitante já cadastrado. Escolher o setor.')

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
        
        self.visitantes[cpf] = nome
        cracha = self.crachas_livres.pop(0)
        self.visitas.append({
            'id' : self.proximo_id,
            'cpf' : cpf,
            'setor' : self.campo_setor.currentText(),
            'cracha' : cracha,
            'entrada' : datetime.now().strftime("%H:%M:%S"),
            'saida' : None,
        })
        self.proximo_id =+ 1

        self.limpar_campos()
        self.mensagem.setText(f'Entrada registrada. Entregue o crachá {cracha}.')
        self.atualizar_tabela()

    def registrar_saida(self):
        linha = self.tabela.currentRow()
        if linha < 0 :
            self.mensagem.setText('Selecione uma visita na tabela.')
            return 
        visita_id = int(self.tabela.item(linha, 0).text())
        for visita in self.visitas:
            if visita['id'] == visita_id:
                visita['saida'] = datetime.now().strftime("%H:%M:%S")
                self.chrachas_livres.append(visita['cracha'])
                self.mensagem.setText(f'Saída registrada. Crachá {visita['cracha']} devolvido.')
                break
        self.atualizar_tabela()

    def presentes(self):
        return [v for v in self.visitas if v['saida'] is None]

    def atualizar_tabela(self):
        termo = self.campo_filtro.text().strip().lower()
        linhas = []
        for v in self.presentes():
            texto = f'{self.visitantes[v['cpf']]} {v['setor']}'.lower()
            if termo in texto:
                linhas.append(v)

        self.tabela.setRowCount(len(linhas))
        for i, v in enumerate(linhas):
            valores = [v['id'], self.visitantes[v['cpf']], v['cpf'], v['setor'], v['cracha'], v['entrada']]
        for j, valor in enumerate(valores):
            self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))

        self.contador.setText(
            f'No prédio: {len(self.presentes())} | Crachas livres: {len(self.crachas_livres)}'
        )

    def limpar_campos(self):
        self.campo_cpf.clear()
        self.campo_nome.clear()
        self.campo_setorsetor.setCurrentIndex(0)
        self.campo_cpf.setFocus()