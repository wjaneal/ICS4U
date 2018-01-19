
from math import *
import random

Trials = 1000
LottoSize = 49
LineSize = 7
TrialCount = LineSize*[0]


def LineComp(Line1, Line2):
	Size1 = len(Line1)
	Size2 = len(Line2)
	Count = 0
	for i in range(0, Size1):
		for  j in range(0,Size2):
			if Line1[i] == Line2[j]:
				Count +=1
	return Count

def AssignLine(Size):
	Numbers = [0]*(Size+1)
	Count = 0
	Lines = [0]*(Size+1)
	while Count<Size:	
		Number = int(random.random()*Size+1)
		if Numbers[Number] == 0:
			Numbers[Number] = 1
			Lines[Count] = Number
			Count += 1
	return Lines
PickLine = [0]*(LineSize)
LottoLine = [0]*(LineSize)
for i in range(1, Trials):
	LottoResult = AssignLine(LottoSize)
	#print "Lotto Result", LottoResult
	LottoPicks = AssignLine(LottoSize)
	#print "LottoPicks", LottoPicks
	Count = 0
	for j in range (0, LineSize):
		LottoLine[j] = LottoResult[j]
	while Count < (1.0*LottoSize/LineSize):
		for j in range(0, LineSize-1):
			#print Count*LineSize+j
			PickLine[j] = LottoPicks[Count*LineSize+j]
	
		Count +=1
	NumberPicked = LineComp(LottoLine, PickLine)
	TrialCount[NumberPicked] += 1
	print NumberPicked
 	if i % 100 == 0:
		print i	
print TrialCount	

