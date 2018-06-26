from sys import maxsize


class Contact:

    def __init__(self, f_name=None, l_name=None, company=None, id=None, info=None, phone=None):
        self.f_name = f_name
        self.l_name = l_name
        self.company = company
        self.id = id
        self.info = info
        self.phone = phone


    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.info, self.f_name, self.company)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.info == other.info

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize