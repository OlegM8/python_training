from model.contact import Contact
import random
import string


constant = [
    Contact(f_name="f_name1", l_name="l_name1", company="Company1"),
    Contact(f_name="f_name2", l_name="l_name2", company="Company2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(f_name=random_string("FN", 10), l_name=random_string("LN", 10), company=random_string("C", 10))
    for i in range(1)
]