#Python program to find the maximum of two numbers

def maximum(a, b):

    if a >= b:
        return a
    else:
        return b
    
#Assign value
a = 2
b = 4
print(maximum(a, b))