def a_b_func(a, b):
    return a, b

this_is_lambda = lambda first, age: f'Цей код написав: {first}, мені {age} років.'

print("Це просто функція:", a_b_func)
print("А це лямбда:", this_is_lambda)
print("Виклик лямбди:", this_is_lambda('Андрій', 17))
print(this_is_lambda(*a_b_func("a", 1)))
