nota1 = int(input("Digite nota 1 en número entero entre 0 a 100: "))
nota2 = int(input("Digite nota 2 en número entero entre 0 a 100: "))
nota3 = int(input("Digite nota 3 en número entero entre 0 a 100: "))
nota4 = int(input("Digite nota 4 en número entero entre 0 a 100: "))
nota5 = int(input("Digite nota 5 en número entero entre 0 a 100: "))

promedio = (nota1+nota2+nota3+nota4+nota5)/5

if promedio >=60:
    print("Aprobado, su promedio es :",promedio)

elif promedio >= 40:
    print ("En recuperación, su promedio es:", promedio)

else:
    print("Reprobado, su promedio es:", promedio)

