# coding:utf-8

import unreal as u

editor_util = u.EditorUtilityLibrary()
editor_filter_lib = u.EditorFilterLibrary()
# layer_sys = u.LayersSubsystem()  # 4.26 ?
editor_level_lib = u.EditorLevelLibrary()

selected_assets = editor_util.get_selected_assets()
materials = editor_filter_lib.by_class(selected_assets, u.Material)

if not materials:
    u.log_warning('Please select the to be assigned material')
else:
    material = materials[0]
    material_name = material.get_fname()

    # actors = layer_sys.get_selected_actors()
    actors = editor_level_lib.get_selected_level_actors()
    sm_actors = editor_filter_lib.by_class(actors, u.StaticMeshActor)
    if sm_actors:
        for sm_actor in sm_actors:
            sm_name = sm_actor.get_fname()
            print(sm_name)

            component = sm_actor.static_mesh_component
            component.set_material(0, material)

            u.log('Assigning material {} to actor {}'.format(material_name, sm_name))
