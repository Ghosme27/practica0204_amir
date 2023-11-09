divisa={'euro':'€','dollar':'$','yen':'¥'}
a=input('Que tipo de divisa usa:')
if a.lower() in divisa.keys():
    print('Su divisa esta en el diccionario')
elif a in divisa.values():
    print('Su divisa esta en el diccionario')
else:
    print('Su divisa no esta en el diccionario')