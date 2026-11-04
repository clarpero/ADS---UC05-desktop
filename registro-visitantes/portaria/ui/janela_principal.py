import sqlite3
from datetime import datetime

from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from portaria import repositorio as repo
from portaria.validacao import cpf_valido, mascarar_documento, normalizar_documento

COLUNAS = ["Visita", "Nome", "CPF", "Setor", "Crachá", "Entrada"]


def agora():
    return datetime.now().isoformat(sep=" ", timespec="seconds")


class JanelaPrincipal(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.setWindowTitle("Portaria Digital")
        self.resize(820, 520)

        # ---------- formulário de entrada ----------
        self.campo_cpf = QLineEdit()
        self.campo_cpf.setPlaceholderText("Somente números")
        self.campo_cpf.setMaxLength(14)
        self.campo_nome = QLineEdit()
        self.combo_setor = QComboBox()
        self.botao_entrada = QPushButton("&Registrar entrada")  # Alt+R
        self.botao_limpar = QPushButton("&Limpar campos")       # Alt+L
        self.mensagem = QLabel("Informe o CPF do visitante.")

        formulario = QFormLayout()
        formulario.addRow("&CPF:", self.campo_cpf)      # Alt+C
        formulario.addRow("&Nome:", self.campo_nome)    # Alt+N
        formulario.addRow("S&etor:", self.combo_setor)  # Alt+E

        botoes = QHBoxLayout()
        botoes.addWidget(self.botao_entrada)
        botoes.addWidget(self.botao_limpar)

        # ---------- quem está no prédio ----------
        self.campo_filtro = QLineEdit()
        self.campo_filtro.setPlaceholderText("Filtrar por nome ou setor")
        self.tabela = QTableWidget(0, len(COLUNAS))
        self.tabela.setHorizontalHeaderLabels(COLUNAS)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.verticalHeader().setVisible(False)
        self.botao_saida = QPushButton("Registrar &saída da visita selecionada")  # Alt+S
        self.contador = QLabel()

        layout = QVBoxLayout()
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.mensagem)
        layout.addWidget(QLabel("No prédio agora:"))
        layout.addWidget(self.campo_filtro)
        layout.addWidget(self.tabela)
        layout.addWidget(self.botao_saida)
        layout.addWidget(self.contador)
        self.setLayout(layout)

        # ---------- eventos ----------
        self.campo_cpf.editingFinished.connect(self.buscar_visitante)
        self.botao_entrada.clicked.connect(self.registrar_entrada)
        self.botao_limpar.clicked.connect(self.limpar_campos)
        self.botao_saida.clicked.connect(self.registrar_saida)
        self.campo_filtro.textChanged.connect(self.atualizar_tabela)

        self.carregar_setores()
        self.atualizar_tabela()

    def carregar_setores(self):
        self.combo_setor.clear()
        self.combo_setor.addItem("Selecione um setor", None)
        for linha in repo.listar_setores_ativos(self.conn):
            self.combo_setor.addItem(linha["nome"], linha["id"])

    def buscar_visitante(self):
        cpf = normalizar_documento(self.campo_cpf.text())
        visitante = repo.buscar_visitante_por_documento(self.conn, cpf)
        if visitante:
            self.campo_nome.setText(visitante["nome"])
            self.campo_nome.setReadOnly(True)
            self.mensagem.setText("Visitante já cadastrado. Escolha o setor.")
        else:
            self.campo_nome.setReadOnly(False)

    def registrar_entrada(self):
        cpf = normalizar_documento(self.campo_cpf.text())
        nome = " ".join(self.campo_nome.text().split())
        setor_id = self.combo_setor.currentData()

        if not cpf_valido(cpf):
            self.mensagem.setText("CPF inválido. Confira os 11 dígitos.")
            self.campo_cpf.setFocus()
            return
        if not nome:
            self.mensagem.setText("Informe o nome do visitante.")
            self.campo_nome.setFocus()
            return
        if setor_id is None:
            self.mensagem.setText("Selecione o setor de destino.")
            return

        try:
            with self.conn:  # commit se tudo der certo, rollback se houver exceção
                visitante = repo.buscar_visitante_por_documento(self.conn, cpf)
                if visitante is None:
                    visitante_id = repo.inserir_visitante(self.conn, nome, cpf)
                else:
                    visitante_id = visitante["id"]

                if repo.visita_aberta_do_visitante(self.conn, visitante_id):
                    self.mensagem.setText(f"{nome} já está no prédio. Registre a saída antes.")
                    return

                cracha = repo.buscar_cracha_disponivel(self.conn)
                if cracha is None:
                    self.mensagem.setText("Não há crachá disponível. Aguarde uma devolução.")
                    return

                repo.inserir_visita(
                    self.conn, visitante_id, setor_id, cracha["id"], None, agora()
                )
                repo.atualizar_situacao_cracha(self.conn, cracha["id"], "em_uso")
        except sqlite3.Error as erro:
            QMessageBox.critical(self, "Portaria Digital", f"Erro no banco: {erro}")
            return

        self.limpar_campos()
        self.mensagem.setText(f"Entrada registrada. Entregue o crachá {cracha['codigo']}.")
        self.atualizar_tabela()

    def registrar_saida(self):
        linha = self.tabela.currentRow()
        if linha < 0:
            self.mensagem.setText("Selecione uma visita na tabela.")
            return
        visita_id = int(self.tabela.item(linha, 0).text())

        try:
            with self.conn:
                visita = repo.obter_visita(self.conn, visita_id)
                if visita is None or visita["saida"] is not None:
                    self.mensagem.setText("Esta visita já foi encerrada.")
                    return
                repo.encerrar_visita(self.conn, visita_id, agora())
                repo.atualizar_situacao_cracha(self.conn, visita["cracha_id"], "disponivel")
        except sqlite3.Error as erro:
            QMessageBox.critical(self, "Portaria Digital", f"Erro no banco: {erro}")
            return

        self.mensagem.setText("Saída registrada. Crachá devolvido.")
        self.atualizar_tabela()

    def atualizar_tabela(self):
        # O SQL ficou no repositório; o filtro por nome ou setor é feito aqui.
        presentes = repo.listar_presentes(self.conn)
        termo = self.campo_filtro.text().strip().lower()
        linhas = [l for l in presentes if termo in f"{l['nome']} {l['setor']}".lower()]

        self.tabela.setRowCount(len(linhas))
        for i, l in enumerate(linhas):
            valores = [l["id"], l["nome"], mascarar_documento(l["documento"]),
                       l["setor"], l["cracha"], l["entrada"]]
            for j, valor in enumerate(valores):
                self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))
        self.tabela.setCurrentCell(-1, -1)

        crachas = repo.contar_crachas_por_situacao(self.conn)
        self.contador.setText(
            f"No prédio: {len(presentes)} | Crachás livres: {crachas.get('disponivel', 0)}"
        )

    def limpar_campos(self):
        self.campo_cpf.clear()
        self.campo_nome.clear()
        self.campo_nome.setReadOnly(False)
        self.combo_setor.setCurrentIndex(0)
        self.campo_cpf.setFocus()
