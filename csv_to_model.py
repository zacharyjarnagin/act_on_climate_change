#!/usr/bin/env python
"""
Convert politician csv data to models
"""

import csv
from climateapp.models import  Politician

CSV_PATH = 'rep_contact_info.csv'

with open(CSV_PATH, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        Politician.objects.create(state=row[0], name=row[1], phone_number=row[2])
