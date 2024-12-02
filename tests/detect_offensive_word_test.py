from detect_offensive_word import detect_offensive_word


def test_offensive_word_detection():
    sentence = "How ugly She is"
    result = detect_offensive_word(sentence)
    assert result is True


def test_no_offensive_word():
    sentence = "She is a beautiful girl with blue eyes"
    result = detect_offensive_word(sentence)
    assert result is False
