import sys
import json

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

if __name__ == "__main__":
    pathFile1, pathFile2 = parsowanie()
    data = json(pathFile1)
    print(data)
    json_zapis(data, pathFile2)



