import array as np
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

for i in range(len(number)): 
    if number[i]<0:
        number[i]=0
print(number)