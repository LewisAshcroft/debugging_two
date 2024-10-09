from lib.letter_counter import *

def test_two_words():
    counter = LetterCounter("Digital Punk")
    result = counter.calculate_most_common()
    assert result == [2, "i"]