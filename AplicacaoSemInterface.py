from local import Local

# A entrada é definida aqui, 
# 1 primeiro defino o input que recebe a cordenada
# 2 em seguida separo a (str) por virgula
# 3 garanto que (entrada) sera (float) com o metodo 'map' em seguida uso 'list' para não me retornar a cordenada do obj
entrada = list(map(float, input('digite aqui o valor da coordenada separada por virgula: ').split(',')))
coordenada = []

# Filtro a lista para garantir apenas cordenada (x) e (y)
for x in range(2):
    coordenada.append(entrada[x])

local0 = Local(coordenada[0], coordenada[1])

print(local0.pesquisa())