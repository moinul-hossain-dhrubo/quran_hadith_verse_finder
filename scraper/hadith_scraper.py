import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome() 
    
    with open('hadith_data_abudawud.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Book Name', 'Hadith']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for book_number in range(1, 44):
            url = f"https://sunnah.com/abudawud/{book_number}"
            driver.get(url)

            time.sleep(2)

            book_name_elements = driver.find_elements(By.CLASS_NAME, "book_page_english_name")
            book_name = ""
            for element in book_name_elements:
                book_name = element.text

            hadith_elements = driver.find_elements(By.CLASS_NAME, "englishcontainer")
            for hadith_element in hadith_elements:
                hadith = hadith_element.text
                writer.writerow({'Book Name': book_name, 'Hadith': hadith})
                
    driver.quit()

if __name__ == "__main__":
    main()
