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
    def __init__(self, name, surname, park, age, salary):
        self.name = name
        self.surname = surname
        self.park = park
        self.age = age
        self.salary = salary
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
    def __init__(self, name, surname, location, posts):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts
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
    name = entry_imie.get()
    location = entry_miejscowosc.get()

    park = Park(name=name, location=location)
    parks.append(park)
    map_widget.set_marker(park.coordinates[0], park.coordinates[1], text=f"{name} {location}")
    print(parks)

##pokaz parki
def show_all_parks()->None:
    name = entry_nazwa_park.get()
    location = entry_miejscowosc.get()

    park = Park(name=name, location=location)
    parks.append(park)
    map_widget.set_marker(park.coordinates[0], park.coordinates[1], text=f"{name} {location}")
    print(parks)


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
    entry_miejscowosc.insert(0, location)

    button_dodaj_park.config(text='Zapisz', command=lambda: update_park(i))

def update_park(i)->None:
    name= entry_nazwa_park.get()
    location= entry_miejscowosc.get()

    parks[i].name = name
    parks[i].location = location

    parks[i].coordinates=parks[i].get_coordinates()
    parks[i].marker.delete()
    parks[i].marker= map_widget.set_marker(parks[i].coordinates[0], parks[i].coordinates[1], text=f"{parks[i].name} {parks[i].location}")

    show_all_parks()
    button_dodaj_park.config(text='Dodaj', command=add_park)

    entry_nazwa_park.delete(0, END)
    entry_miejscowosc.delete(0, END)

    entry_nazwa_park.focus()



###################################################################
#EMPLOYEE
####name, surname, park, age, salary)
def add_employee()->None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    park = entry_nazwa_park.get()
    age = entry_wiek.get()
    salary = entry_placa.get()

    employee = Employee(name=name, surname=surname, park=park, age=age, salary=salary)
    employees.append(employee)
    map_widget.set_marker(employee.coordinates[0], employee.coordinates[1], text=f"{name} {surname}")
    print(employees)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_park.delete(0, END)

    entry_imie.focus()
    show_all_employees()



def show_all_employees()->None:
    listbox_lista_ogrodnikow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_ogrodnikow.insert(idx, f'{idx + 1}. {user.name} {user.surname}')


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
    age=employees[i].age
    salary=employees[i].salary

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_nazwa_park.insert(0, park)
    entry_wiek.insert(0, age)
    entry_placa.insert(0, salary)

    button_dodaj_pracownika.config(text='Zapisz', command=lambda: update_employee(i))

def update_employee(i)->None:
    name= entry_imie.get()
    surname=entry_nazwisko.get()
    park=entry_nazwa_park.get()
    age=entry_wiek.get()
    salary=entry_placa.get()


    employees[i].name = name
    employees[i].surname = surname
    employees[i].park = park
    employees[i].age = age
    employees[i].salary = salary

    employees[i].coordinates=employees[i].get_coordinates()
    employees[i].marker.delete()
    employees[i].marker= map_widget.set_marker(employees[i].coordinates[0], employees[i].coordinates[1], text=f"{employees[i].name} {employees[i].location}")

    show_all_employees()
    button_dodaj_pracownika.config(text='Dodaj', command=add_employee)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_nazwa_park.delete(0, END)
    entry_wiek.delete(0, END)
    entry_placa.delete(0, END)

    entry_imie.focus()


############################################################
#EMPLOYEE FROM PARK
def show_employees_park()->None:
    listbox_lista_ogrodnikow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{idx+1}. {user.name} {user.surname}')




def add_user()->None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    posts = entry_posts.get()

    user = User(name=name, surname=surname, location=location, posts=posts)
    users.append(user)
    map_widget.set_marker(user.coordinates[0], user.coordinates[1], text=f"{name} {surname}")
    print(users)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posts.delete(0, END)

    entry_imie.focus()
    show_users()



def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{idx+1}. {user.name} {user.surname}')


def remove_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users[i].marker.delete()
    users.pop(i)
    show_users()

def edit_user()->None:
    i=listbox_lista_obiektow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location
    posts=users[i].posts

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_miejscowosc.insert(0, location)
    entry_posts.insert(0, posts)

    button_dodaj_objekt.config(text='Zapisz', command=lambda: update_user(i))

def update_user(i)->None:
    name= entry_imie.get()
    surname= entry_nazwisko.get()
    location= entry_miejscowosc.get()
    posts= entry_posts.get()

    users[i].name = name
    users[i].surname = surname
    users[i].location = location
    users[i].posts = posts

    users[i].coordinates=users[i].get_coordinates()
    users[i].marker.delete()
    users[i].marker= map_widget.set_marker(users[i].coordinates[0], users[i].coordinates[1], text=f"{users[i].name} {users[i].surname}")

    show_users()
    button_dodaj_objekt.config(text='Dodaj', command=add_user)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posts.delete(0, END)

    entry_imie.focus()
def show_user_details():
    i=listbox_lista_obiektow.index(ACTIVE)
    label_szczegoly_obiektu_name_wartosc.config(text=users[i].name)
    label_szczegoly_obiektu_surname_wartosc.config(text=users[i].surname)
    label_szczegoly_obiektu_miejscowosc_wartosc.config(text=users[i].location)
    label_szczegoly_obiektu_posts_wartosc.config(text=users[i].posts)

    map_widget.set_zoom(15)
    map_widget.set_position(users[i].coordinates[0],users[i].coordinates[1])















#GUI

root= Tk()
root.geometry("1500x800")
root.title("Projekt_Parki_i_ogrody")


ramka_generowanie_map=Frame(root)
ramka_parki_i_ogrody=Frame(root)
ramka_ogrodnicy=Frame(root)
ramka_uzytkownicy=Frame(root)
ramka_mapa=Frame(root)


ramka_generowanie_map.grid(row=0, column=0, sticky=NW)
ramka_parki_i_ogrody.grid(row=0, column=1, sticky=NW)
ramka_ogrodnicy.grid(row=0, column=2, sticky=NW)
ramka_uzytkownicy.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)


#ramka_generowanie_map
label_generownie_map=Label(ramka_generowanie_map, text="Generuj mapę: ")
label_generownie_map.grid(row=0, column=0, sticky='w')

button_parki_i_ogrody= Button(ramka_generowanie_map, text="Parki i ogrody", command=show_all_parks)
button_parki_i_ogrody.grid(row=1, column=0, sticky='w')
button_ogrodnicy= Button(ramka_generowanie_map, text='Ogrodnicy', command=show_all_employees)
button_ogrodnicy.grid(row=2, column=0, sticky='w')
button_ogrodnicy_dla_parku= Button(ramka_generowanie_map, text='Ogrodnicy dla wybranego parku', command=show_employees_park)
button_ogrodnicy_dla_parku.grid(row=3, column=0, sticky='w')













#######################################
#poprawione listy

listbox_lista_parkow= Listbox(ramka_parki_i_ogrody, width=30, height=10)
listbox_lista_parkow.grid(row=0, column=1, sticky="n")

listbox_lista_ogrodnikow= Listbox(ramka_ogrodnicy, width=30, height=10)
listbox_lista_ogrodnikow.grid(row=0, column=2, columnspan=3)

listbox_lista_uzytkownikow= Listbox(ramka_uzytkownicy, width=50, height=10)
listbox_lista_uzytkownikow.grid(row=0, column=3, columnspan=3)
########################################










############################################################################
#ramka_ogrodnicy
#label_formularz=Label(ramka_formularz, text="Formularz: ")
#label_formularz.grid(row=0, column=0)

label_imie=Label(ramka_ogrodnicy, text="Imie: ")
label_imie.grid(row=1, column=0, sticky=W)

label_nazwisko=Label(ramka_ogrodnicy, text="Nazwisko: ")
label_nazwisko.grid(row=2, column=0, sticky=W)

label_miejscowosc=Label(ramka_ogrodnicy, text="Miejscowość: ")
label_miejscowosc.grid(row=3, column=0, sticky=W)

label_park=Label(ramka_ogrodnicy, text="Park: ")
label_park.grid(row=4, column=0, sticky=W)

label_age=Label(ramka_ogrodnicy, text="Age: ")
label_age.grid(row=5, column=0, sticky=W)

label_salary=Label(ramka_ogrodnicy, text="Płaca: ")

entry_imie=Entry(ramka_ogrodnicy)
entry_imie.grid(row=1, column=1)

entry_nazwisko=Entry(ramka_ogrodnicy)
entry_nazwisko.grid(row=2, column=1)

entry_miejscowosc=Entry(ramka_ogrodnicy)
entry_miejscowosc.grid(row=3, column=1)

entry_park=Entry(ramka_ogrodnicy)
entry_park.grid(row=4, column=1)

entry_wiek=Entry(ramka_ogrodnicy)
entry_wiek.grid(row=5, column=1)

entry_placa=Entry(ramka_ogrodnicy)
entry_placa.grid(row=6, column=1)


button_dodaj_pracownika=Button(ramka_ogrodnicy, text='Dodaj', command=add_employee)
button_dodaj_pracownika.grid(row=5, column=0, columnspan=2)


##################################################################

#ramka_parki
label_park=Label(ramka_parki_i_ogrody, text="Parki: ")
label_park.grid(row=0, column=0,)

label_nazwa = Label(ramka_parki_i_ogrody, text="Nazwa parku:")
label_nazwa.grid(row=1, column=0, sticky=W)

entry_nazwa_park = Entry(ramka_parki_i_ogrody)
entry_nazwa_park.grid(row=1, column=1)

label_miejscowosc = Label(ramka_parki_i_ogrody, text="Miejscowość:")
label_miejscowosc.grid(row=2, column=0, sticky=W)

entry_miejscowosc = Entry(ramka_parki_i_ogrody)
entry_miejscowosc.grid(row=2, column=1)

button_dodaj_park = Button(ramka_parki_i_ogrody, text="Dodaj park", command=lambda: add_park())
button_dodaj_park.grid(row=3, column=0, columnspan=2)

#################################################################

#RAMKA EMPLOYEE




#ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=400, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)







root.mainloop()