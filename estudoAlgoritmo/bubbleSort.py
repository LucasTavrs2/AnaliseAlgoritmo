# bubbleSort(a):
#     for i = 1 to len(a)-1
#         for j in range(len(a) - 1 - i):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a

# print(bubbleSort([5, 3, 8, 6, 2]))

def bubbleSort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(bubbleSort([5, 3, 8, 6, 2]))
