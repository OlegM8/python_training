from sys import maxsize


class Contact:

    def __init__(self, f_name=None, l_name=None, company=None, id=None, full_name=None):
        self.f_name = f_name
        self.l_name = l_name
        self.company = company
        self.id = id
        self.full_name = full_name

    def __repr__(self):
        return "%s:%s" % (self.id, self.full_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.full_name == other.full_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize