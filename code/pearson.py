def pearson(ratinga, ratingb):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for k in ratinga:
        if k in ratingb:
            n += 1
            sum_xy += ratinga[k] * ratingb[k]
            sum_x += ratinga[k]
            sum_y += ratingb[k]
            sum_x2 = ratinga[k]**2
            sum_y2 = ratingb[k]**2
    denominator = sqrt(sum_x2 - sum_x**2/n)*sqrt(sum_y2 - sum_y**2/n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - sum_x*sum_y/n)/denominator
