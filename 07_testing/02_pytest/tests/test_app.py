import pytest

from app import Figure, count_symbols, count_vowels, divide, read_positive_number


@pytest.mark.unit
@pytest.mark.parameterized
@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure_types(figure_type: str) -> None:
    assert Figure(figure_type, 1).get_figure_type == figure_type


@pytest.mark.unit
@pytest.mark.uses_fixtures
def test_square_fixture_properties(square: Figure) -> None:
    assert square.get_figure_type == "квадрат"
    assert square.get_figure_length == 10
    assert square.get_angles() == [90, 90, 90, 90]


@pytest.mark.unit
@pytest.mark.uses_fixtures
def test_module_fixture_has_all_allowed_figures(
    allowed_figures: tuple[str, ...],
) -> None:
    assert allowed_figures == Figure.FIGURES


@pytest.mark.unit
@pytest.mark.uses_fixtures
def test_module_fixture_values_are_usable_in_another_test(
    allowed_figures: tuple[str, ...],
) -> None:
    assert all(Figure(figure_type, 1).type == figure_type for figure_type in allowed_figures)


@pytest.mark.unit
@pytest.mark.parameterized
@pytest.mark.parametrize("figure_type", ["коло", "", None])
def test_rejects_invalid_figure_types(figure_type: str) -> None:
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 1)


@pytest.mark.unit
@pytest.mark.parameterized
@pytest.mark.parametrize("length", [0, -1, -10])
def test_rejects_invalid_lengths(length: int) -> None:
    with pytest.raises(AssertionError, match="Довжина має бути більшою за 0"):
        Figure("квадрат", length)


@pytest.mark.unit
def test_triangle_angles() -> None:
    assert Figure("трикутник", 4).get_angles() == [60, 60, 60]


@pytest.mark.unit
def test_count_symbols_and_vowels() -> None:
    assert count_symbols("Україна") == 7
    assert count_vowels("Україна") == 4
    assert count_symbols("") == 0
    assert count_vowels("12345") == 0


@pytest.mark.unit
def test_divide() -> None:
    assert divide(10, 2) == 5


@pytest.mark.unit
def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.unit
@pytest.mark.input_handling
def test_read_positive_number(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "7")
    assert read_positive_number() == 7


@pytest.mark.unit
@pytest.mark.input_handling
def test_read_non_integer(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "текст")
    with pytest.raises(ValueError, match="Потрібно ввести ціле число"):
        read_positive_number()


@pytest.mark.unit
@pytest.mark.input_handling
def test_read_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "0")
    with pytest.raises(AssertionError, match="більшим за нуль"):
        read_positive_number()
