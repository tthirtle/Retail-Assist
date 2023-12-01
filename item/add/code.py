import item.add.ui as ui
import csv

def win_read(event,value):
    if event == 'upc' and len(value.get('upc')) == 11:
        brand_check(value.get('upc'))

def brand_check(upc):
    codes = []
    brand = ''
