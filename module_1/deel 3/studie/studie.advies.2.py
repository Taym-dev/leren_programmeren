from studieadvies import *

scores = []

def askQuestion(text):
	print(text)
	print(OPTIES)

	answer = int(input())

	scores.append(answer)

def getAvgScore():
	som = 0

	for score in scores:
		som += score

	return int(som / len(scores))

def getAnswerCount(tillChoice):
	answerCount = 0

	for score in scores:
		if score in range(0, tillChoice):
			answerCount += 1

	return answerCount

askQuestion(COMPETENTIE_STELLING_1)
askQuestion(COMPETENTIE_STELLING_2)
askQuestion(COMPETENTIE_STELLING_3)
askQuestion(COMPETENTIE_STELLING_4)
askQuestion(COMPETENTIE_STELLING_5)
askQuestion(COMPETENTIE_STELLING_6)
askQuestion(COMPETENTIE_STELLING_7)

avgScore = getAvgScore()

print(COMPETENTIE_ADVIES_TITEL)

if avgScore <= 2 or (getAnswerCount(1) >= (len(scores) / 2)):
	print(COMPETENTIE_ADVIES_ZORGELIJK)
elif avgScore <= 3 or (getAnswerCount(2) >= (len(scores) / 2)):
	print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
	print(COMPETENTIE_ADVIES_GERUSTSTELLEND)




	