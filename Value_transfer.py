class ValueTransfer:

    def __init__(self):
        pass

    #when the db is created the valies are specified to be NOT NuLL
    # prob future error
    name = None
    von = None
    bis = None
    nachname = None
    kw = None
    user_stunden_montag = None
    user_beschreibung_montag = None
    user_stunden_dienstag = None
    user_beschreibung_dienstag = None
    user_stunden_mittwoch = None
    user_beschreibung_mittwoch = None
    user_stunden_donnerstag = None
    user_beschreibung_donnerstag = None
    user_stunden_freitag = None
    user_beschreibung_freitag = None
    
    def set_name(self, value):
        self.name = value
        return self
    def get_name(self):
        return self.name

    def set_von(self, value):
        self.von = value
        return self
    def get_von(self):
        return self.von

    def set_bis(self, value):
        self.Bis = value
        return self
    def get_bis(self):
        return self.Bis

    def set_nachname(self, value):
        self.Nachname = value
        return self
    def get_nachname(self):
        return self.Nachname

    def set_von_bis_nachname(self, value):
        self.vonBisNachname = value
        return self
    def get_von_bis_nachname(self):
        return self.vonBisNachname

    def set_kw(self, value):
        self.kw = value
        return self
    def get_kw(self):
        return self.kw

    def set_user_stunden_montag(self, value):
        self.user_stunden_montag = value
        return self
    def get_user_stunden_montag(self):
        return self.user_stunden_montag

    def set_user_beschreibung_montag(self, value):
        self.user_beschreibung_montag = value
        return self
    def get_user_beschreibung_montag(self):
        return self.user_beschreibung_montag

    def set_user_stunden_dienstag(self, value):
        self.user_stunden_dienstag = value
        return self
    def get_user_stunden_dienstag(self):
        return self.user_stunden_dienstag

    def set_user_beschreibung_dienstag(self, value):
        self.user_beschreibung_dienstag = value
        return self
    def get_user_beschreibung_dienstag(self):
        return self.user_beschreibung_dienstag

    def set_user_stunden_mittwoch(self, value):
        self.user_stunden_mittwoch = value
        return self
    def get_user_stunden_mittwoch(self):
        return self.user_stunden_mittwoch

    def set_user_beschreibung_mittwoch(self, value):
        self.user_beschreibung_mittwoch = value
        return self
    def get_user_beschreibung_mittwoch(self):
        return self.user_beschreibung_mittwoch

    def set_user_stunden_donnerstag(self, value):
        self.user_stunden_donnerstag = value
        return self
    def get_user_stunden_donnerstag(self):
        return self.user_stunden_donnerstag

    def set_user_beschreibung_donnerstag(self, value):
        self.user_beschreibung_donnerstag = value
        return self
    def get_user_beschreibung_donnerstag(self):
        return self.user_beschreibung_donnerstag

    def set_user_stunden_freitag(self, value):
        self.user_stunden_freitag = value
        return self
    def get_user_stunden_freitag(self):
        return self.user_stunden_freitag

    def set_user_beschreibung_freitag(self, value):
        self.user_beschreibung_freitag = value
        return self
    def get_user_beschreibung_freitag(self):
        return self.user_beschreibung_freitag

    # def set_temp(self, value):
    #     self.temp = value
    #     return self
    # def get_temp(self):
    #     return self.temp
