#RemoveDuplicateValues.py<----File Name and Module Name
def RemoveDuplicateValues(s):
    lst=[]
    for val in s:
        if val not in lst:
            lst.append(val)
    else:
        print("Unique Values from Given Word={}".format("".join(lst)))
