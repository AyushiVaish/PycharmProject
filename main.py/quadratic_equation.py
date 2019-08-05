
import math
a=input("Enter the value of a");
b=input("Enter the value of b");
c=input("Enter the value of c");
d=b**2-4*a*c;
if d<0:
     print("This equation has no real root");
elif d==0:
    x=(-b+math.sqrt(d))/2*a;
    print("This equation has one solution :" + x);

else:
    x1=(-b+math.sqrt((b**2)-(4*(a*c))))/2*a;
    x2=(-b-math.sqrt((b**2)-(4*(a*c))))/2*a;
    print ("This equation have two solutions : " + x1 +" and " + x2);