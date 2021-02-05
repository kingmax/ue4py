# coding:utf-8

import unreal as u

editor_level_lib = u.EditorLevelLibrary()
editor_level_util = u.EditorLevelUtils()
editor_filter_lib = u.EditorFilterLibrary()

actors = editor_level_lib.get_all_level_actors()

static_meshes = editor_filter_lib.by_class(actors, u.StaticMeshActor)
reflection_caps = editor_filter_lib.by_class(actors, u.ReflectionCapture)
blueprints = editor_filter_lib.by_id_name(actors, "BP_")
lights = editor_filter_lib.by_class(actors, u.Light)

moved = 0

mapping =  {
    'SM': static_meshes,
    'RefCap': reflection_caps,
    'BP': blueprints,
    'Light': lights
}

for folder_name in mapping:
    for actor in mapping[folder_name]:
        actor_name = actor.get_fname()
        actor.set_folder_path(folder_name)

        u.log('Move {} into {}'.format(actor_name, folder_name))
        moved += 1

u.log('Moved {} actors into respective folders'.format(moved))

