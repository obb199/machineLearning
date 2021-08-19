class Cidade:

    def __init__(self, nome_cidade, distancia_curitiba):
        self.nome_cidade = nome_cidade
        self.distancia_curitiba = distancia_curitiba
        self.cidades_vizinhas = []


class Vizinho:

    def __init__(self, nome_vizinho, distancia_vizinho, classe_propria):
        self.nome_vizinho = str(nome_vizinho)
        self.distancia_vizinho = int(distancia_vizinho)
        self.classe_propria = classe_propria


#Mostagem do Grafo - Cidades:

porto_uniao = Cidade('Porto União', 203)
paulo_frontin = Cidade('Paulo Frontin', 172)
canoinhas = Cidade('Canoinhas', 141)
tres_barras = Cidade('Três Barras', 131)
sao_mateus_do_sul = Cidade('São Mateus do Sul', 123)
irati = Cidade('Irati', 139)
curitiba = Cidade('Curitiba', 0)
palmeira = Cidade('Palmeira', 59)
mafra = Cidade('Mafra', 94)
campo_largo = Cidade('Campo Largo', 27)
balsa_nova = Cidade('Balsa Nova', 41)
lapa = Cidade('Lapa', 74)
tijucas_do_sul = Cidade('Tijucas do Sul', 56)
araucaria = Cidade('Araucária', 23)
sao_jose_dos_pinhais = Cidade('São José dos Pinhais', 13)
contenda = Cidade('Contenda', 39)


#Montagem do Grafo - Vizinhos:

porto_uniao.cidades_vizinhas.append(Vizinho('Paulo Frontin', 46, paulo_frontin))
porto_uniao.cidades_vizinhas.append(Vizinho('São Mateus do Sul', 87, sao_mateus_do_sul))
porto_uniao.cidades_vizinhas.append(Vizinho('Canoinhas', 78, canoinhas))

paulo_frontin.cidades_vizinhas.append(Vizinho('Porto União', 46, porto_uniao))
paulo_frontin.cidades_vizinhas.append(Vizinho('Irati', 75, irati))

sao_mateus_do_sul.cidades_vizinhas.append(Vizinho('Porto União', 87, porto_uniao))
sao_mateus_do_sul.cidades_vizinhas.append(Vizinho('Irati', 57, irati))
sao_mateus_do_sul.cidades_vizinhas.append(Vizinho('Três Barras', 43, tres_barras))
sao_mateus_do_sul.cidades_vizinhas.append(Vizinho('Palmeira', 77, palmeira))
sao_mateus_do_sul.cidades_vizinhas.append(Vizinho('Lapa', 60, lapa))

canoinhas.cidades_vizinhas.append(Vizinho('Porto União', 78, porto_uniao))
canoinhas.cidades_vizinhas.append(Vizinho('Três Barras', 12, tres_barras))
canoinhas.cidades_vizinhas.append(Vizinho('Mafra', 66, mafra))

tres_barras.cidades_vizinhas.append(Vizinho('Canoinhas', 12, canoinhas))
tres_barras.cidades_vizinhas.append(Vizinho('São Mateus', 43, sao_mateus_do_sul))

irati.cidades_vizinhas.append(Vizinho('Paulo Frontin', 75, paulo_frontin))
irati.cidades_vizinhas.append(Vizinho('Palmeira', 75, palmeira))
irati.cidades_vizinhas.append(Vizinho('São Mateus do Sul', 57, sao_mateus_do_sul))

palmeira.cidades_vizinhas.append(Vizinho('Irati', 75, irati))
palmeira.cidades_vizinhas.append(Vizinho('Campo Largo', 55, campo_largo))

mafra.cidades_vizinhas.append(Vizinho('Canoinhas', 66, canoinhas))
mafra.cidades_vizinhas.append(Vizinho('Tijucas do Sul', 99, tijucas_do_sul))
mafra.cidades_vizinhas.append(Vizinho('Lapa', 57, lapa))

lapa.cidades_vizinhas.append(Vizinho('Mafra', 57, mafra))
lapa.cidades_vizinhas.append(Vizinho('São Mateus do Sul', 60, sao_mateus_do_sul))
lapa.cidades_vizinhas.append(Vizinho('Contenda', 26, contenda))

contenda.cidades_vizinhas.append(Vizinho('Lapa', 26, lapa))
contenda.cidades_vizinhas.append(Vizinho('Balsa Nova', 19, balsa_nova))
contenda.cidades_vizinhas.append(Vizinho('Araucária', 18, araucaria))

balsa_nova.cidades_vizinhas.append(Vizinho('Contenda', 19, contenda))
balsa_nova.cidades_vizinhas.append(Vizinho('Campo Largo', 22, campo_largo))
balsa_nova.cidades_vizinhas.append(Vizinho('Curitiba', 51, curitiba))

araucaria.cidades_vizinhas.append(Vizinho('Contenda', 18, contenda))
araucaria.cidades_vizinhas.append(Vizinho('Curitiba', 37, curitiba))

tijucas_do_sul.cidades_vizinhas.append(Vizinho('Mafra', 99, mafra))
tijucas_do_sul.cidades_vizinhas.append(Vizinho('São José dos Pinhais', 49, sao_jose_dos_pinhais))

curitiba.cidades_vizinhas.append(Vizinho('São José dos Pinhais', 15, sao_jose_dos_pinhais))
curitiba.cidades_vizinhas.append(Vizinho('Araucária', 37, araucaria))
curitiba.cidades_vizinhas.append(Vizinho('Balsa Nova', 51, balsa_nova))
curitiba.cidades_vizinhas.append(Vizinho('Campo Largo', 29, campo_largo))

sao_jose_dos_pinhais.cidades_vizinhas.append(Vizinho('Tijucas do Sul', 49, tijucas_do_sul))
sao_jose_dos_pinhais.cidades_vizinhas.append(Vizinho('Curitiba', 15, curitiba))

campo_largo.cidades_vizinhas.append(Vizinho('Palmeira', 55, palmeira))
campo_largo.cidades_vizinhas.append(Vizinho('Curitiba', 29, curitiba))


def busca_Aestrela(cidade_inicial):

    cidade_analise = cidade_inicial
    cidades_passadas = []
    distancia_total = 0
    cidade_mais_proxima = ''
    proxima_cidade = ''

    while True:
        for i in range(len(cidade_analise.cidades_vizinhas)):
            if len(cidades_passadas) == 0:
                cidades_passadas.append(cidade_inicial.nome_cidade)
            contador = 0
            k = cidade_analise.cidades_vizinhas[i].distancia_vizinho + cidade_analise.distancia_curitiba
            if k < contador or contador == 0:
                contador = k
                cidade_mais_proxima = cidade_analise.cidades_vizinhas[i].nome_vizinho
                proxima_cidade = cidade_analise.cidades_vizinhas[i].classe_propria

        cidades_passadas.append(cidade_mais_proxima)
        distancia_total += contador
        cidade_analise = proxima_cidade

        if cidade_mais_proxima == 'Curitiba':
            print(cidades_passadas)
            return


# TESTES:

busca_Aestrela(paulo_frontin)
print('\n\n')
busca_Aestrela(tijucas_do_sul)
print('\n\n')
busca_Aestrela(balsa_nova)
print('\n\n')
busca_Aestrela(palmeira)
