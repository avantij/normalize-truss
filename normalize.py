#!/usr/bin/python3
import numpy as np 
import math
import pandas as pd
from datetime import datetime
import pytz 
import sys

class NormalizeCSV:
    def __init__(self, stdin_file):
        self.stdin_file = stdin_file
        self.data = None

    def normalize(self):
        self.read_csv()
        self.format_name()
        self.format_timestamp()
        self.format_zip_code()
        self.time_to_seconds("FooDuration")
        self.time_to_seconds("BarDuration")
        self.calc_total_duration()
        self.write_csv()

    def format_name(self):
        formatted_name_col = self.data['FullName'].str.upper()
        self.data['FullName'] = formatted_name_col

    def format_timestamp(self):
        formatted_timestamp_col = self.data['Timestamp'].map(self.helper_date_time)
        self.data['Timestamp'] = formatted_timestamp_col

    def helper_date_time(self, v):
        new_date = datetime.strptime(v, '%m/%d/%y %I:%M:%S %p')
        curr_timezone = pytz.timezone('US/Pacific')
        desired_timezone = pytz.timezone('US/Eastern')
        localized_time = curr_timezone.localize(new_date)
        updated_time = localized_time.astimezone(desired_timezone)
        final = updated_time.isoformat()
        return final

    def format_zip_code(self):
        formatted_zip_code_col = self.data['ZIP'].map(self.helper_zip_code)
        self.data['ZIP'] = formatted_zip_code_col

    def helper_zip_code(self, zip_code):
        if len(str(zip_code)) < 5:
            padded_zip = str(zip_code).zfill(5)
            return padded_zip
        return zip_code

    def time_to_seconds(self, col):
        self.data[col] = pd.to_timedelta(self.data[col]).dt.total_seconds()
        self.data[col] = self.data[col].round(decimals=0)

    def calc_total_duration(self):
        foo_bar_sum = self.data["FooDuration"] + self.data["BarDuration"]
        self.data["TotalDuration"] = foo_bar_sum

    def read_csv(self):
        self.data = pd.read_csv(self.stdin_file, encoding='utf-8')

    def write_csv(self):
        self.data.to_csv(sys.stdout, index=False)
