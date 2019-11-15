#Two functions to find the max value in an array

#This function runs in O(n)
def fastMax(array):
    currentMax = array[0] #initialize currentMax

    for num in array: #loop over the array

        if num > currentMax: #update currentMax if we find something larger
            currentMax = num
    return currentMax

#This function runs in O(n^2)
def slowMax(array):

    for i in range(len(array)): #loop over the array

        current = array[i]
        isMax = True #assume current is max until proven otherwise

        for j in range(i+1, len(array)): #compare to all other values
            compare = array[j]
            if compare > current:
                isMax = False

        if isMax: #if it made it through, return current
            return current
