import sqlite3

def insert_contact(name, von, bis, nachname, kw, user_stunden_montag, user_beschreibung_montag, user_stunden_dienstag, user_beschreibung_dienstag, user_stunden_mittwoch, user_beschreibung_mittwoch, user_stunden_donnerstag, user_beschreibung_donnerstag, user_stunden_freitag, user_beschreibung_freitag):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("INSERT INTO CONTACT_INFORMATION (NAME,VON,BIS,NACHNAME,KW,USER_STUNDEN_MONTAG,USER_BESCHREIBUNG_MONTAG,USER_STUNDEN_DIENSTAG,USER_BESCHREIBUNG_DIENSTAG,USER_STUNDEN_MITTWOCH,USER_BESCHREIBUNG_MITTWOCH,USER_STUNDEN_DONNERSTAG,USER_BESCHREIBUNG_DONNERSTAG,USER_STUNDEN_FREITAG,USER_BESCHREIBUNG_FREITAG) \
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name,von,bis,nachname,kw,user_stunden_montag,user_beschreibung_montag, user_stunden_dienstag, user_beschreibung_dienstag,user_stunden_mittwoch,user_beschreibung_mittwoch,user_stunden_donnerstag,user_beschreibung_donnerstag,user_stunden_freitag,user_beschreibung_freitag))
    conn.commit()
    conn.close()

def delete_contact_by_name(name):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?",(name,))
    conn.close()

def edit_address_by_name(name, address):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, address))
    conn.commit()
    conn.close()

def edit_phone_number_by_name(name, phone_number):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, phone_number))
    conn.close()

def retrieve_contacts():
    results = []
    conn = sqlite3.connect('contact_information.db')
    cursor = conn.execute("SELECT name, von, bis, nachname, kw, user_stunden_montag, user_beschreibung_montag, user_stunden_dienstag, user_beschreibung_dienstag, user_stunden_mittwoch, user_beschreibung_mittwoch, user_stunden_donnerstag, user_beschreibung_donnerstag, user_stunden_freitag, user_beschreibung_freitag from CONTACT_INFORMATION")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results