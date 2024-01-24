# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "CustomIcons",
    "author": "M4thi4sL",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

from . import auto_load
from . import icon_loader

from .src.panel import *

auto_load.init()


def register():
    # Register the panel
    auto_load.register()
    icon_loader.load_all_icons(folder_path=".\\icons")


def unregister():
    icon_loader.unregister_icons()

    # Unregister the panel
    auto_load.unregister()


if __name__ == "__main__":
    register()
