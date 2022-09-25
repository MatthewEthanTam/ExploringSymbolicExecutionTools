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
    post: max(numbers) - min(numbers)
    '''
    return min(numbers) - max(numbers) 
def getMax(numbers: List[float]) -> float:
    ''' 
    pre: len(numbers) >0
    post:  __return__ == max(numbers)
    '''
    return max(numbers)


from dataclasses import dataclass
from enum import Enum
from typing import Optional

class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    MOTORCYCLE = 3
    BICYCLE = 4

@dataclass(init = False)

class Vehicle:
    type =  VehicleType
    fuel_level =  Optional[float]

def isUsable(vehicle: Vehicle) -> bool:
    ''' 
    pre: vehicle.type == VehicleType.BICYCLE
    post:  vehicle.type in [VehicleType.TRUCK, VehicleType.MOTORCYCLE, VehicleType.CAR]
    '''
    if vehicle.type == VehicleType.CAR:
        return True
    return vehicle.fuel_level > 0