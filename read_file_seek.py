


with open("file") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(f.tell())
