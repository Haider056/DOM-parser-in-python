from xml.dom import minidom
import csv
xmldoc = minidom.parse('compiler.xml')
book_list = []
for book in xmldoc.getElementsByTagName('book'):
    book_id = book.getAttribute('id')
    author_name = book.getElementsByTagName('author')[0].firstChild.nodeValue
    title = book.getElementsByTagName('title')[0].firstChild.nodeValue
    genre = book.getElementsByTagName('genre')[0].firstChild.nodeValue
    price = book.getElementsByTagName('price')[0].firstChild.nodeValue
    publish_date = book.getElementsByTagName('publish_date')[0].firstChild.nodeValue
    description = book.getElementsByTagName('description')[0].firstChild.nodeValue
    book_list.append([book_id,author_name,title,genre,price,publish_date,description])

with open('200901056.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Book_id','Author_Name','Title','Genre','Price','Publish_date','Description'])
    for book in book_list:
        writer.writerow(book)
print("File created")