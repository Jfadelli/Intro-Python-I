import sys
import calendar
from datetime import datetime

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-month', help='user inputted month value', type=int)
parser.add_argument('-year', help='user inputted year value', type=int)
args = parser.parse_args()
cal = calendar.TextCalendar()

if args.month and args.year:
  y = args.year
  m = args.month
  cal.prmonth(y, m)

elif args.month and not args.year:
  today = datetime.today()
  y = today.year
  m = args.month
  cal.prmonth(y, m)

elif not args.month and not args.year:
  today = datetime.today()
  y = today.year
  m = today.month
  cal.prmonth(y, m)

else: 
  print('please format your input as follows.. eg: python 14_cal.py -month M -year Y ')
