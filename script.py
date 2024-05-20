import numpy as np

# create cupcakes recipe array
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print(cupcakes)

# load csv file tu ndarray
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

# select eggs column from recipes
eggs = recipes[:,2]
print(eggs)
# select receips that only requires 1 egg
print(eggs == 1)

cookies = recipes[2,:]
print(cookies)
print(cupcakes)

# double batch of cupcakes
double_batch = cupcakes * 2

# create grocery list
grocery_list = cookies + double_batch
print(grocery_list)
