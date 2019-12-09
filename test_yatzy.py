from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_total_score():
    assert 15 == Yatzy.total_score(2, 3, 4, 5, 1)
    assert 16 == Yatzy.total_score(3, 3, 4, 5, 1)


def test_yatzy():
    assert 50 == Yatzy.yatzy([6, 6, 6, 6, 6])
    assert 0 == Yatzy.yatzy([6, 6, 6, 6, 3])


def test_ones():
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)


def test_twos():
    assert 0 == Yatzy.twos(1, 4, 3, 5, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)


def test_threes():
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 0 == Yatzy.threes(2, 5, 1, 6, 4)


def test_fours():
    assert 0 == Yatzy(3, 1, 6, 5, 5).fours()
    assert 4 == Yatzy(4, 5, 5, 5, 5).fours()


def test_fives():
    assert 10 == Yatzy(4, 4, 4, 5, 5).fives()
    assert 0 == Yatzy(4, 4, 4, 2, 6).fives()
    assert 20 == Yatzy(4, 5, 5, 5, 5).fives()


def test_sixes():
    assert 0 == Yatzy(4, 4, 4, 5, 5).sixes()
    assert 6 == Yatzy(4, 4, 6, 5, 5).sixes()
    assert 18 == Yatzy(6, 5, 6, 6, 5).sixes()


def test_one_pair():
    assert 6 == Yatzy.one_pair(3, 4, 3, 5, 6)
    assert 0 == Yatzy.one_pair(3, 2, 6, 5, 4)
    assert 12 == Yatzy.one_pair(5, 3, 6, 6, 5)


def test_two_Pair():
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)


def test_three_pair():
    assert 9 == Yatzy.three_pair(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_pair(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_pair(3, 3, 3, 3, 5)


def test_four_pair():
    assert 12 == Yatzy.four_pair(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_pair(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_pair(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_pair(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
