def reverse(word):
    return word[::-1]


reverse('testing')

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

sorted(fruits, key=reverse)
