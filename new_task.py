def is_lower_camel_case(word: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the word spelled in lowerCamelCase or not
    More info: https://en.wikipedia.org/wiki/Camel_case
    """
    symblist = list(word)
    capcount = 0
    if symblist[0].isupper():
        return 0
    for i in range(len(symblist)):
        symbol = symblist[i]
        if symbol.isalpha():
            if symbol.isupper():
                capcount+=1
        else:
            return 0
    if capcount == 0:
        if allow_one_word==False:
            return 0
    return 1


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
    assert not is_lower_camel_case("veryLongExpressionWithOneSmallTail_")
    assert not is_lower_camel_case("whatAboutQuestionMark?")
    assert not is_lower_camel_case("andWhatAboutSomeSpaces ")
    assert not is_lower_camel_case("byTheWay,whatAboutCommas")
    assert not is_lower_camel_case("byTheWay,WhatAboutCommas")
    assert not is_lower_camel_case("WTF")
