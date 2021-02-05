# coding:utf-8

import unreal as u

editor_level_lib = u.EditorLevelLibrary()
editor_filter_lib = u.EditorFilterLibrary()

actors = editor_level_lib.get_all_level_actors()
static_meshes = editor_filter_lib.by_class(actors, u.StaticMeshActor)

deleted = 0

for actor in static_meshes:
    actor_name = actor.get_fname()

    static_mesh_component = actor.static_mesh_component
    static_mesh = static_mesh_component.static_mesh
    is_valid_actor = static_mesh is not None

    if not is_valid_actor:
        actor.destroy_actor()
        deleted += 1
        u.log_warning('The Mesh Component of Actor {} is invalid and was deleted'.format(actor_name))

u.log('Deleted {} Actors with invalid Mesh Component'.format(deleted))
