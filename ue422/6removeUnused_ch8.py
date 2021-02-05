# coding:utf-8

import os
import unreal as u

editor_util = u.EditorUtilityLibrary()
editor_asset_lib = u.EditorAssetLibrary()

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
removed = 0

instant_delete = True
to_be_deleted = []
trash_folder = os.path.join(os.sep, 'Game', 'Unused')

for asset in selected_assets:
    # u.log('asset: {}'.format(asset))
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

    references = editor_asset_lib.find_package_referencers_for_asset(asset_path)
    if not references:
        to_be_deleted.append(asset)

for asset in to_be_deleted:
    asset_name = asset.get_fname()

    if instant_delete:
        deleted = editor_asset_lib.delete_loaded_asset(asset)

        if not deleted:
            u.log_warning('Asset {} could not be deleted'.format(asset_name))
            continue

        removed += 1
    # move the assets to the trash folder
    else:
        new_path = os.path.join(trash_folder, asset_name)
        moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

        if not moved:
            u.log_warning('Asset {} could not be moved to Trash'.format(asset_name))
            continue

        removed += 1

output_test = 'removed' if instant_delete else 'moved to Trash folder'
u.log('{} of {} to be {}, of {} seleted'.format(removed, len(to_be_deleted), output_test, num_assets))


