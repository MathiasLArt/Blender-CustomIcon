from bpy.utils import previews
import os


ICONS = previews.new()


def load_all_icons(folder_path=".\\icons"):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            icon_name, _ = os.path.splitext(filename)
            icon_path = os.path.join(folder_path, filename)
            ICONS.load(name=icon_name, path=icon_path, path_type="IMAGE")


def unregister_icons():
    previews.remove(ICONS)
