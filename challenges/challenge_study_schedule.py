def study_schedule(permanence_period, target_time):

    permanence_students = 0
    # print(type(permanence_period), type(target_time))

    for period in permanence_period:
        if period[0] is None or period[1] is None or target_time is None:
            return None

        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        if period[0] <= target_time <= period[1]:
            permanence_students += 1

    return permanence_students


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 5

print(study_schedule(permanence_period, target_time))
