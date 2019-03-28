def merge (left ,right):

 
    left_index,right_index =0,0

    result =[]

    i ,j = 0,0
    while (len(result)<len(left_index) + len(right_index)):

        if left_index[i] <right_index[j]:
            result.append[i]

            i = i +1
        else :

            result.append(right_index[j])
            j += 1

    return result

def mergesort(arr):

    if len(arr) >1:

        half = len(arr)/2
        half_left = mergesort(arr[:half])
        rest_left = mergesort(arr[half:])

 

    return merge(half_left,rest_left)


arr=[2,466,6767,3223,65656]



print("the merge sorted",arr)