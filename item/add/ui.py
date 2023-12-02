import PySimpleGUI as sg

brand_label = sg.Text('Brand')
brand_combo = sg.Combo([],'Choose Brand',size=(20),key='brand')

desc_label = sg.Text('Description')
desc_text = sg.Input(key='desc',tooltip='Human readable description')

alt_label = sg.Text('Alternate description')
alt_text = sg.Input(key='alt',tooltip='Shortend description\n30 characters max')

upc_label = sg.Text("Barcode")
upc_text = sg.Input(key='upc',tooltip='Product barcode usally UPC',enable_events=True)

num_label = sg.Text("Item number")
num_text = sg.Input(key='num',tooltip='Item number\nSeperate from the product barcode')

size_label = sg.Text("Size")
size_text = sg.Input(key='size',size=(5))
unit_combo = sg.Combo([],key='units',size=7)

add_button = sg.Button('Add item',key='add')
cancel_button = sg.Cancel()

layout = [
    [brand_label,brand_combo],
    [desc_label,desc_text],
    [alt_label,alt_text],
    [upc_label,upc_text],
    [num_label,num_text],
    [size_label,size_text,unit_combo],
    [add_button,cancel_button]
]

window = sg.Window('Add item',layout,finalize=True,enable_close_attempted_event=True)