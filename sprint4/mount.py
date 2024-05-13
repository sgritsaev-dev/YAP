from array import array
def valid_mountain_array(arr):
    if len(arr.split())<3:
        return False
    count = 0
    direction = 'up'
    position = -127
    for el in array('b', [int(el) for el in arr.split()]):
        if el==position:
            return False
        if direction=='up':
            if el<position:
                count+=1
                direction='down'
            position=el
        if direction=='down':
            if el>position:
                return False
    if count!=1:
        return False
    if list(sorted([int(el) for el in arr.split()]))==[int(el) for el in arr.split()] or list(reversed(sorted([int(el) for el in arr.split()])))==[int(el) for el in arr.split()]:
        return False
    return True
print(valid_mountain_array(input()))
        
        
            