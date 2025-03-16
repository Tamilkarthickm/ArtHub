import json
s_open = open("c://Codepy//json_book.txt", "r")
s_read = s_open.read()
# print(s_read)
book_dict = json.loads(s_read)
# print(book_dict)
data_type = type(book_dict)
# print(data_type)
book_record = book_dict['Tamil']
# print(book_record)
phone = book_dict['Tamil']['Phone']
# print(phone)
for person in book_dict:
    print(book_dict[person])

