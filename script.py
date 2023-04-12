import random
import time
# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://forms.gle/UFgfo4esug8AWGci6"

# Get the number of times to run the script from the user
times = int(input("Enter the number of times to run the script: "))

# Loop for the specified number of times
for x in range(times):
    driver = webdriver.Firefox()  # Create a new Firefox WebDriver for each iteration

    # Navigate to Google Form
    driver.get(link)  # Replace 'link' with the actual link of your Google Form

    # Wait for the page to load
    time.sleep(2)
    # Check for all the questions with radio buttons    
    questionsWithRadio = driver.find_elements(By.CLASS_NAME, "SG0AAe")
    questionsWithChecks = driver.find_elements(By.CLASS_NAME, "Y6Myld")
    radio = driver.find_elements(By.CLASS_NAME, "nWQGrd.zwllIb")
    my_questions = {}
    for index, s in enumerate(radio):
        radio[index].click()
        clickedRadio = driver.find_elements(By.CLASS_NAME, "N2RpBe")
        if((len(clickedRadio) / 2) in my_questions):
            my_questions[len(clickedRadio) / 2] += 1
        else:
            my_questions[len(clickedRadio) / 2] = 1

    my_answers = {}
    prev = 0
    spacing = 0
    for question in my_questions:
        if(spacing == 0):
            spacing = my_questions[question]
        else:
            spacing += my_questions[question]
        rand = random.randint(prev, spacing - 1)
        my_answers[question] = rand
        prev += my_questions[question]


    # Fill out the form with randomly selected answers
    for question in my_questions:
        if(radio[my_answers[question]] != radio[my_questions[question]]):
            radio[my_answers[question]].click()
            time.sleep(0.2)
  
    # Click the submit button
    submit_button = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit_button.click()

    # Close the WebDriver for this iteration
    driver.quit()

