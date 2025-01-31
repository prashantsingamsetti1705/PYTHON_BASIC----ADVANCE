#Program for Searching a Word in a given line of Text.
#RegExpr1.py
import re
line="Python is an oop lang.Python is also fun prog lang"
sp="Python"
noc=re.findall(sp,line)
# here noc is an object of type <class, list>
print(" '{}' Found {} Time(s) ".format(sp,len(noc)))