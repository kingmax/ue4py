import unreal


def cast(obj, cls):
    # unreal._ObjectBase
    # https://api.unrealengine.com/INT/PythonAPI/class/_ObjectBase.html
    try:
        return cls.cast(obj)
    except:
        return None


def getActors(isSelected=False, aClass=None, tag=None):
    # unreal.EditorLevelLibrary
    # https://api.unrealengine.com/INT/PythonAPI/class/EditorLevelLibrary.html
    # unreal.GameplayStatics
    # https://api.unrealengine.com/INT/PythonAPI/class/GameplayStatics.html
    # unreal.Actors
    # https://api.unrealengine.com/INT/PythonAPI/class/Actor.html
    if isSelected:
        # selected
        actors = unreal.EditorLevelLibrary.get_selected_level_actors()
        # class
        if aClass:
            actors = [a for a in actors if cast(a, aClass)]
        # tag
        if tag:
            actors = [a for a in actors if a.actor_has_tag(tag)]
        return actors

    elif aClass:
        actors = unreal.GameplayStatics.get_all_actors_of_class(unreal.EditorLevelLibrary.get_editor_world(), aClass)
        # tag
        if tag:
            actors = [a for a in actors if a.actor_has_tag(tag)]
        return actors

    elif tag:
        actors = unreal.GameplayStatics.get_all_actors_with_tag(unreal.EditorLevelLibrary.get_editor_world(), tag)
        return actors

    else:
        actors = unreal.GameplayStatics.get_all_actors_of_class(unreal.EditorLevelLibrary.get_editor_world(), unreal.Actor)
        return actors


def spawnActors():
    # unreal.EditorAssetLibrary
    # https://api.unrealengine.com/INT/PythonAPI/class/EditorAssetLibrary.html
    # unreal.EditorLevelLibrary
    # https://api.unrealengine.com/INT/PythonAPI/class/EditorLevelLibrary.html
    _class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/BpActor')
    location = unreal.Vector(0, 0, 0)
    rotation = unreal.Rotator(0, 0, 0)
    unreal.EditorLevelLibrary.spawn_actor_from_class(_class, location, rotation)


def deferredSpawnActor():
    # unreal.GameplayStatics
    # https://api.unrealengine.com/INT/PythonAPI/class/GameplayStatics.html
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


def main():
    # test
    spawnActors()
    deferredSpawnActor()
    deferredSpawnActor()

    def sep():
        print('-'*40)

    # all Actors
    print('all Actors::')
    for a in getActors():
        print(a.get_name())
    sep()

    print('selected Actors::')
    from pprint import pprint
    # selected Actors
    for a in getActors(True):
        pprint(a.get_name())
    sep()

    print('StaticMeshActors::')
    # StaticMeshActor
    for a in getActors(False, unreal.StaticMeshActor):
        pprint(a.get_name())
    sep()

    print('Actors with tag (My Python Tag)::')
    # Actors with tag
    for a in getActors(tag='My Python Tag'):
        pprint(a.get_name())

