#программа выводит оптимальное количество получившихся идеальных фигур массой x за время t, а так же их номер из изначального списка(нумерация с 1)

#n - количество фигур, x - идеал фигуры, t - время на выполнения
#вводятся целочисленные данные через пробел(пример 6 7 10)
#за единицу времени t можно уменьшить или увеличить вес фигуры на 1, чтобы приблизить ее к идеалу x
n, x, t = map(int,str(input()).split(' '))

#n_ice - список веса фигур, количество фигур составляет число n(пример ввода: 1 4 6 2 13 7)
n_ice = list(map(int,str(input()).split(' ')))

#будущий список номеров полученных идеальных фигур за время t
i_ice = []

#словарь: ключ - номер фигуры, значение - изначальный вес фигуры
new_dict = dict(zip(list(range(1, n+1)), n_ice))

def delAndAdd(i):
    key_i = list(new_dict.keys())[list(new_dict.values()).index(i)]
    i_ice.append(key_i)
    del new_dict[key_i]
    n_ice.remove(i)

while x in n_ice:
    delAndAdd(x)

while t:
    if len(n_ice)==0:
        break
    minInIce = min(n_ice, key=lambda y:abs(y-x))
    if minInIce>x:
        if minInIce-x<=t:
            delAndAdd(minInIce)
            t-=minInIce-x
        else:
            break
    else:
        if x-minInIce<=t:
            delAndAdd(minInIce)
            t-=x-minInIce
        else:
            break

i_ice.sort()

print(len(i_ice)) 
for i in i_ice:
    print(i, end=' ')