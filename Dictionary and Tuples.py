dict = {"Karthick":99916191919, "Moni":94998419849, "Adhiran": 9481919199, "Anna":8184815181}
# print(dict)
dict["Appa"] = 5781888181
# print(dict)
del dict["Appa"]
# print(dict)

##Method 1 to access and print dictionary

for person in dict:
    print("Name:", person, "Mobile No:", dict[person])
print("\n")
##Method 1 End


##Method 2 to access and print dictionary

for person, Mobile in dict.items():
    print("Name:", person, "Mobile No:", Mobile)


"""
Tuples Test Code
It is used to have different types of data unlike list(Homogenous values) but Tuples are Heterogenous.
Example Address contains Alpa-numeric and List is either numeric or Alpha and coordinates
Tuples are immutable whereas List we can change the value(Mutable)
"""
point = (4,5) #x and y Coordinates
