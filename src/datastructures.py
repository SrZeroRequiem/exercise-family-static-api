
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
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        id = randint(0, 99999999)
        if id == self.last_id:
            id = self._generateId()
        return randint(0, 99999999)

    def add_member(self, member):
        for i in self._members:
                if i["first_name"] == member["first_name"] and i["age"] == member["age"] and i["lucky_numbers"] == member["lucky_numbers"]:
                    return "Member was already added to the family"
        handler_member = {
            "id" : self._generateId(),
            "first_name" : member["first_name"],
            "last_name" : member["last_name"],
            "age": member["age"],
            "lucky_numbers" : list(member["lucky_numbers"])
            }
        if int(handler_member["age"]) < 1:
            return "Age must be greather than 0"
        elif handler_member["last_name"] != self.last_name:
            return "Incorrect last_name or Family"
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
        member = list(filter(lambda n : n["id"] == id,self._members))
        if member == []:
            return f"Member {id} not found"
        else:
            return member[0]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
