import requests
from bs4 import BeautifulSoup
import json
import time


def get_fish_count_data():
    base_url = "https://www.cbr.washington.edu/dart/cs/data"

    # Initialize an empty list to store fish count data
    all_fish_counts = []

    # Make an initial request to get available parameters (years, locations, species)
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract available years, locations, and species from dropdowns or links
    years = [
        option.text for option in soup.select("select[name='year'] option")
    ]
    locations = [
        option.text for option in soup.select("select[name='location'] option")
    ]
    species = [
        option.text for option in soup.select("select[name='species'] option")
    ]

    # Loop through each combination of year, location, and species to get fish count data
    for year in years:
        for location in locations:
            for fish in species:

                # Construct the URL with query parameters for year, location, and species
                query_params = {
                    "year": year,
                    "location": location,
                    "species": fish,
                }

                # Send request to fetch the data
                response = requests.get(base_url, params=query_params)
                soup = BeautifulSoup(response.text, "html.parser")

                # Parse the fish count data from the table (assuming it's in a table format)
                table = soup.find("table")
                if table:
                    rows = table.find_all("tr")
                    for row in rows[1:]:  # Skip the header row
                        columns = row.find_all("td")
                        if len(columns) >= 2:  # Ensure the row contains data
                            date = columns[0].text.strip()
                            count = columns[1].text.strip()

                            # Store the parsed data in a dictionary
                            fish_data = {
                                "year": year,
                                "location": location,
                                "species": fish,
                                "date": date,
                                "count": count,
                            }
                            all_fish_counts.append(fish_data)

                # Pause for a short time between requests to prevent overloading the server
                time.sleep(1)

    # Save the collected data to a JSON file
    with open("fish_counts.json", "w") as json_file:
        json.dump(all_fish_counts, json_file, indent=4)

    print("Fish count data saved to fish_counts.json")


# Run the function to start scraping
get_fish_count_data()
