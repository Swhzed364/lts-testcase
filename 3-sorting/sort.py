class Sort:

    def getMinRun(len: int):

        minRun = 32
        run = 0

        while len >= minRun: 
            run |= len & 1
            len >>= 1
        
        return len + run 
    
    def insertionSort(array, start = 0, end = None):

        if end == None: end = len(array) - 1

        for i in range(start + 1, end + 1):
            j = i
            while j > start and array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
                j -= 1

        return array
    
    def mergeSort(array, start1, end1, end2):

        subArray1, subArray2 = [], []
        lenSubArray1 = end1 - start1 + 1
        lenSubArray2 = end2 - end1

        for i in range(0, lenSubArray1):
            subArray1.append(array[start1 + i])
        
        for i in range(0, lenSubArray2):
            subArray2.append(array[end1 + 1 + i])

        i, j = 0, 0
        iArr = start1

        while i < lenSubArray1 and j < lenSubArray2:
            if subArray1[i] <= subArray2[j]:
                array[iArr] = subArray1[i]
                i += 1
            else:
                array[iArr] = subArray2[j]
                j += 1

            iArr += 1

        while i < lenSubArray1:
            array[iArr] = subArray1[i]
            i += 1
            iArr += 1

        while j < lenSubArray2:
            array[iArr] = subArray2[j]
            j += 1
            iArr += 1

    def timSort(array):

        lenArray = len(array)
        minRun = Sort.getMinRun(lenArray)

        for start in range(0, lenArray, minRun):
            end = min(start + minRun - 1, lenArray - 1)
            Sort.insertionSort(array, start, end)

        currentRun = minRun

        while currentRun < lenArray:
            for start1 in range(0, lenArray, currentRun * 2):
                end1 = min(start1 + currentRun - 1, lenArray - 1)
                end2 = min(start1 + currentRun * 2 - 1, lenArray - 1)

                if end1 < end2:
                    Sort.mergeSort(array, start1, end1, end2)

            currentRun *= 2