import json
import os
import re

from targets.btop     import apply_colours_to_btop
from targets.foot     import apply_colours_to_foot
from targets.fuzzel   import apply_colours_to_fuzzel
from targets.hyprland import apply_colours_to_hyprland
from targets.nvim     import apply_colours_to_nvim
from targets.waybar   import apply_colours_to_waybar


def main():
    try:

        # Get list of palette names
        files = os.listdir("./palettes/")
        palettes = []
        for file in files:
            if file.endswith(".json"):
                palettes.append(re.sub(r"\.json$", "", file))
        print(palettes)

        # Select a colour palette
        selected_palette = None

        if len(palettes) == 0:
            raise RuntimeError("Error: No palettes in ./palettes/")
        elif len(palettes) == 1:
            selected_palette = palettes[0]
        else:
            print("Select a colour palette to apply:")
            for index, palette in enumerate(palettes):
                print("[" + str(index + 1) + "] " + palette)

            while not selected_palette in palettes:
                if selected_palette is not None:
                    print("Invalid selection! Try again:")
                user_input = input()
                if (
                    re.match(r"^[0-9]+$", user_input)
                    and int(user_input) <= len(palettes)
                ):
                    selected_palette = palettes[int(user_input) - 1]
                else:
                    selected_palette = user_input
            print()

        print("Applying " + selected_palette + " palette...")

        # Load palette
        palette = None
        with open("./palettes/" + selected_palette + ".json") as palette_file:
            palette = json.load(palette_file)

        colours = palette["colours"]

        # Apply palette to targets
        apply_colours_to_btop(colours)
        apply_colours_to_foot(colours)
        apply_colours_to_fuzzel(colours)
        apply_colours_to_hyprland(colours)
        apply_colours_to_nvim(colours)
        apply_colours_to_waybar(colours)

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
