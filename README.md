Some small helper functions that allow you to setup custom icons and use them throughout Blender UI. 

![image](https://github.com/MathiasLArt/Blender-CustomIcon/assets/59111832/37c42da2-fc7b-45c1-b6b8-13c4788c8106)



Point the helper to the folder where you keep your icons, it will scan them and add them all. Every entry will use the filename for future reference.
You can pass along a custom path should you decide to keep your icons elsehwere, if none is specified it will go with the default (.\\icons)
``` 
def register():
    auto_load.register()
    icon_loader.load_all_icons(folder_path=".\\icons")
``` 
You can acces your custom icons simply by importing ICONS from the icon-loader.py.
``` 
from ..icon_loader import ICONS
``` 
And then calling them like this:
``` 
ICONS["ico-devices"].icon_id
```
For a more conrete example, check the github panel.py file.
