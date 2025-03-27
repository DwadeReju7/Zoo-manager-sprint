

class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        Print(f"Added {animal.name} to the zoo")
    def remove_animal(self, animal_name_or_id):
        for animal in self.animals:
            if animal.name == animal_name_or_id:
                print(f"Remove {animal.name}")
                return
                print(f"Animal '{animal_name_or_id}' not found.")

    def list_animals(self):
        if not self.animals:
            print("No animals at the zoo")
        else:
            print("Current animals at the zoo:")
            for animal in self.animals:
                print(f"- {animal.name} ({animal.species})")
    
