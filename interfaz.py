
from entidades.alumno import Alumno
from repositorios.alumno_repositorio import AlumnoRepositorio
from entidades.curso import Curso
from repositorios.curso_repositorio import CursoRepositorio
from entidades.examen import Examen
from repositorios.examen_repositorio import ExamenRepositorio

opcion = ""
while opcion != "99":
    print("¿Qué operación desea realizar?")
    print("1. Agregar un alumno")
    print("2. Modificar alumno")
    print("3. Ver alumnos")
    print("4. Eliminar un alumno")
    print("5. Agregar un curso")
    print("6. Modificar curso")
    print("7. Ver curso")
    print("8. Eliminar un curso")
    print("9. Cargar examen")
    print("99. Salir")
    
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
        nuevoCurso = input("ingrese el nuevo alias: ")
        nuevoEmail = input("ingrese el nuevo email: ")
        alumnoRepo = AlumnoRepositorio()
        alumnoRepo.modificar(id, nuevoCurso, nuevoEmail)
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

    elif opcion == "5":
        nombre = input("Ingrese el nombre del curso: ")
        duracion = input("Ingrese la duracion en semanas: ")
        
        nuevoCurso = Curso(None, nombre, duracion)
        cursoRepo = CursoRepositorio()
        cursoRepo.guardar(nuevoCurso)
        print("Curso guardado con exito")
    
    elif opcion == "6":
        id = input("ingrese el id del curso a modificar: ")
        nuevoNombre = input("ingrese el nuevo nombre del curso: ")
        nuevaDuracion = input("ingrese la nueva duracion en semanas: ")
        cursoRepo = CursoRepositorio()
        cursoRepo.modificar(id, nuevoNombre, nuevaDuracion)
        print("Curso modificado con exito")

    elif opcion == "7":
        cursoRepo = CursoRepositorio()
        cursos = cursoRepo.buscarTodos()
        for curso in cursos:
            print(curso)
    
    elif opcion == "8":
        id = input("ingrese el id del curso a eliminar: ")
        cursoRepo = CursoRepositorio()
        curso = cursoRepo.eliminar(id)
        print("Curso eliminado con exito")

    elif opcion == "9":
        nota = float(input("Ingrese una nota del 1 al 10: "))
        idCurso = int(input("Ingrese el id del curso: "))
        idAlumno = int(input("Ingrese el id del alumno: "))
        
        nuevoExamen = Examen(None, nota, idCurso, idAlumno)
        examenRepo = ExamenRepositorio()
        examenRepo.guardar(nuevoExamen)
        print("Examen guardado con exito")


   
    
