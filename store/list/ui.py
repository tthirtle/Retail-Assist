import PySimpleGUI as sg

store_table = sg.Table([],['Store name','Store number'],col_widths=[35,14],auto_size_columns=False)

add_button = sg.Button("Add store",key='add')
edit_button = sg.Button("Edit store",key='edit')
del_button = sg.Button("Delete store",key='del')
menu_button = sg.Button("Back to menu",key='menu')

button_col_layout = [
    [add_button],
    [edit_button],
    [del_button],
    [menu_button]
]

button_col = sg.Column(button_col_layout)

window_layout = [
    [store_table,button_col]
]

window = sg.Window('Stores',window_layout,enable_close_attempted_event=True)
