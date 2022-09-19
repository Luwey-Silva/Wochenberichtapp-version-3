import PySimpleGUI as sg
import contact_information_window
import database_interface
import validation

layout = [[sg.Text('Bitte gebe den Folgende :', font=("Helvetica", 15))],
          [sg.Text("Dein Name:", font=("Helvetica", 15)), sg.Input(key="-NAME-")],
          [sg.Text('Von', font=("Helvetica", 15)), sg.InputText(key='-VON-')],
          [sg.Text('Bis', font=("Helvetica", 15)), sg.InputText(key='-BIS-')],
          [sg.Text("Dein Nachname:", font=("Helvetica", 15)), sg.Input(key="-NACHNAME-")],
          [sg.Text("Kalenderwoche:", font=("Helvetica", 15)), sg.Input(key="-KW-")],
          [sg.Text("Gib die Stunden für Montag ein:", font=("Helvetica", 15)), sg.Input(key="-USER_STUNDEN_MONTAG-")],
          [sg.Text("Was würde am Montag gemacht?", font=("Helvetica", 15)), sg.Multiline(key="-USER_BESCHREIBUNG_MONTAG-", size=(50, 3))],    
          [sg.Text("Gib die Stunden für Dienstag ein:", font=("Helvetica", 15)), sg.Input(key="-USER_STUNDEN_DIENSTAG-")],
          [sg.Text("Was würde am Dienstag gemacht?", font=("Helvetica", 15)), sg.Multiline(key="-USER_BESCHREIBUNG_DIENSTAG-", size=(50, 3))],
          [sg.Text("Gib die Stunden für Mittwoch ein:", font=("Helvetica", 15)), sg.Input(key="-USER_STUNDEN_MITTWOCH-")],
          [sg.Text("Was würde am Mittwoch gemacht?", font=("Helvetica", 15)), sg.Multiline(key="-USER_BESCHREIBUNG_MITTWOCH-", size=(50, 3))],
          [sg.Text("Gib die Stunden für Donnerstag ein:", font=("Helvetica", 15)), sg.Input(key="-USER_STUNDEN_DONNERSTAG-")],
          [sg.Text("Was würde am Donnerstag gemacht?", font=("Helvetica", 15)), sg.Multiline(key="-USER_BESCHREIBUNG_DONNERSTAG-", size=(50, 3))],
          [sg.Text("Gib die Stunden für Freitag ein:", font=("Helvetica", 15)), sg.Input(key="-USER_STUNDEN_FREITAG-")],
          [sg.Text("Was würde am Freitag gemacht?", font=("Helvetica", 15)), sg.Multiline(key="-USER_BESCHREIBUNG_FREITAG-", size=(50, 3))],
          [sg.Button('Submit Contact Information', font=("Helvetica", 15)), sg.Button('Show Table', font=("Helvetica", 15)), sg.Exit(font=("Helvetica", 15))]]

window = sg.Window("Submit Contact Information", layout, element_justification="right", finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Contact Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            database_interface.insert_contact(values['-NAME-'], values['-NACHNAME-'], values['-VON-'], values['-BIS-'], values['-KW-'], values['-USER_STUNDEN_MONTAG-'], 
                                                values['-USER_BESCHREIBUNG_MONTAG-'], values['-USER_STUNDEN_DIENSTAG-'], values['-USER_BESCHREIBUNG_DIENSTAG-'], 
                                                values['-USER_STUNDEN_MITTWOCH-'], values['-USER_BESCHREIBUNG_MITTWOCH-'], 
                                                values['-USER_STUNDEN_DONNERSTAG-'], values['-USER_BESCHREIBUNG_DONNERSTAG-'], values['-USER_STUNDEN_FREITAG-'], 
                                                values['-USER_BESCHREIBUNG_FREITAG-'])
            sg.popup("Contact Information submitted!")
        else:
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message)
    elif event == 'Show Table':
        contact_information_window.create()
