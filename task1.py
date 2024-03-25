N=10
print("Задание 1. Вариант ",(N-1)%10+1,"""
В городе M расположена кольцевая автодорога длиной в N километров с движением в обе стороны.
На каждом километре автодороги расположены пункты приема мусора определенной вместимости. В пределах кольцевой
дороги в одном из пунктов сборки мусора мусороперерабатывающий завод таким образом, чтобы стоимость доставки
мусора была минимальной. Стоимость доставки мусора вычисляется как вместимость пункта сбора, умноженная на
расстояние от пункта сбора мусора до мусороперерабатывающего завода. Если мусороперерабатывающий завод
находится рядом с пунктом сбора, расстояние считается нулевым. Пункты сбора мусора нумеруются с 1 до N.
Рядом с каким пунктом сбора мусора нужно поставить мусороперерабатывающий завод?
""")

def min_delivery_cost(path):
    file=open(path,'r')
    n=int(file.readline())
    trash_can=[]
    answer=[0 for i in range(n)]
    for i in range(n):
        trash_can.append(int(file.readline()))
    file.close()
    sum=0
    left_sum=0
    right_sum=0
    for i in range(1,n//2):
        right_sum+=trash_can[i]
        sum += trash_can[i] * i   
    for i in range(n//2,n):
        left_sum+=trash_can[i]
        sum+=trash_can[i]*(n-i)
    answer[0] = sum
    for i in range(1, n):
        answer[i] = answer[i - 1] + left_sum + trash_can[i - 1] - right_sum - 2*trash_can[(i + n // 2 - 1) % n]
        right_sum += trash_can[(i + n // 2 - 1) % n] - trash_can[i]
        left_sum += trash_can[i - 1] - trash_can[(i + n // 2 - 1) % n]
    return [answer.index(min(answer))+1,min(answer)]

def print_answer(data):
    print("Пункт сбора №",data[0],", минимальная стоимость доставки равна",data[1])

example='example.txt'
file1='27-99a.txt'
file2='27-99b.txt'

print("Ответ для файла с примером:")
print_answer(min_delivery_cost(example))

print("Ответ для файла 27-99a.txt:")
print_answer(min_delivery_cost(file1))

print("Ответ для файла 27-99b.txt:")
print_answer(min_delivery_cost(file2))