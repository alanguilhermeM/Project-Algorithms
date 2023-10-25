import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    "Se key e message não possuírem os tipos corretos, lança erro"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('Ae', 'a')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)

    "Se key não for um índice positivo válido de message, a string inverte"
    "impar"
    assert encrypt_message('podese', 3) == 'dop_ese'
    assert encrypt_message('podese', 9) == 'esedop'
    "par"
    assert encrypt_message('podese', 4) == 'es_edop'
