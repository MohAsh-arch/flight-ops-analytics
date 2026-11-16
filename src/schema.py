import re

def get_header_names(spark, path, expected_count=109):
    names = spark.read.csv(path, header=True).columns
    if re.fullmatch(r"_c\d+", names[-1]):
        names = names[:-1]
    if len(names) != expected_count:
        raise ValueError(f"expected {expected_count} columns, found {len(names)} in {path}")
    return names