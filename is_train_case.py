def is_train_case(string: str, allow_one_word: bool = True) -> bool:
    """
    Determine if the string spelled in TRAIN-CASE or not
    More info: https://en.wikipedia.org/wiki/Letter_case#Kebab_case
    :param string: Sequence of symbols to check on TRAIN-CASE
    :param allow_one_word: Flag to determine one-word string as correct TRAIN-CASE string
    """
    pass


if __name__ == "__main__":
    # Positive cases
    assert is_train_case("TRAIN")
    assert is_train_case("TRAIN-CASE")
    assert is_train_case("TRAIN-CASE", allow_one_word=False)

    # Negative cases
    assert not is_train_case("TRAIN", allow_one_word=False)
    assert not is_train_case("CamelCase")
    assert not is_train_case("lowerCamelCase")
    assert not is_train_case("TRAIN-CASE_")
    assert not is_train_case("NOT-TRAIN-CASE-")
    assert not is_train_case("-NOT-TRAIN-CASE")
    assert not is_train_case("NOT--TRAIN-CASE")
    assert not is_train_case("NOT-TRAIN--CASE")
    assert not is_train_case("TRAIN_UNDERSCOPE_CASE")
    assert not is_train_case("snake")
    assert not is_train_case("snake_case")
    assert not is_train_case("snake_case", allow_one_word=False)
    assert not is_train_case("lower_case_with_underscores")
    assert not is_train_case("CamelCase")
    assert not is_train_case("PowerPoint")
    assert not is_train_case("JetBrains")
    assert not is_train_case("PyCharm")
    assert not is_train_case("PyCharm2022")
    assert not is_train_case("ThreeWordsTest")
    assert not is_train_case("ALittleBitLongerExpression")
    assert not is_train_case("ParseDBMXML")
    assert not is_train_case("SQLServer")
    assert not is_train_case("ParseDbmXml")
    assert not is_train_case("SqlServer")
    assert not is_train_case("NewYork2022")
