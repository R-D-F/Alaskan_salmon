from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import requests
import os

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.adfg.alaska.gov/sf/FishCounts/")
# Create a directory to save JSON files
os.makedirs("data/json", exist_ok=True)

# Locate the location dropdown
dropdown_location = driver.find_element(By.ID, "countLocationID")
select_location = Select(dropdown_location)

options_location = select_location.options
# Extract the text of each option into a list
options_location_list = [option.text for option in options_location]
# Removing "Select a Location" from the list
for i in range(28, len(options_location_list)):
    options_location_list.pop(28)
print(options_location_list[0])

manual = []

# Loop through each location
for location in options_location_list:
    select_location.select_by_visible_text(location)
    # Find and click the Submit button
    driver.find_element(By.NAME, "Submit").click()

    # Wait for the page to load (you might want to wait for a specific element instead)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "speciesID"))
    )

    # Locate the species dropdown
    dropdown_species = driver.find_element(By.NAME, "speciesID")
    select_species = Select(dropdown_species)

    options_species = select_species.options
    options_species_list = [option.text for option in options_species]

    # Loop through each species
    for species in options_species_list:

        select_species.select_by_visible_text(species)

        dropdown_year = driver.find_element(By.NAME, "year")
        select_year = Select(dropdown_year)
        options_year = select_year.options
        options_year_list = [option.text for option in options_year]

        # Select all years
        for option in options_year_list:
            select_year.select_by_visible_text(option)

        # Find and click the Submit button
        driver.find_element(By.NAME, "Submit").click()

        try:
            # Wait for the JSON link to appear
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "JSON format"))
            )

            # Find the JSON download link
            json_link_element = driver.find_element(By.LINK_TEXT, "JSON format")
            # Extract the URL
            json_url = json_link_element.get_attribute("href")

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://www.adfg.alaska.gov",
            }
            # Download the JSON file
            response = requests.get(json_url, headers=headers)

            # Save the JSON file
            if response.status_code == 200:
                with open(f"data/json/{location}_{species}.json", "wb") as file:
                    file.write(response.content)
                print(
                    f"JSON file for {location} and {species} downloaded successfully!"
                )
            else:
                print(
                    f"Failed to download JSON for {location} and {species}. Status Code: {response.status_code}"
                )

        except exceptions.TimeoutException as e:
            manual.append(f"{location}: {species}")
        finally:
            # Go back to the species selection page
            driver.back()
            # Wait until the species dropdown is present again
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "speciesID"))
            )

            # Re-locate the species dropdown after going back
            dropdown_species = driver.find_element(By.NAME, "speciesID")
            select_species = Select(dropdown_species)

    # Go back to the location selection page
    driver.back()
    # Wait until the location dropdown is present again
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "countLocationID"))
    )

    # Re-locate the location dropdown after going back
    dropdown_location = driver.find_element(By.ID, "countLocationID")
    select_location = Select(dropdown_location)

# Close the driver after all downloads
driver.quit()
print(f"TODO:\n{manual}")
