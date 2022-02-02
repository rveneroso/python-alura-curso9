from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

ivan = Usuario('Ivan Piro')
osmar = Usuario('Osmar Telo')

lance_ivan = Lance(ivan, 100.0)
lance_osmar = Lance(osmar, 150.0)

leilao_celular = Leilao('Celular Moto E7 Power')
leilao_celular.lances.append(lance_ivan)
leilao_celular.lances.append(lance_osmar)

for lance in leilao_celular.lances:
    print(f'O usuário {lance.usuario.nome} de um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao_celular)
print(avaliador.menor_lance)
print(avaliador.maior_lance)


