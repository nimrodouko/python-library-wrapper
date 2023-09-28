import ctypes

add_lib = ctypes.CDLL('./main.so')
add_lib.add.argtypes = (ctypes.c_int,ctypes.c_int)
add_lib.add.retype = ctypes.c_int

def add(a,b):
    return add_lib.add(a,b)

result = add(3,5)
print(result)