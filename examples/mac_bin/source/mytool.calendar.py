#pip install ics
#pip install pytz
import datetime
from ics import Calendar, Event
import argparse
import pytz
from argparse import RawTextHelpFormatter

def generate_reminders(title, start_date, end_date, schedule, time):
    c = Calendar()
    current_date = start_date
    end_date += datetime.timedelta(days=1)  # Include the end date

    sgt = pytz.timezone('Asia/Singapore')

    while current_date < end_date:
        if schedule == 'daily':
            if current_date.weekday() < 5:  # Skip weekends (Saturday and Sunday)
                e = Event()
                e.name = title
                event_datetime = sgt.localize(datetime.datetime.combine(current_date, time))
                e.begin = event_datetime
                e.duration = datetime.timedelta(minutes=15)  # Set the duration of the reminder
                c.events.add(e)
        elif schedule == 'every_other_day':
            if current_date.weekday() < 5 and (current_date - start_date).days % 2 == 0:  # Skip weekends and alternate days
                e = Event()
                e.name = title
                event_datetime = sgt.localize(datetime.datetime.combine(current_date, time))
                e.begin = event_datetime
                e.duration = datetime.timedelta(minutes=15)  # Set the duration of the reminder
                c.events.add(e)
        elif schedule == 'weekly':
            if current_date.weekday() < 5 and current_date.weekday() == start_date.weekday():  # Skip weekends and occur on the same weekday as start date
                e = Event()
                e.name = title
                event_datetime = sgt.localize(datetime.datetime.combine(current_date, time))
                e.begin = event_datetime
                e.duration = datetime.timedelta(minutes=15)  # Set the duration of the reminder
                c.events.add(e)
        elif schedule == 'weekend':
            if current_date.weekday() >= 5:  # Skip weekdays (Monday to Friday)
                e = Event()
                e.name = title
                event_datetime = sgt.localize(datetime.datetime.combine(current_date, time))
                e.begin = event_datetime
                e.duration = datetime.timedelta(minutes=15)  # Set the duration of the reminder
                c.events.add(e)

        current_date += datetime.timedelta(days=1)

    return c

if __name__ == '__main__':
    helptext = 'Generate weekly reminders in .ics format. for example: \npython mytool.task-ics.py "Meeting" "2023-07-12" "2023-07-20" every_other_day "14:30" reminder.ics \npython mytool.task-ics.py "Weekend IVF Info" "2023-07-12" "2023-08-30" weekend "14:30" reminder.ics'
    parser = argparse.ArgumentParser(description=helptext, formatter_class=RawTextHelpFormatter)
    parser.add_argument('title', type=str, help='Title of the reminder')
    parser.add_argument('start_date', type=str, help='Start date in YYYY-MM-DD format')
    parser.add_argument('end_date', type=str, help='End date in YYYY-MM-DD format')
    parser.add_argument('schedule', type=str, choices=['daily', 'every_other_day', 'weekly', 'weekend'], help='Schedule type')
    parser.add_argument('time', type=str, help='Time in HH:MM format')
    parser.add_argument('output_file', type=str, help='Output .ics file')

    args = parser.parse_args()

    try:
        start_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(args.end_date, '%Y-%m-%d')
        time = datetime.datetime.strptime(args.time, '%H:%M').time()

        c = generate_reminders(args.title, start_date, end_date, args.schedule, time)

        with open(args.output_file, 'w') as f:
            f.writelines(c)

        print(f'Successfully generated reminders in {args.output_file}')

    except ValueError as e:
        print(f'Error: {e}')


