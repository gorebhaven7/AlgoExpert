def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    i,j = 0,0
    minn = [0,0]
    minnVal = float('inf')
    
    while i != len(arrayOne) and j != len(arrayTwo):
        val = abs(arrayOne[i] - arrayTwo[j])
        if val < minnVal:
            minnVal = val
            minn[0],minn[1] = arrayOne[i],arrayTwo[j]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
        # print(minnVal,minn)
    return minn
    
