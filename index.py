from utils import *

config = load_config()
mods_folder = config["mods_folder"]

help_string = """
This program will help you to easily enable and disable mods for The Sims 4. Mod folders are simply moved from the Mods folder.
Just add the mod folder or file name. All disabled mods have been moved to the "archive" in the program folder

0. Exit
1. Set mods folder (if changed)
2. Show current mods
3. Enable mod(s) (comma-separated)
4. Enable all mods
5. Disable mod(s) (comma-separated)
6. Disable all mods
7. Show config
8. Create profile
9. Show profiles
10. Delete profile
11. Apply profile
12. Backup mods



> """


while True:
    try:
        option = int(input(help_string))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if option == 0:
        print("Exiting...")
        break
    elif option == 1:
        mods_folder = input("Enter the path to your mods folder: ")
        if os.path.exists(mods_folder):
            config["mods_folder"] = mods_folder
            save_config(config)
            print(f'Current mods folder specified ({mods_folder})')
        else:
            print("Mods folder does not exist! Mods folder specified as default")
    elif option == 2:
        mods = list_mods(mods_folder)
        print("Current mods folder: ", mods_folder)
        print("Reading folder . . .")
        print("\n".join(mods))
        print(f"Total {len(mods)} mods")
    elif option == 3:
        mod_names = input("Enter the mod names to enable (comma-separated): ").split(',')
        mod_names = [name.strip() for name in mod_names]
        enable_mods(mod_names, mods_folder)
    elif option == 4:
        enable_all_mods(mods_folder)
    elif option == 5:
        mod_names = input("Enter the mod names to disable (comma-separated): ").split(',')
        mod_names = [name.strip() for name in mod_names]
        disable_mods(mod_names, mods_folder)
    elif option == 6:
        disable_all_mods(mods_folder)
    elif option == 7:
        print("Current config: ", config)
    elif option == 8:
        create_profile(mods_folder)
    elif option == 9:
        show_profiles()
    elif option == 10:
        delete_profile()
    elif option == 11:
        profile_name = input("Enter the profile name to apply: ")
        apply_profile(profile_name, mods_folder)
    elif option == 12:
        print("Current mods folder: ", mods_folder)
        backup_name = str(input('Enter backup name: '))
        backup(mods_folder, backup_name)
    else:
        print("Invalid option. Please choose a number from the list.")
    
    input('\n\n\nPress ENTER to continue . . .')