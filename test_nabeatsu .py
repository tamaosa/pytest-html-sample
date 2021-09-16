def is_aho(n: int) -> bool:
    """3の倍数と3のつく数字はあほになる。"""
    return n % 3 == 0


def test_aho_1():
    """
    Tests:
        1を入力する。
    Expects:
        あほにならないこと。
    """
    assert not is_aho(1)


def test_aho_2():
    """
    Tests:
        2を入力する。
    Expects:
        あほにならないこと。
    """
    assert not is_aho(2)


def test_aho_3():
    """
    Tests:
        3を入力する。
    Expects:
        あほになること。
    """
    assert is_aho(3)


def test_aho_9():
    """
    Tests:
        9を入力する。
    Expects:
        あほになること。
    """
    assert is_aho(9)


def test_aho_13():
    """
    Tests:
        13を入力する。
    Expects:
        あほになること。
    """
    assert is_aho(13)
