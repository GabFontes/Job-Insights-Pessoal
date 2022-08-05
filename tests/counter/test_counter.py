from src.counter import count_ocurrences


def test_counter():
    word_count = count_ocurrences("src/jobs.csv", "Python")
    assert type(word_count) == int
    assert word_count == 1639
    word_count = count_ocurrences("src/jobs.csv", "python")
    assert type(word_count) == int
    assert word_count == 1639
    word_count = count_ocurrences("src/jobs.csv", "zero")
    assert type(word_count) == int
    assert word_count == 14
