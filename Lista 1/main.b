import data as dt
import utils as ut

ut.add_person(dt.people_data, "Naomi", 86, "Porto", ["ler", "escrever"])
print(dt.people_data)

print("#" * 80)

ut.remove_person(dt.people_data, "Alice")
print(dt.people_data)

print("#" * 80)

ut.get_ages(dt.people_data)

print("#" * 80)

ut.get_hobbies(dt.people_data)
