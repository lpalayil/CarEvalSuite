import os
import csv

class OutputValidation:

    def read_csv_to_dict(self):
        """
        Reads all CSV files with 'output' in the name and combines their data into a dictionary.

        :return: Dictionary with combined CSV data for all registration numbers
        """

        data_dict = {}

        # Get the folder path where the script is located
        folder_path = os.path.dirname(os.path.abspath(__file__))

        # Get all files in the folder that contain 'output' in their name and end with .csv
        try:
            output_files = [f for f in os.listdir(folder_path) if 'output' in f and f.endswith('.txt')]

            if not output_files:
                print("No files with 'output' in the name and .txt extension found in the folder.")
                return data_dict

            # Iterate over all output files
            for output_file_name in output_files:
                output_file_path = os.path.join(folder_path, output_file_name)

                # Read each CSV file
                with open(output_file_path, mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        reg_number = row['VARIANT_REG'].strip().lower().replace(" ", "")
                        data_dict[reg_number] = {
                            'MAKE_MODEL': row['MAKE_MODEL'],
                            'YEAR': row['YEAR']
                        }

            print(f"Final dictionary created: {data_dict}")

        except FileNotFoundError:
            print(f"Error: The folder or file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return data_dict


