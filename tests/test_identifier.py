import pytest

from src.identifier import identifier

@pytest.mark.parametrize(
    "numero, entrada, esperado",
    [
        (1, "abcd", "válido"),
        (2, "abc12", "válido"),
        (3, "a", "válido"),
        (4, "abc123", "válido"),
        (5, "7belo", "inválido"),
        (6, "s&nha", "inválido"),
        (7, None, "inválido"),
        (8, "senhalonga123", "inválido"),
    ]
)
def test_identifier(numero, entrada, esperado):
    # Setup
    # Os dados do caso de teste foram definidos no parâmetro.

    # Invocation
    resultado = identifier(entrada)

    # Assessment
    assert resultado == esperado

@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("", "inválido"),          # 0
        ("a", "válido"),            # 1
        ("abc123", "válido"),       # 6
        ("abcdefg", "inválido"),    # 7
    ]
)
def test_valores_limite(entrada, esperado):
    # Setup
    # Entrada e resultado esperado definidos no parâmetro.

    # Invocation
    resultado = identifier(entrada)

    # Assessment
    assert resultado == esperado