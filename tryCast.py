import unreal


def tryCast():
    if unreal.Texture2D.cast(unreal.load_asset('/Game/Textures/T_Snow_N')):
        print('Texture2D Cast Succeeded')
    else:
        print('Texture2D Cast Failed')

    if unreal.Actor.cast(unreal.load_asset('/Game/Textures/T_Snow_N')):
        print('Actor Cast Succeeded')
    else:
        print('Actor Cast Failed')


def cast(obj, cls):
    try:
        return cls.cast(obj)
    except Exception as ex:
        print(ex.message)


