# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("01_intermedio/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Jorge\nMi apellido es Orellana\n45 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Cobol")
print(txt_file.readline())

txt_file.close()

with open("01_intermedio/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

# Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# .json file


json_file = open("01_intermedio/my_file.json", "w+")

json_test = {
    "name": "Jorge Eduardo",
    "surname": "Orellana",
    "age": 45,
    "languages": ["Python", "Cobol"],
    "website": "https://jeodev.com.ar"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("01_intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("01_intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("01_intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Jorge", "Orellana", 45, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("01_intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?