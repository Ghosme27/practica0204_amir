nombre=input('Introduzca su nombre:')
edad=input('Introduzca su edad:')
calle=input('Introduzca su calle:')
telefono=input('Introduzca su numero de telefono:')
diccionario={'nombre':nombre,'edad':edad,'calle':calle,'telefono':telefono}
print(diccionario['nombre'],'tiene',diccionario['edad'],'vive en',diccionario['calle'],'y su numero es',diccionario['telefono'])