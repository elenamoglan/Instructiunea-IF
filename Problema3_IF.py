#Să se verifice dacă o literă introdusă este vocală sau consoană

litera=input('Introduceti litera: ')
vocale={'a', 'e', 'i', 'o', 'u','ă','â','î','A','E','O','I','U','Ă','Î', 'Â'}
consoane={'b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'ț', 'v', 'w', 'x', 'z', 'y','ș','Ș','B', 'C', 'D', 'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'Ț', 'V', 'W', 'X', 'Z', 'Y'}
if litera in vocale:
    print(litera, 'este vocala')
elif litera in consoane:
    print(litera, 'este consoana')
else:
    print('Eroare')