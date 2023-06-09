# quick sort:
def quick_sort(s):

    if len(s)<=1:
        return s

    elem = s[0]
    smaller = list(filter(lambda x: x<elem,s))
    center = [i for i in s if i == elem]
    bigger = list(filter(lambda x: x>elem,s))

    return quick_sort(smaller) + center + quick_sort(bigger)

print(quick_sort([7,6,10,5,9,8,3,4]))

# как это работает?
# берется массив и берем любое опорное число из этого массива а потом при помощи filter
# мы на левую часть ставим элементы которые меньше опорного а с права те которые больше
# и так еще раз тоесть на левой части мы снова выбираем опорное число и точно так же распологаем


# merge sort:

def merge(a,b):
    ak = 0
    bk = 0
    out = []
    while ak < len(a) and bk < len(b):
        if a[ak] < b[bk]:
            out.append(a[ak])
            ak += 1
        else:
            out.append(b[bk])
            bk += 1

    while ak < len(a):
        out.append(a[ak])
        ak += 1
    while bk < len(b):
        out.append(b[bk])
        bk += 1
    return out


def div(a):
    if len(a) == 1:
        return a

    middle = len(a)//2
    left = div(a[:middle])
    right = div(a[middle:])
    return merge(left, right)


f = [2,4,5,1,3,9,7,1,3,5,7]
print(div(f))
# как это работает?
# берется массив и мы его делим на два пока у нас не будет масив с одним значением а потом при помощи
# сортировки слиянием мы сравниваем левый и правый и меньший из ни мы добовляем в out


# Insertion Sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        position = i
        while position > 0 and lst[position-1] > current_value:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = current_value
    return lst
a = [1,2,4,6,3,5,8,9,7]
print(insertion_sort(a))

# как это работает?
# берется первый элемент массива и сравнивается с пребидущим(нулевым) если он меньше
# то мы ставим его на место нулевого элемента и потом берем следущий элемент и уже
# сравниваем его со вторым элементом и так далее до самого конца массива




# selection sort:

g = [-3,5,0,-8,1,10]
def selection_sort(g):
    n = len(g)

    for i in range(n-1):
        for d in range(i+1,n):
            if g[i] > g[d]:
                g[i],g[d] = g[d], g[i]
    return g
j = [-3,5,0,-8,1,10]
print(selection_sort(j))
# как это работает?
# у нас есть 2 указателя i and d, i-является главным тоесть с ним мы будем сравинать
# последущие числа тоесть при помощи d мы пробегаемся по массиву и находим наименьшее
# число и если это число меньше чем число i то они меняются местами до самого конца
