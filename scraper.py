import requests
from bs4 import BeautifulSoup
import json
import time

# Base URL of the fish count page
BASE_URL = "https://fishcountwebsite.example.com"
SEARCH_URL = f"{BASE_URL}/search"

# Headers to mimic a browser request
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def get_form_options():
    """Extract available years, locations, and species from the search form."""
    response = requests.get(SEARCH_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract dropdown options
    def extract_options(select_name):
        return [
            option["value"]
            for option in soup.select(f'select[name="{select_name}"] option')
            if option["value"]
        ]

    years = extract_options("year")
    locations = extract_options("location")
    species = extract_options("species")

    return years, locations, species


def fetch_fish_count(year, location, species):
    """Submit the form for a specific combination and extract data."""
    payload = {"year": year, "location": location, "species": species}
    response = requests.post(SEARCH_URL, data=payload, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract fish count table (assuming it exists in a table)
    table = soup.find("table", {"id": "resultsTable"})

    if not table:
        return None

    data = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cols = row.find_all("td")
        data.append(
            {"date": cols[0].text.strip(), "count": int(cols[1].text.strip())}
        )

    return data


def main():
    years, locations, species = get_form_options()
    fish_counts = {}

    for year in years:
        for location in locations:
            for fish in species:
                print(f"Fetching data for {year} - {location} - {fish}...")
                data = fetch_fish_count(year, location, fish)
                if data:
                    fish_counts.setdefault(year, {}).setdefault(location, {})[
                        fish
                    ] = data
                time.sleep(1)  # Avoid overwhelming the server

    # Save to JSON file
    with open("fish_counts.json", "w") as f:
        json.dump(fish_counts, f, indent=4)
    print("Data saved to fish_counts.json")


if __name__ == "__main__":
    main()
