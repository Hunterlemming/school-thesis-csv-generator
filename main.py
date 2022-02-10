import csv
from utils.generators.timeline import TimelineGenerator as tlg
from utils.generators.activity import ActivityGenerator as ag


FILE_LOCATION = './data/time-series.csv'


def get_random_increase(current_value: float) -> float:
    return 0


def generate_data():
    data = []
    for row in tlg.generate_timeline():
        row += ag.generate_random_activity()
        data.append(row)
    return data 


with open(FILE_LOCATION, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    data = generate_data()
    for line in data:
        writer.writerow(line)
