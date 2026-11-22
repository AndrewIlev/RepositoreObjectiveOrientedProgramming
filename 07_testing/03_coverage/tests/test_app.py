import pytest

from app import Figure


@pytest.mark.parametrize(
    ("figure_type", "expected_angles"),
    [
        ("квадрат", [90, 90, 90, 90]),
        ("прямокутник", [90, 90, 90, 90]),
        ("трикутник", [60, 60, 60]),
    ],
    ids=["square", "rectangle", "triangle"],
)
def test_get_angles(figure_type: str, expected_angles: list[int]) -> None:
    figure = Figure(figure_type, 5)

    assert figure.get_figure_type == figure_type
    assert figure.get_figure_length == 5
    assert figure.get_angles() == expected_angles


@pytest.mark.parametrize("figure_type", ["коло", ""])
def test_rejects_unknown_figure_type(figure_type: str) -> None:
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 5)


@pytest.mark.parametrize("length", [0, -1])
def test_rejects_non_positive_length(length: int) -> None:
    with pytest.raises(AssertionError, match="Довжина має бути більшою за 0"):
        Figure("квадрат", length)
