
from entidades.alumno import Alumno
from repositorios.alumno_repositorio import AlumnoRepositorio
opcion = 0
while opcion != 7:
    print("¿Qué operación desea realizar?")
    print("1. Agregar un alumno")
    print("2. Modificar alumno")
    print("3. Ver alumnos")
    print("4. Eliminar un alumno")

    print("7. Salir")
    
    opcion = input("Ingrese una opción: ")

    # Agregar una persona
    if opcion == "1":
        alias = input("Ingrese un alias: ")
        email = input("Ingrese un email: ")
        
        nuevoAlumno = Alumno(None, alias, email)
        alumnoRepo = AlumnoRepositorio()
        alumnoRepo.guardar(nuevoAlumno)
        print("Alumno guardado con exito")
    
    elif opcion == "2":
        id = input("ingrese el id del alumno a modificar: ")
        nuevoAlias = input("ingrese el nuevo alias: ")
        nuevoEmail = input("ingrese el nuevo email: ")
        alumnoRepo = AlumnoRepositorio()
        alumnoRepo.modificar(id, nuevoAlias, nuevoEmail)
        print("Alumno modificado con exito")

    elif opcion == "3":
        alumnoRepo = AlumnoRepositorio()
        alumnos = alumnoRepo.buscarTodos()
        for alumno in alumnos:
            print(alumno)
    
    elif opcion == "4":
        id = input("ingrese el id del alumno a eliminar: ")
        alumnoRepo = AlumnoRepositorio()
        alumnos = alumnoRepo.eliminar(id)
        print("Alumno eliminado con exito")