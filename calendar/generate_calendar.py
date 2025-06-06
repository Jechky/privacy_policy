import csv
from datetime import datetime
from pathlib import Path


def load_events(csv_path: Path):
    events = {}
    with csv_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['Date']
            events.setdefault(date, []).append(row)
    return events


def print_calendar(events):
    for date in sorted(events.keys()):
        print(date)
        for event in events[date]:
            print(f"  {event['Time']} - {event['Event']}")
        print()


def main():
    data_file = Path(__file__).resolve().parent / 'us_high_impact_events.csv'
    events = load_events(data_file)
    print_calendar(events)


if __name__ == '__main__':
    main()
