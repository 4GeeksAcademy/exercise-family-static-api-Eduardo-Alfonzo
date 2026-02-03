"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, data):
       member = {
           "id": data.get("id", self._generate_id()), 
           "first_name": data["first_name"],
           "last_name": self.last_name,
           "age": data["age"],
           "lucky_numbers": data["lucky_numbers"]
       }
       self._members.append(member)
       return member
            

    def delete_member(self, id):
        new_family = list(filter(lambda member: member["id"] != id, self._members))
        self._members = new_family
        return self._members
        
        

    def get_member(self, id):
        for character in self._members:
            if character["id"] == id:
                return character
        return None
    
    def update_member(self, data, id):
        member = self.get_member(id)
        if member:
            member["first_name"] = data.get("first_name", member["first_name"])
            member["age"] = data.get("age", member["age"])
            member["lucky_numbers"] = data.get("lucky_numbers", member["lucky_numbers"])
            return member
        return None
    

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members