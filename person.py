from peewee import *

from datetime import date

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


def create_and_connect():
    db.connect()
    db.create_tables([Person, Pet], safe=True)


def create_family_members():
    uncle_tommy = Person(name="tommy", birthday=date(2000, 11, 11, ), is_relative=True)
    uncle_tommy.save()

    grandma_ana = Person.create(name="Ana", birthday=date(1960, 10, 10), is_relative=False)
    grandma_rosa = Person.create(name="rosa", birthday=date(1960, 10, 10), is_relative=False)

    tommys_dog = Pet.create(owner=uncle_tommy, name="fido", animal_type="perro")
    anas_cat = Pet.create(owner=grandma_ana, name="pelusa", animal_type="gato")

    tommys_dog.name = "firulais"
    tommys_dog.save()


def get_family_members():
    for person in Person.select():
        print("nombre : {}  fecha de nacimiento  : {}    ".format(person.name, person.birthday))


def get_family_member_birthday(name):
    family_member = Person.select().where(Person.name == name).get()
    print("{} Cumple el: {}".format(name, family_member.birthday))



def delete_pet(name):
        fido = Pet.get().where(Pet.name == "fido" )
       deleted_entry = fido.delete_instance()
        print ("{} registros borrados ".format(deleted_entry))


create_and_connect()

