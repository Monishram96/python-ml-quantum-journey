##DICTIONARY##

marks={"Mram": 96,"Monish": 27,"Moam":100}
print("Initial:",marks)


### READ/UPDATE/INNSERT

print("Mram :",marks["Mram"]) # access value
marks["Monish"]= 97
marks["Monishram"]= 27
print("After updates:",marks)


### SAFE ACCESS

print("esha in marks?", "Esha" in marks)
print("Esha via get:", marks.get("Esha","Not Found"))


### DELETE

removed = marks.pop("Monish",None)
print("Removed:", removed)
print("Now:",marks)
