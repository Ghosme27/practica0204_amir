traduccion={}
while True:
    a=input('Introduzca palabras en español con su traduccion en ingles separado por dos puntos (:) :')
    b=input('Si no quieres continuar ponga terminar,si no es asi solo dale a enter:')
    if b=='terminar':
        break   
    else:
        español,ingles=a.split(':')
        traduccion[español]=ingles
print ('Estas son las palabras con su traduccion que tenemos',traduccion)
frase_traduce=input('Escriba una frase:')
palabra_traducir=[traduccion.get(español,español) for español in  frase_traduce.split()]
frase_enes=' '.join(palabra_traducir)
print(frase_enes)