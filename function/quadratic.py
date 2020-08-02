```Python
#!/usr/bin/python
import math
import time
def quadratic(a,b,c):
    if b*b-4*a*c<0:
        print('the equation has no real roots')
    elif b*b-4*a*c==0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        print('the equation has only one real root: %d'%x1)
    elif b*b-4*a*c > 0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print('the equation has two roots: %d and %d'%(x1,x2))
        #return x1,x2
        
print('this is a program that calculating the roots of a quadratic equation in one unknown\n')
time.sleep(2)
print('please input a,b,c of the equation in turn,and then tap Enter one by one:') #operate discription
time.sleep(2)
a = int(input('first input \'a\':'))
print('\n')
time.sleep(1)
b = int(input('great, then input \'b\':'))
print('\n')
time.sleep(1)
c = int(input('last step,just input \'c\':'))
print('\n')
time.sleep(2)
quadratic(a,b,c)
