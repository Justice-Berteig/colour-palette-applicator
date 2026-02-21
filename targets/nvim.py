import re
from utils import getConfigPath

CONFIG_FILE_PATH = getConfigPath() + "/nvim/colourschemes/metalheart/lua/lush_theme/metalheart.lua"


def apply_colours_to_nvim(colours):
    print("Applying colours to nvim config... ", end='')

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
