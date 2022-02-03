import sys

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        lance = Lance(self, valor)
        leilao.registra_lance(lance)

        self.__carteira -= valor

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def registra_lance(self, lance: Lance):
        if (not self.__lances or self.__lances[-1].usuario != lance.usuario and self.__lances[-1].valor < lance.valor):
            self.__lances.append(lance)
            if (lance.valor > self.maior_lance):
                self.maior_lance = lance.valor
            if (lance.valor < self.menor_lance):
                self.menor_lance = lance.valor
        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        # Com a sintaxe [:] o Python não irá retornar o objeto lances original da classe Leilao.
        # Ele irá devolver uma cópia da lista (shallow copy). A sintaxe [:] nada mais é do que o
        # slicing da lista no qual estão sendo omitidos o elemento inicial e o elemento final.
        # A cópia rasa também é obtida quando se usa o método copy() sobre uma lista.
        # Para realizarmos uma deep copy (cópia profunda) devemos usar o módulo copy que é nativo
        # do Python:
        '''
        from copy import deepcopy

        livros_yan = [[‘Banco MySQL’], [‘Certificação PHP’, ‘TDD PHP’], [‘HTML5 e CSS3’]]
        livros_pedro = deepcopy(livros_yan)
        '''
        return self.__lances[:]
