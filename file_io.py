# This code block will handle input and output functions of animal objects in zoo_data.txt
# This code block will also use try and except blocks to ensure robust error handling 

from animals import Animal
from zoo import Zoo 

class FileInputOutput:
    """Create class to handle input and output for zoo animal objects"""
    def __init__(self, filename="zoo_data.txt"): #initialize filename object within class
        self.filename = filename #instatiates variable filename for later use

    def save_data(self, zoo):
        """Method to save zoo with animal objects in text file"""
        try:
            with open(self.filename, "w") as file: #Expected: open file, write animal objects, and close file
                for animal in zoo.animals: #Expected: iterate through animals objects within zoo
                    file.write(f"{animal.name},{animal.species}\n") #format print animal object name and species
            print("Zoo File Updated") #Expected: Print to console of saved zoo data
        except FileNotFoundError as e: #Expected: Catch missing file errors and print to console for graceful error handling
            print(f"Error with file: {e}")
        except ValueError as e: #Expected: Catch value in list errors and print to console for graceful error handling
            print(f"Improper Animal: {e}")
        except Exception as e: #Expected: General exception for errors while completing task and print to console for graceful error handling
            print(f"Another error found when saving file: {e}")
        finally: #Expected: Final print statement to show operation completed without run errors
            print("Current Zoo data saved. Task complete!")

    def load_data(self, zoo):
        """Method to load data from file and adjust animal onjects in zoo"""
        try:
            with open(self.filename, "r") as file: #Expected: Open file, iterate through file lines, and close file
                for line in file: #Expected: For loop to iterate through each line in file
                    data = line.strip().split(",") #Expected: Data variable and format of what properly stored zoo data
                    if len(data) != 2: #Expected: If statement to handle malformed data
                        print(f"Malformed Data Detected: {line.strip()}") 
                        continue #Expected: skip rest of line and move on to next line
                    name, species = data #Expected: Unpack data into two variables to reconstruct animal objects in zoo
                    if species == "Dog": #Expected: Check verify animal object name in file, if matches, adds to zoo
                        zoo.add_animal(Dog(name))
                    elif species == "Cat":
                        zoo.add_animal(Cat(name))
                    elif species == "Bird":
                        zoo.add_animal(Bird(name))
                    elif species == "Reptile":
                        zoo.add_animal(Reptile(name))
                    else:
                        print(f"Is this a new species we want to add: {species}, skipping for now") #Expected: Handle unknown species
                print("Zoo data loaded and updated Zoo accurately") #Expected: Print to console at end of if statement
        except FileNotFoundError as e: #Expected: Catch missing file errors and print to console for graceful error handling
            print(f"Error with file: {e}")
        except Exception as e:#Expected: General exception for errors while completing task and print to console for graceful error handling
            print(f"Another error found when loading file: {e}")
        finally:  #Expected: Final print statement to show operation completed without run errors
            print("Zoo file loaded, parsed, and Zoo updated. Task Complete")