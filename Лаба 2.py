import random

# Три сортировки
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

# Главная программа
print("Выберите сортировку:")
print("1 - Сортировка выбором")
print("2 - Сортировка пузырьком")
print("3 - Сортировка вставками")

sort_choice = input("Ваш выбор (1-3): ")

print("\nВыберите режим:")
print("1 - Демонстрационный")
print("2 - Интерактивный")

mode_choice = input("Ваш выбор (1-2): ")

if mode_choice == "1":
    # Демонстрационный режим
    print("\n--- Демонстрационный режим ---")
    demo_array = [random.randint(0, 99) for _ in range(8)]
    print(f"Массив для демонстрации: {demo_array}")
    
    if sort_choice == "1":
        result_array, comparisons_count, swaps_count = selection_sort(demo_array)
        print("Сортировка выбором:")
    elif sort_choice == "2":
        result_array, comparisons_count, swaps_count = bubble_sort(demo_array)
        print("Сортировка пузырьком:")
    elif sort_choice == "3":
        result_array, comparisons_count, swaps_count = insertion_sort(demo_array)
        print("Сортировка вставками:")
    
    print(f"Результат: {result_array}")
    print(f"Сравнений: {comparisons_count}")
    print(f"Перестановок: {swaps_count}")

elif mode_choice == "2":
    # Интерактивный режим
    print("\n--- Интерактивный режим ---")
    
    # Ввод массива
    try:
        array_size = int(input("Введите размер массива: "))
        user_array = []
        print("Введите элементы массива:")
        for index in range(array_size):
            element = int(input(f"Элемент {index + 1}: "))
            user_array.append(element)
    except ValueError:
        print("Ошибка ввода! Будет использован случайный массив.")
        user_array = [random.randint(0, 99) for _ in range(10)]
    
    print(f"\nВаш массив: {user_array}")
    
    # Выполнение сортировки
    if sort_choice == "1":
        result_array, comparisons_count, swaps_count = selection_sort(user_array)
        print("Сортировка выбором:")
    elif sort_choice == "2":
        result_array, comparisons_count, swaps_count = bubble_sort(user_array)
        print("Сортировка пузырьком:")
    elif sort_choice == "3":
        result_array, comparisons_count, swaps_count = insertion_sort(user_array)
        print("Сортировка вставками:")
    
    print(f"Результат: {result_array}")
    print(f"Сравнений: {comparisons_count}")
    print(f"Перестановок: {swaps_count}")
