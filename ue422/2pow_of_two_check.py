# coding:utf-8

import unreal as u
import math

editor_util = u.EditorUtilityLibrary()

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
not_pow = 0

for asset in selected_assets:
    asset_name = asset.get_fname()
    asset_path = asset.get_path_name()
    u.log(asset_name)

    try:
        x = asset.blueprint_get_size_x()
        y = asset.blueprint_get_size_y()
        print(x, y)

        is_x_valid = math.log(x, 2).is_integer()
        is_y_valid = math.log(y, 2).is_integer()
        if not is_x_valid or not is_y_valid:
            u.log_warning('{} is not power of two ({}, {})'.format(asset_name, x, y))
            u.log("It's path is {}".format(asset_path))
            not_pow += 1
    except Exception as ex:
        u.log_warning('{} is not a Texture - {}'.format(asset_name, ex))

u.log('{} checked, {} textures problematic'.format(num_assets, not_pow))
