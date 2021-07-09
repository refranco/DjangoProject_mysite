import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

"""Script para leer un csv específico e importarlo a una base de datos que tiene una relación many to one.py

REQUISITOS: instalar django-extensions: pip3 install django-extensions
            crear una carpeta {scripts} dentro de la carpeta del proyecto
            crear un archivo {__init__.py} dentro de la carpeta {scripts}
            este archivo, debe ir dentro de la carpeta scripts. 
            para correr el archivo usar:
            python3 manage.py runscript {nombre_script} sin extension, ejemplo:"""
# python3 manage.py runscript cats_load

from cats.models import Cat, Breed

def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Cat.objects.all().delete()
    Breed.objects.all().delete()

    # Name,Breed,Weight
    # Abby,Sphinx,6.4
    # Annie,Burmese,7.6
    # Ash,Manx,7.8
    # Athena,Manx,8.9
    # Baby,Tabby,6.9

    for row in reader:
        print(row)

        b, created = Breed.objects.get_or_create(name=row[1])

        c = Cat(nickname=row[0], breed=b, weight=row[2])
        c.save()

