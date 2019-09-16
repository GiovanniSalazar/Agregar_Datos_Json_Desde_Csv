# Agregar objetos a documentos json desde datos en csv | ES

El presente script agrega objetos a documentos json dinamicamente .El escenario es tener una lista de documentos json , cada documento json representa a un documento de indentidad con la información de la persona.Adicional a esto se tiene un csv con el numero de documento de identidad con los valores adicionales que se desean agregar a cada documento json.

  - documentos json : cada documento json tiene la información de los datos personales de cada trabajador , el nombre del documento es igual al # de DNI de la persona.
  - csv : Tiene la información del ultimo puesto de trabajo de cada persona. 


# Ejecución:

  - python3 AgregarValoresJson.py
