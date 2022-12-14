from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_dict = read(path)
    job_types = []
    for job in jobs_dict:
        job_types.append(job["job_type"])
    return [*set(job_types)]


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    job_by_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_by_type.append(job)
    return job_by_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_dict = read(path)
    job_industries = []
    for job in jobs_dict:
        if job["industry"] != '':
            job_industries.append(job["industry"])
    return [*set(job_industries)]


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    job_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            job_by_industry.append(job)
    return job_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_dict = read(path)
    salaries = []
    for job in jobs_dict:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_dict = read(path)
    salaries = []
    for job in jobs_dict:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError("'max_salary' or 'min_salary' is undefined")

    elif (type(job["max_salary"]) is not int or
            type(job["min_salary"]) is not int):
        raise ValueError("'max_salary' or 'min_salary' is not an integer")

    elif type(salary) is not int:
        raise ValueError("'salary' is not an integer")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("'min_salary' is higher than 'max_salary'")

    min_salary = job['min_salary']
    max_salary = job['max_salary']

    return salary in range(min_salary, max_salary)


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except ValueError:
            print('ValueError')
    return jobs_by_salary_range
