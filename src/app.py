def get_greeting(name: str = "World") -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(get_greeting())
    print(get_greeting("Alice"))
    print(add(2, 3))


if __name__ == "__main__":
    main()
