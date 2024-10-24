import csv
import re
import os
import chardet

input_folder_path = os.path.join(".", "input")

reviewID = 0
hotelID = 0
all_extracted_data = []

def extract_hotel_name(file_name, city_name):
    city2 = ["beijing", "montreal", "new-delhi", "san-francisco", "shanghai"]
    city3 = ["chicago", "las-vegas", "london"]
    hotel_name_parts = []
    if city_name in city2:
        hotel_name_parts = file_name.split('_')[2:]  
    elif city_name in city3:
        hotel_name_parts = file_name.split('_')[3:] 
    else:
        print(f"City {city_name} is not handled specifically. Skipping file: {file_name}")
    if not hotel_name_parts:
        return None  
    hotel_name = ' '.join(hotel_name_parts)
    hotel_name = os.path.splitext(hotel_name)[0]  
    return hotel_name

punctuation_pattern = re.compile(r'\?{4}')

# Iterate through folders in the input directory
for folder in os.listdir(input_folder_path):
    folder_path = os.path.join(input_folder_path, folder)

    if os.path.isdir(folder_path):
        city_name = folder  # Use the folder name as the city name
        print(f'Processing city folder: {city_name}')
        for index, folder in enumerate(folder):
        # Get all files inside the city folder (hotel files)
            hotel_files = [os.path.join(folder_path, hotel_file) for hotel_file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, hotel_file))]

            if not hotel_files:
                print(f"No hotel files found in city: {city_name}")  # Debug if no hotel files found
                continue

        # Extract hotel names and process reviews
        for hotel_file in hotel_files:
            hotelID = (index +1)*1000  # Increment hotelID for each hotel in the city
            hotel_name = extract_hotel_name(os.path.basename(hotel_file), city_name)

            if hotel_name is None:
                print(f"Skipping file {hotel_file} due to extraction issue.")
                continue

            print(f"Extracted hotel: {hotel_name} from {hotel_file}")  # Debug statement
            
            # Read reviews for the current hotel
            try:
                # Detect encoding and read the file
                with open(hotel_file, 'rb') as binary_file:
                    raw_data = binary_file.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']

                with open(hotel_file, 'r', encoding=encoding, errors='ignore') as text_file:
                    input_text = text_file.readlines()  # Use readlines to read all lines

                # Regular expression to match the date, title, and review
                pattern = re.compile(r'(\w+ \d+ \d{4})\s+(.+?)\t(.+)', re.DOTALL)

                # Process each line in the input text
                for line in input_text:
                    match = pattern.search(line)
                    if match:
                        reviewID += 1  # Increment review ID for each review
                        date = match.group(1).strip()
                        title = match.group(2).strip()
                        review = match.group(3).strip()

                        # Check for three consecutive punctuation marks
                        if punctuation_pattern.search(review):
                            print(f"Skipping review {reviewID} for hotel {hotel_name} due to punctuation issue.")
                            continue  # Skip the review if it contains three consecutive punctuation marks

                        # Append hotel name along with review data
                        all_extracted_data.append([reviewID, hotelID, city_name, hotel_name, date, title, review])

            except Exception as e:
                print(f"Could not process file {hotel_file}: {e}")

# Define the output CSV file name
output_file = 'test2_hotel_reviews.csv'

# Write the extracted data to a single CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(['Review ID', 'Hotel ID', 'City', 'Hotel Name', 'Date', 'Title', 'Review'])
    # Write data
    writer.writerows(all_extracted_data)

print(f'All data exported to {output_file}')
