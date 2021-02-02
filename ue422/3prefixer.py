# coding:utf-8

import unreal as u
import json
import os
_cd_ = os.path.dirname(__file__)
print(_cd_)

editor_util = u.EditorUtilityLibrary()
system_lib = u.SystemLibrary()

prefix_mapping = {}
_prefix_mapping_file = os.path.join(_cd_, 'prefix_mapping.json')
print(_prefix_mapping_file)
with open(_prefix_mapping_file, 'r') as fp:
    prefix_mapping = json.load(fp)
    print(prefix_mapping)

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

for asset in selected_assets:
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    print('name:{}, class:{}, className:{}'.format(asset_name, asset_class, class_name))

    class_prefix = prefix_mapping.get(class_name, None)
    if not class_prefix:
        u.log_warning('No mapping for asset {} of type {}'.format(asset_name, class_name))
        continue

    if not asset_name.startswith(class_prefix):
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        u.log('Prefixed {} of type {} with {}'.format(asset_name, class_name, class_prefix))
    else:
        u.log('Asset {} of type {} is already prefixed with {}'.format(asset_name, class_name, class_prefix))

u.log('Prefixed {} of {} assets'.format(prefixed, num_assets))
