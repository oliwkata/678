import sys
import json
import yaml

def parsowanie():
    if len(sys.argv) != 3:
        print("Użyj trzech argumentów")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Niepoprawny format: {e}")
        sys.exit(1)

def json_zapis(data, file_path):
    with open (file_path, 'w') as file:
        json.dumb(data, file)

def yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = ymal(file)
        return data
    except yaml.YmalError as e:
        print(f"Niepoprawny format: {e}")
        sys.exit(1)


if __name__ == "__main__":
    pathFile1, pathFile2 = parsowanie()
    if pathFile1.endswitch('.json'):
        data = json(pathFile1)
    elif pathFile1.endwitch('.yaml'):
        data = ymal(pathFile1)
    else:
        print("Niepoprawny format.")
        sys.exit(1)

    json_zapis(data, pathFile2)
    


