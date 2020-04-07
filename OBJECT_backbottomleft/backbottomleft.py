import bpy
 
class OBJECT_PT_recenter(bpy.types.Panel):
	bl_label = "Recenter BBL"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Tools"
	bl_context = "objectmode"


	def execute(self, context):
		layout = self.layout
		return {'FINISHED'}

	def draw_header(self, context):
		layout = self.layout

	def draw(self, context):
		layout = self.layout
		layout.operator("object.recenter", text="Recenter")

class OBJECT_OT_recenter(bpy.types.Operator):
	bl_label = "Recenter BBL"
	bl_idname = "object.recenter"
	bl_description = "Move the ball"
 
	def execute(self, context):
		bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
		obj = bpy.context.scene.objects.active
		bpy.context.scene.cursor_location = (0,0,0)
		bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
		obj.location = (obj.dimensions.x/2, -obj.dimensions.y/2, obj.dimensions.z/2)
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
		self.report({'INFO'}, "Recentering")
		return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()