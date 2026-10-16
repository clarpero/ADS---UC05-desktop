import sqlite3
import tempfile
import unittest
from pathlib import Path
from app import database as db


class BancoDeDadosTestes(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.caminho = Path(self.temp.name) / "teste.db"
        db.inicializar(self.caminho)

    def tearDown(self):
        self.temp.cleanup()

    def test_crud_e_persistencia(self):
        identificador = db.inserir("Teclado", 2, self.caminho)
        self.assertEqual(db.listar(self.caminho)[0]["nome"], "Teclado")
        self.assertTrue(db.atualizar(identificador, "Teclado USB", 3, self.caminho))
        self.assertEqual(db.listar(self.caminho)[0]["quantidade"], 3)
        self.assertTrue(db.excluir(identificador, self.caminho))
        self.assertEqual(len(db.listar(self.caminho)), 0)

    def test_validacao(self):
        with self.assertRaises(ValueError):
            db.inserir("  ", 1, self.caminho)
        with self.assertRaises(ValueError):
            db.inserir("Mouse", -2, self.caminho)

    def test_sql_parametrizado(self):
        texto = "Produto '); DROP TABLE produtos; --"
        db.inserir(texto, 1, self.caminho)
        self.assertEqual(db.listar(self.caminho)[0]["nome"], texto)
        self.assertEqual(len(db.listar(self.caminho)), 1)


if __name__ == "__main__":
    unittest.main()
