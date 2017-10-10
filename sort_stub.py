from random import sample

# a very simple, but slow sorting algorithm
def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(1, len(alist) - i):
            if (alist[j - 1] > alist[j]):
                temp = alist[j - 1]
                alist[j - 1] = alist[j]
                alist[j] = temp

# this is the function you should fill in
def my_sort(alist):
    
    # do something here with alist to sort it
    print (alist)

# create a list of random numbers up to maximum_value
maximum_value = 1000000
length_of_list = 100
alist = sample(range(maximum_value), length_of_list)

# sort the list and print it out
# bubble_sort(alist) # do not try this with a very long list (> 100)- the time grows exponentially!
my_sort(alist)
print(alist)
