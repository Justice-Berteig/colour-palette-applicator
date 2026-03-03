import json
import os
import re
from utils import getConfigPath

CONFIG_FOLDER_PATH   = getConfigPath() + "/btop"
THEMES_FOLDER_PATH   = CONFIG_FOLDER_PATH + "/themes"
COLOUR_MAP_FILE_PATH = THEMES_FOLDER_PATH + "/colour_map.json"


def apply_colours_to_btop(colours):
    print("Applying colours to btop theme... ", end='')

    # Map palette colours to btop theme colours
    colour_map = {}
    try:
        with open(COLOUR_MAP_FILE_PATH) as colour_map_file:
            colour_map = json.load(colour_map_file)
    except Exception as e:
        print()
        print("\t" + str(e))
        print("\tFailed to apply colours to btop config!")
        return


    files = os.listdir(THEMES_FOLDER_PATH)
    theme_files = []
    for file in files:
        if file.endswith(".theme"):
            theme_files.append(file)

    if len(theme_files) < 1:
        raise RuntimeError(
            "Error: Could not locate btop theme file!"
        )
    elif len(theme_files) > 1:
        raise RuntimeError(
            "Error: Multiple btop theme files present."
            + " Don't know which to replace!"
        )

    THEME_FILE_PATH = THEMES_FOLDER_PATH + "/" + theme_files[0]

    lines = []
    with open(THEME_FILE_PATH) as theme_file:
        while line := theme_file.readline():
            match = re.search(r"^theme\[([a-z_]+)\]\s*=\s*\"", line)
            if match and match.group(1) in colour_map:
                btop_colour_name    = match.group(1)
                palette_colour_name = colour_map[btop_colour_name]

                palette_colour = ""
                if len(palette_colour_name) > 0:
                    palette_colour = colours[palette_colour_name]

                line = match.group(0) + palette_colour + "\"\n"

            lines.append(line)

    with open(THEME_FILE_PATH, "w") as theme_file:
        theme_file.write("".join(lines))

    print("Done!")
