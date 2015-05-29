__author__ = 'Sorostitude'


# Takes a list and sorts it in O(log(n)) time.
def linear_sort(some_list):

    for n in range(len(some_list)/2):

        temp_var = some_list[n]

        some_list[n] = some_list[-1 - n]

        some_list[-1 - n] = temp_var

    return some_list

x = [3, 4, 5, 6, 7, 8]

linear_sort(x)
print x

