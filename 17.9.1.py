def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находимо середину
    if array[middle] < element:  # если элемент в середине,
        return middle
    elif array[middle] > element:
        return binary_search(array, element, left, middle - 1)
    else:
        print("Значения, удовлетворяющего условию, нет")




a=int(input("введите число\t"))
str_a=input("введите набор чисел через пробел\t")

list_a=list(map(int,str_a.split())) # преобразование чисел из строки в список

for i in range(1, len(list_a)):# сортировка списка
    x = list_a[i]
    idx = i
    while idx > 0 and list_a[idx-1] > x:
        list_a[idx] = list_a[idx-1]
        idx -= 1
    list_a[idx] = x
print(list_a)
print("-------------------")
print(binary_search(list_a, a, 0, 4))
next_id=(binary_search(list_a, a, 0, 4)+1)# указание индекса числа, следующего за минимальным
print('--------------------')

if list_a[next_id]>=a:
    print(next_id)
else:
    print("Значения, удовлетворяющего условию, нет")
