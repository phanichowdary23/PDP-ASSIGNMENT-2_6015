a= input("a: ")
b= input("b: ")
c= input("c: ")
d= (int(b)**2)-4*int(a)*int(c)
if d>0:
    print("the roots are real and distinct")
    x1= -int(b)+(int(d))/(2*int(a))
    x2= -int(b)-(int(d))/(2*int(a))
    print("the roots are","\nx1=",x1,"\nx2=",x2)
elif d==0:
     print("the roots are real and equal")
     x1= -int(b)/(2*int(a))
     x2= -int(b)/(2*int(a))
     print("the roots are","\nx1=",x1,"\nx2=",x2)
else:
     print("the roots are infinite")