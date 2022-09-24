from typing import List
def consecutive_pairs(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post: min(numbers) <= __return__ <= max(numbers)
    '''
    return sum(numbers) - len(numbers)