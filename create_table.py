import sqlite3

conn = sqlite3.connect('contact_information.db')
query = (''' CREATE TABLE CONTACT_INFORMATION
            (NAME	                        TEXT    NOT NULL,
            VON    		                    INT,
            BIS		                        INT,
            NACHNAME                        TEXT    NOT NULL,
            KW		                        INT,
            USER_STUNDEN_MONTAG		        INT,
            USER_BESCHREIBUNG_MONTAG        TEXT    NOT NULL,
            USER_STUNDEN_DIENSTAG		    INT,
            USER_BESCHREIBUNG_DIENSTAG      TEXT    NOT NULL,
            USER_STUNDEN_MITTWOCH		    INT,
            USER_BESCHREIBUNG_MITTWOCH      TEXT    NOT NULL,
            USER_STUNDEN_DONNERSTAG		    INT,
            USER_BESCHREIBUNG_DONNERSTAG    TEXT    NOT NULL,
            USER_STUNDEN_FREITAG		    INT,
            USER_BESCHREIBUNG_FREITAG       TEXT    NOT NULL);''')
conn.execute(query)
conn.close()