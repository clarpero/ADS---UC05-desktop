import sys 
from PySide6.QtWidgets import QApplication
from views.janela_principal import JanelaPrincipal

def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal(layout = None, label = None, campo_nome = None, botao_cadastrar = None, 
                            botao_limpar = None, mensagem = None, contador = None, formulario = None, 
                            campo_destino = None, lista = None, limpar_campos = None)
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
