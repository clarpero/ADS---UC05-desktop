from PySide6.QtWidgets import QApplication
from views.janela_principal import JanelaPrincipal

app = QApplication([])
window = JanelaPrincipal(layout=None, label=None, campo_nome=None, botao_cadastrar=None, botao_limpar=None, mensagem=None)
window.show()
app.exec()
