# coding:utf-8

import unreal as u
import os

editor_util = u.EditorUtilityLibrary()
system_lib = u.SystemLibrary()
editor_asset_lib = u.EditorAssetLibrary()

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
cleaned = 0

parent_dir = '/Game'

if  num_assets > 0:
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
    parent_dir = os.path.dirname(asset_path)
    u.log('parent_dir: {}'.format(parent_dir))

for asset in selected_assets:
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    try:
        new_path = os.path.join(parent_dir, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1
        u.log('Cleaned up {} to {}'.format(asset_name, new_path))
    except Exception as ex:
        u.log_warning('Could not move {} to new location {}'.format(asset_name, new_path))

u.log('Cleaned up {} of {} assets'.format(cleaned, num_assets))

