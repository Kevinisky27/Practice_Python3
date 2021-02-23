# frutas = ['manzana', 'pera', 'mango', 'piña', 'melocotón', 'sandia']
# for fruta in frutas:
#   print(fruta)

# iter('cadena') # cadena
# iter(['a', 'b', 'c']) # lista
# iter(('a', 'b', 'c')) # tupla
# iter({'a', 'b', 'c'}) # conjunto
# iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')