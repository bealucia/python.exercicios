def add_person(data, name, age, city, hobbies):
    # Verifica se name já existe em data
    for d in data: 
        try:
            if d["name"] == name:
                raise ValueError("Nome já existe")
        except ValueError:
            print("Nome já existe")
            return data
    
    # Verifica se age é válido
    try: 
        if age > 100 or age < 0:
            raise ValueError("Idade precisa ser um inteiro entre 0 e 100")
    except ValueError:
        print("Idade deve ser um inteiro entre 0 e 100")
        return data
    
    # Verifica se hobbies não é uma lista 
    try:  
        if len(hobbies) == 0:
            raise ValueError("A lista de hobbies não pode ser vazia")
    except ValueError:
        print("A lista de hobbies não pode ser vazia")
        return data
    
    # Veerificar se city é uma string
    try:
        if not type(city) == str:
            raise TypeError("tipo de dado inválido")
    except TypeError:
        print("tipo de dado inválido")
        return data
        
    data.append({"name": name, "age" : age, "hobbies" : hobbies})
    
def remove_person(data, name):
    for d in data:
        if d["name"] == name:
            del d["name"]
            return
        
    print("este nome não existe")
    return data     
    
def get_ages(data):
    age_list = []
    for d in data:
        age_list.append(d["age"])
    return print(min(age_list), sum(age_list)/len(data), max(age_list))

def get_hobbies(data):
    hobbies_set = set()
    for d in data:
        hobbies_set = hobbies_set.union(d["hobbies"])
    return print(hobbies_set)
    














