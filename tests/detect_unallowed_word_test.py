from detect_unallowed_word import detect_unallowed_word


def test_unallowed_word_detection():
    sentence = "This is a way to hack the system"
    result = detect_unallowed_word(sentence)
    assert result is True


def test_no_unallowed_word():
    sentence = "whack the serial killer"
    result = detect_unallowed_word(sentence)
    assert result is False


def test_special_characters_replacement():
    sentence = "He is a h@cker"
    result = detect_unallowed_word(sentence)
    assert result is True


def test_case_insensitivity():
    sentence = "Fu*k YOU, bitches"
    result = detect_unallowed_word(sentence)
    assert result is True
