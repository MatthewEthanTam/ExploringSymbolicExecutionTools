from typing import List
def sumNumbers(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post: __return__ == sum(numbers)
    '''
    if len(numbers)  > 4 :
        return sum(numbers)*2
    else :
        return sum(numbers)
    

def getDifferenceOfMaxAndMin(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post: __return__ == max(numbers) - min(numbers)
    '''
    return min(numbers) - max(numbers) 
def getMax(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post:  __return__ == max(numbers)
    '''
    return max(numbers)