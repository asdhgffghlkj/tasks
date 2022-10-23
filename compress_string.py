def compress_string(string: str) -> str:
    """
    Сжимает строку, заменяя последовательно идущие одинаковые символы на их количество и один символ
    :param string: Строка, которую необходимо сжать
    :return: Сжатая строка
    """
    pass


if __name__ == "__main__":
    assert compress_string("a") == "a"
    assert compress_string("ab") == "ab"
    assert compress_string("aa") == "2a"
    assert compress_string("aab") == "2ab"
    assert compress_string("aaa") == "3a"
    assert compress_string("abca") == "abca"
    assert compress_string("aaabaaabaaa") == "3ab3ab3a"
    assert compress_string("aaa_baaa_baaa") == "3a_b3a_b3a"
    assert compress_string("22") == "22"
    assert compress_string("222") == "32"
