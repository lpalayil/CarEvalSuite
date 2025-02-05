import os
import re

class CarInputData:


    def read_car_input_data(self):

        registration_numbers = []

        # Get the current folder path where the script is located
        folder_path = os.path.dirname(os.path.abspath(__file__))

        # Get all files in the folder that contain 'input' in their name and end with .txt
        try:
            files = [f for f in os.listdir(folder_path) if 'input' in f and f.endswith('.txt')]
            print(files)

            if not files:
                print("No input files found in the folder.")
                return registration_numbers

            # Regex pattern car registration numbers
            pattern = r'\b[A-Z]{2}[0-9]{2}\s?[A-Z]{3}\b'

            # Iterate through all the files
            for file_name in files:
                file_path = os.path.join(folder_path, file_name)
                try:
                    with open(file_path, 'r') as file:
                        text = file.read()
                        # Find all matches in the text
                        registration_numbers += re.findall(pattern, text)
                except FileNotFoundError:
                    print(f"Error: The file {file_name} was not found.")
                except Exception as e:
                    print(f"An error occurred while reading {file_name}: {e}")

        except FileNotFoundError:
            print("Error: The specified folder was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return tuple(registration_numbers)
