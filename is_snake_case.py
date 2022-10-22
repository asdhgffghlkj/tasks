def is_snake_case(string: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the string spelled in snake_case or not
    More info: https://en.wikipedia.org/wiki/Snake_case
    :param string: Sequence of symbols to check on snake_case
    :param allow_one_word: Flag to determine one-word string as correct snake_case string
    """
    pass


if __name__ == "__main__":
    # Positive cases
    assert is_snake_case("snake")
    assert is_snake_case("snake_case")
    assert is_snake_case("snake_case", allow_one_word=False)
    assert is_snake_case("lower_case_with_underscores")

    # Negative cases
    assert not is_snake_case("snake", allow_one_word=False)
    assert not is_snake_case("CamelCase")
    assert not is_snake_case("lowerCamelCase")
    assert not is_snake_case("kebab-case")
    assert not is_snake_case("not_snake-case")
