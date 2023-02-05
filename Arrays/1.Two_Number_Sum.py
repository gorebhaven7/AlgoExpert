def twoNumberSum(array, targetSum):
    # Write your code here.
    hm = {}
    for num in array:
        if targetSum - num in hm:
            return sorted([num,targetSum-num])
        else:
            hm[num] = 1

    return []
