import bpy

#----RENDER SETTINGS----
samples = 2000
resolution_x = 1920
resolution_y = 1080
resolution_percentage = 200
tile_size = 512
freestyle_samples = 1
use_filename = True
use_denoising = False
use_simplify = False
max_texture_size = 2048
max_subdivisions = 2
is_freestyle_array = [False]

is_animation = True
use_motion_blur = True
frame_start = 283
frame_end = 300


#----SCENE SETTINGS----
scenes_to_render = ["Scene"]

viewlayers_to_render = ["white"]
cameras_to_render = ["Camera"]
material_override = ["None"]


#----COLOR MANAGEMENT----
view_transform = "Filmic"
look = "Filmic - Medium High Contrast"
exposure = 1
gamma = 1

# file_format = "JPEG", "PNG", "OPEN_EXR_MULTILAYER"
file_format = "PNG"
exr_codec = "ZIP"
color_mode = "RGB"
color_depth = "8"
render_engine = "CYCLES"

prefix = "TEST_"
filepath = "//renders\\"

#----VIEWLAYER SETTINGS----
use_pass_crypto_object = True
use_pass_crypto_material = True
use_pass_crypto_asset = True
pass_crypto_depth = 6


def render(filename, scene, view_layer):
    # print(f"{scene}: {view_layer}")
    for layer in bpy.data.scenes[scene].view_layers:
        if layer.name == view_layer:
            layer.use = True
        else:
            layer.use = False
    print(f"-----{scene}:{view_layer}-----\n{layer.use}")
    bpy.ops.render.render(animation=is_animation, write_still=True, scene=scene, layer=view_layer)


def set_freestyle(scene='Scene', view_layer='View Layer'):
    lineset = "render_only"
    bpy.data.scenes[scene].view_layers[view_layer].freestyle_settings.linesets.new(lineset)
    bpy.data.scenes[scene].view_layers[view_layer].freestyle_settings.linesets[lineset].select_contour = True
    bpy.data.scenes[scene].view_layers[view_layer].freestyle_settings.linesets[lineset].select_edge_mark = True
    bpy.data.scenes[scene].view_layers[view_layer].freestyle_settings.linesets[lineset].select_external_contour = True
    bpy.context.scene.render.line_thickness = 0.5


def settings_list():
    material_keys = bpy.data.materials.keys() + ["None"]
    filename = bpy.path.display_name_from_filepath(bpy.data.filepath) + "_" if use_filename else ""

    render_settings = [{
        "filename": ("fsr_" if is_freestyle else "prr_") + scene + "_" + view_layer + "_" + material + "_" + filename + camera,
        "is_freestyle": is_freestyle,
        "scene": scene,
        "view_layer": view_layer,
        "camera": camera,
        "material": material
    }
        for scene in scenes_to_render if scene in bpy.data.scenes.keys()
        for view_layer in viewlayers_to_render if view_layer in bpy.data.scenes[scene].view_layers.keys()
        for camera in cameras_to_render if camera in bpy.data.cameras.keys()
        for material in material_override if material in material_keys
        for is_freestyle in is_freestyle_array if (material != "None" and is_freestyle) or (material == "None" and not is_freestyle)
    ]
    return render_settings

def set_wall_width(scene_name):
    strWidth = int(scene_name[0:scene_name.find("ft")])
    width = ((strWidth*12)+1.5)*0.0254
    bpy.data.objects['emptyDimensions'].location[0] = width

def set_local_render_settings(render_settings):
    for scene in bpy.data.scenes.keys():
        for view_layer in bpy.data.scenes[scene].view_layers.keys():
            set_freestyle(scene, view_layer)

    for setting in render_settings:
        print("--------------------------START SETTINGS-------------------------")
        bpy.data.scenes[setting["scene"]].render.use_freestyle = setting["is_freestyle"]
        bpy.data.scenes[setting["scene"]].cycles.samples = freestyle_samples if setting["is_freestyle"] else samples
        # bpy.data.scenescontext.window.scene = bpy.data.scenes[setting["scene"]]
        # bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]] = bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]]
        bpy.data.scenes[setting["scene"]].camera = bpy.data.objects[setting["camera"]]
        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].material_override = bpy.data.materials[setting["material"]] if setting["material"] != "None" else None
        bpy.data.scenes[setting["scene"]].render.filepath = f"{filepath}{setting['filename']}"

        bpy.data.scenes[setting["scene"]].render.resolution_x = resolution_x
        bpy.data.scenes[setting["scene"]].render.resolution_y = resolution_y
        bpy.data.scenes[setting["scene"]].render.resolution_percentage = resolution_percentage
        bpy.data.scenes[setting["scene"]].render.tile_x = tile_size
        bpy.data.scenes[setting["scene"]].render.tile_y = tile_size
        bpy.data.scenes[setting["scene"]].render.film_transparent = True
        bpy.data.scenes[setting["scene"]].render.engine = render_engine
        bpy.data.scenes[setting["scene"]].render.use_motion_blur = use_motion_blur
        
        bpy.data.scenes[setting["scene"]].render.image_settings.file_format = file_format
        bpy.data.scenes[setting["scene"]].render.image_settings.exr_codec = exr_codec
        bpy.data.scenes[setting["scene"]].render.image_settings.color_mode = color_mode
        bpy.data.scenes[setting["scene"]].render.image_settings.color_depth = color_depth

        bpy.data.scenes[setting["scene"]].frame_start = frame_start
        bpy.data.scenes[setting["scene"]].frame_end = frame_end

        bpy.data.scenes[setting["scene"]].render.use_simplify = use_simplify
        bpy.data.scenes[setting["scene"]].render.simplify_subdivision_render = max_subdivisions
        bpy.data.scenes[setting["scene"]].cycles.texture_limit = str(max_texture_size)

        bpy.data.scenes[setting["scene"]].view_settings.view_transform = view_transform
        bpy.data.scenes[setting["scene"]].view_settings.exposure = exposure
        bpy.data.scenes[setting["scene"]].view_settings.gamma = gamma
        bpy.data.scenes[setting["scene"]].view_settings.look = look

        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].cycles.use_denoising = use_denoising
        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].cycles.use_pass_crypto_object = use_pass_crypto_object
        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].cycles.use_pass_crypto_material = use_pass_crypto_material
        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].cycles.use_pass_crypto_asset = use_pass_crypto_asset
        bpy.data.scenes[setting["scene"]].view_layers[setting["view_layer"]].cycles.pass_crypto_depth = pass_crypto_depth
        
        print("--------------------------END SETTINGS-------------------------")
        render(setting["filename"], setting['scene'], setting['view_layer'])



mock_settings = [{
    "filename": "ARMANDO",
    "is_freestyle": False,
    "scene": "scene",
    "view_layer": "props",
    "camera": "camera.M",
    "material": "clay"
}
]

render_settings = settings_list()
set_local_render_settings(render_settings)
