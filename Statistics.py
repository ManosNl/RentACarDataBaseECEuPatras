import sqlite3
import PySimpleGUI as sg
from random import choice
from datetime import date

con = sqlite3.connect("Car_Rent.sqlite")

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
    
    con.close()	
    window.close()


if __name__ == "__main__":
    main()
