import PySimpleGUI as sg
from _global import prog_logo

logo_img = sg.Image(prog_logo)
author_text = sg.Text("By: Thomas Thirtle")
license_text = sg.Text("Liscensed with GNU GPL3")

col_layout = [
    [logo_img],
    [author_text],
    [license_text]
]

col = sg.Column(col_layout,element_justification='center')

win_layout = [
    [col]
]

window = sg.Window('',win_layout)