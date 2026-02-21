import re
from utils import getConfigPath

CONFIG_FILE_PATH = getConfigPath() + "/waybar/style.css"


def apply_colours_to_waybar(colours):
    print("Applying colours to waybar config... ", end='')

    waybar_colours = colours.copy()

    lines = []
    with open(CONFIG_FILE_PATH) as config_file:
        while line := config_file.readline():
            match = re.search(r"^@define-color .+ #[0-9a-fA-F]{6};$", line)
            if not match :
                lines.append(line)
            elif len(waybar_colours) > 0:
                for key, value in waybar_colours.items():
                    lines.append("@define-color " + key + " " + value.lower() + ";\n")

                waybar_colours = {}

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write("".join(lines))

    print("Done!")
