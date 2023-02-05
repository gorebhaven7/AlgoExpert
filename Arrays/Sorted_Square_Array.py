def sortedSquaredArray(array):
    # Write your code here.
    i,j,k = 0,len(array)-1,len(array)-1
    ans = [0] * len(array)
    while i<=j:
        if abs(array[i]) > abs(array[j]):
            ans[k] = array[i] ** 2
            i += 1
        else:
            ans[k] = array[j] ** 2
            j -= 1
        k -= 1
    return ans