import json5, json
import sys
import os
import subprocess
import shutil
from pathlib import Path

ffpath = Path.home() / ".config/fastfetch/"

if (ffpath / "config.jsonc").exists():
    while True:
        backup_prompt = input("make a backup of current config.jsonc? [y/n] ")
        if ((backup_prompt == "y") or (backup_prompt == "Y")): 
            shutil.copy2(
                f"{str(ffpath / "config.jsonc")}", 
                f"{str(ffpath / "config.jsonc.bak")}"
            )
        elif ((backup_prompt == "n") or (backup_prompt == "N")):
            break
            
        if (((backup_prompt == "y") or (backup_prompt == "Y")) or ((backup_prompt == "y") or (backup_prompt == "Y"))):
            break
            
else:
    gen_config = subprocess.run(["fastfetch", "--gen-config"], capture_output=True, text=True)
    print(f"generating config file {str(ffpath)}.jsonc\n" + gen_config.stdout)
    
ffconfigpath = ffpath / "config.jsonc"

hats = {}

print("available hats:")

for path, dirname, filename in os.walk(ffpath / "fastfetch-touhou-hats/hats"):
    for item in filename:
        if item.endswith(".jsonc"):
            #checking if an ascii art is present
            if item.replace(".jsonc", ".ascii") in filename:
                hatname = item.split(".")[0]
                hats[hatname] = ffpath / "fastfetch-touhou-hats/hats" / hatname
                print(hatname)
            else:
                hatname = item.split(".")[0]
                print(f"\x1b[33m{hatname} (ascii not found)\x1b[0m")

chosen_hat = input("choose the desired hat: ")

if chosen_hat not in hats:
    #errors with code 1 if user input is invalid
    print("\x1b[31mno such hat\x1b[0m")
    sys.exit(1)

ffconfig = None
hatconfig = None

with open(ffconfigpath) as f:
    ffconfig = json5.load(f)

with open(hats[chosen_hat] / (chosen_hat + ".jsonc")) as f:
    hatconfig = json5.load(f)

def deep_merge(base: dict, override: dict) -> dict:
    result = base.copy()
    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

ffconfignew = deep_merge(ffconfig, hatconfig)

ffconfignew["logo"]["source"] = str(hats[chosen_hat] / (chosen_hat + ".ascii"))
ffconfignew["display"]["brightColor"] = "false"

with open(ffconfigpath, "w") as f:
    json.dump(ffconfignew, f, indent=4)

print("\x1b[32msuccesfully changed the fastfetch hat!\x1b[0m")
