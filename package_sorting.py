from enum import Enum

class Stack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width: int, height: int, length: int, mass: int) -> Stack:
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All values must be positive integers.")
    
    bulky = _is_bulky(width, height, length)
    heavy = _is_heavy(mass)

    if bulky and heavy:
        return Stack.REJECTED
    
    if bulky or heavy:
        return Stack.SPECIAL
    
    return Stack.STANDARD

def _is_bulky(width: int, height: int, length:int) -> bool:
    if width * height * length >= 1000000:
        return True

    if width >= 150 or height >= 150 or length >= 150:
        return True

    return False

def _is_heavy(mass: int) -> bool:
    if mass >= 20:
        return True
    
    return False

if __name__ == "__main__":
    print("Package Sorting System")
    print("Enter package dimensions and mass:")
    
    try:
        width = int(input("Width (cm): "))
        height = int(input("Height (cm): "))
        length = int(input("Length (cm): "))
        mass = int(input("Mass (kg): "))
        
        result = sort(width, height, length, mass)
        print(f"\nPackage sorted to: {result.value}")
        
    except ValueError:
        print("Error: Please enter all positive integer values.")
        exit(1)
    