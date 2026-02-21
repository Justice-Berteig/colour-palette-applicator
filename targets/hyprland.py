from utils import getConfigPath

CONFIG_FILE_PATH = getConfigPath() + "/hypr/colours.conf"


def apply_colours_to_hyprland(colours):
    print("Applying colours to hyprland config... ", end='')

    hypr_colours = ""
    for key, value in colours.items():
        hypr_colours += "$" + key + " = rgba(" + value[1:] + "ff)\n"

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write(hypr_colours)

    print("Done!")
