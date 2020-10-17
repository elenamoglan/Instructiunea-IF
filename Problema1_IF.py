#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. 

a=int(input('Numarul curent pentru primul elev: '))
x=int(input('Punctajul pentru primul elev: '))
b=int(input('Numarul curent pentru al doilea elev: '))
y=int(input('Punctajul pentru al doilea elev: '))
c=int(input('Numarul curent pentru al treilea elev: '))
z=int(input('Punctajul pentru al treilea elev elev: '))
if (x>=y):
    max = x
    n_max = a
else:
    max = y
    n_max = b
if z>=max:
    max = z
    n_max = c
print('Punctajul maxim il are elevul cu numarul curent ', n_max)
