import requests  # For making HTTP requests to the website
from bs4 import BeautifulSoup  # For parsing HTML content
import json  # For saving data in JSON format
import time  # To add delays between requests and avoid overwhelming the server

# Base URL where fish count data is hosted
BASE_URL = "https://www.adfg.alaska.gov/sf/FishCounts/index.cfm?ADFG=main.displayResults"
# URL for the search page where form data is submitted
SEARCH_URL = f"{BASE_URL}/search"

# HTTP headers to make the request look like it's coming from a real web browser
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def get_form_options():
    """Extract available years, locations, and species from the search form."""

    # Send an HTTP GET request to the search page to get the available options
    response = requests.get(SEARCH_URL, headers=HEADERS)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Function to extract values from dropdown menus (HTML <select> elements)
    def extract_options(select_name):
        return [
            option["value"]  # Get the value of each <option> tag
            for option in soup.select(f'select[name="{select_name}"] option')
            if option["value"]  # Ignore empty values
        ]

    # Extract available years, locations, and species from the form
    years = extract_options("year")
    locations = extract_options("location")
    species = extract_options("species")

    return years, locations, species  # Return the extracted lists


def fetch_fish_count(year, location, species):
    """Submit the form for a specific combination and extract data."""

    # Create a dictionary with form data to send in the request
    payload = {"year": year, "location": location, "species": species}

    # Send an HTTP POST request with the form data to get the filtered results
    response = requests.post(SEARCH_URL, data=payload, headers=HEADERS)

    # Parse the response HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the results table using its ID (assuming it exists on the page)
    table = soup.find("table", {"id": "resultsTable"})

    # If no table is found, return None (no data available)
    if not table:
        return None

    data = []  # List to store extracted fish count data

    # Loop through all rows in the table, skipping the first row (header)
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")  # Get all columns (cells) in the row
        data.append(
            {  # Store the extracted date and count as a dictionary
                "date": cols[
                    0
                ].text.strip(),  # First column: date (strip removes extra spaces)
                "count": int(
                    cols[1].text.strip()
                ),  # Second column: fish count (converted to an integer)
            }
        )

    return data  # Return the extracted fish count data


def main():
    """Main function to fetch and save fish count data."""

    # Get available options for years, locations, and species
    years, locations, species = get_form_options()

    fish_counts = {}  # Dictionary to store all retrieved fish count data

    # Loop through all combinations of year, location, and species
    for year in years:
        for location in locations:
            for fish in species:
                print(f"Fetching data for {year} - {location} - {fish}...")

                # Fetch fish count data for the given combination
                data = fetch_fish_count(year, location, fish)

                # If data is found, store it in the dictionary
                if data:
                    fish_counts.setdefault(year, {}).setdefault(location, {})[
                        fish
                    ] = data

                # Wait 1 second before making the next request (to avoid overloading the server)
                time.sleep(1)

    # Save the collected data to a JSON file
    with open("fish_counts.json", "w") as f:
        json.dump(fish_counts, f, indent=4)  # Format the JSON for readability

    print("Data saved to fish_counts.json")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
