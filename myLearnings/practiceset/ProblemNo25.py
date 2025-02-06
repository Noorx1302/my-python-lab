with open("poems.txt", "r") as f:
    f = f.read()
    if "twinkle" in f:
        print(True)
    else:
        print(False)