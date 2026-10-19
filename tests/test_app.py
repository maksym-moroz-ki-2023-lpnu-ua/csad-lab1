from src.app import add, get_greeting


def test_get_greeting_default() -> None:
    assert get_greeting() == "Hello, World!"


def test_get_greeting_custom_name() -> None:
    assert get_greeting("Alice") == "Hello, Alice!"


def test_add() -> None:
    # assert add(2, 3) == 999  # РОЗКОМЕНТУЙ ДЛЯ ТЕСТУ ЗЛАМАНОЇ ПЕРЕВІРКИ
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
