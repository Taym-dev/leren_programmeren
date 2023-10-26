from studieadvies import *

scores = []

print(COMPETENTIE_STELLING_1)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_2)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_3)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_4)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_5)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_6)
print(OPTIES)
answer = int(input())
scores.append(answer)

print(COMPETENTIE_STELLING_7)
print(OPTIES)
answer = int(input())
scores.append(answer)

total_scores = sum(scores)
average_score = int(total_scores / len(scores))

print(COMPETENTIE_ADVIES_TITEL)

if average_score <= 2 or (scores.count(1) >= (len(scores) / 2)):
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif average_score <= 3 or (scores.count(2) >= (len(scores) / 2)):
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
