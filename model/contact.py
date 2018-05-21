

class Contact:

    def __init__(self, f_name=None, l_name=None, company=None, idd=None, full_name=None):
        self.f_name = f_name
        self.l_name = l_name
        self.company = company
        self.idd = idd
        self.full_name = full_name

    def __repr__(self):
        return "%s:%s" % (self.idd, self.full_name)

    def __eq__(self, other):
        return self.idd == other.idd and self.full_name == other.full_name
