lista1=[]
def lista(num):
    for i in range(num):
        x = int(input("ingrese su rut: {}: ".format(i+1)))
        lista1.append(x)
    lista1.reverse()
    return lista1
print(lista(8))
lista2=[2,3,4,5,6,7,2,3]

multiplicacion1=lista1[0] * lista2[0] 
multiplicacion2=lista1[1] * lista2[1] 
multiplicacion3=lista1[2] * lista2[2] 
multiplicacion4=lista1[3] * lista2[3] 
multiplicacion5=lista1[4] * lista2[4] 
multiplicacion6=lista1[5] * lista2[5] 
multiplicacion7=lista1[6] * lista2[6] 
multiplicacion8=lista1[7] * lista2[7] 
lista3=[multiplicacion1, multiplicacion2, multiplicacion3, multiplicacion4, multiplicacion5, multiplicacion6, multiplicacion7, multiplicacion8]
print(lista3)
lista4=multiplicacion1+multiplicacion2+multiplicacion3+multiplicacion4+multiplicacion5+multiplicacion6+multiplicacion7+multiplicacion8
print(lista4)
lista5=lista4//11 
print(lista5)
lista6=lista5*11
print(lista6)
lista7=lista4-lista6
print(lista7)
lista8=11-lista7
print(lista8)
lista1.reverse()
print(lista1)

if lista8 == 11: 
    print("su digito verificador es 0")
    lista9=0
    print(f"entonces su rut quedaría en: {lista1}" + str(lista9))
elif lista8 == 10:
    print("su digito verificador es K")
    lista10=str(" k ")
    print(f"entonces su rut quedaría en: {lista1}" + str(lista10))

print(f"su rut es: {lista1}"+ str(lista8))


