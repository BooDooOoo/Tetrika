def task(array):
    '''
    Функция использует реализацию бинарного поиска, сложность - log(N)
    '''

    low_index = 0
    high_index = len(array) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        guess_zero = array[mid_index]

        if guess_zero == '1':
            if array[mid_index + 1] == '0':
                return mid_index + 1
            else:
                low_index = mid_index + 1

        elif guess_zero == '0':
            if array[mid_index - 1] == '1':
                return mid_index
            else:
                high_index = mid_index - 1


print(task("111111111111111111111111100000000"))
