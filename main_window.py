import PySimpleGUI as sg
import contact_information_window
import database_interface
import validation
import valueTransfer


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

def fill_valueTransfer(values):
    tempValueTransferInstance = valueTransfer.ValueTransfer()
    tempValueTransferInstance \
        .set_name(values['-NAME-']) \
        .set_nachname(values['-NACHNAME-']) \
        .set_von(values['-VON-']) \
        .set_bis(values['-BIS-']) \
        .set_kw(values['-KW-']) \
        .set_user_stunden_montag(values['-USER_STUNDEN_MONTAG-']) \
        .set_user_beschreibung_montag(values['-USER_BESCHREIBUNG_MONTAG-']) \
        .set_user_stunden_dienstag(values['-USER_STUNDEN_DIENSTAG-']) \
        .set_user_beschreibung_dienstag(values['-USER_BESCHREIBUNG_DIENSTAG-']) \
        .set_user_stunden_mittwoch(values['-USER_STUNDEN_MITTWOCH-']) \
        .set_user_beschreibung_mittwoch(values['-USER_BESCHREIBUNG_MITTWOCH-']) \
        .set_user_stunden_donnerstag(values['-USER_STUNDEN_DONNERSTAG-']) \
        .set_user_beschreibung_donnerstag(values['-USER_BESCHREIBUNG_DONNERSTAG-']) \
        .set_user_stunden_freitag(values['-USER_STUNDEN_FREITAG-']) \
        .set_user_beschreibung_freitag(values['-USER_BESCHREIBUNG_FREITAG-'])
    return tempValueTransferInstance

window = sg.Window("Submit Contact Information", layout, element_justification="right", finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Submit Contact Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            valueTransferInstance = fill_valueTransfer(values)
            database_interface.insert_contact(valueTransferInstance)
            sg.popup("Contact Information submitted!")

        else:
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message)

    elif event == 'Show Table':
        contact_information_window.create()





window.close()
