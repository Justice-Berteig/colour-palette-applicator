import json

from targets.foot     import apply_colours_to_foot
from targets.fuzzel   import apply_colours_to_fuzzel
from targets.hyprland import apply_colours_to_hyprland
from targets.nvim     import apply_colours_to_nvim
from targets.waybar   import apply_colours_to_waybar

PALETTES_FILE_NAME = "palettes.json"


def choose_palette(palettes):
    # Get list of palette names
    palette_names = list(palettes.keys())
    if len(palette_names) < 1:
        print("Error: " + PALETTES_FILE_NAME + " contained no colour palettes!")
        return {}

    # Choose a colour palette
    chosen_palette = {}
    if len(palette_names) == 1:
        # If there is only one palette choose that one
        chosen_palette = palettes[palette_names[0]]
    else:
        # Otherwise ask the user which palette to use
        print("Choose a colour palette from " + str(palette_names) + ":")

        chosen_palette_name = None
        while not chosen_palette_name in palette_names:
            if chosen_palette_name is not None:
                print(
                    "Invalid selection! Please choose from "
                    + str(palette_names)
                    + ":"
                )
            chosen_palette_name = input()
        print()

        chosen_palette = palettes[chosen_palette_name]

        # Print the chosen palette
        print(
            "You chose \'"
            + chosen_palette_name
            + "\' which contains the colours:"
        );
        for key, value in chosen_palette.items():
            print("{: <13}: {: <7}".format(key, value))
        print()

    return chosen_palette


def main():
    # Read the palettes from JSON
    palettes = {}
    try:
        with open(PALETTES_FILE_NAME) as infile:
            palettes = json.load(infile)
    except Exception as e:
        print(e)
        return

    # Choose a colour palette from the palettes
    palette = choose_palette(palettes)

    # Apply colours to all targets
    apply_colours_to_foot(palette)
    apply_colours_to_fuzzel(palette)
    apply_colours_to_hyprland(palette)
    apply_colours_to_nvim(palette)
    apply_colours_to_waybar(palette)


if __name__ == "__main__":
    main()
