class Folder:
    def __init__(self, name, files=None, subfolders=None):
        """
        Initialize a Folder object with a name, an optional list of files, and an optional list of subfolders.
        """
        self.name = name
        self.files = files if files else []  # Initialize files as an empty list if not provided
        self.subfolders = subfolders if subfolders else []  # Initialize subfolders as an empty list if not provided
        self.current_folder = self  # Tracks the folder that the user is currently in

    def add_file(self, file_name):
        """
        Add a file (string) to the current folder's file list.
        """
        self.files.append(file_name)

    def add_subfolder(self, subfolder):
        """
        Add a subfolder (another Folder object) to the current folder's subfolder list.
        """
        self.subfolders.append(subfolder)

    def select_folder(self, name):
        """
        Select a subfolder by its name and make it the current folder.
        If no matching folder is found, print an error message.
        """
        name = name.lower() #convert user input to lowercase
        if self.name.lower() == name:
            self.current_folder = self
        else:
            for subfolder in self.subfolders:
                if subfolder.name.lower() == name:
                    self.current_folder = subfolder
                    return
                # Recursively search for the folder in subfolders
                subfolder.select_folder(name)
            if self.current_folder == self:  # If no folder was selected, it means the folder wasn't found
                print(f"Folder '{name}' not found")

    def __count_files(self):
        """
        Recursively count the total number of files in the folder and all its subfolders.
        Private method.
        """
        count = len(self.files)  # Count the number of files in the current folder
        for subfolder in self.subfolders:
            # Recursively count the files in each subfolder
            count += subfolder.__count_files()
        return count

    def __eq__(self, other):
        """
        Check if two Folder objects (or Folder and string) are equal by comparing their names.
        """
        if isinstance(other, Folder):
            return self.name.lower() == other.name.lower()
        elif isinstance(other, str):
            return self.name.lower() == other.lower()
        return False

    def __len__(self):
        """
        Return the total number of files in the folder and its subfolders.
        This uses the __count_files method.
        """
        return self.__count_files()

    def __str__(self, level=0):
        """
        Recursively return a string representation of the folder, showing the folder name, its files,
        and its subfolders, using indentation for nested subfolders.
        """
        indent = "----" * level  # Indentation increases with folder depth
        result = f"{indent}Folder: {self.name}\n"

        # Add files to the string representation
        for file in self.files:
            result += f"{indent}----File: {file}\n"

        # Add subfolders to the string representation (recursively)
        for subfolder in self.subfolders:
            result += subfolder.__str__(level + 1)  # Increase indentation for nested subfolders

        return result

    def menu(self):
        """
        Display an interactive menu that allows the user to:
        - Add files
        - Add subfolders
        - Select a folder
        - Print the current folder structure
        - Exit the program
        """
        while True:
            print("\n===Menu===")
            print(f"==Current Folder: {self.current_folder.name} ==")
            print("1) Add File")
            print("2) Add Folder")
            print("3) Select Folder")
            print("4) Print Folder")
            print("5) Exit")

            try:
                # Get the user's choice
                choice = int(input(">>Input: ").strip())
            except ValueError:
                print("Enter a valid input")

            if choice == 1:
                # Add a file
                file_name = input("Enter file name: ").strip()
                self.current_folder.add_file(file_name)
                print(f"Added file: {file_name}")

            elif choice == 2:
                # Add a subfolder
                folder_name = input("Enter a folder name: ").strip()
                new_folder = Folder(folder_name)
                self.current_folder.add_subfolder(new_folder)
                print(f"Added folder: {folder_name}")

            elif choice == 3:
                # Select a folder
                folder_name = input("Enter a folder name to select: ").strip()
                self.select_folder(folder_name)

            elif choice == 4:
                # Print the current folder structure
                print(self.current_folder)

            elif choice == 5:
                # Exit the menu loop
                print("Exiting Menu.")
                break

            else:
                # Handle invalid choices
                print("Invalid choice, please try again.")


# Create the root folder and run the menu
start_folder = Folder("Start Folder")
start_folder.menu()
