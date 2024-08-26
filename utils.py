import json
import os
import shutil
from tqdm import tqdm
import zipfile



def progress_bar(iterable, description="Processing"):
    """Wrap an iterable with a progress bar."""
    return tqdm(iterable, desc=description, unit="item", ncols=50, colour="#009FBD")

def load_config():
    """Load configuration from config.json."""
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return {"mods_folder": os.path.join(os.path.expanduser("~"), "Documents", "Electronic Arts", "The Sims 4", "Mods")}

def save_config(config):
    """Save configuration to config.json."""
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def list_mods(mods_folder):
    """List all mods and directories in the specified mods folder."""
    mods = []
    if os.path.exists(mods_folder):
        for root, dirs, files in os.walk(mods_folder):
            # Добавляем файлы модов
            mods.extend(
                [os.path.relpath(os.path.join(root, f), mods_folder) for f in files if f.endswith(('.package', '.ts4script'))]
            )
            # Добавляем каталоги
            mods.extend(
                [os.path.relpath(os.path.join(root, d), mods_folder) for d in dirs]
            )
            break
    return sorted(mods)

def move_mod(mod_name, from_folder, to_folder):
    """Move a specific mod between folders."""
    source = os.path.join(from_folder, mod_name)
    destination = os.path.join(to_folder, mod_name)
    
    if os.path.exists(source):
        os.makedirs(to_folder, exist_ok=True)
        shutil.move(source, destination)
        print(f"Mod {mod_name} moved.")
    else:
        print(f"Mod {mod_name} not found in {from_folder}.")

def enable_mods(mod_names, mods_folder):
    """Enable multiple mods by moving them from the archive to the mods folder."""
    archive_folder = os.path.join(os.path.dirname(__file__), "archive")
    for mod_name in mod_names:
        move_mod(mod_name, archive_folder, mods_folder)
    print(f"Total {len(mod_names)} enabled!")

def disable_mods(mod_names, mods_folder):
    """Disable multiple mods by moving them from the mods folder to the archive."""
    archive_folder = os.path.join(os.path.dirname(__file__), "archive")
    for mod_name in mod_names:
        move_mod(mod_name, mods_folder, archive_folder)
    print(f"Total {len(mod_names)} disabled!")

def enable_all_mods(mods_folder):
    """Enable all mods in the archive."""
    archive_folder = os.path.join(os.path.dirname(__file__), "archive")
    if os.path.exists(archive_folder):
        for mod_name in os.listdir(archive_folder):
            move_mod(mod_name, archive_folder, mods_folder)
    else:
        print("No mods found in archive.")

def disable_all_mods(mods_folder):
    """Disable all mods in the mods folder."""
    if os.path.exists(mods_folder):
        archive_folder = os.path.join(os.path.dirname(__file__), "archive")
        os.makedirs(archive_folder, exist_ok=True)
        for mod_name in os.listdir(mods_folder):
            move_mod(mod_name, mods_folder, archive_folder)
    else:
        print("No mods found in mods folder.")

def load_profile(profile_name):
    """Load a profile from a JSON file."""
    profile_path = os.path.join(os.path.dirname(__file__), "profiles", f"{profile_name}.json")
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            return json.load(f)
    print(f"Profile {profile_name} does not exist.")
    return {"enabled_mods": [], "disabled_mods": []}

def save_profile(profile_name, enabled_mods, disabled_mods):
    """Save a profile to a JSON file."""
    profile_path = os.path.join(os.path.dirname(__file__), "profiles", f"{profile_name}.json")
    if not os.path.exists(os.path.dirname(profile_path)):
        os.makedirs(os.path.dirname(profile_path))
    with open(profile_path, "w") as f:
        json.dump({"enabled_mods": sorted(enabled_mods), "disabled_mods": sorted(disabled_mods)}, f, indent=4)
    with open(os.path.join(os.path.dirname(__file__), "profiles", f"{profile_name}.e.txt"), "w") as f:
        f.write(", ".join(enabled_mods))
        f.close()
    with open(os.path.join(os.path.dirname(__file__), "profiles", f"{profile_name}.d.txt"), "w") as f:
        f.write(", ".join(disabled_mods))
        f.close()

def create_profile(mods_folder):
    """Create a new profile."""
    profile_name = input("Enter the name of the new profile: ")
    enabled_mods = list_mods(mods_folder)
    archive_folder = os.path.join(os.path.dirname(__file__), "archive")
    disabled_mods = list_mods(archive_folder) if os.path.exists(archive_folder) else []
    save_profile(profile_name, enabled_mods, disabled_mods)
    print(f"Profile {profile_name} created.")
    print(f"{len(enabled_mods)} mods enabled, {len(disabled_mods)} mods disabled!")

def show_profiles():
    """Show a list of all profiles."""
    profiles_folder = os.path.join(os.path.dirname(__file__), "profiles")
    profiles = [f.split('.')[0] for f in os.listdir(profiles_folder) if f.endswith('.json')]
    if os.path.exists(profiles_folder) and len(profiles) > 0:
        print("Available profiles:")
        print("\n".join(profiles))
    else:
        print("No profiles found.")

def delete_profile():
    """Delete a profile."""
    profile_name = input("Enter the name of the profile to delete: ")
    profile_path = os.path.join(os.path.dirname(__file__), "profiles", f"{profile_name}.json")
    if os.path.exists(profile_path):
        os.remove(profile_path)
        print(f"Profile {profile_name} deleted.")
    else:
        print(f"Profile {profile_name} does not exist.")

def apply_profile(profile_name, mods_folder):
    """Apply a profile to enable or disable mods."""
    profile = load_profile(profile_name)
    enabled_mods = profile.get("enabled_mods", [])
    disabled_mods = profile.get("disabled_mods", [])
    
    archive_folder = os.path.join(os.path.dirname(__file__), "archive")
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Disable all mods not in the enabled list
    mods_in_folder = list_mods(mods_folder)
    for mod in progress_bar(mods_in_folder, description="Disabling mods"):
        if mod not in enabled_mods:
            move_mod(mod, mods_folder, archive_folder)
    
    # Enable all mods listed in the profile
    for mod in progress_bar(enabled_mods, description="Enabling mods"):
        if not os.path.exists(os.path.join(mods_folder, mod)):
            move_mod(mod, archive_folder, mods_folder)
    
    # Disable all mods listed in the disabled list
    for mod in progress_bar(disabled_mods, description="Disabling mods"):
        if not os.path.exists(os.path.join(archive_folder, mod)):
            move_mod(mod, mods_folder, archive_folder)
    
    print(f"Profile {profile_name} applied.")
    print(f"{len(enabled_mods)} mods are enabled, {len(disabled_mods)} mods are disabled!")

def backup(mods_folder, backup_name):
    """Create a backup of the mods folder."""
    backup_folder = os.path.join(os.path.dirname(__file__), "backups")
    os.makedirs(backup_folder, exist_ok=True)
    
    backup_path = os.path.join(backup_folder, f"{backup_name}.zip")
    
    with zipfile.ZipFile(backup_path, 'w', compression=zipfile.ZIP_LZMA) as backup_zip:
        for root, dirs, files in os.walk(mods_folder):
            for file in progress_bar(files, description="Backing up mods"):
                file_path = os.path.join(root, file)
                backup_zip.write(file_path, os.path.relpath(file_path, mods_folder))
    print(f"Backup created ({backup_path})")
