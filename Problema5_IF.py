'''Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi.'''

z, l, a = map(int, input("Data curenta este ").split('.'))
zn, ln, an = map(int, input("Data nasterii este ").split('.'))
ar = a - an
if (l<ln) or (l==ln and z<zn):
    ar -= 1
print(ar)