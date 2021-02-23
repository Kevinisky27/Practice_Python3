def msj_principal():
  diseño_saludo1 = ('_____________________________________________________________')
  diseño_saludo2 = '-------------------------------------------------------------'
  saludo = ('|' '          Bienvenido al portal Automotriz Mundial          ' '|')
  print(diseño_saludo1)
  print(saludo)
  print(diseño_saludo2)

def requisitos_compra_auto():
  nombre = input('Digita tu nombre: ')
  apellido = input('Digita tu apellido: ')
  edad = int(input('Digita tu edad: '))


  if edad < 18:
    print(f'Lo sentimos {nombre} no cuentas con la edad necesaria para adquirir un automóvil.')
  elif edad >= 18:
    print(f'Bienvenido {nombre} puedes seguir realizando el proceso de tu compra.')


if __name__ == '__main__':
  msj_principal()
  requisitos_compra_auto()

  Dark#2018-2021