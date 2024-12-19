# import numpy as np
# import matplotlib.pyplot as plt
# import time
# def b_s(A):
#     for j in range(len(A) - 1):
#         for i in range(len(A) - 1 - j):
#                 if A[i]>A[i + 1]:
#                   A[i], A[i + 1]=A[i + 1], A[i]
#     return A
# def i_s(B):
#     for i in range(1, len(B)):
#         key = B[i]
#         j = i-1
#         while j >= 0 and key < B[j]:
#             B[j + 1] = B[j]
#             j -= 1
#         B[j + 1] = key
# def q_s(C):
#     if len(C) <= 1:
#         return C
#     pivot = C[len(C) // 2]
#     left = [x for x in C if x < pivot]
#     middle = [x for x in C if x == pivot]
#     right = [x for x in C if x > pivot]
#     return q_s(left) + middle + q_s(right)
# def time_sort(s_f, e):
#     start_time = time.time()
#     s_f(e.copy())
#     return time.time() - start_time
# sizes = [100, 200, 500, 780]
# b_t = []
# i_t = []
# q_t = []
# for size in sizes:
#     arr = np.random.randint(0, 10000, size)
#     b_t.append(time_sort(b_s, arr))
#     i_t.append(time_sort(i_s, arr))
#     q_t.append(time_sort(q_s, arr))
# plt.figure(figsize=(10, 6))
# plt.plot(sizes, b_t, label='Пузырьковая')
# plt.plot(sizes, i_t, label='Вставками')
# plt.plot(sizes, q_t, label='Быстрая')
# plt.xlabel('Размер массива')
# plt.ylabel('Время, c')
# plt.title('Время работы')
# plt.legend()
# plt.grid()
# plt.show()