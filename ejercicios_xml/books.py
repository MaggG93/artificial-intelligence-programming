# IMPORTS
import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

# Ejercicio 1 (Atributos y Texto): Muestra por pantalla el ID del libro (id), 
# su título (title) y su autor (author) con el siguiente formato:
# [ID: <id>] "<title>" de <author>

# BUSCAR LIBRO EN LA RAÍZ
for book in root.findall("book"):
     id_book = book.get("id") 
     title = book.find("title").text 
     author = book.find("author").text
     
     # PRINT
     print(f'[ID: {id_book}] "{title}" de {author}')

# Ejercicio 2 (Extracción con atributos secundarios): Imprime el título del libro junto con su precio (price) y la moneda (currency) que viene dentro del atributo del precio. 
# Formato:
# "<title>" cuesta <price> <currency>

for book in root.findall("book"):
    title = book.find("title").text
    price_element = book.find("price") # Obtengo el elemento price completo
    price = price_element.text # Saco el price de dicho elemento
    currency = price_element.get("currency") # Saco el currency de dicho elemento

    # PRINT
    print(f'{title} cuesta {price} {currency}')

# Ejercicio 3 (Filtrado por condición de inventario): Muestra el título de los libros que tienen stock disponible (stock mayor a 0) e indica cuántas unidades quedan. 
# Formato: 
# Quedan <stock> unidades de "<title>"

for book in root.findall("book"):
    stock = int(book.find("stock").text)

    if stock > 0:
        title = book.find("title").text
        
        # PRINT
        print(f'Quedan {stock} unidades de {title}')

# Ejercicio 4 (Filtrado por atributo de categoría): Muestra únicamente los libros de la categoría "tecnologia", 
# imprimiendo su título y autor con el formato: 
# [Tecnología] "<title>" - <author>

for book in root.findall("book[@category='tecnologia']"):
    title = book.find("title").text
    author = book.find("author").text
    
    # PRINT
    print(f'[Tecnología] {title} - {author}')
     