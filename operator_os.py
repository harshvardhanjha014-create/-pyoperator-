import time
import os
from tqdm import tqdm #this is a 3rd party module that helps in loading bar animation
import sys

#Below are ANSI Colour codes
RED = "\033[91m"

GREEN = "\033[92m"

YELLOW = "\033[93m"

BLUE = "\033[94m"

RESET = "\033[0m"

my_script_name = "operator_os.py"
my_folder_name = "my file os operator"
#in this project i will be creating a file management system for all the file located
#inside my folder named 'my file os operator'

get_current_working_directory = os.getcwd()

print('Your CWD is: ',get_current_working_directory)
get_current_script_location = os.path.dirname(__file__)
print(f"Location of this {my_script_name} is: ",get_current_script_location)

def terminate_action():
    sys.exit(RED+"Action Terminated"+RESET)


def create_file_in_cwd():
    #fxn to create a file in cwd
    ask_user =  input(BLUE+"Enter file name: "+RESET)
    folder = get_current_working_directory
    path = os.path.join(folder,ask_user)
    time.sleep(0.5)
    for i in tqdm(range(5)):
            time.sleep(1)
    print(GREEN+"\n\nFile created\n\n"+RESET)
    file_created = open(path,"a")
    time.sleep(0.6)
    print(YELLOW+"Path of file is: "+RESET,YELLOW+path+RESET)

def create_file_beside_this_script():
    #fxn to have a file just-besides this script
    cwd_folder = os.getcwd()
    this_folder = os.path.join(cwd_folder,"my file os operator")
    ask_user = input(BLUE+"Enter file name: "+RESET)
    file_path = os.path.join(this_folder,ask_user)
    file_created = open(file_path,"a")
    time.sleep(0.5)
    print(GREEN+"File created!"+RESET)
    time.sleep(0.6)
    print("Path is: ",file_path)

def generate_files_besides_this_script():
    #fxn to automatically generate random files in this directory just-besides our operator_os.py file
    
    file_names = [
    "battle_of_stalingrad.pdf",
    "silk_road_history.txt",
    "indus_valley_civilization.docx",
    "fall_of_constantinople.md",
    "french_revolution.pdf",
    "apollo_11_mission.csv",
    "cold_war_timeline.txt",
    "renaissance_europe.docx",
    "roman_empire.jpg",
    "age_of_exploration.json",

    "albert_einstein_biography.pdf",
    "life_of_steve_jobs.txt",
    "nikola_tesla_profile.jpg",
    "leonardo_da_vinci.docx",
    "abraham_lincoln_biography.pdf",
    "alan_turing_story.md",
    "mahatma_gandhi_biography.txt",
    "apj_abdul_kalam.docx",
    "elon_musk_biography.pdf",
    "nelson_mandela.jpg",

    "butter_chicken_recipe.txt",
    "masala_dosa_recipe.pdf",
    "paneer_tikka_recipe.docx",
    "chole_bhature_recipe.md",
    "vegetable_biryani_recipe.txt",
    "margherita_pizza_recipe.jpg",
    "chocolate_brownie_recipe.pdf",
    "spaghetti_carbonara.docx",
    "gulab_jamun_recipe.txt",
    "mango_lassi_recipe.json",

    "fifa_world_cup_2026.pdf",
    "olympic_games_2028.jpg",
    "wimbledon_final.txt",
    "champions_league_final.mp4",
    "monaco_grand_prix.csv",
    "super_bowl_final.pdf",
    "asian_games.docx",
    "cricket_world_cup.txt",
    "the_ashes_series.jpg",
    "nba_finals.json",

    "the_dark_knight.mp4",
    "inception.mkv",
    "interstellar.mp4",
    "the_matrix.txt",
    "oppenheimer.pdf",
    "the_social_network.jpg",
    "dune_part_two.mp4",
    "parasite.mkv",
    "three_idiots.mp4",
    "lagaan.txt",

    "hackathon_ignite.pdf",
    "code_for_change.txt",
    "hack_the_future.docx",
    "buildathon_2026.csv",
    "ai_innovation_challenge.json",
    "cyberstorm_hackathon.pdf",
    "open_source_sprint.md",
    "devs_united.jpg",
    "hackverse.txt",
    "code_crusaders.docx",

    "blinding_lights.mp3",
    "bohemian_rhapsody.wav",
    "stairway_to_heaven.mp3",
    "shape_of_you.m4a",
    "believer.mp3",
    "tum_hi_ho.mp3",
    "kun_faya_kun.wav",
    "agar_tum_saath_ho.m4a",
    "ilahi.mp3",
    "apna_bana_le.wav",

    "attention_is_all_you_need.pdf",
    "imagenet_classification.pdf",
    "deep_residual_learning.pdf",
    "generative_adversarial_nets.pdf",
    "word2vec_research_paper.pdf",
    "neural_machine_translation.pdf",
    "transformer_architecture.png",
    "reinforcement_learning_notes.md",
    "computer_vision_dataset.csv",
    "random_filenames_dataset.json"
    ]#list of random file names
    size = len(file_names)#80 file names here

    cwd_folder =os.getcwd()
    this_folder = os.path.join(cwd_folder,"my file os operator")
    for i in range(0,size):
        random_file_path = os.path.join(this_folder,file_names[i])

        file = open(random_file_path,"a")
        time.sleep(0.3)
        print(GREEN+f"Successfully created: {file_names[i]}"+RESET)
        print(YELLOW+"Path is -->"+RESET,YELLOW+random_file_path+RESET)
        
def delete_the_required_file_in_this_folder():
    #fxn to delete specific files
    ask_user = input(BLUE+"Enter file name: "+RESET)
    cwd_folder = os.getcwd()
    this_folder = os.path.join(cwd_folder,"my file os operator")
    file_path = os.path.join(this_folder,ask_user)
    check_existence = os.path.exists(file_path)
    if(check_existence == True):
        print(GREEN+"File located successfully!"+RESET)
        for i in tqdm(range(5)):
            time.sleep(1)
             
        os.remove(file_path)
        print(BLUE+f"Successfully removed {ask_user}!")
    else:
        print(RED+"No such file found"+RESET)
def delete_all_files_in_this_folder():
    #fxn to delete all the other files apart from main script.py file
    cwd_folder = os.getcwd()
    this_folder = os.path.join(cwd_folder,"my file os operator")

    folder_system_files = os.listdir(this_folder)#list of all the files in this directory
    
    print(BLUE+"Your files: \n"+RESET)
    print(folder_system_files)
    yes_no = my_script_name in  folder_system_files
    #now removing this code file from the list
    folder_system_files.remove(my_script_name)
    for i in tqdm(range(3)):
            time.sleep(1)
    print(GREEN+"\nThis File Manager OS is safe from deletion!"+RESET)

    size = len(folder_system_files)

    time.sleep(0.5)
    
    ask_user = input(BLUE+f"\nAre you sure, you want to delete all {size} files?"+RESET)
    if(ask_user == "YES"):
         for i in range (0,size):
            file_path = os.path.join(this_folder,folder_system_files[i])
            
            os.remove(file_path)
            print(RED+"Removed -->"+RESET,YELLOW+file_path+RESET)
            time.sleep(0.3)
    elif(ask_user == 'NO'):
        terminate_action()
        
def search_file_in_this_folder():
    cwd_folder = os.getcwd()
    this_folder = os.path.join(cwd_folder,my_folder_name)

    
    ask_user = input(BLUE+"Search for: "+RESET)
    search_path = os.path.join(this_folder,ask_user)

    this_folder_files = os.listdir(this_folder)#list of all files and directories in this folder

    check = ask_user in this_folder_files
    for i in tqdm(range(5)):
            time.sleep(1)
                 

    file_type = os.path.isfile(search_path)

    if(check == True):
         
        print(GREEN+"File found!"+RESET)
        if(file_type == True):
              print(YELLOW+"File type -->"+RESET,"FILE")
        else:
             print(YELLOW+"File type -->"+RESET,"DIRECTORY/FOLDER")
    else:
         print(RED+"File Not found!"+RESET)
        

def create_directory_in_this_folder():
     #fxn to create a directory in this folder just-beside my script.py file
    cwd_folder = os.getcwd()
    this_folder = os.path.join(cwd_folder,my_folder_name)
    
    ask_user = input(BLUE+"Enter folder name: "+RESET)
    path = os.path.join(this_folder,ask_user)
    for i in tqdm(range(2)):
            time.sleep(1)
                  
    os.mkdir(path)
    print(GREEN+f"{ask_user} created successfully in this folder!"+RESET)


def show_menu():#note that this menu is designed by ChatGPT for saving time
    #All other important fxns have been carefully coded by me w/o any look-ups.Thank You.
    print("\n" + "=" * 50)
    print("        📁 OPERATOR OS - FILE MANAGER")
    print("=" * 50)

    print("\n  FILE OPERATIONS")
    print("  1. Create a file in CWD")
    print("  2. Create a file beside this script")
    print("  3. Generate multiple files beside this script")
    print("  4. Delete a required file in this folder")
    print("  5. Delete all files in this folder")
    print("  6. Search for a file in this folder")

    print("\n  DIRECTORY OPERATIONS")
    print("  7. Create a directory in this folder")

    print("\n  0. Exit")

    print("=" * 50)


while True:
    show_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_file_in_cwd()

    elif choice == "2":
        create_file_beside_this_script()

    elif choice == "3":
        generate_files_besides_this_script()

    elif choice == "4":
        delete_the_required_file_in_this_folder()

    elif choice == "5":
        delete_all_files_in_this_folder()

    elif choice == "6":
        search_file_in_this_folder()

    elif choice == "7":
        create_directory_in_this_folder()

    elif choice == "0":
        print("\nExiting Operator OS... 👋")
        break

    else:
        print("\n❌ Invalid choice. Please enter a number from 0-7.")