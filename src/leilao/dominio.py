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
        if(self._valor_eh_invalido(valor)):
            raise ValueError('O valor do lance não pode ser superior ao saldo da carteira ')
        lance = Lance(self, valor)
        leilao.registra_lance(lance)

        self.__carteira -= valor

    def _valor_eh_invalido(self,valor):
        return valor > self.__carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def registra_lance(self, lance: Lance):
        if (self._lance_eh_valido(lance)):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
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

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_maior_que_lance_anterior(self, lance):
        return self.__lances[-1].valor < lance.valor

    def _lance_eh_valido(self, lance):
        return not self.__lances or self._usuarios_diferentes(lance) and self._valor_maior_que_lance_anterior(lance)

