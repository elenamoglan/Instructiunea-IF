#Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?

x=int(input('Radu este pe locul '))
n_clasa = x//25
if x % 25 != 0 :
    n_clasa += 1
if n_clasa<=5:
    print('Radu va fi repartizat in clasa', end=' ')
    if n_clasa==1:
        print('A')
    elif n_clasa==2:    
        print('B')
    elif n_clasa==3:    
        print('C')
    elif n_clasa==4:    
        print('D')
    else:
        print('E')
else:
    print('Nu mai sunt clase disponibile')