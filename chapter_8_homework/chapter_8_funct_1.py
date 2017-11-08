total_rainfalls = []
max_months = []
min_months = []

def get_rainfalls():
    for i in range(12):
        total_rainfalls.append(float(input('Enter rainfall for mouth %d:' % (i + 1))))

    return total_rainfalls

def cal_total_rainfall():
    total_rainfall = sum(total_rainfalls)

    return total_rainfall

def cal_avg_rainfall():
    avg_rainfall = cal_total_rainfall() / 12

    return avg_rainfall

def max_min_rainfall():
    max_month_val = max(total_rainfalls)

    position_max = 1
    position_min = 1

    for i in total_rainfalls:
        if i == max_month_val:
            max_months.append(position_max)
        position_max +=1

    min_month_val = min(total_rainfalls)

    for i in total_rainfalls:
        if i == min_month_val:
            min_months.append(position_min)
        position_min += 1
            
    return max_months, min_months

get_rainfalls()
max_min_rainfall()
print("""total rainfall: %f
Average monthly rainfall: %.2f
Highest rainfall month(s): %s
Lowest rainfall month(s): %s""" %(cal_total_rainfall(), cal_avg_rainfall(), max_months, min_months))
