'''Вариант с линейным поиском. O(n^2)'''
def multiplicate(A):
    result = []
    for i in range(len(A)): # Проходим по массиву два раза, чтобы посчитать произведение
        product = 1 # Инициализируем переменную product для подсчета произведений
        for j in range(len(A)):
            if i != j: # По условию задачи (произведение всех чисел массива А, кроме числа, стоящего на i-ом месте.)
                product *= A[j] # Считаю произведение
        result.append(product) # Каждое произведение запишу в массив result
    return result

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(multiplicate(A))