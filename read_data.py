def read_data(filepath, enemy_times, enemy_lanes, enemy_types):
    file = open(filepath)
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        splitted = line.split('\t')
        start_time_seconds = float(splitted[0])
        lane_number = int(splitted[1])
        enemy_type = str(splitted[2])

        enemy_times.append(start_time_seconds)
        # -1 for offset so when we annotate with
        # c = 1, d = 2, etc.
        enemy_lanes.append(lane_number - 1)
        enemy_types.append(enemy_type)