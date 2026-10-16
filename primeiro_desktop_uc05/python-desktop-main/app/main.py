"""Interface PySide6: widgets -> eventos -> função Python -> banco SQLite."""
import sqlite3
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox,
    QPushButton, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QHeaderView,
)
from app import database as db


class JanelaEstoque(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UC05 • Primeiro aplicativo desktop")
        self.resize(760, 540)
        self.produto_id: int | None = None

        centro = QWidget()
        self.setCentralWidget(centro)
        layout = QVBoxLayout(centro)
        layout.setSpacing(12)

        titulo = QLabel("Controle de produtos")
        titulo.setStyleSheet("font-size: 24px; font-weight: 700;")
        layout.addWidget(titulo)
        layout.addWidget(QLabel("Experimente cadastrar, selecionar, atualizar e excluir. Feche e abra o programa para verificar a persistência."))

        formulario = QHBoxLayout()
        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome do produto")
        self.nome.setAccessibleName("Nome do produto")
        self.quantidade = QSpinBox()
        self.quantidade.setRange(0, 1_000_000)
        self.quantidade.setPrefix("Qtd: ")
        self.quantidade.setAccessibleName("Quantidade")
        formulario.addWidget(self.nome, 3)
        formulario.addWidget(self.quantidade, 1)
        layout.addLayout(formulario)

        botoes = QHBoxLayout()
        self.salvar_btn = QPushButton("Cadastrar")
        self.salvar_btn.clicked.connect(self.salvar)
        limpar_btn = QPushButton("Limpar seleção")
        limpar_btn.clicked.connect(self.limpar)
        excluir_btn = QPushButton("Excluir selecionado")
        excluir_btn.clicked.connect(self.excluir)
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(limpar_btn)
        botoes.addWidget(excluir_btn)
        layout.addLayout(botoes)

        self.tabela = QTableWidget(0, 3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade"])
        self.tabela.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.tabela.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabela.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabela.itemSelectionChanged.connect(self.selecionar)
        layout.addWidget(self.tabela)

        self.status = QLabel("Pronto.")
        layout.addWidget(self.status)
        self.recarregar()

    def recarregar(self):
        registros = db.listar()
        self.tabela.blockSignals(True)
        self.tabela.setRowCount(len(registros))
        for linha, registro in enumerate(registros):
            for coluna, valor in enumerate((registro["id"], registro["nome"], registro["quantidade"])):
                item = QTableWidgetItem(str(valor))
                if coluna != 1:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tabela.setItem(linha, coluna, item)
        self.tabela.blockSignals(False)
        self.status.setText(f"{len(registros)} produto(s) registrado(s).")

    def selecionar(self):
        linha = self.tabela.currentRow()
        if linha < 0 or self.tabela.item(linha, 0) is None:
            return
        self.produto_id = int(self.tabela.item(linha, 0).text())
        self.nome.setText(self.tabela.item(linha, 1).text())
        self.quantidade.setValue(int(self.tabela.item(linha, 2).text()))
        self.salvar_btn.setText("Atualizar")

    def limpar(self):
        self.produto_id = None
        self.tabela.clearSelection()
        self.nome.clear()
        self.quantidade.setValue(0)
        self.salvar_btn.setText("Cadastrar")
        self.nome.setFocus()

    def salvar(self):
        try:
            if self.produto_id is None:
                db.inserir(self.nome.text(), self.quantidade.value())
                mensagem = "Produto cadastrado."
            else:
                db.atualizar(self.produto_id, self.nome.text(), self.quantidade.value())
                mensagem = "Produto atualizado."
            self.limpar()
            self.recarregar()
            self.status.setText(mensagem)
        except (ValueError, sqlite3.Error) as erro:
            QMessageBox.warning(self, "Não foi possível salvar", str(erro))

    def excluir(self):
        if self.produto_id is None:
            QMessageBox.information(self, "Selecione um produto", "Escolha uma linha antes de excluir.")
            return
        resposta = QMessageBox.question(self, "Confirmar exclusão", "Excluir o produto selecionado?")
        if resposta != QMessageBox.StandardButton.Yes:
            return
        try:
            db.excluir(self.produto_id)
            self.limpar()
            self.recarregar()
        except sqlite3.Error as erro:
            QMessageBox.warning(self, "Erro ao excluir", str(erro))


def main() -> int:
    db.inicializar()
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    janela = JanelaEstoque()
    janela.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
