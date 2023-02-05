def isValidSubsequence(array, sequence):
    # Write your code here.
    i,j = 0,0
    while(i != len(array) and j != len(sequence)):
        if array[i] == sequence[j]:
            j += 1
        i += 1

    if j == len(sequence):
        return True
    return False
            
