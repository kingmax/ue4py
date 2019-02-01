# coding:utf-8
# ue4 asset functions

import unreal


def build_import_task(filename, dest_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', dest_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    return task


def do_import_tasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            unreal.log_warning('Imported: %s'%path)


def main():
    # testing
    import os
    _dir = 'D:/download/'
    _textures = ['T_Snow_N.psd', 'Cliffs0464_7_seamless_S.jpg']
    
    tasks = []
    for tex in _textures:
        task = build_import_task(os.path.join(_dir, tex), '/Game/Textures')
        tasks.append(task)

    do_import_tasks(tasks)

