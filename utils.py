from pathlib import Path


def getConfigPath():
    return str(Path.home()) + "/.config"
