import re


def test_info_on_homepage(app):
    info_from_home_page = app.contact.get_contacts_list()[0]
    info_from_edit = app.contact.get_info_from_edit(0)
    assert info_from_home_page.info == info_from_edit.info
    assert info_from_home_page.f_name == info_from_edit.f_name
    assert info_from_home_page.l_name == info_from_edit.l_name
    assert info_from_home_page.company == info_from_edit.company
    assert info_from_home_page.id == info_from_edit.id


def test_selected_list(app):
    info_from_select = app.contact.get_info_from_select(0)
    info_from_edit = app.contact.get_info_from_edit(0)
<<<<<<< HEAD
    assert info_from_select.info == info_from_edit.info
=======
#    assert info_from_select.info == clear(info_from_edit.info)
>>>>>>> fe9a84b808f15488dcd9531a5c6b7a3aae934ab5
    assert info_from_select.f_name == clear(info_from_edit.f_name)
    assert info_from_select.l_name == clear(info_from_edit.l_name)
    assert info_from_select.company == clear(info_from_edit.company)
    assert info_from_select.id == clear(info_from_edit.id)
    assert info_from_select.phone == clear(info_from_edit.phone)


def clear(s):
<<<<<<< HEAD
    return re.sub("[(+) -]", "", s)


def test_print_two_lists(app):
    info_from_select = app.contact.get_info_from_select(0)
    info_from_edit = app.contact.get_info_from_edit(0)
    assert clear(info_from_select.info) == merge_info(info_from_edit)
    print("seelcted: " + str(app.contact.get_info_from_select(0)))
    print("selected info: " + str(info_from_select.info))
    print("edited info: " + str(info_from_edit.info))


def merge_info(contact):
    return "".join(map(lambda x: clear(x), [contact.f_name, contact.l_name, contact.company]))
=======
    return re.sub("[(+)-]", "", s)
>>>>>>> fe9a84b808f15488dcd9531a5c6b7a3aae934ab5
