import unreal

# unreal.EditorAssetLibrary
# https://api.unrealengine.com/INT/PythonAPI/class/EditorAssetLibrary.html
# unreal.EditorLevelLibrary
# https://api.unrealengine.com/INT/PythonAPI/class/EditorLevelLibrary.html
def spawActors():
    _class = unreal.EditorAssetLibrary.load_blueprint_class('Game/BpActor')
    location = unreal.Vector(0, 0, 0)
    rotation = unreal.Rotator(0, 0, 0)
    unreal.EditorLevelLibrary.spawn_actor_from_class(_class, location, rotation)

# unreal.GameplayStatics
# https://api.unrealengine.com/INT/PythonAPI/class/GameplayStatics.html
def deferredSpawnActor():
    world = unreal.EditorLevelLibrary.get_editor_world()
    _class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/BpActor')
    location = unreal.Vector(0, 0, 0)
    rotation = unreal.Rotator(0, 0, 0)
    scale = unreal.Vector(1, 1, 1)
    transform = unreal.Transform(location, rotation, scale)
    # begin spawn
    actor = unreal.GameplayStatics.begin_spawning_actor_from_class(world, _class, transform)
    # edit tags
    tags = actor.get_editor_property('tags')
    tags.append('My Python Tag')
    actor.set_editor_property('tags', tags)
    # complete spawn
    unreal.GameplayStatics.finish_spawning_actor(actor, transform)