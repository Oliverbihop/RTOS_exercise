import math
import array as np

def isPrimeNumber(n):
    if (n < 2):
        return False;
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
try:
        n = int(input("Nhap n: "))
        if n <= 0:
            exit()
except:
        print('Phai nhap so tu nhien')
        exit()
max=0
number = np.array('i',[])
for i in range(n):
    number.append(int(input('Nhap so thu %d: ' % (i+1))))
print(number)
for i in range(len(number)): 
    if isPrimeNumber(number[i]) and i %2 ==0:
        print(number[i]," is even Prime")
    else:
        print(number[i]," is not even prime")

