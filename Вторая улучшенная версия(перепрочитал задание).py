import random
def selection_sort(array):
    array_copy = array.copy()
    length = len(array_copy)
    comparisons = 0
    swaps = 0
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            comparisons += 1
            if array_copy[j] < array_copy[min_index]:
                min_index = j
        if min_index != i:
            array_copy[i], array_copy[min_index] = array_copy[min_index], array_copy[i]
            swaps += 1
    return array_copy, comparisons, swaps
def bubble_sort(array):
    array_copy = array.copy()
    length = len(array_copy)
    comparisons = 0
    swaps = 0
    for i in range(length - 1):
        for j in range(length - 1 - i):
            comparisons += 1
            if array_copy[j] > array_copy[j + 1]:
                array_copy[j], array_copy[j + 1] = array_copy[j + 1], array_copy[j]
                swaps += 1
    return array_copy, comparisons, swaps
def insertion_sort(array):
    array_copy = array.copy()
    comparisons = 0
    swaps = 0
    for i in range(1, len(array_copy)):
        key = array_copy[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if array_copy[j] > key:
                array_copy[j + 1] = array_copy[j]
                swaps += 1
                j -= 1
            else:
                break
        array_copy[j + 1] = key
    return array_copy, comparisons, swaps
def demo_mode():
    array = [random.randint(0, 99) for _ in range(8)]
    print("Случайный массив:", array)
    return array
def interactive_mode():
    try:
        size = int(input("Размер массива: "))
        if size <= 0:
            print("Ошибка: размер должен быть больше 0")
            return None
        array = []
        for i in range(size):
            element = int(input(f"Элемент {i+1}: "))
            array.append(element)
        print("Ваш массив:", array)
        return array
    except:
        print("Ошибка ввода")
        return None

print("1 - Демонстрационный режим")
print("2 - Интерактивный режим")
try:
    mode = int(input("Выбор: "))
except:
    print("Ошибка ввода")
    mode = -1
array = None
if mode == 1:
    array = demo_mode()
elif mode == 2:
    array = interactive_mode()
else:
    print("Неверный выбор")
if array:
    sorted_selection, comparisons_selection, swaps_selection = selection_sort(array)
    sorted_bubble, comparisons_bubble, swaps_bubble = bubble_sort(array)
    sorted_insertion, comparisons_insertion, swaps_insertion = insertion_sort(array)
    print("\nРезультаты сортировок:")
    print("Сортировка выбором: сравнений =", comparisons_selection, "перестановок =", swaps_selection)
    print("Сортировка пузырьком: сравнений =", comparisons_bubble, "перестановок =", swaps_bubble)
    print("Сортировка вставками: сравнений =", comparisons_insertion, "перестановок =", swaps_insertion)
