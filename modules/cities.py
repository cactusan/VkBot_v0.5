used = []
unused = []

with open(r"modules\RussiaCities.txt", "r") as file:
    for text in file:
        text = text[:-1]
        unused.append(text)