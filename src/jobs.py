import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf8") as jobs_file:
        list_all = []
        jobs_list = csv.DictReader(jobs_file, delimiter=",", quotechar='"')
        for job in jobs_list:
            list_all.append(job)
        return list_all
