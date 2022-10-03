from typing import Set


def find_alphabet(
        alphabet: Set[str],
        sentence: str
) -> str:
    found_symbols = set()
    found_sentence = []
    for symbol in sentence:
        if symbol not in found_symbols:
            found_symbols.add(symbol)
            if found_symbols == alphabet:
                found_sentence.append(symbol)
                return str(found_sentence)
        found_sentence.append(symbol)


if __name__ == "__main__":
    assert find_alphabet({"1", "2", "3", "4", "5"}, "12345") == "12345"
    assert find_alphabet({"1", "2", "3", "4", "5"}, "123454321") == "12345"
    assert find_alphabet({"1", "2", "3", "4", "5"}, "12134345") == "12134345"
