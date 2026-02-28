import os
import re
from utils import getConfigPath

CONFIG_FOLDER_PATH = getConfigPath() + "/nvim/colourschemes"


def apply_colours_to_nvim(colours):
    print("Applying colours to nvim config... ")
    print("\tTrying to find colourscheme file...")

    dir_names = os.listdir(CONFIG_FOLDER_PATH)
    if len(dir_names) > 1:
        raise RuntimeError("Error: Multiple Neovim colourschemes present. Don't know which to replace!")
    elif len(dir_names) < 1:
        raise RuntimeError("Error: No Neovim colourscheme present!")
    CONFIG_FILE_PATH = CONFIG_FOLDER_PATH + "/" + dir_names[0] + "/lua/lush_theme/" + dir_names[0] + ".lua"
    print("\tFound colourscheme file at " + CONFIG_FILE_PATH)

    lines = []
    with open(CONFIG_FILE_PATH) as config_file:
        while line := config_file.readline():
            match = re.search(r"^local\s+([a-z0-5\_]+)\s*=\s*hsl\(\"#[0-9a-fA-F]{6}\"\)$", line)
            if(match and match.group(1) in colours):
                colour_name = match.group(1)
                line = "local " + colour_name + " = hsl(\"" + colours[colour_name] + "\")\n"

            lines.append(line)

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write("".join(lines))

    print("Done!")
