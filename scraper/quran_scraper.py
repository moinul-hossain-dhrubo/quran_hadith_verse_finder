import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome() 
    max_ayat = 1000
    
    try:
        # Open the CSV file in append mode
        with open('quran_data_5.csv', 'a', encoding='utf-8') as csvfile:

            # Open the webpage and retrieve ayats for each ayat number in the surah
        
            for surah_number in range(1, 115):
                for ayat in range(1,max_ayat):
                        # Change this to the desired surah number
                    

                    try:
                    # Find all elements with class 'TranslationText_text__4atf8'
                        url = f"https://quran.com/{surah_number}/{ayat}"
                        driver.get(url)
                        time.sleep(1)
                        
                        ayat_elements = driver.find_elements(By.CSS_SELECTOR, '.TranslationText_text__4atf8')
                        print(len(ayat_elements))
                        if len(ayat_elements) == 0:
                            break
                        print(ayat_elements)
                        for element in ayat_elements:
                            print(element.text)

                              # Concatenate ayats into a single string
                        ayats_combined = ' '.join([f"{surah_number}/{ayat}: {element.text}" for element in ayat_elements])

                        # Write the concatenated ayats directly to the file
                        csvfile.write(ayats_combined + '\n')

                        time.sleep(0.5)
                    except:
                        print('error found')
                        break

              

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
