url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

protocol, seperator, rest_of_url = url.partition('://')
host, seperator, document_with_path = rest_of_url.partition('/')
print(host)
path, seperator, document = document_with_path.rpartition('/')
print(path)

