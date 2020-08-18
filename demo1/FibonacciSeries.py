# 斐波那契数列：从第三个数开始，每个数等于前两个数之和
a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b
