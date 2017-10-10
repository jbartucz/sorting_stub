from random import sample

def my_sort(alist):
    
    # do something here with alist to sort it
    return alist

# create a list of random numbers up to maximum_value
maximum_value = 1000000
length_of_list = 100
alist = sample(range(maximum_value), length_of_list)

# sort the list and print it out
my_sort(alist)
print(alist)