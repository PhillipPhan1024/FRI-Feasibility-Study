import os
import pandas as pd

def combine_csv_files(folder_path, output_file):
    # Get a list of all CSV files in the specified folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Loop through each CSV file and append its data to the combined DataFrame
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, df], ignore_index=True)

    # Sort the combined data by the column "teff_gspphot"
    combined_data = combined_data.sort_values(by="teff_gspphot")
    
    # Save the combined data to the master CSV file
    combined_data.to_csv(output_file, index=False)

    print(f"Combined data saved to {output_file}")

# Specify the path to the folder containing your CSV files
csv_folder_path = '/Users/phil/Downloads/2500-40000/'

# Specify the path for the master CSV file
output_csv_file = '2500-40000K_with_metallicity.csv'

# Call the function to combine CSV files
combine_csv_files(csv_folder_path, output_csv_file)
