import sqlite3
import PySimpleGUI as sg
from datetime import date

con = sqlite3.connect("Car_Rent.sqlite")



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Εισάγετε Ενοικίαση')],
            [sg.Text('Πραγματική Ημ. Παραλαβής', size=(20,	1)), sg.InputText()],
            [sg.Text('Πραγματική Ημ. Παράδοσης', size=(20,	1)), sg.InputText()],
            [sg.Text('Ημ. Ακύρωσης', size=(20,	1)), sg.InputText()],
            [sg.Text('Ημ. Παραλαβής', size=(20,	1)), sg.InputText()],
            [sg.Text('Ημ. Παράδοσης', size=(20,	1)), sg.InputText()],
            [sg.Text('Έκπτωση', size=(20,	1)), sg.InputText()],
            [sg.Text('ID Πελάτη', size=(20,	1)), sg.InputText()],
            [sg.Text('Όνομα Ασφάλειας', size=(20,	1)), sg.InputText()],
            [sg.Text('Τύπος Οχήματος', size=(20,	1)), sg.InputText()],
            [sg.Text('Κατάστημα Παραλαβής', size=(20,	1)), sg.InputText()],
            [sg.Text('Κατάστημα Παράδωσης', size=(20,	1)), sg.InputText()],
            [sg.Text('Κόστος', size=(20,	1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Εισάγετε Ενοικίαση', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('Πραγματική Ημ. Παραλαβής', values[0])
        print('Πραγματική Ημ. Παράδοσης', values[1])
        print('Ημ. Ακύρωσης', values[2])
        print('Ημ. Παραλαβής', values[3])
        print('Ημ. Παράδοσης', values[4])
        print('Έκπτωση', values[5])
        print('ID Πελάτη', values[6])
        print('Όνομα Ασφάλειας', values[7])
        print('Τύπος Οχήματος', values[8])
        print('Κατάστημα Παραλαβής', values[9])
        print('Κατάστημα Παράδωσης', values[10])
        print('Κόστος', values[11])
    con.execute('''INSERT INTO 
                Ενοικίαση(ΠραγματΗμΠαραλ, ΠραγματΗμΠαραδ, Ημ_Ακύρωσης, ΗμΠαραλαβής, ΗμΠαράδοσης, Έκπτωση, ID_πελάτη, Όνομα_Aσφάλειας, ID_Κατ_Αυτοκ, Παραλ_ID_Καταστ, Παραδ_ID_Καταστ, Κόστος) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (values[0], values[1], values[2], values[3], values[4], int(values[5]), int(values[6]), values[7], values[8], int(values[9]), int(values[10]), int(values[11])))								
    
    ID_EnCurs = con.cursor()
    ID_EnCurs.execute('''SELECT ID 
                FROM    Ενοικίαση
                WHERE   ID = (SELECT MAX(ID) FROM Ενοικίαση);''')

    ID_En = ID_EnCurs.fetchall()
    print('ID Ενοικίασης', ID_En[0][0])
    today = date.today()
    dtoday = today.strftime("%Y-%m-%d")
    print('Σημερινή Ημερομηνία', dtoday)
    
    con.execute('''INSERT INTO κάνει(Ημερομηνία, ID_πελάτη, ID_ενοικίασης ) VALUES (?, ?, ?);''', ( dtoday, int(values[6]), ID_En[0][0]))								
    
    
    con.commit()	
con.close()	

window.close()