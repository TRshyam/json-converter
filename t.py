import json

for i in range(2):
    question=input()
    marks=input()
    difficulty=input()
    type=input()
    answer=input()

    dictionary = {
        "question": question,
        "marks": marks,
        "difficulty":difficulty,
        "type": type,
        "answer":answer
    }

with open("database.json", "w") as outfile:
	json.dump(dictionary, outfile)

