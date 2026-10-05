VOWELS = set("аеєиіїоуюя")


class Figure:
    FIGURES = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type: str, length: int) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> int:
        return self.length

    def get_angles(self) -> list[int]:
        if self.type == "трикутник":
            return [60, 60, 60]
        return [90, 90, 90, 90]


def count_symbols(text: str) -> int:
    return len(text)


def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor


def count_vowels(text: str) -> int:
    return sum(1 for character in text.lower() if character in VOWELS)


def read_positive_number() -> int:
    value = input("Введіть додатне ціле число: ")
    try:
        number = int(value)
    except ValueError as error:
        raise ValueError("Потрібно ввести ціле число!") from error

    assert number > 0, "Число має бути більшим за нуль!"
    return number


def main() -> None:
    try:
        number = read_positive_number()
    except ValueError as error:
        print(f"Помилка: {error}")
    except AssertionError as error:
        print(f"Помилка: {error}")
    else:
        print(f"Введено правильне число: {number}")


if __name__ == "__main__":
    main()