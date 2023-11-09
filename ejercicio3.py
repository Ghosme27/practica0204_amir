producto={'Pan':'pan','Huevos':'huevos','cebolla':'Cebolla','Aceite':'aceite'}
precio={'pan':1.40,'huevos':2.30,'cebolla':0.85,'aceite':4.35}
articulo=input('Diga que producto quiere:')
if articulo.lower() in producto.values():
    unidades=int(input('introduzca cuantos unidades quiere:'))
    if articulo.lower() in precio.keys():
        precio_nuevo=unidades*precio[articulo]
        print('el articulo',articulo,'pidendo estas',unidades,'unidades','tiene el precio',precio_nuevo)
else:
    print('No esta disponible ese articulo')
