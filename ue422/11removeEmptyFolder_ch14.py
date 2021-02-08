# coding:utf-8

import unreal as u
import os
import sys

editor_asset_lib = u.EditorAssetLibrary()

source_dir = '/Game/'
include_subfolder = True
deleted = 0


# get all assets in source dir
assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolder, include_folder=True)
forders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

for folder in forders:
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:
        editor_asset_lib.delete_directory(folder)
        deleted += 1
        u.log('Folder {} without assets was deleted'.format(folder))

u.log('Deleted {} folders without assets'.format(deleted))
