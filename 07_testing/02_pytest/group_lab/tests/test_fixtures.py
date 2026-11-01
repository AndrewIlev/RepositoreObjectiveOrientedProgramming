from pathlib import Path

import pytest

from lab.main import CardGame, SingleCardGame


pytestmark = [pytest.mark.unit, pytest.mark.uses_fixtures]


@pytest.fixture
def card_game() -> CardGame:
    return CardGame()


@pytest.fixture
def single_card_game() -> SingleCardGame:
    return SingleCardGame("Epic")


@pytest.fixture
def single_card_game_incremented(single_card_game: SingleCardGame) -> SingleCardGame:
    single_card_game.increment()
    yield single_card_game
    single_card_game.decrement()


@pytest.fixture(scope="module")
def rarity_levels() -> tuple[str, ...]:
    return SingleCardGame.RARITY_LEVELS


@pytest.fixture
def result_file(tmp_path: Path) -> Path:
    path = tmp_path / "result.txt"
    path.write_text("done", encoding="utf-8")
    yield path
    path.unlink()


def test_card_game_fixture(card_game: CardGame) -> None:
    assert card_game.name in CardGame.CARD_NAMES


def test_yield_fixture_prepares_card(single_card_game_incremented: SingleCardGame) -> None:
    assert (single_card_game_incremented.attack, single_card_game_incremented.health) == (6, 40)


def test_card_fixture_is_independent(single_card_game: SingleCardGame) -> None:
    assert (single_card_game.attack, single_card_game.health) == (5, 30)


def test_module_fixture_first_use(rarity_levels: tuple[str, ...]) -> None:
    assert rarity_levels[0] == "Common"


def test_module_fixture_second_use(rarity_levels: tuple[str, ...]) -> None:
    assert rarity_levels == SingleCardGame.RARITY_LEVELS


def test_yield_fixture_cleans_up_temporary_file(result_file: Path) -> None:
    assert result_file.read_text(encoding="utf-8") == "done"
