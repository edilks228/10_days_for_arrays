# binary search

def binary_search(lst,res):
    low = 0
    hight = len(lst)
    search_rez = False
    while low < hight and not search_rez:
        middle = (hight + low) //2
        guess = lst[middle]
        if guess == res:
            search_rez = True
            return search_rez
        elif guess > res:
            hight = middle-1
        else:
            low = middle+1

    return search_rez

a = [1,2,3,4,5,6,7,8,9]
b = 9
print(binary_search(a,b))


# search an element in sorted array

def search(lst, res):
    index = 0
    for i in lst:
        if i == res:
            return index
        else:
            index+=1

a = [1,2,3,4,5,6,7,8,9]
b = 7
print(search(a,b))
# i don't sure that is correct and usefull but i'll tried