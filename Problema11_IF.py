#Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR.

a=int(input('Primul numar este '))
b=int(input('Al doilea numar este '))
c=int(input('Al treilea numar este '))
if a%2==0:
    print(f'{a} - Par')
else:
    print(f'{a} - Impar')
if b%2==0:
    print(f'{b} - Par')
else:
    print(f'{b} - Impar')
if c%2==0:
    print(f'{c} - Par')
else:
    print(f'{c} - Impar')