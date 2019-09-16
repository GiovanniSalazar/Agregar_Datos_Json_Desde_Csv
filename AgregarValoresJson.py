# encoding=utf8
import sys
import json
import fnmatch
import os
import csv
from collections import OrderedDict
###########
# python3 AgregarValoresJson.py
###########

#Rutas in y out de los documentos json.
ruta_in="doc_json/"
ruta_out="doc_json_nuevos/"

#Archivo csv a leer y agregar en documentos json.
archivocsv='ultimo_trabajo.csv'

#Función para agregar los valores
def AgregarValoresDocJson():

    # Abre el csv para leer la ruta del archivo json dependiendo del campo 1 del dni
    with open(archivocsv,encoding='utf-8') as ac:
        lc = csv.reader(ac)
        for row in lc:
            #Validamos si el archivo existe dependiendo de el valor del campo del csv
            if os.path.isfile(ruta_in+str(row[0])+".json"):
                #armamos el dic json
                empresa=str(row[1])
                puesto=str(row[2])
                salario=str(row[3])
                inicio=str(row[4])
                fin=str(row[5])
                
                #Dic que almacenara los nuevos valores.
                ultimo_puesto = {}                    
                ultimo_puesto.update({"empresa": str(empresa)})
                ultimo_puesto.update({"puesto": str(puesto)})
                ultimo_puesto.update({"salario": str(salario)})
                ultimo_puesto.update({"inicio": str(inicio)})
                ultimo_puesto.update({"fin": str(fin)})
                print(ultimo_puesto)
                #Abrimos el documento json
                with open(ruta_in+str(row[0])+".json") as json_doc:
                    data = json.load(json_doc,object_pairs_hook=OrderedDict)#usamos OrderedDict para no alterar el orden del doc
                    data.update({"ultimo_puesto" : ultimo_puesto})
                    print(data)
                #Guardamos el documento en una nueva carpeta                        
                with open(ruta_out+str(row[0])+".json",'w') as jd:
                    #Realizamos el dump de "data" del open de arriba
                    json.dump(data,jd,ensure_ascii=False)# aseguramos el utf-8 con ensure_ascii=False
                 
if __name__ == '__main__':
    AgregarValoresDocJson()