
def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-NAME-']) == 0:
        values_invalid.append('Name')
        is_valid = False
    
    if len(values['-VON-']) == 0:
        values_invalid.append('Von')
        is_valid = False

    if len(values['-BIS-']) == 0:
        values_invalid.append('Bis')
        is_valid = False

    if len(values['-NACHNAME-']) == 0:
        values_invalid.append('Nachname')
        is_valid = False
    
    if len(values['-KW-']) == 0:
        values_invalid.append('Kw')
        is_valid = False

    if len(values['-USER_STUNDEN_MONTAG-']) == 0:
        values_invalid.append('User_stunden_montag')
        is_valid = False

    if len(values['-USER_BESCHREIBUNG_MONTAG-']) == 0:
        values_invalid.append('User_beschreibung_montag')
        is_valid = False
    
    if len(values['-USER_STUNDEN_DIENSTAG-']) == 0:
        values_invalid.append('User_stunden_dienstag')
        is_valid = False

    if len(values['-USER_BESCHREIBUNG_DIENSTAG-']) == 0:
        values_invalid.append('User_beschreibung_dienstag')
        is_valid = False

    if len(values['-USER_STUNDEN_MITTWOCH-']) == 0:
        values_invalid.append('User_stunden_mittwoch')
        is_valid = False
    
    if len(values['-USER_BESCHREIBUNG_MITTWOCH-']) == 0:
        values_invalid.append('User_beschreibung_mittwoch')
        is_valid = False

    if len(values['-USER_STUNDEN_DONNERSTAG-']) == 0:
        values_invalid.append('User_stunden_donnerstag')
        is_valid = False

    if len(values['-USER_BESCHREIBUNG_DONNERSTAG-']) == 0:
        values_invalid.append('User_beschreibung_donnerstag')
        is_valid = False
    
    if len(values['-USER_STUNDEN_FREITAG-']) == 0:
        values_invalid.append('User_stunden_freitag')
        is_valid = False

    if len(values['-USER_BESCHREIBUNG_FREITAG-']) == 0:
        values_invalid.append('User_beschreibung_freitag')
        is_valid = False

    result = {"is_valid": is_valid, "values_invalid": values_invalid}
    return result

def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message