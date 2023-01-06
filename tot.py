import sqlite3
import PySimpleGUI as sg
from random import choice
from datetime import date

con = sqlite3.connect("Car_Rent.sqlite")

def ImportClient():
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
    window.close()

def ImportRental():
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
    window.close()

def ImportCrash():

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Εισάγετε Ζημιά')],
                [sg.Text('Ημερομηνία', size=(20,	1)), sg.InputText()],
                [sg.Text('Κόστος', size=(20,	1)), sg.InputText()],
                [sg.Text('Περιγραφή', size=(20,	1)), sg.InputText()],
                [sg.Text('ID αυτοκινήτου', size=(20,	1)), sg.InputText()],
                [sg.Text('ID ενοικίασης', size=(20,	1)), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Εισάγετε Ζημιά', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Ημερομηνία', values[0])
            print('Κόστος', values[1])
            print('Περιγραφή', values[2])
            print('ID αυτοκινήτου', values[3])
            print('ID ενοικίασης', values[4])
        con.execute('''INSERT INTO 
                    Ζημιά(Ημερομηνία, Κόστος, Περιγραφή, ID_Αυτοκίνητο, ID_Ενοικίαση) 
                    VALUES (?, ?, ?, ?, ?);''', (values[0], values[1], values[2], values[3], values[4]))								
    
        con.commit()		
    window.close()

def ChooseClient():
    sg.theme('DarkAmber')   # Add a touch of color
    layout = [ [sg.Button("Όλοι οι Πελάτες", key="open", size=(20,	1))]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            allClients()
    window.close()

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def UpdateClientvalues(ClientID):
    print(ClientID)
    print("updating client")
    Rent = con.cursor()
    Rent.execute('''SELECT *
                    FROM   Πελάτης 
                    where ID='%s';''' % ClientID)
    Rent_info = Rent.fetchall()



    # All the stuff inside your window.
    layout = [  [sg.Text('Ο Πελάτης %s' % ClientID)],
               
                [sg.Text('Ονομα Πελάτη: %s' % Rent_info[0][1])],
                [sg.InputText()],
                [sg.Text('Επώνυμο Πελάτη: %s' %  Rent_info[0][2])],
                [sg.InputText()],
                [sg.Text('Αριθμός Διπλώματος: %s' % Rent_info[0][3])],
                [sg.InputText()],
                [sg.Text('Φύλο: %s' % Rent_info[0][4])],
                [sg.InputText()],
                [sg.Text('Τηλέφωνο: %s' % Rent_info[0][5])],
                [sg.InputText()],
                [sg.Text('Ημερομηνία Γεννήσεως: %s' % Rent_info[0][6])],
                [sg.InputText()],
                [sg.Text('email: %s' % Rent_info[0][7])],
                [sg.InputText()],
                [sg.Text('ΑΦΜ: %s' % Rent_info[0][8])],
                [sg.InputText()],
                [sg.Text('Πιστωτική Κάρτα: %s' % Rent_info[0][9])],
                [sg.InputText()],
                [sg.Text('Λογαριασμός Τράπεζας: %s' % Rent_info[0][10])],
                [sg.InputText()],
                [sg.Text('Διέυθνυση μόνιμης κατοικίας: %s' % Rent_info[0][11])],
                [sg.InputText()],
                [sg.Text('Status: %s' % Rent_info[0][12])],                
                [sg.InputText()],     

                [sg.Button('ok'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'ok':
            print('Όνομα Πελάτη', values[0])
            print('Επώνυμο Πελάτη', values[1])
            print('Αριθμός Διπλώματος', values[2])
            print('Φύλο', values[3])
            print('Τηλέφωνο', values[4])
            print('Ημερομηνία Γεννήσεως', values[5])
            print('email', values[6])
            print('ΑΦΜ', values[7])
            print('Πιστωτική Κάρτα', values[8])
            print('Λογαριασμός Τράπεζας', values[9])
            print('Διέυθνυση μόνιμης κατοικίας', values[10])
            print('Status', values[11])
        
        if values[0] == '':
            values[0] = Rent_info[0][1]
        if values[1] == '':
            values[1] = Rent_info[0][2]
        if values[2] == '':
            values[2] = Rent_info[0][3]
        if values[3] == '':
            values[3] = Rent_info[0][4]
        if values[4] == '':
            values[4] = Rent_info[0][5]
        if values[5] == '':
            values[5] = Rent_info[0][6]
        if values[6] == '':
            values[6] = Rent_info[0][7]
        if values[7] == '':
            values[7] = Rent_info[0][8]
        if values[8] == '':
            values[8] = Rent_info[0][9]
        if values[9] == '':
            values[9] = Rent_info[0][10]
        if values[10] == '':
            values[10] = Rent_info[0][11]
        if values[11] == '':
            values[11] = Rent_info[0][12]
       

        con.execute('''UPDATE Πελάτης 
                       SET  όνομα = '%s', 
                            Επίθετο = '%s', 
                            Δίπλωμα = '%s', 
                            Φύλο = '%s', 
                            Τηλέφωνο = '%s', 
                            DoB = '%s', 
                            email = '%s', 
                            ΑΦΜ = '%s', 
                            Πιστ_Κάρτα = '%s', 
                            ΛογαριασμόςΤραπέζης = '%s',
                            Δνση_Μόνιμης_Κατ = '%s',
                            Status = '%s'
                       WHERE  Πελάτης.ID = '%s';''' % (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9],values[10],values[11],ClientID))								
           
        con.commit()	
   

    window.close()

def CarType(value):
    print(value)
    Rent = con.cursor()
    Rent.execute('''SELECT *
                    FROM  Τύπος_Οχήματος
                    WHERE Τύπος_Οχήματος.ID = '%s';''' % value)
    Rent_info = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Τύπος Οχήματος: %s' % value)],
               
                [sg.Text('Όνομα: %s' % Rent_info[0][1])],
                [sg.Text('Ημερήσιο Κόστος: %s€' % Rent_info[0][2])],
                [sg.Text('Χώρος αποσκευών: %s' % Rent_info[0][3])],
                [sg.Text('Κατάθεση Εγγύησης: %s€' % Rent_info[0][4])],
                [sg.Text('Ελάχιστη Ηλικία Οδήγησης: %s' % Rent_info[0][5])],
                [sg.Text('Αριθμός Επιβατών: %s' % Rent_info[0][6])],
                [sg.Text('Καύσισμο: %s' % Rent_info[0][7])],
                [sg.Text('Κλιματισμός: %s' % Rent_info[0][8])],
                [sg.Text('Κιβώτιο Ταχυτήτων: %s' % Rent_info[0][9])],
                
                [sg.Button('Cancel')],
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
    	
    window.close()

def showRent(value):
    print(value)
    Rent = con.cursor()
    Rent.execute('''SELECT Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ID, Ενοικίαση.ΠραγματΗμΠαραλ, 
                    Ενοικίαση.ΠραγματΗμΠαραδ, Ενοικίαση.Ημ_Ακύρωσης, Ενοικίαση.ΗμΠαραλαβής, Ενοικίαση.ΗμΠαράδοσης,
                    Ενοικίαση.Έκπτωση, Ενοικίαση.ID_πελάτη, Ενοικίαση.Όνομα_Aσφάλειας, Ενοικίαση.ID_Κατ_Αυτοκ,
                    Ενοικίαση.Παραλ_ID_Καταστ, Ενοικίαση.Παραδ_ID_Καταστ, Κόστος
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη
                    WHERE  Ενοικίαση.ID = '%s';''' % value)
    Rent_info = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Ασφάλεια
                    WHERE  Ασφάλεια.ID = '%s';''' % Rent_info[0][10])
    Insurance = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][12])
    Get_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][13])
    Give_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Παρέχει
                    WHERE  Παρέχει.ID_ενοικίασης = '%s';''' % value)
    Give_Car = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Αυτοκίνητο
                    WHERE  Αυτοκίνητο.ID = '%s';''' % Give_Car[0][3])
    CarT = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Η ενοικίαση:  %s' % value)],
               
                [sg.Text('Ονομα Πελάτη: %s' % Rent_info[0][0])],
                [sg.Text('Επώνυμο Πελάτη: %s' % Rent_info[0][1])],
                [sg.Text('Πραγματική Ημ. Παραλαβής: %s' % Rent_info[0][3])],
                [sg.Text('Πραγματική Ημ. Παράδοσης: %s' % Rent_info[0][4])],
                [sg.Text('Ημ. Ακύρωσης: %s' % Rent_info[0][5])],
                [sg.Text('Ημ. Παραλαβής: %s' % Rent_info[0][6])],
                [sg.Text('Ημ. Παράδοσης: %s' % Rent_info[0][7])],
                [sg.Text('Έκπτωση: %s' % Rent_info[0][8])],
                [sg.Text('ID Πελάτη: %s' % Rent_info[0][9])],
                [sg.Text('Όνομα Ασφάλειας: %s' % Rent_info[0][10])],
                [sg.Text('Η ασφάλεια καλύπτει: %s' % Insurance[0][1])],
                [sg.Text('Τύπος Οχήματος: %s' % Rent_info[0][11])],
                
                [sg.Button('Τύπος Οχήματος')],

                [sg.Text('Κατάστημα Παραλαβής: %s' % Get_Shop[0][1])],
                [sg.Text('Τηλ. Καταστήματος: %s' % Get_Shop[0][2])],
                [sg.Text('Κατάστημα Παράδωσης: %s' % Give_Shop[0][1])],
                [sg.Text('Τηλ. Καταστήματος: %s' % Give_Shop[0][2])],
                [sg.Text('Κόστος: %s€' % Rent_info[0][14])],
                
                [sg.Text('Αυτοκίνητο')],
                [sg.Text('Μάρκα: %s' % CarT[0][1])],
                [sg.Text('Μοντέλο: %s' % CarT[0][2])],
                [sg.Text('ΧΛΜ πριν: %s' % Give_Car[0][1])],
                [sg.Text('ΧΛΜ μετά: %s' % Give_Car[0][0])],
                
                [sg.Button('Αυτοκίνητο')],

                [sg.Button('Update'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Update':
            Updatevalues(value, Give_Car[0][3])
        if event == 'Τύπος Οχήματος':
            CarType(Rent_info[0][11])
        if event == 'Αυτοκίνητο':
            Car(Give_Car[0][3])
    	
    window.close()

def Updatevalues(RentID, CarID):
    print(RentID)
    print(CarID)
    Rent = con.cursor()
    Rent.execute('''SELECT Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ID, Ενοικίαση.ΠραγματΗμΠαραλ, 
                    Ενοικίαση.ΠραγματΗμΠαραδ, Ενοικίαση.Ημ_Ακύρωσης, Ενοικίαση.ΗμΠαραλαβής, Ενοικίαση.ΗμΠαράδοσης,
                    Ενοικίαση.Έκπτωση, Ενοικίαση.ID_πελάτη, Ενοικίαση.Όνομα_Aσφάλειας, Ενοικίαση.ID_Κατ_Αυτοκ,
                    Ενοικίαση.Παραλ_ID_Καταστ, Ενοικίαση.Παραδ_ID_Καταστ, Κόστος
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη
                    WHERE  Ενοικίαση.ID = '%s';''' % RentID)
    Rent_info = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Ασφάλεια
                    WHERE  Ασφάλεια.ID = '%s';''' % Rent_info[0][10])
    Insurance = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][12])
    Get_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][13])
    Give_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Παρέχει
                    WHERE  Παρέχει.ID_ενοικίασης = '%s';''' % RentID)
    Give_Car = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Αυτοκίνητο
                    WHERE  Αυτοκίνητο.ID = '%s';''' % Give_Car[0][3])
    CarT = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Η ενοικίαση %s' % RentID)],
               
                [sg.Text('Ονομα Πελάτη: %s' % Rent_info[0][0])],
                [sg.Text('Επώνυμο Πελάτη: %s' % Rent_info[0][1])],
                [sg.Text('Πραγματική Ημ. Παραλαβής: %s' % Rent_info[0][3])],
                [sg.InputText()],
                [sg.Text('Πραγματική Ημ. Παράδοσης: %s' % Rent_info[0][4])],
                [sg.InputText()],
                [sg.Text('Ημ. Ακύρωσης: %s' % Rent_info[0][5])],
                [sg.InputText()],
                [sg.Text('Ημ. Παραλαβής: %s' % Rent_info[0][6])],
                [sg.InputText()],
                [sg.Text('Ημ. Παράδοσης: %s' % Rent_info[0][7])],
                [sg.InputText()],
                [sg.Text('Έκπτωση: %s' % Rent_info[0][8])],
                [sg.InputText()],
                [sg.Text('ID Πελάτη: %s' % Rent_info[0][9])],
                [sg.InputText()],
                [sg.Text('Όνομα Ασφάλειας: %s' % Rent_info[0][10])],
                [sg.Text('Η ασφάλεια καλύπτει: %s' % Insurance[0][1])],
                [sg.InputText()],
                [sg.Text('Τύπος Οχήματος: %s' % Rent_info[0][11])],
                [sg.InputText()],
                [sg.Text('Κατάστημα Παραλαβής: %s' % Get_Shop[0][1])],
                [sg.Text('Κωδικός: %s' % Rent_info[0][12])],
                [sg.InputText()],
                [sg.Text('Κατάστημα Παράδωσης: %s' % Give_Shop[0][1])],
                [sg.Text('Κωδικός: %s' % Rent_info[0][13])],
                [sg.InputText()],
                [sg.Text('Κόστος: %s€' % Rent_info[0][14])],
                
                [sg.Text('Αυτοκίνητο')],
                [sg.Text('Μάρκα: %s' % CarT[0][1])],
                [sg.Text('Μοντέλο: %s' % CarT[0][2])],
                [sg.Text('Κωδικός: %s' % Give_Car[0][3])],
                [sg.InputText()],
                [sg.Text('ΧΛΜ πριν: %s' % Give_Car[0][1])],
                [sg.InputText()],
                [sg.Text('ΧΛΜ μετά: %s' % Give_Car[0][0])],
                [sg.InputText()],
                

                [sg.Button('ok'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'ok':
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
            print('ID αυτοκινήτου', values[11])
            print('ΧΛΜ πριν', values[12])
            print('ΧΛΜ μετά', values[13])
        
        if values[0] == '':
            values[0] = Rent_info[0][3]
        if values[1] == '':
            values[1] = Rent_info[0][4]
        if values[2] == '':
            values[2] = Rent_info[0][5]
        if values[3] == '':
            values[3] = Rent_info[0][6]
        if values[4] == '':
            values[4] = Rent_info[0][7]
        if values[5] == '':
            values[5] = Rent_info[0][8]
        if values[6] == '':
            values[6] = Rent_info[0][9]
        if values[7] == '':
            values[7] = Rent_info[0][10]
        if values[8] == '':
            values[8] = Rent_info[0][11]
        if values[9] == '':
            values[9] = Rent_info[0][12]
        if values[10] == '':
            values[10] = Rent_info[0][13]
        if values[11] == '':
            values[11] = Give_Car[0][3]
        if values[12] == '':
            values[12] = Give_Car[0][1]
        if values[13] == '':
            values[13] = Give_Car[0][0]

        con.execute('''UPDATE Ενοικίαση 
                       SET  ΠραγματΗμΠαραλ = '%s', 
                            ΠραγματΗμΠαραδ = '%s', 
                            Ημ_Ακύρωσης = '%s', 
                            ΗμΠαραλαβής = '%s', 
                            ΗμΠαράδοσης = '%s', 
                            Έκπτωση = '%s', 
                            ID_πελάτη = '%s', 
                            Όνομα_Aσφάλειας = '%s', 
                            ID_Κατ_Αυτοκ = '%s', 
                            Παραλ_ID_Καταστ = '%s', 
                            Παραδ_ID_Καταστ = '%s'
                       WHERE  Ενοικίαση.ID = '%s';''' % (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], RentID))								
        con.execute('''UPDATE Παρέχει 
                       SET  Χλμ_μετά = '%s', 
                            Χλμ_πριν = '%s', 
                            ID_αυτοκινήτου = '%s'
                       WHERE  Παρέχει.ID_ενοικίασης = '%s';''' % (values[13], values[12], values[11], RentID))								
        
        con.commit()	
    	

    window.close()

def ClientRents(ClientID):
    Rent = con.cursor()
    Rent.execute('''SELECT Ενοικίαση.ID, Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ΗμΠαραλαβής
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη
                    where Πελάτης.ID='%s';''' % ClientID)
    chunk_size = 1
    Rentlist = list(split(Rent.fetchall(), chunk_size))

    # All the stuff inside your window.
    layout = [  [sg.Text('Όλες οι ενοικιάσεις του Πελάτη')],
                [sg.Text('Ενοικίαση ID | Όνοματεπώνυμο Πελάτη | Ημ. Παραλλάβής')],
                [sg.Listbox(Rentlist, no_scrollbar=False,  size=(70, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε ενοικίαση επιλέγοντας το ID της', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]


    # Create the Window
    window = sg.Window('Εισάγετε Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Επέλεξες την ενοικίαση', values[0])
            showRent(values[0])
    	
    window.close()

def Car(value):
    print(value)
    Rent = con.cursor()
    Rent.execute('''SELECT *
                    FROM   Αυτοκίνητο
                    WHERE  Αυτοκίνητο.ID = '%s';''' % value)
    Car = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Car[0][10])
    Shop = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Αυτοκίνητο: %s' % value)],
            
                [sg.Text('Μάρκα: %s' % Car[0][1])],
                [sg.Text('Μοντέλο: %s' % Car[0][2])],
                [sg.Text('Χιλιόμετρα: %s' % Car[0][3])],
                [sg.Text('Κυβικά: %s' % Car[0][4])],
                [sg.Text('Ημερομηνία Αγοράς: %s' % Car[0][5])],
                [sg.Text('Πινακίδες: %s' % Car[0][6])],
                [sg.Text('Εκπομπές CO2: %s' % Car[0][7])],
                [sg.Text('Αριθμός Πλαισίου: %s' % Car[0][8])],
                [sg.Text('Τύπος Αυτοκινήτου: %s' % Car[0][9])],
                [sg.Text('Κατάστημα: %s' % Shop[0][1])],
                [sg.Text('Κατάσταση σέρβις: %s' % Car[0][11])],
                
                [sg.Button('Cancel')],
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        
    window.close()

def UpdateCrashvalues(CrashID):
    print(CrashID)
    print("updating crash")
    Rent = con.cursor()
    Rent.execute('''SELECT *
                    FROM   Ζημιά 
                    where ID='%s';''' % CrashID)
    Rent_info = Rent.fetchall()



    # All the stuff inside your window.
    layout = [  [sg.Text('Η ζημιά %s' % CrashID)],
               
                [sg.Text('Ημερομηνία: %s' % Rent_info[0][1])],
                [sg.InputText()],
                [sg.Text('Κόστος: %s' %  Rent_info[0][2])],
                [sg.InputText()],
                [sg.Text('Περιγραφή: %s' % Rent_info[0][3])],
                [sg.InputText()],
                [sg.Text('ID Αυτοκινήτου: %s' % Rent_info[0][4])],
                [sg.InputText()],
                [sg.Text('ID Ενοικίασης: %s' % Rent_info[0][5])],
                [sg.InputText()],
                
                [sg.Button('ok'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ζημιά', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'ok':
            print('Ημερομηνία', values[0])
            print('Κόστος', values[1])
            print('Περιγραφή', values[2])
            print('ID Αυτοκινήτου', values[3])
            print('ID Ενοικίασης', values[4])
        
        if values[0] == '':
            values[0] = Rent_info[0][1]
        if values[1] == '':
            values[1] = Rent_info[0][2]
        if values[2] == '':
            values[2] = Rent_info[0][3]
        if values[3] == '':
            values[3] = Rent_info[0][4]
        if values[4] == '':
            values[4] = Rent_info[0][5]
       
       

        con.execute('''UPDATE Ζημιά
                       SET  Ημερομηνία =  '%s',
							Κόστος =  '%s',
							Περιγραφή =  '%s',
                            ID_Αυτοκίνητο=  '%s',
                            ID_Ενοικίαση =  '%s'
                            WHERE ID =  '%s';''' % (values[0], values[1], values[2], values[3], values[4],CrashID))								
           
        con.commit()	
    	

    window.close()

def showCrash(CrashID):
    print(CrashID)
    Rent = con.cursor()
    Rent.execute('''SELECT Ζημιά.ID, Ζημιά.Ημερομηνία, Ζημιά.Κόστος, Ζημιά.Περιγραφή,   Ζημιά.ID_Αυτοκίνητο,  Ζημιά.ID_Ενοικίαση
                    FROM   Ζημιά 
                    where ID='%s';''' % CrashID)
    Rent_info = Rent.fetchall()


    # All the stuff inside your window.
    layout = [  [sg.Text('Η Ζημιά:  %s' % CrashID)],
            
                [sg.Text('Ημερομηνία: %s' % Rent_info[0][1])],
                [sg.Text('Κόστος %s' % Rent_info[0][2])],
                [sg.Text('Περιγραφή: %s' % Rent_info[0][3])],
                [sg.Text('ID Αυτοκινήτου: %s' % Rent_info[0][4])],
                [sg.Text('ID Ενοικίασης: %s' % Rent_info[0][5])],
                            
                [sg.Text('Αυτοκίνητο')],

                [sg.Button('Update'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Update':
            UpdateCrashvalues(CrashID)
        if event == 'Αυτοκίνητο':
            Car(Rent_info[0][4])
    	
    window.close()

def ClientCrash(ClientID):
    Rent = con.cursor()
    Rent.execute('''SELECT Ζημιά.ID, Ζημιά.Κόστος, Ζημιά.Περιγραφή
                    FROM   Ζημιά JOIN Ενοικίαση ON Ενοικίαση.ID = Ζημιά.ID_Ενοικίαση
                    where Ενοικίαση.ID_πελάτη = '%s';''' %ClientID)
    chunk_size = 1
    Rentlist = list(split(Rent.fetchall(), chunk_size))

    # All the stuff inside your window.
    layout = [  [sg.Text('Όλες οι Ζημιές')],
                [sg.Text('ID | Κόστος | Περιγραφή')],
                [sg.Listbox(Rentlist, no_scrollbar=False,  size=(70, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε Ζημιά επιλέγοντας το ID της', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]


    # Create the Window
    window = sg.Window('Εισάγετε Ζημιά', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Επέλεξες την Ζημιά', values[0])
            showCrash(values[0])
    	
    window.close()

def ClientCars(ClientID):
    print(ClientID)
    ## pending ...
    ##query missing 

def showClient(value):
    print(value)
    Rent = con.cursor()
    Rent.execute('''SELECT *
                    FROM   Πελάτης 
                    where ID='%s';''' % value)
    Rent_info = Rent.fetchall()


    # All the stuff inside your window.
    layout = [  [sg.Text('Ο πελάτης: %s' % value)],
               
                [sg.Text('ID: %s' % Rent_info[0][0])], 
                [sg.Text('Ονομα Πελάτη: %s' % Rent_info[0][1])],
                [sg.Text('Επώνυμο Πελάτη: %s' % Rent_info[0][2])],
                [sg.Text('Δίπλωμα Πελάτη: %s' % Rent_info[0][3])],
                [sg.Text('Φύλλο Πελάτη: %s' % Rent_info[0][4])],
                [sg.Text('Τηλέφωνο Πελάτη: %s' % Rent_info[0][5])],
                [sg.Text('Ημερομηνία Γεννήσεως: %s' % Rent_info[0][6])],
                [sg.Text('Email: %s' % Rent_info[0][7])],
                [sg.Text('ΑΦΜ: %s' % Rent_info[0][8])],
                [sg.Text('Πιστωτική Κάρτα: %s' % Rent_info[0][9])],
                [sg.Text('Λογραριασμός Τραπέζης: %s' % Rent_info[0][10])],
                [sg.Text('Δ/νση Μόνιμης Κατοικίας: %s' % Rent_info[0][11])],
                [sg.Text('Status: %s' % Rent_info[0][12])],          
                  
                [sg.Button('Ενοικιάσεις')],
                
                [sg.Button('Αυτοκίνητα')],
                [sg.Button('Ζημιές')],
                [sg.Button('Update Πληροφορίες Πελάτη'), sg.Button('Cancel')], 
                
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Update Πληροφορίες Πελάτη':
            UpdateClientvalues(value)
        if event == 'Ενοικιάσεις':
            ClientRents(value)
        if event == 'Ζημιές':
            ClientCrash(value)
            print('crashes')
        if event == 'Αυτοκίνητα':
            ClientCars(value)
    	
    window.close()

def allClients():
   
    Rent = con.cursor()
    Rent.execute('''SELECT ID, όνομα , Επίθετο
                    FROM   Πελάτης ''')
    chunk_size = 1
    Clientlist = list(split(Rent.fetchall(), chunk_size))

    # All the stuff inside your window.
    layout = [  [sg.Text('Όλες οι Πελάτες')],
                [sg.Text('ID Πελάτη | Όνοματεπώνυμο Πελάτη ')],
                [sg.Listbox(Clientlist, no_scrollbar=False,  size=(70, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε Πελάτη επιλέγοντας το ID τou', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]


    # Create the Window
    window = sg.Window('Εισάγετε Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Επέλεξες τον πελάτη', values[0])
            showClient(values[0])
    	
    window.close()

def ChooseRental():
    sg.theme('DarkAmber')   # Add a touch of color
    layout = [  [sg.Button("Ενοικιάσεις Ημέρας", key="opentoday", size=(20,	1))], 
                [sg.Button("Όλες οι ενοικιάσεις", key="open", size=(20,	1))]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            allRent()
        if event == "opentoday":
            todayRent()
    window.close()

def Updatevalues(RentID, CarID):
    print(RentID)
    print(CarID)
    Rent = con.cursor()
    Rent.execute('''SELECT Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ID, Ενοικίαση.ΠραγματΗμΠαραλ, 
                    Ενοικίαση.ΠραγματΗμΠαραδ, Ενοικίαση.Ημ_Ακύρωσης, Ενοικίαση.ΗμΠαραλαβής, Ενοικίαση.ΗμΠαράδοσης,
                    Ενοικίαση.Έκπτωση, Ενοικίαση.ID_πελάτη, Ενοικίαση.Όνομα_Aσφάλειας, Ενοικίαση.ID_Κατ_Αυτοκ,
                    Ενοικίαση.Παραλ_ID_Καταστ, Ενοικίαση.Παραδ_ID_Καταστ, Κόστος
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη
                    WHERE  Ενοικίαση.ID = '%s';''' % RentID)
    Rent_info = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Ασφάλεια
                    WHERE  Ασφάλεια.ID = '%s';''' % Rent_info[0][10])
    Insurance = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][12])
    Get_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Κατάστημα
                    WHERE  Κατάστημα.ID = '%s';''' % Rent_info[0][13])
    Give_Shop = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Παρέχει
                    WHERE  Παρέχει.ID_ενοικίασης = '%s';''' % RentID)
    Give_Car = Rent.fetchall()

    Rent.execute('''SELECT *
                    FROM   Αυτοκίνητο
                    WHERE  Αυτοκίνητο.ID = '%s';''' % Give_Car[0][3])
    CarT = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Η ενοικίαση %s' % RentID)],
               
                [sg.Text('Ονομα Πελάτη: %s' % Rent_info[0][0])],
                [sg.Text('Επώνυμο Πελάτη: %s' % Rent_info[0][1])],
                [sg.Text('Πραγματική Ημ. Παραλαβής: %s' % Rent_info[0][3])],
                [sg.InputText()],
                [sg.Text('Πραγματική Ημ. Παράδοσης: %s' % Rent_info[0][4])],
                [sg.InputText()],
                [sg.Text('Ημ. Ακύρωσης: %s' % Rent_info[0][5])],
                [sg.InputText()],
                [sg.Text('Ημ. Παραλαβής: %s' % Rent_info[0][6])],
                [sg.InputText()],
                [sg.Text('Ημ. Παράδοσης: %s' % Rent_info[0][7])],
                [sg.InputText()],
                [sg.Text('Έκπτωση: %s' % Rent_info[0][8])],
                [sg.InputText()],
                [sg.Text('ID Πελάτη: %s' % Rent_info[0][9])],
                [sg.InputText()],
                [sg.Text('Όνομα Ασφάλειας: %s' % Rent_info[0][10])],
                [sg.Text('Η ασφάλεια καλύπτει: %s' % Insurance[0][1])],
                [sg.InputText()],
                [sg.Text('Τύπος Οχήματος: %s' % Rent_info[0][11])],
                [sg.InputText()],
                [sg.Text('Κατάστημα Παραλαβής: %s' % Get_Shop[0][1])],
                [sg.Text('Κωδικός: %s' % Rent_info[0][12])],
                [sg.InputText()],
                [sg.Text('Κατάστημα Παράδωσης: %s' % Give_Shop[0][1])],
                [sg.Text('Κωδικός: %s' % Rent_info[0][13])],
                [sg.InputText()],
                [sg.Text('Κόστος: %s€' % Rent_info[0][14])],
                
                [sg.Text('Αυτοκίνητο')],
                [sg.Text('Μάρκα: %s' % CarT[0][1])],
                [sg.Text('Μοντέλο: %s' % CarT[0][2])],
                [sg.Text('Κωδικός: %s' % Give_Car[0][3])],
                [sg.InputText()],
                [sg.Text('ΧΛΜ πριν: %s' % Give_Car[0][1])],
                [sg.InputText()],
                [sg.Text('ΧΛΜ μετά: %s' % Give_Car[0][0])],
                [sg.InputText()],
                

                [sg.Button('ok'), sg.Button('Cancel')], 
                
                ]


    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'ok':
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
            print('ID αυτοκινήτου', values[11])
            print('ΧΛΜ πριν', values[12])
            print('ΧΛΜ μετά', values[13])
        
        if values[0] == '':
            values[0] = Rent_info[0][3]
        if values[1] == '':
            values[1] = Rent_info[0][4]
        if values[2] == '':
            values[2] = Rent_info[0][5]
        if values[3] == '':
            values[3] = Rent_info[0][6]
        if values[4] == '':
            values[4] = Rent_info[0][7]
        if values[5] == '':
            values[5] = Rent_info[0][8]
        if values[6] == '':
            values[6] = Rent_info[0][9]
        if values[7] == '':
            values[7] = Rent_info[0][10]
        if values[8] == '':
            values[8] = Rent_info[0][11]
        if values[9] == '':
            values[9] = Rent_info[0][12]
        if values[10] == '':
            values[10] = Rent_info[0][13]
        if values[11] == '':
            values[11] = Give_Car[0][3]
        if values[12] == '':
            values[12] = Give_Car[0][1]
        if values[13] == '':
            values[13] = Give_Car[0][0]

        con.execute('''UPDATE Ενοικίαση 
                       SET  ΠραγματΗμΠαραλ = '%s', 
                            ΠραγματΗμΠαραδ = '%s', 
                            Ημ_Ακύρωσης = '%s', 
                            ΗμΠαραλαβής = '%s', 
                            ΗμΠαράδοσης = '%s', 
                            Έκπτωση = '%s', 
                            ID_πελάτη = '%s', 
                            Όνομα_Aσφάλειας = '%s', 
                            ID_Κατ_Αυτοκ = '%s', 
                            Παραλ_ID_Καταστ = '%s', 
                            Παραδ_ID_Καταστ = '%s'
                       WHERE  Ενοικίαση.ID = '%s';''' % (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], RentID))								
        con.execute('''UPDATE Παρέχει 
                       SET  Χλμ_μετά = '%s', 
                            Χλμ_πριν = '%s', 
                            ID_αυτοκινήτου = '%s'
                       WHERE  Παρέχει.ID_ενοικίασης = '%s';''' % (values[13], values[12], values[11], RentID))								
        
       	
   	

    window.close()

def todayRent():
   
    Rent = con.cursor()
    Rent.execute('''SELECT Ενοικίαση.ID, Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ΗμΠαραλαβής
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη
                    WHERE  ΗμΠαραλαβής = '2020-10-1';''')
    chunk_size = 1
    Rentlist = list(split(Rent.fetchall(), chunk_size))

    # All the stuff inside your window.
    layout = [  [sg.Text('Σημερινές ενοικιάσεις')],
                [sg.Text('Ενοικίαση ID | Όνοματεπώνυμο Πελάτη | Ημ. Παραλλάβής')],
                [sg.Listbox(Rentlist, no_scrollbar=False,  size=(70, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε ενοικίαση επιλέγοντας το ID της', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]


    # Create the Window
    window = sg.Window('Εισάγετε Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Επέλεξες την ενοικίαση', values[0])
            showRent(values[0])
    	
    window.close()

def allRent():
   
    Rent = con.cursor()
    Rent.execute('''SELECT Ενοικίαση.ID, Πελάτης.όνομα, Πελάτης.Επίθετο, Ενοικίαση.ΗμΠαραλαβής
                    FROM   Πελάτης JOIN Ενοικίαση ON Πελάτης.ID = Ενοικίαση.ID_πελάτη;''')
    chunk_size = 1
    Rentlist = list(split(Rent.fetchall(), chunk_size))

    # All the stuff inside your window.
    layout = [  [sg.Text('Όλες οι ενοικιάσεις')],
                [sg.Text('Ενοικίαση ID | Όνοματεπώνυμο Πελάτη | Ημ. Παραλλάβής')],
                [sg.Listbox(Rentlist, no_scrollbar=False,  size=(70, 20), key='LISTBOX')],
                [sg.Text('Επέλεξε ενοικίαση επιλέγοντας το ID της', size=(30,1)), sg.InputText(size=(10,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]


    # Create the Window
    window = sg.Window('Εισάγετε Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('Επέλεξες την ενοικίαση', values[0])
            showRent(values[0])
    	
    window.close()

def Statistics():
    sg.theme('DarkAmber')   # Add a touch of color
    layout = [  [sg.Button("Μέσος Χρόνος Ενοικίασης", key="avgRental", size=(40,	1))],
                [sg.Button("Μέσα χλμ ανά Ενοικίαση", key="avgMileage", size=(40,	1))],
                [sg.Button("Ποια κατηγορία οχημάτων προτιμάται", key="bestCategory", size=(40,	1))],
                [sg.Button("Ποια ασφάλεια προτιμάται", key="insurance", size=(40,	1))],
                [sg.Button("Μηνιαίες κρατήσεις, τελευταίου έτους", key="montlyRentals", size=(40,	1))],
                [sg.Button("Ποσοστό μηνιαίων ακυρώσεων, τελευταίου έτους", key="MonthyCancelations", size=(40,	1))],
                [sg.Button("Μηνιαία κέρδη ανά έτος", key="MontlhyEarnings", size=(40,	1))]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "avgRental":
            avgRental()
        if event == "avgMileage":
            avgMileage()
        if event == "bestCategory":
            avgCarCat()
        if event == "insurance":
            insurance()
        if event == "montlyRentals":
            monthlyRentals()
        if event == "MonthyCancelations":
            MonthyCancelations()
        if event == "MontlhyEarnings":
            MonthyEarnings()
    
    window.close()

def avgMileage():
    Rent = con.cursor()
    Rent.execute('''select avg( Χλμ_μετά - Χλμ_πριν )as Mileage
                    From Παρέχει;''' )
    Rent_info = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Μέσα χλμ ανά Ενοικίαση %s km' % Rent_info[0][0])],
                [sg.Button('ΟΚ')],
                ]
    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'ΟΚ': # if user closes window or clicks cancel
            break
    	
    window.close()

def avgRental():
    Rent = con.cursor()
    Rent.execute('''select avg( julianday(ΠραγματΗμΠαραδ) - julianday(ΠραγματΗμΠαραλ)) as duration
                    From Ενοικίαση''' )
    Rent_info = Rent.fetchall()

    # All the stuff inside your window.
    layout = [  [sg.Text('Μέσος Χρόνος Ενοικίασης %s ημέρες' % Rent_info[0][0])],
                [sg.Button('ΟΚ')],
                ]
    # Create the Window
    window = sg.Window('Ενοικίαση', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'ΟΚ': # if user closes window or clicks cancel
            break
    	
    window.close()

def avgCarCat():
    Rent = con.cursor()
    Rent.execute('''SELECT t.ID, t.Όνομα, count(t.ID) as Occurancy, (SELECT count(*) from Ενοικίαση) as totall
                    FROM Ενοικίαση as e join Τύπος_Οχήματος as t on t.ID = e.ID_Κατ_Αυτοκ
                    GROUP by t.ID;''' )
    Rent_info = Rent.fetchall()


    sg.theme('DarkAmber') 
    layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')]]
    window = sg.Window('Ποια κατηγορία οχημάτων προτιμάται', layout,
                   grab_anywhere=True,
                   finalize=True)
    graph = window['graph']
    dataSize = 2
    dataRangeMin = 0
    dataRangeMax = 100

    xData =[(Rent_info[0][2] / Rent_info[0][3])*100,(Rent_info[1][2] / Rent_info[1][3])*100]

    # METHODS

    def drawAxis():
        # Draw Vertical Y Axis
        graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
        # Draw Horizontal X Axis
        graph.DrawLine((0, 0), (0, dataRangeMax))


    def drawTicks(step):
        # We only need the Y axis ticks for this plot..
        for y in range(dataRangeMin, dataRangeMax+1, step):
            # But we can add horizontal grid lines
            graph.DrawLine((0, y), (100, y), color='grey')
            graph.DrawLine((-3, y), (3, y))
            if y != 0:
                graph.DrawText(y, (-10, y), color='black')


    def drawPlot():
        # Divide horizontal axis space by data points :
        barStep = dataRangeMax/dataSize

        for i, x in enumerate(xData):
            graph.draw_rectangle(top_left=(i*barStep, x),
                                bottom_right=(i*barStep+barStep, 0),
                                fill_color='#B6B6B6')


    # CALL METHODS:
    drawAxis()
    drawPlot()
    drawTicks(20)

def monthlyRentals():
    Rent = con.cursor()
    Rent.execute('''SELECT count() as rentals, STRFTIME("%m-%Y", ΠραγματΗμΠαραλ) AS year_month
                    from Ενοικίαση
                    GROUP By year_month
                    order by year_month DESC
                    limit 3;''' )    ## αλλαγη το λιμιτ σε 12
    Rent_info = Rent.fetchall()
    RentalSumYear =0
    for i in range(3):
        RentalSumYear = RentalSumYear + Rent_info[i][0]
    print(RentalSumYear)
    sg.theme('DarkAmber') 
    layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')]]
    window = sg.Window('Μηνιαίες κρατήσεις, τελευταίου έτους', layout,
                   grab_anywhere=True,
                   finalize=True)
    graph = window['graph']
    dataSize = 3  ##change se 12
    dataRangeMin = 0
    dataRangeMax = 100

    xData =[(Rent_info[0][0] / RentalSumYear)*100,(Rent_info[1][0]/ RentalSumYear)*100,(Rent_info[2][0]/ RentalSumYear)*100]

    # METHODS

    def drawAxis():
        # Draw Vertical Y Axis
        graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
        # Draw Horizontal X Axis
        graph.DrawLine((0, 0), (0, dataRangeMax))


    def drawTicks(step):
        # We only need the Y axis ticks for this plot..
        for y in range(dataRangeMin, dataRangeMax+1, step):
            # But we can add horizontal grid lines
            graph.DrawLine((0, y), (100, y), color='grey')
            graph.DrawLine((-3, y), (3, y))
            if y != 0:
                graph.DrawText(y, (-10, y), color='black')


    def drawPlot():
        # Divide horizontal axis space by data points :
        barStep = dataRangeMax/dataSize

        for i, x in enumerate(xData):
            graph.draw_rectangle(top_left=(i*barStep, x),
                                bottom_right=(i*barStep+barStep, 0),
                                fill_color='#B6B6B6')


    # CALL METHODS:
    drawAxis()
    drawPlot()
    drawTicks(20)

##pending  
def MonthyCancelations():
    print("monthly cancellations")
    Rent = con.cursor()
    Rent.execute('''SELECT count() as rentals, STRFTIME("%m-%Y", ΠραγματΗμΠαραλ) AS year_month
                    from Ενοικίαση
                    GROUP By year_month
                    order by year_month DESC
                    limit 3;''' )    ## αλλαγη το λιμιτ σε 12
    Rent_info = Rent.fetchall()
    RentalSumYear =0
    for i in range(3):
        RentalSumYear = RentalSumYear + Rent_info[i][0]
    print(RentalSumYear)
    sg.theme('DarkAmber') 
    layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')]]
    window = sg.Window('Μηνιαίες ακυρώσεισ (ποσοστό), τελευταίου έτους', layout,
                   grab_anywhere=True,
                   finalize=True)
    graph = window['graph']
    dataSize = 3  ##change se 12
    dataRangeMin = 0
    dataRangeMax = 100

    xData =[(Rent_info[0][0] / RentalSumYear)*100,(Rent_info[1][0]/ RentalSumYear)*100,(Rent_info[2][0]/ RentalSumYear)*100]

    # METHODS

    def drawAxis():
        # Draw Vertical Y Axis
        graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
        # Draw Horizontal X Axis
        graph.DrawLine((0, 0), (0, dataRangeMax))


    def drawTicks(step):
        # We only need the Y axis ticks for this plot..
        for y in range(dataRangeMin, dataRangeMax+1, step):
            # But we can add horizontal grid lines
            graph.DrawLine((0, y), (100, y), color='grey')
            graph.DrawLine((-3, y), (3, y))
            if y != 0:
                graph.DrawText(y, (-10, y), color='black')


    def drawPlot():
        # Divide horizontal axis space by data points :
        barStep = dataRangeMax/dataSize

        for i, x in enumerate(xData):
            graph.draw_rectangle(top_left=(i*barStep, x),
                                bottom_right=(i*barStep+barStep, 0),
                                fill_color='#B6B6B6')


    # CALL METHODS:
    drawAxis()
    drawPlot()
    drawTicks(20)

def MonthyEarnings():
    print("montlyh earnings")
    Rent = con.cursor()
    Rent.execute('''SELECT sum(Κόστος) as earnings,STRFTIME("%m-%Y", ΠραγματΗμΠαραλ) AS year_month
                    from Ενοικίαση
                    GROUP By year_month
                    limit 3;''' )    ## αλλαγη το λιμιτ σε 12
    Rent_info = Rent.fetchall()
    SumEarnings =0
    for i in range(3):
        SumEarnings = SumEarnings + Rent_info[i][0]
    print(SumEarnings)
    sg.theme('DarkAmber') 
    layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')]]
    window = sg.Window('Μηνιαία Έσοδα, τελευταίου έτους', layout,
                   grab_anywhere=True,
                   finalize=True)
    graph = window['graph']
    dataSize = 3  ##change se 12
    dataRangeMin = 0
    dataRangeMax = 100

    xData =[(Rent_info[0][0] / SumEarnings)*100,(Rent_info[1][0]/ SumEarnings)*100,(Rent_info[2][0]/ SumEarnings)*100]

    # METHODS

    def drawAxis():
        # Draw Vertical Y Axis
        graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
        # Draw Horizontal X Axis
        graph.DrawLine((0, 0), (0, dataRangeMax))


    def drawTicks(step):
        # We only need the Y axis ticks for this plot..
        for y in range(dataRangeMin, dataRangeMax+1, step):
            # But we can add horizontal grid lines
            graph.DrawLine((0, y), (100, y), color='grey')
            graph.DrawLine((-3, y), (3, y))
            if y != 0:
                graph.DrawText(y, (-10, y), color='black')


    def drawPlot():
        # Divide horizontal axis space by data points :
        barStep = dataRangeMax/dataSize

        for i, x in enumerate(xData):
            graph.draw_rectangle(top_left=(i*barStep, x),
                                bottom_right=(i*barStep+barStep, 0),
                                fill_color='#B6B6B6')


    # CALL METHODS:
    drawAxis()
    drawPlot()
    drawTicks(20)

def insurance():
    Rent = con.cursor()
    Rent.execute('''SELECT a.ID, a.Περιγραφή, count(a.ID) as Occurancy, (SELECT count(*) from Ενοικίαση) as totall
                    FROM Ενοικίαση as e join Ασφάλεια as a on a.ID = e.Όνομα_Aσφάλειας
                    GROUP by a.ID;''' )
    Rent_info = Rent.fetchall()


    sg.theme('DarkAmber') 
    layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')]]
    window = sg.Window('Ποια κατηγορία ασφάλειας προτιμάται', layout,
                   grab_anywhere=True,
                   finalize=True)
    graph = window['graph']
    dataSize = 3
    dataRangeMin = 0
    dataRangeMax = 100

    xData =[(Rent_info[0][2] / Rent_info[0][3])*100,(Rent_info[1][2] / Rent_info[1][3])*100,(Rent_info[2][2] / Rent_info[2][3])*100]

    # METHODS

    def drawAxis():
        # Draw Vertical Y Axis
        graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
        # Draw Horizontal X Axis
        graph.DrawLine((0, 0), (0, dataRangeMax))


    def drawTicks(step):
        # We only need the Y axis ticks for this plot..
        for y in range(dataRangeMin, dataRangeMax+1, step):
            # But we can add horizontal grid lines
            graph.DrawLine((0, y), (100, y), color='grey')
            graph.DrawLine((-3, y), (3, y))
            if y != 0:
                graph.DrawText(y, (-10, y), color='black')


    def drawPlot():
        # Divide horizontal axis space by data points :
        barStep = dataRangeMax/dataSize

        for i, x in enumerate(xData):
            graph.draw_rectangle(top_left=(i*barStep, x),
                                bottom_right=(i*barStep+barStep, 0),
                                fill_color='#B6B6B6')


    # CALL METHODS:
    drawAxis()
    drawPlot()
    drawTicks(20)


def main():
    sg.theme('DarkAmber')   # Add a touch of color
    layout = [  [sg.Button("Εισαγωγή Στοιχέιων Πελάτη", key="ImportClient", size=(40,	1))], 
                [sg.Button("Εισαγωγή Στοιχέιων Ενοικίασης", key="ImportRental", size=(40,	1))], 
                [sg.Button("Εισαγωγή Στοιχέιων Ζημιάς", key="ImportCrash", size=(40,	1))], 
                [sg.Button("Επιλογή Πελάτη", key="ChooseClient", size=(40,	1))], 
                [sg.Button("Επιλογή Ενοικίασης", key="ChooseRental", size=(40,	1))], 
                [sg.Button("Στατιστικά", key="Statistics", size=(40,	1))], 
                [sg.Button("Cancel", key="exit", size=(40,	1))]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "ImportClient":
            ImportClient()
        if event == "ImportRental":
            ImportRental()
        if event == "ImportCrash":
            ImportCrash()
        if event == "ChooseClient":
            ChooseClient()
        if event == "ChooseRental":
            ChooseRental()
        if event == "Statistics":
            Statistics()
    
    con.close()	
    window.close()

if __name__ == "__main__":
    main()
