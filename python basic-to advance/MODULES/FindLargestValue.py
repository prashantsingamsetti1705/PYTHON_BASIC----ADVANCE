#FindLargestValue.py<---File Name and Module Name
def findlarsubstringvalue(value):#value:
    d={}
    for val in value:
        if val not in d:
            d[val]=1
        else:
            d[val]=d[val]+1
    else:
        print(d)
        mv=max(d.values())
        for k,v in d.items():
            if(mv==v):
                print("Largest Value:",k)

