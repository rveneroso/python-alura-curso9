from src.leilao.dominio import Usuario, Leilao
import pytest

# Python criará os objetos usuario_teste e leilao_teste sob demanda.Eles não serão instanciados a menos que sejam passados como parâmetros
# para algum método da classe de testes.
from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def usuario_teste():
    return Usuario('Usuario Teste', 100.0)

@pytest.fixture
def leilao_teste():
    return Leilao('Item fictício')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(usuario_teste, leilao_teste):
    usuario_teste.propoe_lance(leilao_teste, 50.0)

    assert usuario_teste.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(usuario_teste, leilao_teste):
    usuario_teste.propoe_lance(leilao_teste, 1.0)

    assert usuario_teste.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_que_o_valor_da_carteira(usuario_teste, leilao_teste):
    usuario_teste.propoe_lance(leilao_teste, 100.0)

    assert usuario_teste.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(usuario_teste, leilao_teste):
    with pytest.raises(LanceInvalido):
        usuario_teste.propoe_lance(leilao_teste, 200.0)
