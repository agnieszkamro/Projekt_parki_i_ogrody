from tkinter import *

import tkintermapview
from geocoder import location

users: list=[]
parks: list=[]
employees: list=[]

class Park:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name} {self.location}')

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]

class Employee:
    def __init__(self, name, surname, park, location, age):
        self.name = name
        self.surname = surname
        self.park = park
        self.location = location
        self.age = age
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name} {self.surname}')

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


class User:
    def __init__(self, name, surname, location):
        self.name=name
        self.surname=surname
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name} {self.surname}')

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]
#########################################################
#PARK
##dodaj park
def add_park()->None:
    name = entry_nazwa_park.get()
    location = entry_miejscowosc_park.get()

    park = Park(name=name, location=location)
    parks.append(park)
    show_all_parks()
    entry_nazwa_park.delete(0, END)
    entry_miejscowosc_park.delete(0, END)

    entry_nazwa_park.focus()

    #map_widget.set_marker(park.coordinates[0], park.coordinates[1], text=f"{name} {location}")
    #print(parks)

def show_all_parks()->None:
    listbox_lista_parkow.delete(0, END)
    for idx, park in enumerate(parks):
        listbox_lista_parkow.insert(idx, f"{idx + 1}. {park.name} ({park.location})")


def remove_park():
    i = listbox_lista_parkow.index(ACTIVE)
    print(i)
    parks[i].marker.delete()
    parks.pop(i)
    show_all_parks()

def edit_park()->None:
    i=listbox_lista_parkow.index(ACTIVE)
    name=parks[i].name
    location=parks[i].location

    entry_nazwa_park.insert(0, name)
    entry_miejscowosc_park.insert(0, location)

    button_dodaj_park.config(text='Zapisz', command=lambda: update_park(i))

def update_park(i)->None:
    name= entry_nazwa_park.get()
    location= entry_miejscowosc_park.get()

    parks[i].name = name
    parks[i].location = location

    parks[i].coordinates=parks[i].get_coordinates()
    parks[i].marker.delete()
    parks[i].marker= map_widget.set_marker(parks[i].coordinates[0], parks[i].coordinates[1], text=f"{parks[i].name} {parks[i].location}")

    show_all_parks()
    button_dodaj_park.config(text='Dodaj', command=add_park)

    entry_nazwa_park.delete(0, END)
    entry_miejscowosc_park.delete(0, END)

    entry_nazwa_park.focus()

def show_selected_park() -> None:
    sel = listbox_lista_parkow.curselection()
    if not sel:
        return
    p = parks[sel[0]]
    map_widget.set_zoom(14)
    map_widget.set_position(p.coordinates[0], p.coordinates[1])

#####################################################################################################
#EMPLOYEE - OGRODNICY
def add_employee()->None:
    name = entry_imie_og.get()
    surname = entry_nazwisko_og.get()
    park = entry_nazwa_park_og.get()
    location = entry_miejscowosc_og.get()
    age = entry_wiek_og.get()

    employee = Employee(name=name, surname=surname, park=park, location=location, age=age)
    employees.append(employee)
    show_all_employees()

    entry_imie_og.delete(0, END)
    entry_nazwisko_og.delete(0, END)
    entry_nazwa_park_og.delete(0, END)
    entry_miejscowosc_og.delete(0, END)
    entry_wiek_og.delete(0, END)

    entry_imie_og.focus()


def show_all_employees()->None:
    listbox_lista_ogrodnikow.delete(0, END)
    for idx, employee in enumerate(employees):
        listbox_lista_ogrodnikow.insert(idx, f'{idx + 1}. {employee.name} {employee.surname}')


def remove_employee():
    i = listbox_lista_ogrodnikow.index(ACTIVE)
    print(i)
    employees[i].marker.delete()
    employees.pop(i)
    show_all_employees()

def edit_employee()->None:
    i=listbox_lista_ogrodnikow.index(ACTIVE)
    name=employees[i].name
    surname=employees[i].surname
    park=employees[i].park
    location=employees[i].location
    age=employees[i].age

    entry_imie_og.insert(0, name)
    entry_nazwisko_og.insert(0, surname)
    entry_nazwa_park_og.insert(0, park)
    entry_miejscowosc_og.insert(0, location)
    entry_wiek_og.insert(0, age)

    button_dodaj_pracownika.config(text='Zapisz', command=lambda: update_employee(i))

def update_employee(i)->None:
    name= entry_imie_og.get()
    surname=entry_nazwisko_og.get()
    park=entry_nazwa_park_og.get()
    location=entry_miejscowosc_og.get()
    age=entry_wiek_og.get()


    employees[i].name = name
    employees[i].surname = surname
    employees[i].park = park
    employees[i].location = location
    employees[i].age = age

    employees[i].coordinates=employees[i].get_coordinates()
    employees[i].marker.delete()
    employees[i].marker= map_widget.set_marker(employees[i].coordinates[0], employees[i].coordinates[1], text=f"{employees[i].name} {employees[i].location}")

    show_all_employees()
    button_dodaj_pracownika.config(text='Dodaj', command=add_employee)

    entry_imie_og.delete(0, END)
    entry_nazwisko_og.delete(0, END)
    entry_nazwa_park_og.delete(0, END)
    entry_miejscowosc_og.delete(0, END)
    entry_wiek_og.delete(0, END)

    entry_imie_og.focus()

def show_selected_employee() -> None:
    sel = listbox_lista_ogrodnikow.curselection()
    if not sel:
        return
    e = employees[sel[0]]
    map_widget.set_zoom(14)
    map_widget.set_position(e.coordinates[0], e.coordinates[1])

############################################################
#EMPLOYEE FROM PARK
#def show_employees_park()->None:
#    listbox_lista_ogrodnikow.delete(0, END)
#    for idx,user in enumerate(users):
#        listbox_lista_obiektow.insert(idx, f'{idx+1}. {user.name} {user.surname}')



########################################################################################
def add_user()->None:
    name = entry_imie_u.get()
    surname = entry_nazwisko_u.get()
    location = entry_miejscowosc_u.get()

    user = User(name=name, surname=surname, location=location)
    users.append(user)
    #map_widget.set_marker(user.coordinates[0], user.coordinates[1], text=f"{name} {surname}")
    #print(users)
    show_users()

    entry_imie_u.delete(0, END)
    entry_nazwisko_u.delete(0, END)
    entry_miejscowosc_u.delete(0, END)

    entry_imie_u.focus()



def show_users():
    listbox_lista_uzytkownikow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_uzytkownikow.insert(idx, f'{idx+1}. {user.name} {user.surname}')


def remove_user():
    i = listbox_lista_uzytkownikow.index(ACTIVE)
    print(i)
    users[i].marker.delete()
    users.pop(i)
    show_users()

def edit_user()->None:
    i=listbox_lista_uzytkownikow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location


    entry_imie_u.insert(0, name)
    entry_nazwisko_u.insert(0, surname)
    entry_miejscowosc_u.insert(0, location)

    button_dodaj_uzytkownika.config(text='Zapisz', command=lambda: update_user(i))

def update_user(i)->None:
    name= entry_imie_u.get()
    surname= entry_nazwisko_u.get()
    location= entry_miejscowosc_u.get()

    users[i].name = name
    users[i].surname = surname
    users[i].location = location

    users[i].coordinates=users[i].get_coordinates()
    users[i].marker.delete()
    users[i].marker= map_widget.set_marker(users[i].coordinates[0], users[i].coordinates[1], text=f"{users[i].name} {users[i].surname}")

    show_users()
    button_dodaj_uzytkownika.config(text='Dodaj', command=add_user)

    entry_imie_u.delete(0, END)
    entry_nazwisko_u.delete(0, END)
    entry_miejscowosc_u.delete(0, END)

    entry_imie_u.focus()

#def show_user_details():
#    i=listbox_lista_uzytkownikow.index(ACTIVE)
#    label_szczegoly_obiektu_name_wartosc.config(text=users[i].name)
#    label_szczegoly_obiektu_surname_wartosc.config(text=users[i].surname)
#    label_szczegoly_obiektu_miejscowosc_wartosc.config(text=users[i].location)
#    label_szczegoly_obiektu_posts_wartosc.config(text=users[i].posts)

#    map_widget.set_zoom(15)
#    map_widget.set_position(users[i].coordinates[0],users[i].coordinates[1])















#GUI

root= Tk()
root.geometry("1500x800")
root.title("Projekt_Parki_i_ogrody")


ramka_generowanie_map=Frame(root)
ramka_parki_i_ogrody = Frame(root, width=220)
ramka_ogrodnicy=Frame(root)
ramka_uzytkownicy=Frame(root)
ramka_mapa=Frame(root)


ramka_generowanie_map.grid(row=0, column=0)
ramka_parki_i_ogrody.grid(row=0, column=1, sticky=N)
ramka_ogrodnicy.grid(row=0, column=2)
ramka_uzytkownicy.grid(row=0, column=3, sticky=N)
ramka_mapa.grid(row=6, column=0, columnspan=5)


#ramka_generowanie_map
label_generownie_map=Label(ramka_generowanie_map, text="Generuj mapę: ")
label_generownie_map.grid(row=0, column=0, sticky='w')
button_parki_i_ogrody= Button(ramka_generowanie_map, text="Parki i ogrody", command=show_all_parks)
button_parki_i_ogrody.grid(row=1, column=0, sticky='w')
button_ogrodnicy= Button(ramka_generowanie_map, text='Ogrodnicy', command=show_all_employees)
button_ogrodnicy.grid(row=2, column=0, sticky='w')
button_ogrodnicy_dla_parku= Button(ramka_generowanie_map, text='Ogrodnicy dla wybranego parku', command=show_users)
button_ogrodnicy_dla_parku.grid(row=3, column=0, sticky='w')



#######################################
#poprawione listy

listbox_lista_parkow= Listbox(ramka_parki_i_ogrody, width=30, height=10)
listbox_lista_parkow.grid(row=0, column=1, sticky=N)

listbox_lista_ogrodnikow= Listbox(ramka_ogrodnicy, width=30, height=10)
listbox_lista_ogrodnikow.grid(row=0, column=2, columnspan=3)

listbox_lista_uzytkownikow= Listbox(ramka_uzytkownicy, width=20, height=10)
listbox_lista_uzytkownikow.grid(row=0, column=3, columnspan=3)
########################################



############################################################################
#ramka_ogrodnicy
label_park_og=Label(ramka_ogrodnicy, text="Pracownicy: ")
label_park_og.grid(row=0, column=0,)

label_imie_og=Label(ramka_ogrodnicy, text="Imie: ")
label_imie_og.grid(row=1, column=1, sticky=E)

label_nazwisko_og=Label(ramka_ogrodnicy, text="Nazwisko: ")
label_nazwisko_og.grid(row=2, column=1, sticky=E)

label_miejscowosc_og=Label(ramka_ogrodnicy, text="Miejscowość: ")
label_miejscowosc_og.grid(row=3, column=1, sticky=E)

label_nazwa_park_og=Label(ramka_ogrodnicy, text="Park: ")
label_nazwa_park_og.grid(row=4, column=1, sticky=E)

label_age=Label(ramka_ogrodnicy, text="Wiek: ")
label_age.grid(row=5, column=1, sticky=E)


entry_imie_og=Entry(ramka_ogrodnicy)
entry_imie_og.grid(row=1, column=2)

entry_nazwisko_og=Entry(ramka_ogrodnicy)
entry_nazwisko_og.grid(row=2, column=2)

entry_miejscowosc_og=Entry(ramka_ogrodnicy)
entry_miejscowosc_og.grid(row=3, column=2)

entry_nazwa_park_og=Entry(ramka_ogrodnicy)
entry_nazwa_park_og.grid(row=4, column=2)

entry_wiek_og=Entry(ramka_ogrodnicy)
entry_wiek_og.grid(row=5, column=2)


button_dodaj_pracownika=Button(ramka_ogrodnicy, text='Dodaj pracownika', command=add_employee)
button_dodaj_pracownika.grid(row=1, column=5)
button_usun_ogrodnika = Button(ramka_ogrodnicy, text="Usuń", command=remove_employee)
button_usun_ogrodnika.grid(row=2, column=5)

button_edytuj_ogrodnika = Button(ramka_ogrodnicy, text="Edytuj", command=edit_employee)
button_edytuj_ogrodnika.grid(row=3, column=5)

button_pokaz_ogrodnika = Button(ramka_ogrodnicy, text="Pokaż", command=show_selected_employee)
button_pokaz_ogrodnika.grid(row=4, column=5)
####################################################################################################################

#RAMKA_PARKI
label_park=Label(ramka_parki_i_ogrody, text="Parki: ")
label_park.grid(row=0, column=0, padx=30)

label_nazwa = Label(ramka_parki_i_ogrody, text="Nazwa parku:")
label_nazwa.grid(row=1, column=0, padx=30)

entry_nazwa_park = Entry(ramka_parki_i_ogrody)
entry_nazwa_park.grid(row=1, column=1, padx=30)

label_miejscowosc_park = Label(ramka_parki_i_ogrody, text="Miejscowość:")
label_miejscowosc_park.grid(row=2, column=0, padx=30)

entry_miejscowosc_park = Entry(ramka_parki_i_ogrody)
entry_miejscowosc_park.grid(row=2, column=1, padx=30)

button_dodaj_park = Button(ramka_parki_i_ogrody, text="Dodaj park", command=lambda: add_park())
button_dodaj_park.grid(row=3, column=0, sticky=W)

button_usun_park = Button(ramka_parki_i_ogrody, text="Usuń park", command=remove_park)
button_usun_park.grid(row=3, column=0, sticky=E)

button_edytuj_park = Button(ramka_parki_i_ogrody, text="Edytuj park", command=edit_park)
button_edytuj_park.grid(row=3, column=1, sticky=W)

button_pokaz_park = Button(ramka_parki_i_ogrody, text="Pokaż park", command=show_selected_park)
button_pokaz_park.grid(row=3, column=1, sticky=E)
#############################################################################################################


#RAMKA users
label_park=Label(ramka_uzytkownicy, text="Użytkownicy: ")
label_park.grid(row=0, column=0, padx=30)

label_imie=Label(ramka_uzytkownicy, text="Imie: ")
label_imie.grid(row=1, column=2, sticky=W)

label_nazwisko=Label(ramka_uzytkownicy, text="Nazwisko: ")
label_nazwisko.grid(row=2, column=2, sticky=W)

label_miejscowosc=Label(ramka_uzytkownicy, text="Miejscowość: ")
label_miejscowosc.grid(row=3, column=2, sticky=W)

entry_imie_u=Entry(ramka_uzytkownicy)
entry_imie_u.grid(row=1, column=3, sticky=E)

entry_nazwisko_u=Entry(ramka_uzytkownicy)
entry_nazwisko_u.grid(row=2, column=3)

entry_miejscowosc_u=Entry(ramka_uzytkownicy)
entry_miejscowosc_u.grid(row=3, column=3)

button_dodaj_uzytkownika=Button(ramka_uzytkownicy, text='Dodaj użytkownika', command=add_employee)
button_dodaj_uzytkownika.grid(row=5, column=3)

#ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1500, height=450, corner_radius=0)
map_widget.grid(row=2, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)




root.mainloop()