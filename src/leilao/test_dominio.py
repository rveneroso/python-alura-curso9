from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        ivan = Usuario('Ivan Piro')
        osmar = Usuario('Osmar Telo')

        lance_ivan = Lance(ivan, 100.0)
        lance_osmar = Lance(osmar, 150.0)

        leilao_celular = Leilao('Celular Moto E7 Power')
        leilao_celular.lances.append(lance_ivan)
        leilao_celular.lances.append(lance_osmar)

        avaliador = Avaliador()
        avaliador.avalia(leilao_celular)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance)
