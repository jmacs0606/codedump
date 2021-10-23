# img_viewer.py

import PySimpleGUI as sg
import os.path

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Please enter a subreddit to begin scanning for data:"),
        sg.Input(size=(25, 1), enable_events=True, key="-Input-"),
        sg.Button("Enter")
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]


data_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(80, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(data_viewer_column),
    ]
]

window = sg.Window("Intelligent Algorithms from Mimifur", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder


window.close()
