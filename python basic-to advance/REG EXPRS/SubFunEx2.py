#SubFunEx2.py
import re
txt = "The rain in Spain"
x = re.sub(r"\s", "_", txt)
print(x)

"""
>>> txt = "The rain in Spain"
>>> txt=txt.replace(" ","-")
>>> print(txt)
The-rain-in-Spain
"""