with open("example.txt", "w") as f:
    f.write("Перша лінія\nДруга лінія\nТретя лінія")


with open("example.txt", "r") as f:
    for i, line in enumerate(f):
        print(f"{i})> {line.strip()}")
