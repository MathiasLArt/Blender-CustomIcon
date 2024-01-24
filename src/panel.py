from bpy.types import Panel
from ..icon_loader import ICONS


class ICON_PT_PARENT_PANEL(Panel):
    bl_idname = "ICON_PT_PARENT_PANEL"
    bl_label = "Custom Icons"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "custom icons"

    def draw(self, context):
        layout = self.layout

        # Loop over all icons in the ICONS
        for icon_name, icon_data in ICONS.items():
            row = layout.row()
            row.operator("render.render", text=icon_name, icon_value=icon_data.icon_id)


class ICON_PT_CHILD_PANEL(Panel):
    bl_idname = "ICON_PT_CHILD_PANEL"
    bl_label = "Child Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "custom icons"
    bl_parent_id = "ICON_PT_PARENT_PANEL"

    def draw(self, context):
        layout = self.layout

        # manually assign our custom item to an operator
        row = layout.row()
        row.operator(
            "render.render", text="manualmode", icon_value=ICONS["ico-devices"].icon_id
        )
