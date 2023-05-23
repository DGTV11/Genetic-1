#I DID NOT MAKE THIS MYSELF!!!!!
def counting_sort(array, exp1):
    n = len(array)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (array[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (array[i] / exp1)
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]

def radix_sort(array):
    max1 = max(array)
    exp = 1
    while max1 / exp > 0:
        counting_sort(array, exp)
        exp *= 10
    return array