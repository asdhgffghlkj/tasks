def is_kebab_case(string: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the string spelled in kebab-case or not
    More info: https://en.wikipedia.org/wiki/Letter_case#Kebab_case
    :param string: Sequence of symbols to check on kebab-case
    :param allow_one_word: Flag to determine one-word string as correct kebab-case string
    """
    pass


if __name__ == "__main__":
    # Positive cases
    assert is_kebab_case("kebab")
    assert is_kebab_case("kebab-case")
    assert is_kebab_case("kebab-case", allow_one_word=False)
    assert is_kebab_case("upper-intermediate")
    assert is_kebab_case("the-quick-brown-fox-jumps-over-the-lazy-dog")
    assert is_kebab_case("semi-auto")

    # Negative cases
    assert not is_kebab_case("kebab", allow_one_word=False)
    assert not is_kebab_case("CamelCase")
    assert not is_kebab_case("lowerCamelCase")
    assert not is_kebab_case("not-kebab-case-")
    assert not is_kebab_case("-not-kebab-case")
    assert not is_kebab_case("not--kebab-case")
    assert not is_kebab_case("also_not-kebab-case")
    assert not is_kebab_case("also,not-kebab-case")
