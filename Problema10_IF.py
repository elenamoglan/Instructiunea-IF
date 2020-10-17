'''La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
numărul de boabe de porumb.'''

g=int(input('Numărul de găini: '))
b=int(input('Numarul de boabe: '))
r=b%g #nr. boabe care se duc la Clapon
c=b//g #nr boabe la fiecare gaina
if r==c:
    print(f'Numarul de boabe primite este {c} - egalitate')
elif r>c:
    print(f'Clapon a primit mai multe boabe cu {r-c} boabe')
else:
    print(f'Gainele au primit mai multe boabe cu {c-r} boabe')