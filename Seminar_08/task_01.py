import json


def txt_to_json(source, output):
    data1 = {}
    with open(source, 'r') as f:
        data = f.read()

    for line in data.split('\n'):
        name, number = line.split(' ')
        data1[name.capitalize()] = float(number)


    with open(output, 'w') as f:
        json.dump(data1, f, indent=4)

txt_to_json('data.txt', 'output.json')       