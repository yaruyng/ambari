#!/usr/bin/env python3
from apscheduler.util import convert_to_datetime


class SimpleTrigger(object):
    def __init__(self, run_date):
        self.run_date = convert_to_datetime(run_date)

    def get_next_fire_time(self, start_date):
        if self.run_date >= start_date:
            return self.run_date

    def __str__(self):
        return f'date[{str(self.run_date)}]'

    def __repr__(self):
        return f'<{self.__class__.__name__} (run_date={repr(self.run_date)})>'
