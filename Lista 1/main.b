import data as dt
import utils_b as ut

ut.add_person(dt.people_data, "Naomi", 86, "Porto", ["ler", "escrever"])
print(dt.people_data)

print("-" * 100)

ut.remove_person(dt.people_data, "Alice")
print(dt.people_data)

print("-" * 100)

ut.get_ages(dt.people_data)

print("-" * 100)

ut.get_hobbies(dt.people_data)
print(ut.get_hobbies(dt.people_data))

print("-" * 100)

hobbie =  ['photography','hiking', 'reading', 'cooking', 'gardening', 'ler', 'correr']
ut.get_people_by_hobbies(dt.people_data, hobbie )

#print(ut.get_people_by_hobbies(dt.people_data, hobbie))
