import bpy

textWidth = 0
textDepth = 0
textHeight = 0
textBevel = 0.00025
textExtrude = 0.00025
textSize = 0.05
textLeading = 0.1
arrowRadius = 0.01
arrowDepth = 0.03
intObjects = 0

strObject = bpy.context.active_object.name
arrObjects = bpy.context.active_object.name

floatWidth = bpy.context.active_object.dimensions.x
floatDepth = bpy.context.active_object.dimensions.y
floatHeight = bpy.context.active_object.dimensions.z

floatX = bpy.context.active_object.location.x
floatY = bpy.context.active_object.location.y
floatZ = bpy.context.active_object.location.z


bpy.context.scene.cursor_location = (floatX,floatY,floatZ)

if floatWidth < 1:
    strWidth = str("%.2f" % round(floatWidth*100,2)) + "cm"
else:
    strWidth = str("%.2f" % round(floatWidth,2)) + "m"
    
if floatDepth < 1:
    strDepth = str("%.2f" % round(floatDepth*100,2)) + "cm"
else:
    strDepth = str("%.2f" % round(floatDepth,2)) + "m"
    
if floatHeight < 1:
    strHeight = str("%.2f" % round(floatHeight*100,2)) + "cm"
else:
    strHeight = str("%.2f" % round(floatHeight,2)) + "m"


#Width text
bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'TxtWidth'

ob = bpy.context.object
ob.data.body = strWidth
ob.data.align_x = 'CENTER'
ob.data.bevel_depth = textBevel
ob.data.extrude = textExtrude
ob.data.size = textSize
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
ob.location = (floatX + floatWidth/2, floatY - floatDepth - textLeading, floatZ)
bpy.ops.object.convert(target='MESH')


#Depth text
bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'TxtDepth'

ob = bpy.context.object
ob.data.body = strDepth
ob.data.align_x = 'CENTER'
ob.data.bevel_depth = textBevel
ob.data.extrude = textExtrude
ob.data.size = textSize
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
ob.location = (floatX - ob.dimensions.x/2 - textLeading, floatY - floatDepth/2, floatZ)
bpy.ops.object.convert(target='MESH')


#Height text
bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'TxtHeight'

ob = bpy.context.object
ob.data.body = strHeight
ob.data.align_x = 'CENTER'
ob.data.bevel_depth = textBevel
ob.data.extrude = textExtrude
ob.data.size = textSize
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
ob.location = (floatX + floatWidth + ob.dimensions.x/2 + textLeading, floatY - floatDepth/2, floatZ + floatHeight/2)
textWidth = ob.dimensions.x
textDepth = ob.dimensions.y
textHeight = ob.dimensions.z
bpy.ops.object.convert(target='MESH')



#Width arrows
bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowWidthRight'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (floatX + floatWidth - ob.dimensions.x/2, bpy.data.objects['TxtWidth'].location.y, floatZ + bpy.data.objects['TxtWidth'].dimensions.y/2)

bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, -1.5708, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowWidthLeft'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (floatX + ob.dimensions.x/2, bpy.data.objects['TxtWidth'].location.y, floatZ + bpy.data.objects['TxtWidth'].dimensions.y/2)

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatWidth-bpy.data.objects['TxtWidth'].dimensions.x-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylWidthRight'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (floatX + floatWidth - bpy.data.objects['arrowWidthRight'].dimensions.x - ob.dimensions.x/2, bpy.data.objects['TxtWidth'].location.y, floatZ + bpy.data.objects['TxtWidth'].dimensions.y/2)

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatWidth-bpy.data.objects['TxtWidth'].dimensions.x-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylWidthLeft'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (floatX + bpy.data.objects['arrowWidthRight'].dimensions.x + ob.dimensions.x/2, bpy.data.objects['TxtWidth'].location.y, floatZ + bpy.data.objects['TxtWidth'].dimensions.y/2)

#Height arrows
bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowHeightTop'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtHeight'].location.x, bpy.data.objects['TxtHeight'].location.y, floatZ + floatHeight - ob.dimensions.z/2)

bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(3.14159, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowHeightBottom'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtHeight'].location.x, bpy.data.objects['TxtHeight'].location.y, floatZ + ob.dimensions.z/2)

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatHeight-bpy.data.objects['TxtHeight'].dimensions.y-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylHeightTop'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtHeight'].location.x, bpy.data.objects['TxtHeight'].location.y, floatZ + floatHeight - bpy.data.objects['arrowHeightTop'].dimensions.z - ob.dimensions.z/2)

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatHeight-bpy.data.objects['TxtHeight'].dimensions.y-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylHeightBottom'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtHeight'].location.x, bpy.data.objects['TxtHeight'].location.y, floatZ + floatHeight/2 - bpy.data.objects['arrowHeightTop'].dimensions.z/2 - ob.dimensions.z/2)

#Depth arrows
bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(-1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowDepthBack'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtDepth'].location.x, floatY - ob.dimensions.y/2, floatZ + bpy.data.objects['TxtDepth'].dimensions.y/2 )

bpy.ops.mesh.primitive_cone_add(radius1=arrowRadius, radius2=0, depth=arrowDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'arrowDepthFront'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtDepth'].location.x, floatY - floatDepth + ob.dimensions.y/2, floatZ + bpy.data.objects['TxtDepth'].dimensions.y/2 )

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatDepth-bpy.data.objects['TxtDepth'].dimensions.y-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylDepthBack'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtDepth'].location.x, floatY - bpy.data.objects['arrowDepthBack'].dimensions.y - ob.dimensions.y/2, floatZ + bpy.data.objects['TxtDepth'].dimensions.y/2 )

bpy.ops.mesh.primitive_cylinder_add(radius=(arrowRadius/10), depth=((floatDepth-bpy.data.objects['TxtDepth'].dimensions.y-textLeading)/2), view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.active_object.name = 'cylDepthFront'
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
ob = bpy.context.object
ob.location = (bpy.data.objects['TxtDepth'].location.x, floatY - floatDepth + bpy.data.objects['arrowDepthBack'].dimensions.y + ob.dimensions.y/2, floatZ + bpy.data.objects['TxtDepth'].dimensions.y/2 )

bpy.data.objects['TxtWidth'].select = True
bpy.data.objects['TxtDepth'].select = True
bpy.data.objects['TxtHeight'].select = True

bpy.data.objects['arrowWidthRight'].select = True
bpy.data.objects['arrowWidthLeft'].select = True
bpy.data.objects['cylWidthRight'].select = True
bpy.data.objects['cylWidthLeft'].select = True

bpy.data.objects['arrowHeightTop'].select = True
bpy.data.objects['arrowHeightBottom'].select = True
bpy.data.objects['cylHeightTop'].select = True
bpy.data.objects['cylHeightBottom'].select = True

bpy.data.objects['arrowDepthBack'].select = True
bpy.data.objects['arrowDepthFront'].select = True
bpy.data.objects['cylDepthBack'].select = True
bpy.data.objects['cylDepthFront'].select = True


bpy.ops.object.join()
obj = bpy.context.scene.objects.active
bpy.context.scene.cursor_location = (0,0,0)
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

bpy.data.objects[strObject].select = True
obj = bpy.context.scene.objects.active
#strObject = bpy.context.scene.objects.active

bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
