from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Choose phrase to translate and enter the array of language codes you would like the phrase to be translated to
text= "Hello"
language_codes = ['af', 'hr', 'cs', 'da', 'nl', 'et', 'tl', 'fi', 'fr', 'de', 'hu', 'id', 'it', 'lv', 'lt', 'ms', 'no', 'pl', 'pt', 'ro', 'sk', 'sl', 'es', 'sv', 'tr', 'vi']
translations = []

#Enter the path to the chromedriver.exe
driver = webdriver.Chrome(executable_path=r'location of chromedriver.exe')

for code in language_codes:
    myUrl = "https://translate.google.com/?sl#view=home&op=translate&sl=en&tl=" + code + "&text=" + text

    driver.get(myUrl)
    delay = 3 # seconds
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span")))
    except TimeoutException:
        print ("Loading took too much time!")

    element_text = element.text
    translations.append(element_text)

driver.quit()

#Prints the array of completed translations
for word in translations:
    print (word)
