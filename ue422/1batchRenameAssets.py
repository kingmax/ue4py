# coding:utf-8

import unreal as u


def rename_assets(search_pattern, replace_pattern, use_case=False):
    system_lib = u.SystemLibrary()
    editor_util = u.EditorUtilityLibrary()
    string_lib = u.StringLibrary()

    print('{},\n{},\n{}'.format(system_lib, editor_util, string_lib))

    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    u.log('Selected {} asset(s)'.format(num_assets))

    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        print(asset_name)

        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = u.SearchCase.CASE_SENSITIVE if use_case else u.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case)
            editor_util.rename_asset(asset, replaced_name)

            replaced += 1
            u.log('Replaced {} with {}'.format(asset_name, replaced_name))
        else:
            u.log_warning('{} did not match the search pattern, was skipped'.format(asset_name))


if __name__ == '__main__':
    rename_assets('New', 'Old', True)
