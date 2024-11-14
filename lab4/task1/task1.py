# TODO решите задачу
import json
def task() -> float:
    file = 'input.json'
    sum = 0
    with open(file, 'r') as file:
        data = json.load(file)
        for item in data:
            sum += item['score'] * item['weight']
    return round(sum, 3)


print(task())
