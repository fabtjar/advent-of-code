lines = []
with open('input.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace(' b', '#b')
        line = line.replace('-', '')
        line = line.replace(':', '')
        line = line.replace(' ', '')
        line = line.replace('[', '')
        line = line.replace(']', ' ')
        lines.append(line)

lines.sort()
guards = {}

for line in lines:
    check_guard = line.split('#')
    if len(check_guard) > 1:
        guard = check_guard[1]
        if guard not in guards:
            guards[guard] = {}
            guards[guard]['sleep'] = {}
            guards[guard]['total_sleep'] = 0
    elif line.split(' ')[1] == 'fallsasleep':
        sleep = int(line.split(' ')[0][-2:])
    elif line.split(' ')[1] == 'wakesup':
        wake = int(line.split(' ')[0][-2:])
        guards[guard]['total_sleep'] += wake - sleep
        for i in range(sleep, wake):
            time = str(i)
            if time not in guards[guard]['sleep']:
                guards[guard]['sleep'][time] = 0
            guards[guard]['sleep'][time] += 1

most_sleep = 0
for guard in guards:
    for time, sleep in guards[guard]['sleep'].items():
        if sleep >= most_sleep:
            most_sleep = sleep
            sleep_time = time
            sleep_guard = guard
print('{} x {} = {}'.format(sleep_guard, sleep_time, int(sleep_guard) * int(sleep_time)))
