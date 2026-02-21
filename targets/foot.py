import re
from utils import getConfigPath

CONFIG_FILE_PATH = getConfigPath() + "/foot/foot.ini"


def apply_colours_to_foot(colours):
    print("Applying colours to foot config... ", end='')

    # Map palette colours to foot config colours
    colour_map = {
        "background": "bg0",
        "foreground": "fg0",
        "regular0"  : "bg0",
        "regular1"  : "dark_red",
        "regular2"  : "dark_green",
        "regular3"  : "dark_yellow",
        "regular4"  : "dark_blue",
        "regular5"  : "dark_purple",
        "regular6"  : "dark_cyan",
        "regular7"  : "fg2",
        "bright0"   : "bg2",
        "bright1"   : "bright_red",
        "bright2"   : "bright_green",
        "bright3"   : "bright_yellow",
        "bright4"   : "bright_blue",
        "bright5"   : "bright_purple",
        "bright6"   : "bright_cyan",
        "bright7"   : "fg0"
    }

    lines = []
    with open(CONFIG_FILE_PATH) as config_file:
        in_colour_section = False
        while line := config_file.readline():
            if len(colour_map) > 0:
                if in_colour_section:
                    match = re.search(r"^#?\s*([a-z0-7]+)\s*=\s*[0-9a-fA-F]{6}$", line)
                    if(match and match.group(1) in colour_map):
                        foot_colour_name = match.group(1)
                        palette_colour_name = colour_map.pop(foot_colour_name)
                        line = foot_colour_name + " = " + colours[palette_colour_name][1:] + "\n"
                elif line == "[colors]\n":
                    in_colour_section = True

            lines.append(line)

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write("".join(lines))

    print("Done!")
