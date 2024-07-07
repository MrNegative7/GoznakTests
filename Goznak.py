'''Вариант через динамическое программирование с одним параметром. O(n)'''
'''Функция multiplicate(A) использует два вспомогательных массива одинаковой длины left_product и right_product, 
чтобы хранить произведения элементов слева и справа от текущего элемента соответственно. 
Затем происходит проход по массиву A, и на i-ом месте результирующего массива 
result вычисляется произведение left_product[i] * right_product[i]'''
def multiplicate(A):
    n = len(A)
    left_product = [1] * n # Создание массива для хранения произведения элементов слева
    right_product = [1] * n # Создание массива для хранения произведения элементов справа
    result = [1] * n # Создание массива результата

    for i in range(1, n):
        left_product[i] = left_product[i-1] * A[i-1] # Находим произведение элементов слева

    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * A[i+1] # Находим произведение элементов справа

    for i in range(n):
        result[i] = left_product[i] * right_product[i] # Запись результатов в массив result произведением left_product[i] * right_product[i]

    return result

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(multiplicate(A))