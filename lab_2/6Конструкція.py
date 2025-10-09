A = 0
try:
    print("Що буде якщо поділити 10 на", A, "?")
    print(10 / A)
except Exception as e:
    print("Невже це помилка >", e)
finally:
    print("Блок finally виконується завжди — навіть якщо сталася помилка.")
