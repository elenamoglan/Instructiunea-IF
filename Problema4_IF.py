# Se introduc vârstele a 3 persoane. Afişaţi vârstele cuprinse între 18 şi 60 de ani

a=int(input('Varsta primei persoane: '))
b=int(input('Varsta persoanei a doua: '))
c=int(input('Varsta persoanei a treia: '))
f = False
if (18<a<60):
    print('Virsta ',a,end=' ')
    f = True
if (18<b<60):
    print('Virsta ',b,end=' ')
    f = True
if (18<c<60):
    print('Virsta ',c)
    f = True
if f == False:
    print('Toate varstele sunt ori mai mici sau egale cu 18 ori mai mare sau egale cu 60')
