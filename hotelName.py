import os
import csv

input_folder_path = os.path.join(".", "input")
csv_file = 'hotel_names.csv'

def extract_hotel_name(file_name, city_name):
    city2 = ["beijing", "montreal", "new-delhi", "san-francisco", "shanghai"]
    city3 = ["chicago", "las-vegas", "london"]

    hotel_name_parts = []

    if city_name in city2:
        hotel_name_parts = file_name.split('_')[2:]  # Split from the third element onward
    elif city_name in city3:
        hotel_name_parts = file_name.split('_')[3:]  # Split from the fourth element onward
    else:
        print(f"City {city_name} is not handled specifically. Skipping file: {file_name}")

    if not hotel_name_parts:
        return None  # Return None if hotel_name_parts is empty
    
    # Join parts and remove the file extension
    hotel_name = ' '.join(hotel_name_parts)
    hotel_name = os.path.splitext(hotel_name)[0]  # Remove the extension
    
    return hotel_name

# Get all city folders inside the input folder
city_folders = [os.path.join(input_folder_path, folder) for folder in os.listdir(input_folder_path) if os.path.isdir(os.path.join(input_folder_path, folder))]

# Open the CSV file to write the hotel names
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["HotelID", "City", "Hotel Name"])  # CSV header

    # Iterate over each city folder with an index
    for index, city_folder in enumerate(city_folders):
        city_name = os.path.basename(city_folder)  # Extract the city name from folder name
        
        # Calculate the base hotelID for the city based on its index
        hotelID = (index + 1) * 1000
        print(f"Processing city: {city_name} starting from HotelID: {hotelID}")  # Debug statement

        # Get all files inside the city folder (hotel files)
        hotel_files = [os.path.join(city_folder, hotel_file) for hotel_file in os.listdir(city_folder) if os.path.isfile(os.path.join(city_folder, hotel_file))]

        if not hotel_files:
            print(f"No hotel files found in city: {city_name}")  # Debug if no hotel files found
            continue

        # Extract hotel names from the file names and write to CSV
        for hotel_file in hotel_files:
            hotelID += 1  # Increment hotelID for each hotel in the city
            hotel_name = extract_hotel_name(os.path.basename(hotel_file), city_name)

            if hotel_name is None:
                print(f"Skipping file {hotel_file} due to extraction issue.")
                continue

            print(f"Extracted hotel: {hotel_name} from {hotel_file}")  # Debug statement
            writer.writerow([hotelID, city_name, hotel_name])  # Write hotelID, city, and hotel name to CSV

print(f"Hotel names saved to {csv_file}")
