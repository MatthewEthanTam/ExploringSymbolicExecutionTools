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
    assert vehicle.type == VehicleType.BICYCLE
    if vehicle.type == VehicleType.CAR:
        return True
    assert vehicle.type in [VehicleType.TRUCK, VehicleType.MOTORCYCLE, VehicleType.CAR]
    return vehicle.fuel_level > 0

# def isUsableFixed(vehicle: Vehicle) -> bool:
#     assert vehicle.type == VehicleType.BICYCLE
#     if vehicle.type == VehicleType.BICYCLE:
#         return True
#     assert vehicle.type in [VehicleType.TRUCK, VehicleType.MOTORCYCLE, VehicleType.CAR]
    
#     return vehicle.fuel_level > 0