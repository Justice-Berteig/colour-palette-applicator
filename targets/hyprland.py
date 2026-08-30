import re
from utils import getConfigPath

CONFIG_FILE_PATH = getConfigPath() + "/hypr/colours.lua"


def apply_colours_to_hyprland(colours):
    print("Applying colours to hyprland config... ", end='')

    hypr_colours = ""
    for key, value in colours.items():
        hypr_colours += "$" + key + " = rgba(" + value[1:] + "ff)\n"

    lines = []
    with open(CONFIG_FILE_PATH) as config_file:
        while line := config_file.readline():
            match = re.search(r"^([a-zA-Z0-5\_]+)\s*=\s*\"rgba\(([a-zA-Z0-9]{6})ff\)\"", line)
            if(match and match.group(1) in colours):
                colour_name = match.group(1)
                old_colour  = match.group(2)

                # Replace colour with new colour.
                line = line.replace(old_colour, colours[colour_name][1:])

            lines.append(line)

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write("".join(lines))

    print("Done!")
