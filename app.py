from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from IPython.display import display
import pandas
import time
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://dineoncampus.com/uh/whats-on-the-menu")

time.sleep(4) #test this later,  without this the webpage cannot pullup starbuck menu
WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='dropdown-grouped__BV_toggle_']"))).click()


stabucks_dropdown_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='building_60400ad23a585b1bf86c0c3c']/li[4]/button")))
stabucks_dropdown_btn.click()

time.sleep(4)
body = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.TAG_NAME, "body")))
#starbucks_menu = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__BVID__436']/div/div[2]")))
tables = body.find_elements(By.XPATH, "//*[@id='__BVID__264']")
tbodies = body.find_elements_by_tag_name('tbody')

all_foods = []

def write_json(data, filename = "foods.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

try:
    time.sleep(5)
    #with open("foods.json", "w") as json_file:
    for table in tbodies:
        #foodType = table.find_elements(By.TAG_NAME, "tr")
        rows = table.find_elements(By.TAG_NAME, "tr") #foodItemList
        for row in tqdm(rows):            
            cols = row.find_elements(By.TAG_NAME, "td")
            
            item_name =  WebDriverWait(cols[0],20).until(EC.element_to_be_clickable((By.TAG_NAME, "strong"))).text
            '''
            Not currently working
            item_description = cols[0].find_element(By.XPATH, "//*/tbody/tr[1]/td[1]/div/span/text()/following::node()[1][self::BR]")
            '''
            item_portion_size = WebDriverWait(cols[1],20).until(EC.element_to_be_clickable((By.TAG_NAME, "div"))).text
            item_calories = WebDriverWait(cols[2],20).until(EC.element_to_be_clickable((By.TAG_NAME, "div"))).text
            
            time.sleep(2)

            #print(item_name)

            item_macro_btn = WebDriverWait(cols[0],20).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
            
            item_macro_btn.click()

            
            macros_menu = body.find_element(By.XPATH,  "//*[starts-with(@id,'nutritional-modal')]")
            exit_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME, "close"))) 

            item_macros_content = macros_menu.find_element(By.CLASS_NAME, "modal-body")
            #print(item_macros_content.text)

            macros = item_macros_content.find_elements(By.XPATH,  "//*[starts-with(@id,'nutritional-modal')]/ul/li")

            fat_calories_text =  item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[1]').text.strip()
            fat_calories = fat_calories_text.split(":")[-1].strip()
            #print("Fat Calories:", fat_calories)

            total_fat_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[2]').text.strip()
            total_fat = total_fat_text.split(":")[-1].strip()
            #print("Total Fat:", total_fat)

            saturated_fat_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[3]').text.strip()
            saturated_fat = saturated_fat_text.split(":")[-1].strip()
            #print("Saturated Fat:", saturated_fat)

            trans_fat_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[4]').text.strip()
            trans_fat = trans_fat_text.split(":")[-1].strip()
            #print("Trans Fat:", trans_fat)

            cholesterol_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[5]').text.strip()
            cholesterol = cholesterol_text.split(":")[-1].strip()
            #print("Cholesterol:", cholesterol)

            sodium_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[6]').text.strip()
            sodium = sodium_text.split(":")[-1].strip()
            if(sodium == "mg"):
                sodium = "0 mg"
            #print("Sodium:", sodium)

            potassium_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[7]').text.strip()
            potassium = potassium_text.split(":")[-1].strip()
            if(potassium == "g"):
                potassium = "0 g"
            #print("Potassium:", potassium)

            total_carbs_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[8]').text.strip()
            total_carbs = total_carbs_text.split(":")[-1].strip()
            #print("Total Carbs:", total_carbs)

            fiber_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[9]').text.strip()
            fiber = fiber_text.split(":")[-1].strip()
            #print("Dietary Fiber:", fiber)

            sugar_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[10]').text.strip()
            sugar = sugar_text.split(":")[-1].strip()
            #print("Sugars:", sugar)

            protein_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[11]').text.strip()
            protein = protein_text.split(":")[-1].strip()
            #print("Protein:", protein)

            vitamin_A_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[12]').text.strip()
            vitamin_A = vitamin_A_text.split(":")[-1].strip()
            if(vitamin_A == "g"):
                vitamin_A = "0 g"
            #print("Vitamin A:", vitamin_A)

            vitamin_C_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[13]').text.strip()
            vitamin_C = vitamin_C_text.split(":")[-1].strip()
            #print("Vitamin C:", vitamin_C)

            calcium_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[14]').text.strip()
            calcium = calcium_text.split(":")[-1].strip()
            #print("Calcium:", calcium)

            iron_text = item_macros_content.find_element(By.XPATH, '//*[starts-with(@id,"nutritional-modal")]/ul/li[15]').text.strip()
            iron = iron_text.split(":")[-1].strip()
            #print("Iron:", iron)

            exit_btn.click()

            item_dictionary={
                "food_name": item_name,
                "food_portion_size": item_portion_size,
                "food_calories": item_calories,
                "food_fat_calories": fat_calories,
                "food_total_fat": total_fat,
                "food_sat_fat": saturated_fat,
                "food_trans_fat": trans_fat,
                "food_cholesterol": cholesterol,
                "food_sodium": sodium,
                "food_potassium": potassium,
                "food_total_carbs": total_carbs,
                "food_fiber": fiber,
                "food_sugar": sugar,
                "food_protein": protein,
                "food_vitamin_A": vitamin_A,
                "food_vitamin_C": vitamin_C,
                "food_calcium": calcium,
                "food_iron": iron
            }

            all_foods.append(item_dictionary)
    
    #Store each food item into a newly created table using the pandas library
    df = pandas.DataFrame(all_foods)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(df)

finally:
    print("Done")

    with open("foods.json") as json_file:
        data = json.load(json_file)
        temp = data["foods"]
        for food_dict in all_foods:
            print(food_dict["food_name"])
            y = {"name": food_dict["food_name"], "portion_size": food_dict["food_portion_size"], "calories": food_dict["food_calories"], 
                "fat_calories": food_dict["food_fat_calories"], "total_fat": food_dict["food_total_fat"], "sat_fat": food_dict["food_sat_fat"],
                "trans_fat": food_dict["food_trans_fat"], "cholesterol": food_dict["food_cholesterol"], "sodium": food_dict["food_sodium"],
                "potassium": food_dict["food_potassium"], "carbs": food_dict["food_total_carbs"], "fiber": food_dict["food_fiber"], 
                "sugar": food_dict["food_sugar"], "protein": food_dict["food_protein"], "vitamin_A": food_dict["food_vitamin_A"],
                "vitamin_C": food_dict["food_vitamin_C"], "calcium": food_dict["food_calcium"], "iron": food_dict["food_iron"]}
            temp.append(y)
    driver.quit()
    write_json(data)
