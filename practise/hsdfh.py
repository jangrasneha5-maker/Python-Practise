# import numpy as np
# # a = np.zeros((2, 2))
# # a[:, 1] = [1, 2]
# # print(a)
# import matplotlib.pyplot as plt
# # fig, ax = plt.subplots()
# # ax.plot([1,2], [3,4])
# # plt.plot([1,2], [4,3])
# # plt.show()

# a = np.arange(6).reshape(2, 3)
# print(a.shape)


# x = 10
# def f():
#     global x
#     x = 5

# f()
# # print(x)


# x = 10
# def f():
#     x = 5
# f()
# # print(x)

# a = [[1,2],[3,4]]
# b = a.copy()
# b[0][0] = 99
# print(a)


a=[1,2,3,4,5]
print(a[-1]+a[:,-1])