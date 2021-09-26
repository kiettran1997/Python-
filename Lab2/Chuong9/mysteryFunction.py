def mystery_function(values):
    result = []
    for sublist in values:
        result.append([sublist[0]])
    for i in sublist[1:]:
        result[-1].insert(0, i)
    return result