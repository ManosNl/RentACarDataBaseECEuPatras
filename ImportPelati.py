import sqlite3
import PySimpleGUI as sg

con = sqlite3.connect("Car_Rent.sqlite")



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Εισάγετε Πελάτη')],
            [sg.Text('Όνομα', size=(12,	1)), sg.InputText()],
            [sg.Text('Επίθετο', size=(12,	1)), sg.InputText()],
            [sg.Text('Δίπλωμα', size=(12,	1)), sg.InputText()],
            [sg.Text('Φύλο', size=(12,	1)), sg.InputText()],
            [sg.Text('Τηλέφωνο', size=(12,	1)), sg.InputText()],
            [sg.Text('Ημερομηνία Γέννησης', size=(12,	1)), sg.InputText()],
            [sg.Text('Email', size=(12,	1)), sg.InputText()],
            [sg.Text('ΑΦΜ', size=(12,	1)), sg.InputText()],
            [sg.Text('Πιστ Κάρτα', size=(12,	1)), sg.InputText()],
            [sg.Text('Λογαριασμός Τραπέζης', size=(12,	1)), sg.InputText()],
            [sg.Text('Δ/ση Μονιμης Κατ.', size=(12,	1)), sg.InputText()],
            [sg.Text('Status Πελάτη', size=(12,	1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Εισάγετε Πελάτη', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('Όνομα', values[0])
        print('Επίθετο', values[1])
        print('Δίπλωμα', values[2])
        print('Φύλο', values[3])
        print('Τηλέφωνο', values[4])
        print('Ημερομηνία Γέννησης', values[5])
        print('Email', values[6])
        print('ΑΦΜ', values[7])
        print('Πιστ Κάρτα', values[8])
        print('Λογαριασμός Τραπέζης', values[9])
        print('Δ/ση Μονιμης Κατ.', values[10])
        print('Status Πελάτη', values[11])
    con.execute('''INSERT INTO Πελάτης(όνομα, Επίθετο, Δίπλωμα, Φύλο, Τηλέφωνο, DoB, email, ΑΦΜ, Πιστ_Κάρτα, ΛογαριασμόςΤραπέζης, Δνση_Μόνιμης_Κατ, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (values[0], values[1], int(values[2]), values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11]))								
    con.commit()	
con.close()	

window.close()