import birdseye.trace_module_deep
import item.add.ui as ui
from db_sqlite import brand_check
from PySimpleGUI import popup

def win_read(event,value:dict):
    if event == 'upc' and len(value.get('upc')) == 11:
        brand = brand_check(value.get('upc'))
    elif event == 'add':
        brand = value.get('brand')
        if brand == 'Choose Brand':
            brand = ''
        else:
            add_brand(brand)
        if field_check(value.get('upc'),value.get('desc')) == True:
            from _global import item,current_item
            current_item = item(value.get('desc'),value.get('upc'),value.get('alt'),value.get('num'),brand,value.get('size'),value.get('units'))
            popup(current_item.get_descript_display())
            popup(current_item.get_upc())
            popup(current_item.get_brand())
    elif event == 'Cancel':
        exit()


def field_check(upc:str,desc:str):
    if upc == "" or desc == "":
        popup("UPC and Description are required")
        return False
    return True

def add_brand(brand):
    