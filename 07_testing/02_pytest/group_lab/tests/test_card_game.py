import pytest

from lab.main import CardGame, SingleCardGame


@pytest.mark.unit
@pytest.mark.card_game
@pytest.mark.game_initialization
def test_card_game_initializes_expected_attributes() -> None:
    card = CardGame()
    assert card.name in CardGame.CARD_NAMES
    assert 1 <= card.attack <= 10
    assert 20 <= card.health <= 40


@pytest.mark.unit
@pytest.mark.card_combat
def test_hit_another_card_reduces_health_by_damage(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attacker = CardGame()
    defender = CardGame()
    initial_health = defender.health
    monkeypatch.setattr(
        CardGame,
        "_CardGame__calculate_critical_damage",
        staticmethod(lambda damage: damage),
    )
    damage = attacker.hit_another_card(defender)
    assert damage == attacker.attack
    assert defender.health == initial_health - attacker.attack


@pytest.mark.unit
@pytest.mark.card_attributes
@pytest.mark.parametrize(
    "rarity",
    ["Common", "Rare", "Epic", "Legendary", "Unknown"],
)
@pytest.mark.parameterized
def test_single_card_attributes_and_rarity(rarity: str) -> None:
    card = SingleCardGame(rarity)
    assert card.name.startswith("Epic Single Card with rarity ")
    assert card.attack == 5
    assert card.health == 30
    assert card.rarity == (rarity if rarity in SingleCardGame.RARITY_LEVELS else "Common")


@pytest.mark.unit
@pytest.mark.card_attributes
def test_single_card_increment_and_decrement() -> None:
    card = SingleCardGame("Epic")
    card.increment()
    assert (card.attack, card.health) == (6, 40)
    card.decrement()
    assert (card.attack, card.health) == (5, 30)


@pytest.mark.unit
@pytest.mark.input_validation
@pytest.mark.parametrize(("value", "expected"), [(0, 0), (1, 2), (5, 10), (10, 20)])
@pytest.mark.parameterized
def test_interaction_doubles_non_negative_integers(value: int, expected: int) -> None:
    assert CardGame().incorrect_interraction(value) == expected


@pytest.mark.unit
@pytest.mark.input_validation
@pytest.mark.parametrize("value", [-1, -5, -10])
def test_interaction_rejects_negative_values(value: int) -> None:
    with pytest.raises(ValueError, match="від'ємним"):
        CardGame().incorrect_interraction(value)


@pytest.mark.unit
@pytest.mark.input_validation
@pytest.mark.parametrize("value", ["string", 3.14, None, [], {}])
def test_interaction_rejects_non_integer_values(value: object) -> None:
    with pytest.raises(TypeError, match="цілим числом"):
        CardGame().incorrect_interraction(value)


@pytest.mark.unit
@pytest.mark.input_handling
def test_example_with_input_prints_valid_number(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "42")
    assert CardGame().example_with_input() is None
    assert "Ви ввели число: 42" in capsys.readouterr().out


@pytest.mark.unit
@pytest.mark.input_handling
def test_example_with_input_handles_non_integer(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "слово")
    assert CardGame().example_with_input() == 1


@pytest.mark.unit
@pytest.mark.comparison
@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [(5, 3, 5), (-4, -8, -4), (0, 0, None), (0, -5, 0)],
)
@pytest.mark.parameterized
def test_comparison_methods(left: int, right: int, expected: int | None) -> None:
    card = CardGame()
    assert card.compare_input_arguments_original(left, right) == expected
    assert card.compare_input_arguments_reduced(left, right) == expected
