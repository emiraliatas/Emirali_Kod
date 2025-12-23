import numpy as np



# # linspace

# a = np.linspace(0,20,6)

# # 0'la 20 arasında -20 dahil- 6 sayı sec,
# # hepsinin arasında esit mesafe olsun
# print(a)


# random
#print(np.random.randint(1,100,(5,2)))

my_random_array = np.random.randint(0,100,20)
my_numpy_array = np.arange(0,30)


# numpy dizi methodları
print(my_numpy_array)
reshape_array = my_numpy_array.reshape(6,5)
print(my_numpy_array.shape)
print(reshape_array.shape)
