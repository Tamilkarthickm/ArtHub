book = {}
book['Tamil'] = {
    'Name': 'Tamil',
    'Address': '1/100, Bajanai Kovilstr, Arakkonam TN',
    'Phone': 8977511145
}
book['Moni'] = {
    'Name': 'Moni',
    'Address': '1/137, New Agravaram, Mukundraiyapuram, Ranipet TN',
    'Phone': 9823981606
}
book['Adhiran'] = {
    'Name': 'Adhiran',
    'Address': '1/100, Bajanai Kovilstr, Arakkonam TN',
    'Phone': 9190947659
}

import json
s_book = json.dumps(book)
with open("C://Codepy//json_book.txt", "w") as f:
    f.write(s_book)

