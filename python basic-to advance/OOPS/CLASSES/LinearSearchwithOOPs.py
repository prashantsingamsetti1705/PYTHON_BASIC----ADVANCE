#LinearSearchwithOOPs.py
class Linear:
    def readvals(self):
        nov=int(input("Enter How Many Values:"))
        if(nov<=0):
            return []
        else:
            lst=[]
            for i in range(1,nov+1):
                val=float(input("Enter {} Value:".format(i)))
                lst.append(val)
            else:
                return lst
    def search(self,lst):
        #Sort the Data of lst
        lst.sort()  # [-4.0, 1.0, 11.0, 23.0, 45.0]
        skey=float(input("Enter the search Key:"))
        sp=-1
        for i in range(0,len(lst)):
            if(lst[i]==skey):
                sp=i
                break
        if(sp==-1):
            print("{} does not exist in list of values".format(skey))
            print("Search is Un-Sucessful")
        else:
            print("{} Found at {} Postion".format(skey,sp))

#Main Program
lo=Linear()
lst=lo.readvals()
if(len(lst)==0):
    print("List is empty")
else:
    lo.search(lst)


