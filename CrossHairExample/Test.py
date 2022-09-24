from typing import List
def consecutive_pairs(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post: min(numbers) <= __return__ <= max(numbers)
    '''
    return sum(numbers) - len(numbers)

def consecutive_pairs2(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post: min(numbers) <= __return__ <= max(numbers)
    '''
    return max(numbers) - min(numbers)
def consecutive_pairs3(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post:  __return__ == max(numbers)
    '''
    return max(numbers)