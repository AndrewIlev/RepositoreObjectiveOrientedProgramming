from random import randint

A = randint(0, 1)
if A == 1:
    print("Отже, A дорівнює 1")
elif A == 0:
    print("A дорівнює нулю")
else:
    print("Яке дивне число!")

print(f"Значить A={A}" if A else f"Але може бути що A={A}")
