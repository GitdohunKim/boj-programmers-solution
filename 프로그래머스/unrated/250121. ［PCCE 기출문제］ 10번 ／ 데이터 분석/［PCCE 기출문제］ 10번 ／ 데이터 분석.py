def solution(data, ext, val_ext, sort_by):
    data_type = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    return sorted(filter(lambda x: x[data_type[ext]] < val_ext, data), key=lambda x: x[data_type[sort_by]])
