# coding:utf-8
# 或许可以开发一个贴图的属性传递工具（或者所有UAsset的）

import unreal as u

editor_asset_lib = u.EditorAssetLibrary()
string_lib = u.StringLibrary()
editor_filter_lib = u.EditorFilterLibrary()

# get all assets in CB
root = '/Game/'
include_subfolders = True

set_textures = 0

assets = editor_asset_lib.list_assets(root, recursive=include_subfolders)
color_patterns = ["_ORM", "_OcclusionRoughnessMetallic", "_Metallic", "_Roughness", "_Mask"]
num_assets = len(assets)
print('get {} assets'.format(num_assets))

for asset in assets:
    for pattern in color_patterns:
        if string_lib.contains(asset, pattern):
            asset_obj = editor_asset_lib.load_asset(asset)
            asset_obj.set_editor_property('sRGB', False)
            asset_obj.set_editor_property('CompressionSettings', u.TextureCompressionSettings.TC_MASKS)

            u.log('Setting TC_Masks and turning off sRGB for asset {}'.format(asset))
            set_textures += 1
            break

u.log('Linear color for matching textures set for {} assets'.format(set_textures))


# u.Texture2D object
textures = []
for asset in assets:
    # print(asset)
    # print(type(asset))
    asset_obj = editor_asset_lib.load_asset(asset)
    print('[{}]\t{}'.format(type(asset_obj), asset_obj.get_fname()))
    if type(asset_obj) is u.Texture2D:
        textures.append(asset_obj)

print('get {} textures'.format(len(textures)))
for p in dir(textures[0]):
    print(p)

for texture in textures:
    # sRGB = texture.get_editor_property('sRGB')
    sRGB = texture.srgb
    print(sRGB)

# import struct
#
#
# def encode_binary(sentence):
#     length = len(sentence) + 1
#     return struct.pack('I' + str(length) + 's', length, sentence)
