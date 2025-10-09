letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цикл завершився без break.")

count = 0
while count < 3:
    print(f"Ітерація №{count}")
    count += 1
