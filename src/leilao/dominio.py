import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances

class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    # O nome da classe Leilao no método abaixo não está limitando o parâmetro a uma instância de
    # Leilao. É apenas uma referência para quem vier a usar essa classe saber o que passar a esse
    # método.
    def avalia(self,leilao: Leilao):
        for lance in leilao.lances:
            if (lance.valor > self.maior_lance):
                self.maior_lance = lance.valor
            if(lance.valor < self.menor_lance):
                self.menor_lance = lance.valor
