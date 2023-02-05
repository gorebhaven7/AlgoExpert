def threeNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    array.sort()
    for i in range(len(array)):
        target = targetSum-array[i]
        hm = {}
        for j in range(i,len(array)):
            if target - array[j] in hm:
                if array[i] != array[j] and array[i] != target-array[j] and array[j] != target-array[j]:
                    ans.append(sorted([array[i],array[j],target-array[j]]))
                # break
            else:
                hm[array[j]] = 1
    print(ans.sort())
    return ans
        
