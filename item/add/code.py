import item.add.ui as ui
from db_sqlite import brand_check

def win_read(event,value):
    if event == 'upc' and len(value.get('upc')) == 11:
        brand_check(value.get*)