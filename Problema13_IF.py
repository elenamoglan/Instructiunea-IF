#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi?

x=int(input('Ionel este pe locul '))
if x<=100:
    print('Ionel va prii tricou de culoare', end=' ')
    r=x%4
    if r==1:
        print('albă')
    elif r==2:
        print('rosie')
    elif r==3:
        print('albastră')
    else:
        print('neagra')
else:
    print('Ionel nu va primi tricou')