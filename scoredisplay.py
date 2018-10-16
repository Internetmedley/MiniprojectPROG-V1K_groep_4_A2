import json

invoerNaam =  input("Name: ")
score = 20

def high_score(name, score):
    a_dict = {name: score}

    with open('hi-scores.json') as f:
        data = json.load(f)

    data.update(a_dict)

    with open('hi-scores.json', 'w') as f:
        json.dump(data, f)

    for key, value in data.items():
            print("{:14}\t\t{:2}".format(key, value))
    return


high_score(invoerNaam,score)
#kan niet zelfde key als eentje die al bestaat