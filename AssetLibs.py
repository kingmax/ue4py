# coding:utf-8
# ue4 asset functions

import unreal


def build_import_task(filename, dest_path, options=None):
    # unreal.AssetImportTask    https://api.unrealengine.com/INT/PythonAPI/class/AssetImportTask.html
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', dest_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    # for Fbx Mesh
    task.set_editor_property('options', options)
    return task


def do_import_tasks(tasks):
    # unreal.AssetToolsHelpers  https://api.unrealengine.com/INT/PythonAPI/class/AssetToolsHelpers.html
    # unreal.AssetTools [Abstract Class? baseClass is unreal.Interface]
    # https://api.unrealengine.com/INT/PythonAPI/class/AssetTools.html
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            unreal.log_warning('Imported: %s'%path)


def build_static_mesh_import_options():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI    https://api.unrealengine.com/INT/PythonAPI/class/FbxImportUI.html
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)  # Static Mesh
    # unreal.FbxMeshImportData  https://api.unrealengine.com/INT/PythonAPI/class/FbxMeshImportData.html
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxStaticMeshImportData    https://api.unrealengine.com/INT/PythonAPI/class/FbxStaticMeshImportData.html
    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options


def build_skeletal_mesh_import_options():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI    https://api.unrealengine.com/INT/PythonAPI/class/FbxImportUI.html
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', True)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', True)  # Skeletal Mesh
    # unreal.FbxMeshImportData  https://api.unrealengine.com/INT/PythonAPI/class/FbxMeshImportData.html
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxSkeletalMeshImportData
    # https://api.unrealengine.com/INT/PythonAPI/class/FbxSkeletalMeshImportData.html
    options.static_mesh_import_data.set_editor_property('import_morph_targets', True)
    options.static_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)
    return options


# #################################################### Testing
def test_import_textures():
    # import textures testing
    import os
    _dir = 'D:/download/'
    _textures = ['T_Snow_N.psd', 'Cliffs0464_7_seamless_S.jpg']
    tasks = []
    for tex in _textures:
        task = build_import_task(os.path.join(_dir, tex), '/Game/Textures')
        tasks.append(task)
    do_import_tasks(tasks)


def test_import_fbx():
    # import as StaticMesh Or SkeletalMesh
    static_mesh_fbx = r'D:/git/ue4py/myCube.fbx'
    skeletal_mesh_fbx = r'D:/git/ue4py/myCube.fbx'
    static_mesh_task = build_import_task(static_mesh_fbx, '/Game/StaticMeshes', build_static_mesh_import_options())
    skeletal_mesh_task = build_import_task(skeletal_mesh_fbx, '/Game/SkeletalMeshes', build_skeletal_mesh_import_options())
    do_import_tasks([static_mesh_task, skeletal_mesh_task])


def main():
    pass

