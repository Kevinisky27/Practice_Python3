def DatosInscripcionAlumno():
  Nombre = input('Nombres del alumno: ')
  Apellido = input('Apellidos del alumno: ')
  Carnet = input('Digita el número de carnet: ')

  Alumno = print(f'{Apellido}, {Nombre} : {Carnet}')

if __name__ == '__main__':
  DatosInscripcionAlumno()