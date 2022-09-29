import sqlite3


def get_connection():
    return sqlite3.connect('contact_information.db')


def insert_contact(value_transfer):
    conn = get_connection()
    conn.execute(
                "INSERT INTO CONTACT_INFORMATION "
                    "(NAME,"
                    "VON,"
                    "BIS,"
                    "NACHNAME,"
                    "KW,"
                    "USER_STUNDEN_MONTAG,"
                    "USER_BESCHREIBUNG_MONTAG,"
                    "USER_STUNDEN_DIENSTAG,"
                    "USER_BESCHREIBUNG_DIENSTAG,"
                    "USER_STUNDEN_MITTWOCH,"
                    "USER_BESCHREIBUNG_MITTWOCH,"
                    "USER_STUNDEN_DONNERSTAG,"
                    "USER_BESCHREIBUNG_DONNERSTAG,"
                     "USER_STUNDEN_FREITAG,"
                     "USER_BESCHREIBUNG_FREITAG) "
                 "VALUES "
                    "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (value_transfer.get_name(),
                  value_transfer.get_von(),
                  value_transfer.get_bis(),
                  value_transfer.get_nachname(),
                  value_transfer.get_kw(),
                  value_transfer.get_user_stunden_montag(),
                  value_transfer.get_user_beschreibung_montag(),
                  value_transfer.get_user_stunden_dienstag(),
                  value_transfer.get_user_beschreibung_dienstag(),
                  value_transfer.get_user_stunden_mittwoch(),
                  value_transfer.get_user_beschreibung_mittwoch(),
                  value_transfer.get_user_stunden_donnerstag(),
                  value_transfer.get_user_beschreibung_donnerstag(),
                  value_transfer.get_user_stunden_freitag(),
                  value_transfer.get_user_beschreibung_freitag())
                )
    conn.commit()
    conn.close()


def delete_contact_by_name(name):
    conn = get_connection()
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?",(name,))
    conn.close()


def edit_address_by_name(name, address):
    conn = get_connection()
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, address))
    conn.commit()
    conn.close()


def edit_phone_number_by_name(name, phone_number):
    conn = get_connection()
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, phone_number))
    conn.close()


def retrieve_contacts():
    results = []

    query = "SELECT " \
                "name, " \
                "nachname, " \
                "von, " \
                "bis, " \
                "kw, " \
                "user_stunden_montag, " \
                "user_beschreibung_montag, user_stunden_dienstag, " \
                "user_beschreibung_dienstag, user_stunden_mittwoch, " \
                "user_beschreibung_mittwoch, user_stunden_donnerstag, " \
                "user_beschreibung_donnerstag, user_stunden_freitag, " \
                "user_beschreibung_freitag " \
            "from " \
                "CONTACT_INFORMATION"

    conn = get_connection()
    cursor = conn.execute(query)
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results