# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "Origin To Edit Selection",
    "author": "Armando Tello",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "VIEW3D > Specials|Right-click menu > Origin To Selection",
    "description": "Moves the pivot point to the current selection without leaving edit mode.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"}

import bpy

class OriginToSelection(bpy.types.Operator):
    bl_idname = "origin2selection.bba"
    bl_label = "Origin to edit selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

def draw_item(self, context):
    self.layout.operator(OriginToSelection.bl_idname)
    
def register():
    bpy.utils.register_class(OriginToSelection)
    bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_item)

def unregister():
    bpy.utils.unregister_class(OriginToSelection)
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_item)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
