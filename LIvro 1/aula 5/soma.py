soma = 0 
numeros = range(1,1000)
i=0
total = 0
while soma < 100:
    print(soma)
    soma += numeros[i]
    i+=1
print(soma)

soma = 0
x = 0
while x < 1000:
    x+=1
    if x%3==0:
        print(x)
        soma +=x
    else:
        if x%5==0:
            pass
        else:
            print('buscando... ')
            continue
    if soma>300:
        print(soma)
        break