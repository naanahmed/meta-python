def sum_of(**kwargs):
    sum = 0;
    for x, y in kwargs.items():
        sum +=x
    return round(sum, 2);

