class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        # Індивідуальне завдання: перевірка на цифри/символи
        if name is not None and not name.replace(' ', '').isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        
        # Індивідуальне завдання: велика літера
        if name is not None:
            name = name.capitalize()
            
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    # Індивідуальне завдання: функція підрахунку букв
    @property
    def name_length(self) -> int:
        """Повертає довжину імені"""
        return len(self.name)
    
    # Індивідуальне завдання: властивість full_name
    @property
    def full_name(self) -> str:
        """Повертає повну інформацію"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    def create_email(self, domain=None) -> str:
        """Instance method
        """
        # Індивідуальне завдання: модифікація домену
        if domain is not None:
            return f"{self.name}@{domain}"
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"
    
    # Індивідуальне завдання: метод збереження у файл
    def save_to_file(self, filename="users.txt"):
        """Зберігає інформацію у файл"""
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{self.full_name}\n")


print("Розпочинаємо створювати обєкти!")

# Індивідуальне завдання: додати своє ім'я
names = ("Bohdan", "Marta", None, "Andrii")  # Додано "Andrii"
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

# Демонстрація індивідуальних завдань
print("\n" + "="*50)
print("ДЕМОНСТРАЦІЯ ІНДИВІДУАЛЬНИХ ЗАВДАНЬ")
print("="*50)

# Довжина імені
for name, me in all_names.items():
    print(f"Довжина імені '{me.name}': {me.name_length}")

# Full name
print("\nFull names:")
for name, me in all_names.items():
    print(f"  {me.full_name}")

# Зміна привітання
print(f"\nЗміна привітання: {me.say_hello('Привіт з України!')}")

# Модифікація домену
test_obj = MyName("TestUser")
print(f"Стандартний email: {test_obj.create_email()}")
print(f"Модифікований email: {test_obj.create_email('gmail.com')}")

# Збереження у файл
print("\nЗбереження у файл...")
for me in all_names.values():
    me.save_to_file()
    print(f"Збережено: {me.full_name}")

# Перевірка на неправильне ім'я
print("\nПеревірка на неправильне ім'я:")
try:
    bad_user = MyName("User123")
except ValueError as e:
    print(f"Помилка: {e}")

# Перевірка великої літери
test_lower = MyName("john")
print(f"Перевірка великої літери: 'john' -> '{test_lower.name}'")