
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.last_id = 0

        # example list of members
        # John Jackson
        # 33 Years old
        # Lucky Numbers: 7, 13, 22

        # Jane Jackson
        # 35 Years old
        # Lucky Numbers: 10, 14, 3

        # Jimmy Jackson
        # 5 Years old
        # Lucky Numbers: 1
        self._members = [
            {
                "id" : 3443,
                "first_name" :"John" ,
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
                
            },
            {
                "id" : 3444,
                "first_name" :"Jane" ,
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
                
            },
            {
                "id" : self._generateId(),
                "first_name":"Jimmy" ,
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
                
            }
            
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        id = randint(0, 99999999)
        # Comprobamos que la id sea diferente a la de los otro miembros
        if id == self.last_id:
            id = self._generateId()
        return randint(0, 99999999)

    def add_member(self, member):
        ## Buscamos si el miembro ya ha sido añadido anteriormente
        for i in self._members:
                if i["first_name"] == member["first_name"] and i["age"] == member["age"] and i["lucky_numbers"] == member["lucky_numbers"]:
                    return "Member was already added to the family"
        ## Instanciamos el miembro a añadir con su id
        handler_member = {
            "id" : self._generateId(),
            "first_name" : member["first_name"],
            "last_name" : member["last_name"],
            "age": member["age"],
            "lucky_numbers" : list(member["lucky_numbers"])
            }
        ## Comprobamos que la edad sea mayor a o
        if int(handler_member["age"]) < 1:
            return "Age must be greather than 0"
        ## Comprobamos que el apellido sea el mismo que el de la familia
        elif handler_member["last_name"] != self.last_name:
            return "Incorrect last_name or Family"
        ## Añadimos el miembro a la lista
        else:
            self._members.append(handler_member)
            return(self._members)

    def delete_member(self, id):
        handler_members = list(filter(lambda n : n["id"] != id,self._members))
        if handler_members == self._members:
            return "Member not found"
        else:
            self._members = handler_members
            return(self._members)




    def get_member(self, id):
        # Filtramos la lista de miembros para obtener el miembro con ese id
        def filter_list(member):
            return member["id"] == id
        ## Nos devuelve un miembro con la id que buscamos, en caso de que exista
        member = list(filter(filter_list,self._members))
        ##member = list(filter(lambda n : n["id"] == id,self._members))
        ## Comprobamos que el miembro exista
        if member == []:
            return f"Member {id} not found"
        else:
            return member[0] ## -> {}
        ## return member -> [{}]







    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
