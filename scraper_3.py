from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = "https://www.adfg.alaska.gov/sf/FishCounts/index.cfm?ADFG=main.displayResults"


def main():
    # Open browser
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
    driver.get(URL)

    # Wait for the dropdown to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "year"))
        )
    except Exception as e:
        print("Year dropdown did not load:", e)
        driver.quit()
        return

    # Get fully loaded HTML
    html = driver.page_source
    driver.quit()

    # Parse the HTML
    soup = BeautifulSoup(html, "lxml")
    select = soup.find("select", {"name": "year"})

    if select:
        options = [option["value"] for option in select.find_all("option")]
        print("Available Years:", options)
    else:
        print("No <select> element with name='year' found.")


if __name__ == "__main__":
    main()
