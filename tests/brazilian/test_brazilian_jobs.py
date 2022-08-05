from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert type(dict_jobs) == list
    assert len(dict_jobs) == 15
    for job in dict_jobs:
        if 'title' in job and 'salary' in job and 'type' in job:
            expected_keys = True
    assert expected_keys is True
