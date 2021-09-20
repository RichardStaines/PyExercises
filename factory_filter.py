# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import heapq

def factory_filter(A):

    dblSum = sum(A)
    tgt = dblSum / 2.0
    nFilters = 0

    h_neg = [-i for i in A]
    heapq.heapify(h_neg)
#    print(list(h_neg))

    while dblSum > tgt:
        pollution = heapq.heappop(h_neg) / 2
        dblSum += pollution  # note we have stored as -ve values to get the sort to work
        heapq.heappush(h_neg, pollution)
        nFilters += 1
 #       print(f'{nFilters} {dblSum} v {tgt} : {pollution} {list(h_neg)}')

    return nFilters


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Factory Filters')
    A = [5, 18, 4, 3, 2]
    nFilters = factory_filter(A)
    print (nFilters)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
