import sys
def parsowanie():
    if len(sys.argv) != 3:
        print("Użyj trzech argumentów")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    pathFile1, pathFile2 = parsowanie()
