'''Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. '''

A=int(input('Numarul de bile albe mari: '))
a=int(input('Numarul de bile albe mici: '))
R=int(input('Numarul de bile rosii mari: '))
r=int(input('Numarul de bile rosii mici: '))
V=int(input('Numarul de bile verzi mari: '))
v=int(input('Numarul de bile verzi mici: '))
print(f'In total sunt {A+a+R+r+V+v} bile')
if (A+R+V)>(a+r+v):
    print(f'Sunt mai multe bile mari, fiind {A+R+V}')
elif (A+R+V)<(a+r+v):
    print(f'Sunt mai multe bile mici, fiind {a+r+v}')
else:
    print(f'Numarul de bile mari este egal cu numarul de bile mici, fiind {A+R+V}')
if (A+a>=R+r) and (A+a>=V+v):
    print('Bilele cele mai numeroase sunt de culoare alba, fiind ', A+a)
elif (R+r>=A+a) and (R+r>=V+v):
    print('Bilele cele mai numeroase sunt de culoare rosie, fiind ', R+r)
else:
    print('Bilele cele mai numeroase sunt de culoare verde, fiind ', V+v)
