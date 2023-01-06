import sqlite3
import PySimpleGUI as sg
from random import choice
from datetime import date

con = sqlite3.connect("Car_Rent.sqlite")

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def CalculateCost(RentID):
    
    print(RentID)
    
    cost = con.cursor()
    cost.execute('''SELECT (julianday(Ενοικίαση.ΠραγματΗμΠαραδ) - julianday(Ενοικίαση.ΠραγματΗμΠαραλ)) * Τύπος_Οχήματος.ΗμερήσιοΚόστος AS car_cost, (julianday(Ενοικίαση.ΠραγματΗμΠαραδ) - julianday(Ενοικίαση.ΠραγματΗμΠαραλ)) * Ασφάλεια.Κόστος_ανα_μέρα AS ins_cost, Ενοικίαση.Έκπτωση
                    FROM   (Ενοικίαση JOIN Τύπος_Οχήματος ON Ενοικίαση.ID_Κατ_Αυτοκ = Τύπος_Οχήματος.ID) JOIN Ασφάλεια ON Ενοικίαση.Όνομα_Aσφάλειας = Ασφάλεια.ID
                    WHERE  Ενοικίαση.ID = '%s';''' % RentID)
    
    reg_cost = cost.fetchall()
    
    

    dam_test = con.cursor()
    dam_test.execute('''SELECT count(*)
                        FROM   Ζημιά
                        WHERE  Ζημιά.ID_Ενοικίαση = '%s';''' % RentID)
    damage_test = dam_test.fetchall()
    if damage_test[0][0] != 0:
        dam_cost = con.cursor()
        dam_cost.execute('''SELECT SUM(Ζημιά.Κόστος)
                            FROM   Ζημιά
                            WHERE  Ζημιά.ID_Ενοικίαση = '%s';''' % RentID)
        damage_cost = dam_cost.fetchall()[0][0]
    else:
        damage_cost = 0
    
    fnd_cost = reg_cost[0][0] + reg_cost[0][1] 
    f_cost = fnd_cost - (fnd_cost * (reg_cost[0][2]/100)) + damage_cost

    layout = [  [sg.Text('Το τελικό κόστος είναι:')],
                [sg.Text('Κόστος αυτοκινήτου: %s €' % reg_cost[0][0])],
                [sg.Text('Κόστος ασφάλειας: %s €' % reg_cost[0][1])],
                [sg.Text('Έκπτωση: %s τις εκατό' % reg_cost[0][2])],
                [sg.Text('Κόστος Ζημιών: %s €' % damage_cost)],
                [sg.Text('Τελικό Κόστος: %s €' % f_cost)],
                [sg.Text('Αν το τελικό κόστος είναι εντάξει πατήστε OK')],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    

    # Create the Window
    window = sg.Window('Κόστος', layout)
    
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            con.execute('''UPDATE Ενοικίαση 
                       SET  Κόστος = '%s'
                       WHERE  Ενοικίαση.ID = '%s';''' % (f_cost, RentID))		
            today = date.today()
            dtoday = today.strftime("%Y-%m-%d")		
            test = con.execute('''SELECT COUNT(*)
                                FROM Οικ_Συναλλαγή
                                WHERE Οικ_Συναλλαγή.ID_Ενοικίασης = '%s';''' % RentID)	
            
            ex_test = test.fetchall()
            if ex_test[0][0] == 0:		
                print('it created new entry')
                con.execute('''INSERT INTO Οικ_Συναλλαγή(Ποσό, Ημερομηνία, ΦΠΑ, ID_Ενοικίασης) 
                            VALUES (?, ?, ?, ?);''', (f_cost, dtoday, '24%', RentID))								
                rec = con.execute('''SELECT Οικ_Συναλλαγή.ID
                        FROM   Οικ_Συναλλαγή
                        WHERE  Οικ_Συναλλαγή.ID_Ενοικίασης = '%s';''' % RentID)
                
                layout1 = [ [sg.Text('Απόδειξη: %s' % rec.fetchall()[0][0])],
                            [sg.Text('Τελικό κόστος: %s €' % f_cost)],
                            [sg.Text('ΦΠΑ: 24%')],
                            [sg.Text('Ημερομηνία: %s' % dtoday)],
                            [sg.Text('ID Ενοικίασης: %s' % RentID)],]
                # Create the Window
                window = sg.Window('Απόδειξη', layout1)
                while True:
                    event, values = window.read(timeout=500)
                    if event == sg.WIN_CLOSED:
                        break
            else:		
                print('it updated')
                con.execute('''UPDATE Οικ_Συναλλαγή SET Ποσό = '%i', Ημερομηνία = '%s'
                            WHERE Οικ_Συναλλαγή.ID_Ενοικίασης = '%s';''' % (f_cost, dtoday, RentID))								
                rec = con.execute('''SELECT Οικ_Συναλλαγή.ID
                        FROM   Οικ_Συναλλαγή
                        WHERE  Οικ_Συναλλαγή.ID_Ενοικίασης = '%s';''' % RentID)
                
                layout1 = [ [sg.Text('Απόδειξη: %s' % rec.fetchall()[0][0])],
                            [sg.Text('Τελικό κόστος: %s €' % f_cost)],
                            [sg.Text('ΦΠΑ: 24%')],
                            [sg.Text('Ημερομηνία: %s' % dtoday)],
                            [sg.Text('ID Ενοικίασης: %s' % RentID)],]
                            
                # Create the Window
                window = sg.Window('Απόδειξη', layout1)
                while True:
                    event, values = window.read(timeout=500)
                    if event == sg.WIN_CLOSED:
                        break
            

        con.commit()
    
    con.close()	

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
    con.close()	

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
                [sg.Button('Υπολόγησε Κόστος')],

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
        if event == 'Υπολόγησε Κόστος':
            if not Rent_info[0][3] or not Rent_info[0][4] :
                print('Λείπουν οι πραγματικές ημερομηνίες παραλλαβής και παράδωσης')
                break
            else:
                CalculateCost(value)


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

def main():
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
    
    con.close()	
    window.close()

if __name__ == "__main__":
    main()



