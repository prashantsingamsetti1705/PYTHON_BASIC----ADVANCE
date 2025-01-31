#Program for accepting Line of Text and display every word and letters in that word
#WordsGenerateOops.py
import threading,time
class LineOfText:
	def __init__(self,line):
		self.line=line
	def dispwords(self):
		for word in self.line.split():
			print("{}--->{}".format(threading.current_thread().name,word))
			time.sleep(0.25)
			for ch in word:
				print("\t\t\t{}".format(ch))
				time.sleep(0.25)
			print("----------------------------")

#main Program
t1=threading.Thread(target=LineOfText(input("Enter a Line of Text:")).dispwords )
t1.start()

