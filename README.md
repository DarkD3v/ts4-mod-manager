
# The Sims 4 mod manager

[![GitHub last commit](https://img.shields.io/github/last-commit/DarkD3v/ts4-mod-manager)](https://img.shields.io/github/last-commit/DarkD3v/ts4-mod-manager)
[![GitHub issues](https://img.shields.io/github/issues-raw/DarkD3v/ts4-mod-manager)](https://img.shields.io/github/issues-raw/DarkD3v/ts4-mod-manager)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/DarkD3v/ts4-mod-manager)](https://img.shields.io/github/issues-pr/DarkD3v/ts4-mod-manager)
[![GitHub](https://img.shields.io/github/license/DarkD3v/ts4-mod-manager)](https://img.shields.io/github/license/DarkD3v/ts4-mod-manager)

**TS4 Mod Manager** is a straightforward tool designed to simplify the management of mods for The Sims 4. With this utility, you can easily enable or disable mods by moving their folders in and out of the game's Mods directory. The manager also allows you to archive disabled mods in a separate folder within the program's directory, keeping your Mods folder organized and clutter-free.

# Key features
 - **Mod Activation/Deactivation**: Easily manage which mods are active by moving them between folders.
 - **Archiving**: Disabled mods are stored in an archive within the program, keeping your game directory clean.
 - **Simple Interface**: Just add the mod folder or file name to manage your mods effortlessly.

# Installation
[(Back to top)](#table-of-contents)

1. Ensure you have Python 3.x installed on your machine.
2. Clone the repository to your local machine:
```shell
gh repo clone DarkD3v/ts4-mod-manager
```
3. Navigate to the project directory:
```shell
cd ts4-mod-manager
```
4. Install the required dependencies:
```shell
pip install -r requirements.txt
```

# Usage
[(Back to top)](#table-of-contents)
1. Run the program:
```shell
python index.py
```
2. After launching the program, you will see a menu with several options:
```md
0. Exit - Close the program
1. Set mods folder (if changed) - Specify the path to the mods folder. If the folder does not exist, the program will leave the default path.
2. Show current mods - Show a list of all mods in the specified folder.
3. Enable mod(s) (comma-separated) - Enable one or more mods by name.
4. Enable all mods - Enable all mods (what disabled before)
5. Disable mod(s) (comma-separated) - Disable one or more mods by name.
6. Disable all mods - Disable all mods in the folder.
7. Show config - Show the current configuration.
8. Create profile - Create a profile with the current mod settings.
9. Show profiles - Show a list of saved profiles.
10. Delete profile - Delete the selected profile.
11. Apply profile - Apply one of the previously saved profiles.
12. Backup mods - Create a backup of current mods.
```
3. Select the desired option by entering the corresponding number.
4. Follow the prompts to complete the action.
5. Repeat the process as needed to manage your mods.
6. To exit the program, select option 0.
7. To save your current mod settings as a profile, select option 8.
8. To apply a saved profile, select option 11.
9. To delete a saved profile, select option 10.
10. To show a list of saved profiles, select option 9.
11. To create a backup of your current mods, select option 12.
12. To show the current configuration, select option 7.
13. To disable all mods, select option 6.

# License
[(Back to top)](#table-of-contents)

[GPL-3.0 license](./LICENSE)


