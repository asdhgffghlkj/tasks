def is_camel_case(string: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the string spelled in CamelCase or not
    More info: https://en.wikipedia.org/wiki/Camel_case
    :param string: Sequence of symbols to check on CamelCase
    :param allow_one_word: Flag to determine one-word string as correct CamelCase string
    """
    pass


if __name__ == "__main__":
    # Positive cases
    assert is_camel_case("Camel")
    assert is_camel_case("CamelCase")
    assert is_camel_case("CamelCase", allow_one_word=False)
    assert is_camel_case("ThreeWordsTest")
    assert is_camel_case("ALittleBitLongerExpression")
    assert is_camel_case("ParseDBMXML")
    assert is_camel_case("SQLServer")
    assert is_camel_case("ParseDbmXml")
    assert is_camel_case("SqlServer")

    # Negative cases
    assert not is_camel_case("camel")
    assert not is_camel_case("lowerCase")
    assert not is_camel_case("Camel", allow_one_word=False)
    assert not is_camel_case("_")
    assert not is_camel_case("VeryLongExpressionWithOneSmallTail_")
    assert not is_camel_case("WhatAboutQuestionMark?")
    assert not is_camel_case("AndWhatAboutSomeSpaces ")
    assert not is_camel_case("ByTheWay,whatAboutCommas")
    assert not is_camel_case("ByTheWay,WhatAboutCommas")
    assert not is_camel_case("wtf")
