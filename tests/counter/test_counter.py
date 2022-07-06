from src.counter import count_ocurrences


def test_counter():
    total_senior = count_ocurrences("src/jobs.csv", "senior")

    assert count_ocurrences("src/jobs.csv", "Senior") == count_ocurrences(
        "src/jobs.csv", "senior")

    assert total_senior == 1791
