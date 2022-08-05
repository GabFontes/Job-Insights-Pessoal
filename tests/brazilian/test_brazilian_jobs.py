from src.brazilian_jobs import read_brazilian_file
from expected_brazilian_jobs_value import expected_values


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    mock = expected_values()
    assert type(dict_jobs) == list
    assert dict_jobs == mock
    assert len(dict_jobs) == 15
    for job in dict_jobs:
        if 'title' in job and 'salary' in job and 'type' in job:
            expected_keys = True
    assert expected_keys is True
