import json
import re
from utils import getConfigPath

COLOUR_MAP_FILE_PATH = getConfigPath() + "/fuzzel/colour_map.json"
CONFIG_FILE_PATH     = getConfigPath() + "/fuzzel/fuzzel.ini"


def apply_colours_to_fuzzel(colours):
    print("Applying colours to fuzzel config... ", end='')

    # Map palette colours to fuzzel config colours
    colour_map = {}
    try:
        with open(COLOUR_MAP_FILE_PATH) as colour_map_file:
            colour_map = json.load(colour_map_file)
    except Exception as e:
        print()
        print("\t" + str(e))
        print("\tFailed to apply colours to fuzzel config!")
        return

    """
    colour_map = {
        "background"     : "bg0",
        "text"           : "fg0",
        "prompt"         : "bright_blue",
        "placeholder"    : "dark_blue",
        "input"          : "fg2",
        "match"          : "bright_green",
        "selection"      : "fg1",
        "selection-text" : "bg0",
        "selection-match": "dark_green",
        "counter"        : "fg2",
        "border"         : "fg5"
    }
    """

    lines = []
    with open(CONFIG_FILE_PATH) as config_file:
        in_colour_section = False
        while line := config_file.readline():
            if len(colour_map) > 0:
                if in_colour_section:
                    match = re.search(r"^#?\s*([a-z\-]+)\s*=\s*[0-9a-fA-F]{8}$", line)
                    if(match and match.group(1) in colour_map):
                        fuzzel_colour_name = match.group(1)
                        palette_colour_name = colour_map.pop(fuzzel_colour_name)
                        line = fuzzel_colour_name + " = " + colours[palette_colour_name][1:] + "FF\n"
                elif line == "[colors]\n":
                    in_colour_section = True

            lines.append(line)

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write("".join(lines))

    print("Done!")
