# coding:utf-8

import os
import time
import unreal as u

editor_util = u.EditorUtilityLibrary()
editor_asset_lib = u.EditorAssetLibrary()

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
num_copies = 500

total_copies = num_copies * num_assets
running = True

start_time = time.time()

text_label = 'Duplicate Asset'
with u.ScopedSlowTask(total_copies, text_label) as slow_task:
    slow_task.make_dialog(True)

    for asset in selected_assets:
        asset_name = asset.get_fname()
        asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
        source_path = os.path.dirname(asset_path)

        for i in range(num_copies):
            if slow_task.should_cancel():
                running = False
                break

            new_name = '%s_%s'%(asset_name, i)
            # print(new_name)
            u.log(new_name)
            dest_path = os.path.join(source_path, new_name)
            duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)
            # update progress
            slow_task.enter_progress_frame(1)

            if not duplicate:
                u.log_error('Duplicate from {} at {} already exists'.format(source_path, dest_path))

        if not running:
            break

        end_time = time.time()
        u.log('{} asset(s) duplicated {} times in {} seconds'.format(num_assets, num_copies, end_time-start_time))
