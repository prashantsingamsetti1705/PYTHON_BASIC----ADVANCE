#FilterMapReduceEx.py
import functools
print("Enter List of employee Salaries separated by space:")
sals=[float(sal) for sal in input().split() if float(sal) in range(0,1001)]
print("Given Salaries:")
print(sals)
print("----------------------------------------------")
#Filter the sal ranges between 0 to 500
sal0_500=list(filter(lambda sal: 0<=sal<=500,sals))
#Filter the sal ranges between  501 to 1000
sal501_1000=list(filter(lambda sal: 501<=sal<=1000,sals))
#Give Hike 10% to those emp whose sal ranges from 0 to 500
hike0_500=list(map(lambda sal: sal*1.1, sal0_500))
#Give Hike 20% to those emp whose sal ranges from 501 to 1000
hike501_1000=list(map(lambda sal:sal*1.2,sal501_1000))
#Find the total sal of those emp whose sal ranges between 0 to 500 before and after hike
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
hiketotsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hike0_500)
#Find the total sal of those emp whose sal ranges between 501 to 1000 before and after hike
totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
hiketotsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hike501_1000)
print("="*50)
print("Sal0-500\t\tHike0-500")
print("-"*50)
for ol,nl in zip(sal0_500,hike0_500):
    print("\t{}\t\t{}".format(ol,nl))
print("*"*40)
print("\t{}\t\t{}".format(totsal0_500,hiketotsal0_500))
print("-"*50)
print("Sal501-1000\t\tHike501-1000")
print("-"*50)
for ol,nl in zip(sal501_1000,hike501_1000):
    print("\t{}\t\t{}".format(ol,nl))
print("*"*40)
print("\t{}\t\t{}".format(totsal501_1000,hiketotsal501_1000))
print("-"*50)
GTSal0_1000=totsal0_500+totsal501_1000
GTHikesal0_1000=hiketotsal0_500+hiketotsal501_1000
print("\t{}\t\t{}".format(GTSal0_1000,GTHikesal0_1000))
print("="*50)

