from src.jobs import read


def get_unique_job_types(path):
    list_all = read(path)
    job_types = set()

    for job in list_all:
        if job["job_type"] != "":
            job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return[item for item in jobs if item["job_type"] == job_type]
    # Que linha de código horrorosa, pelo amor!


def get_unique_industries(path):
    list_all = read(path)
    industry_types = set()

    for job in list_all:
        if job["industry"] != "":
            industry_types.add(job["industry"])
    return list(industry_types)


def filter_by_industry(jobs, industry):
    return[item for item in jobs if item["industry"] == industry]


def get_max_salary(path):
    list_all = read(path)
    max_salaries = []

    for job in list_all:
        if job["max_salary"].isnumeric():
            max_salaries.append(int(job["max_salary"]))
    return max(max_salaries)


def get_min_salary(path):
    list_all = read(path)
    min_salaries = []

    for job in list_all:
        if job["min_salary"].isnumeric():
            min_salaries.append(int(job["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job, salary):  # feio, porém inteligível
    try:
        if(job["min_salary"] > job["max_salary"]):
            raise ValueError(
                "Salário mínimo não pode ser maior que salário máximo")

        elif(
                type(job["min_salary"]) != int
                or type(job["max_salary"]) != int
                or type(salary) != int
                ):
            raise ValueError("Um dos termos não é um número")

        return job["min_salary"] <= salary <= job["max_salary"]  # True

    except(KeyError, TypeError):
        raise ValueError


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
    return []
