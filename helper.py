import pandas as pd
import os
from IPython.display import SVG, display
import random
from IPython.display import SVG, display, clear_output
import time

folder_path = "flags"  # Change to your folder path
file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
print(f"There are {file_count} files in the folder.")
data = pd.read_csv('names.csv')
print(len(data))
country_dict = data.set_index('Code')['Name'].to_dict()
print(country_dict)
folder_path = "flags"

# List all SVG files in the folder
svg_files = [f for f in os.listdir(folder_path) if f.endswith('.svg')]



def selected_images(num_images):

    folder_path = "flags"  # Change to your folder path
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    print(f"There are {file_count} files in the folder.")
    data = pd.read_csv('names.csv')
    print(len(data))
    country_dict = data.set_index('Code')['Name'].to_dict()
    print(country_dict)
    folder_path = "flags"

    # List all SVG files in the folder
    svg_files = [f for f in os.listdir(folder_path) if f.endswith('.svg')]



    if len(svg_files) < num_images:
        print("Not enough SVG files in the folder.")
    else:
        # Randomly select 5 unique SVG files
        selected_svgs = random.sample(svg_files, num_images)
        return selected_svgs



def special_cases(user_answer, correct_answer):
    correct_answer = correct_answer.split(",")[0].strip() 
    # Special cases
    if user_answer.lower() == "usa":
        user_answer = "United States"
    if user_answer.lower() == "uk":
        user_answer = "United Kingdom"
    if user_answer.lower() == "uae":    
        user_answer = "United Arab Emirates"
    if user_answer.lower() == "vatcain":    
        user_answer = "Holy See (Vatican City State)"
    if user_answer.lower() == "DRC":
        user_answer = "Congo, the Democratic Republic of the"
    if user_answer.lower() == "east timor":
        user_answer = "Timor-Leste"
    if user_answer.lower() == "ivory coast":
        user_answer = "Côte d'Ivoire"
    if user_answer.lower() == "north macedonia":
        user_answer = "Macedonia, the former Yugoslav Republic of"
    if user_answer.lower() == "moldova":
        user_answer = "Moldova, Republic of"
    if user_answer.lower() == "russia":
        user_answer = "Russian Federation"
    if user_answer.lower() == "south korea":
        user_answer = "Korea, Republic of"
    if user_answer.lower() == "syria":
        user_answer = "Syrian Arab Republic"
    if user_answer.lower() == "taiwan":
        user_answer = "Taiwan, Province of China"
    if user_answer.lower() == "tanzania":
        user_answer = "Tanzania, United Republic of"
    if user_answer.lower() == "palenstine":
        user_answer = "Palestine, State of"
    if user_answer.lower() == "venezuela":
        user_answer = "Venezuela, Bolivarian Republic of"
    if user_answer.lower() == "virgin islands":
        user_answer = "Virgin Islands, British"
    if user_answer.lower() == "laos":
        user_answer = "Lao People's Democratic Republic"
    if user_answer.lower() == "macau":
        user_answer = "Macao"
    if user_answer.lower() == "falkland islands ":
        user_answer = "Falkland Islands (Malvinas)"
    if user_answer.lower() == "czechia":
        user_answer = "Czech Republic"
    if user_answer.lower() == "st lucia":
        user_answer = "Saint Lucia"
    if user_answer.lower() == "st vincent":
        user_answer = "Saint Vincent and the Grenadines"
    if user_answer.lower() == "micronesia":
        user_answer = "Micronesia, Federated States of"
    return user_answer, correct_answer



def game(num_images):
    selected_svgs = selected_images(num_images)
    score = 0
    total = len(selected_svgs)
    start_time = time.time()
    i = 1
    while i < len(selected_svgs) + 1:
        clear_output(wait=True)
        print(f"Displaying Flag {i}:")
        display(SVG(os.path.join(folder_path, selected_svgs[i-1])))
        
        # Prompt the user for the country name
        user_answer = input(f"Enter the country name for Flag {i}: ")
        print(f"You entered: {user_answer}\n")

        if selected_svgs[i-1][:-4].upper() == "NA":
            correct_answer = "Namibia"
        else:
            correct_answer = country_dict[selected_svgs[i-1][:-4].upper()]
        
        user_answer, correct_answer = special_cases(user_answer, correct_answer)
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Moving to the next flag...\n")
            score += 1
            i += 1
            continue 
        elif user_answer.lower() == "skip":
            print(f"The correct answer is: {correct_answer}\n")
            print("Moving to the next flag...\n")
            i += 1
            continue
        elif user_answer.lower() == "hint":
            print(f"The first letter of the country name is: {selected_svgs[i-1][:-4].upper()}")
            time.sleep(2)

        elif user_answer.lower() == "exit":
            print(f"The correct answer is: {correct_answer}\n")
            print(f"Game Over! Your final score is {score}")
            end = time.time()
            break

    end = time.time()

    print(f"Congratulations! You have completed the game. Your final score is {score}.")
    print(f"Total time taken: {end - start_time:.2f} seconds")