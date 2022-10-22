def is_lower_camel_case(variable_name: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the string spelled in lowerCamelCase or not
    More info: https://en.wikipedia.org/wiki/Camel_case
    :param variable_name: String that represents correct variable name in Python
    :param allow_one_word: Flag to determine one-word string as correct lowerCamelCase string
    """
    pass


if __name__ == "__main__":
    # Positive cases
    assert is_lower_camel_case("camel")
    assert is_lower_camel_case("camelCase")
    assert is_lower_camel_case("camelCase", allow_one_word=False)
    assert is_lower_camel_case("threeWordsTest")
    assert is_lower_camel_case("aLittleBitLongerExpression")
    assert is_lower_camel_case("parseDBMXML")
    assert is_lower_camel_case("sQLServer")
    assert is_lower_camel_case("parseDbmXml")
    assert is_lower_camel_case("sqlServer")

    # Negative cases
    assert not is_lower_camel_case("Camel")
    assert not is_lower_camel_case("UpperCase")
    assert not is_lower_camel_case("camel", allow_one_word=False)
    assert not is_lower_camel_case("_")
    assert not is_lower_camel_case("__")
    assert not is_lower_camel_case("_id")
    assert not is_lower_camel_case("veryLongExpressionWithOneSmallTail_")
    assert not is_lower_camel_case("WTF")
