import sqlite3
import PySimpleGUI as sg
from datetime import date

con = sqlite3.connect("Car_Rent.sqlite")

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]


def chooseCar(CarType, RentID):
    print(RentID)
    print(CarType)
    
    car_C = con.cursor()
    car_C.execute('''SELECT *
                    FROM   Αυτοκίνητο
                    WHERE  Αυτοκίνητο.ID_τύπος_αυτοκινήτου = '%s';''' % CarType)
    chunk_size = 1
    car = car_C.fetchall()
    Carlist = list(split(car, chunk_size))
    layout = [  [sg.Text('Όλα τα διαθέσιμα αυτοκίνητα')],
                [sg.Text('ID | Μάρκα | Μοντέλο | Χλμ | Κυβικά | ΗμΑγοράς | Πινακίδες | CO2_Εκπομπές | Αριθμός_Πλαισίου | ID_τύπος_αυτοκινήτου | ID_Καταστήματος | Κατασταση_Σερβις')],
                [sg.Listbox(Carlist, no_scrollbar=False,  size=(170, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε ένα αυτοκίνητο επιλέγοντας το ID του', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Επέλεξε αυτοκίνητο', layout)
    
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            
            con.execute('''INSERT INTO 
                    Παρέχει(Χλμ_πριν, ID_ενοικίασης, ID_αυτοκινήτου) 
                    VALUES (?, ?, ?);''', (car[0][3], RentID, values[0]))								
            print('Στην ενοικίαση:', RentID)
            print('Προστέθηκε το αμάξι', values[0])
            print('Που τα χλμ εκίνησης ήταν', car[0][3])

        con.commit()	
    con.close()	

    window.close()


def main():
    
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Εισάγετε Ενοικίαση')],
                [sg.Text('Ημ. Παραλαβής', size=(20,	1)), sg.InputText()],
                [sg.Text('Ημ. Παράδοσης', size=(20,	1)), sg.InputText()],
                [sg.Text('Έκπτωση', size=(20,	1)), sg.InputText()],
                [sg.Text('ID Πελάτη', size=(20,	1)), sg.InputText()],
                [sg.Text('Όνομα Ασφάλειας', size=(20,	1)), sg.InputText()],
                [sg.Text('Τύπος Οχήματος', size=(20,	1)), sg.InputText()],
                [sg.Text('Κατάστημα Παραλαβής', size=(20,	1)), sg.InputText()],
                [sg.Text('Κατάστημα Παράδωσης', size=(20,	1)), sg.InputText()],
                
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Εισάγετε Ενοικίαση', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Ημ. Παραλαβής', values[0])
            print('Ημ. Παράδοσης', values[1])
            print('Έκπτωση', values[2])
            print('ID Πελάτη', values[3])
            print('Όνομα Ασφάλειας', values[4])
            print('Τύπος Οχήματος', values[5])
            print('Κατάστημα Παραλαβής', values[6])
            print('Κατάστημα Παράδωσης', values[7])
        con.execute('''INSERT INTO 
                    Ενοικίαση(ΗμΠαραλαβής, ΗμΠαράδοσης, Έκπτωση, ID_πελάτη, Όνομα_Aσφάλειας, ID_Κατ_Αυτοκ, Παραλ_ID_Καταστ, Παραδ_ID_Καταστ) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', (values[0], values[1], int(values[2]), int(values[3]), values[4], values[5], int(values[6]), int(values[7])))								
        
        ID_EnCurs = con.cursor()
        ID_EnCurs.execute('''SELECT ID 
                    FROM    Ενοικίαση
                    WHERE   ID = (SELECT MAX(ID) FROM Ενοικίαση);''')

        
        ID_En = ID_EnCurs.fetchall()   
        
        print('ID Ενοικίασης', ID_En[0][0])
        today = date.today()
        dtoday = today.strftime("%Y-%m-%d")
        print('Σημερινή Ημερομηνία', dtoday)
        
        con.execute('''INSERT INTO κάνει(Ημερομηνία, ID_πελάτη, ID_ενοικίασης ) VALUES (?, ?, ?);''', ( dtoday, int(values[3]), ID_En[0][0]))								
        
        con.commit()	
        chooseCar(values[5], ID_En[0][0])
    con.close()	

    window.close()


if __name__ == "__main__":
    main()
