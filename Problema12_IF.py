#“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă iubeşte …. 

x=int(input('Nr de petale a margaretei este '))
r=x%5
print('El (ea) mă iubeşte', end=' ')
if r==1:
    print('un pic')
elif r==2:
    print('mult')
elif r==3:
    print('cu pasiune')
elif r==4:
    print('la nebunie')
else: 
    print('de loc')
