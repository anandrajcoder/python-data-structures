def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

          if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



arr=[3323,9889,42342,11,55,34,323]

#print (bubble_sort(arr))

def insertion_sort(arr):

    for i in arr :
        j =arr.index(i)

        while j>0:
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else :
                break

            j -=1
    return arr


print (insertion_sort(arr))

x =[3232.878,2,33,323,3]




