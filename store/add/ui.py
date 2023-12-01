import PySimpleGUI as sg
from states import get_name_list
name_label = sg.Text("Store name")
name_text = sg.Input(key='name')
num_label = sg.Text("Store number")
num_text = sg.Input(key='num')
add_1_label = sg.Text("Address line 1")
add_1_text = sg.Input(key='add 1')
add_2_label = sg.Text("Address line 2")
add_2_text = sg.Input(key='add 2')
city_label = sg.Text("City")
city_text = sg.Input(key='city')
state_label = sg.Text("State")
state_combo = sg.Combo(get_name_list(True),default_value='Select state',readonly=True,key='state')
zip_label = sg.Text("Zip code")
zip_text = sg.Input(size=(5),key='zip')
add_button = sg.Button("Add store",key='add')
cancel_button = sg.Cancel()

layout = [
    [name_label,name_text],
    [num_label,num_text],
    [add_1_label,add_1_text],
    [add_2_label,add_2_text],
    [city_label,city_text],
    [state_label,state_combo],
    [zip_label,zip_text],
    [add_button,cancel_button]
]

window = sg.Window("Add store",layout,enable_close_attempted_event=True,finalize=True)
window.hide()