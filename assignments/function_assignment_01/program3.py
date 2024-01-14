
import array as arr

def fact(num):

    for i in num:
        facto = 1
        for j in range(1,i+1):
            facto = facto*j
        fun.append(facto)

arr1 = arr.array('i',[1,2,3,4,5])
fun = arr.array('i',[])

fact(arr1)

print(fun)

    
