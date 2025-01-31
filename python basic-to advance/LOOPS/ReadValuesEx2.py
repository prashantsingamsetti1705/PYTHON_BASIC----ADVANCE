#Program for Reading the Values from Key Board
#ReadValuesEx2.py
n=int(input("How Many Words u want to enter:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    lst=[] # Empty List--for adding the values
    for i in range(1,n+1):
        value=input("Enter {} Value:".format(i))
        lst.append(value)
    else:
        print("List of Words=",lst)