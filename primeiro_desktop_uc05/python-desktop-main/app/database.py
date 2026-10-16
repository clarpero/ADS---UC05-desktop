"""Persistência SQL explícita: sem ORM nesta primeira versão."""
import sqlite3
from contextlib import contextmanager
from collections.abc import Iterator
from pathlib import Path

DEFAULT_DB = Path.home() / ".uc05_primeiro_desktop" / "estoque.db"


def conectar(caminho: Path = DEFAULT_DB) -> sqlite3.Connection:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


@contextmanager
def sessao(caminho: Path = DEFAULT_DB) -> Iterator[sqlite3.Connection]:
    con = conectar(caminho)
    try:
        with con:
            yield con
    finally:
        con.close()

def inicializar(caminho: Path = DEFAULT_DB) -> None:
    with sessao(caminho) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL CHECK(length(trim(nome)) > 0),
                quantidade INTEGER NOT NULL CHECK(quantidade >= 0)
            )
        """)


def listar(caminho: Path = DEFAULT_DB) -> list[sqlite3.Row]:
    with sessao(caminho) as con:
        return con.execute(
            "SELECT id, nome, quantidade FROM produtos ORDER BY nome COLLATE NOCASE, id"
        ).fetchall()


def inserir(nome: str, quantidade: int, caminho: Path = DEFAULT_DB) -> int:
    nome = nome.strip()
    if not nome:
        raise ValueError("Informe um nome.")
    if not isinstance(quantidade, int) or quantidade < 0:
        raise ValueError("A quantidade deve ser um inteiro não negativo.")
    with sessao(caminho) as con:
        cur = con.execute(
            "INSERT INTO produtos (nome, quantidade) VALUES (?, ?)",
            (nome, quantidade),
        )
        return int(cur.lastrowid)


def atualizar(produto_id: int, nome: str, quantidade: int, caminho: Path = DEFAULT_DB) -> bool:
    nome = nome.strip()
    if not nome or quantidade < 0:
        raise ValueError("Nome e quantidade devem ser válidos.")
    with sessao(caminho) as con:
        cur = con.execute(
            "UPDATE produtos SET nome = ?, quantidade = ? WHERE id = ?",
            (nome, quantidade, produto_id),
        )
        return cur.rowcount > 0


def excluir(produto_id: int, caminho: Path = DEFAULT_DB) -> bool:
    with sessao(caminho) as con:
        cur = con.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        return cur.rowcount > 0
