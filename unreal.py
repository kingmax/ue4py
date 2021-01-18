import sys

##### Glue Code #####

def log(*args):
    r"""
    x.log(str) -> None -- log the given argument as information in the LogPython category
    """
    pass

def log_warning(*args):
    r"""
    x.log_warning(str) -> None -- log the given argument as a warning in the LogPython category
    """
    pass

def log_error(*args):
    r"""
    x.log_error(str) -> None -- log the given argument as an error in the LogPython category
    """
    pass

def log_flush(*args):
    r"""
    x.log_flush() -> None -- flush the log to disk
    """
    pass

def reload(*args):
    r"""
    x.reload(str) -> None -- reload the given Unreal Python module
    """
    pass

def load_module(*args):
    r"""
    x.load_module(str) -> None -- load the given Unreal module and generate any Python code for its reflected types
    """
    pass

def find_object(*args, **kwargs):
    r"""
    x.find_object(outer, name, type=Object) -> Object -- find an already loaded Unreal object with the given outer and name, optionally validating its type
    """
    pass

def load_object(*args, **kwargs):
    r"""
    x.load_object(outer, name, type=Object) -> Object -- load an Unreal object with the given outer and name, optionally validating its type
    """
    pass

def load_class(*args, **kwargs):
    r"""
    x.load_class(outer, name, type=Object) -> Class -- load an Unreal class with the given outer and name, optionally validating its base type
    """
    pass

def find_asset(*args, **kwargs):
    r"""
    x.find_asset(name, type=Object) -> Object -- find an already loaded Unreal asset with the given name, optionally validating its type
    """
    pass

def load_asset(*args, **kwargs):
    r"""
    x.load_asset(name, type=Object) -> Object -- load an Unreal asset with the given name, optionally validating its type
    """
    pass

def find_package(*args):
    r"""
    x.find_package(name) -> Package -- find an already loaded Unreal package with the given name
    """
    pass

def load_package(*args):
    r"""
    x.load_package(name) -> Package -- load an Unreal package with the given name
    """
    pass

def get_default_object(*args):
    r"""
    x.get_default_object(type) -> Object -- get the Unreal class default object (CDO) of the given type
    """
    pass

def purge_object_references(*args, **kwargs):
    r"""
    x.purge_object_references(obj, include_inners=True) -> None -- purge all references to the given Unreal object from any living Python objects
    """
    pass

def generate_class(*args):
    r"""
    x.generate_class(type) -> None -- generate an Unreal class for the given Python type
    """
    pass

def generate_struct(*args):
    r"""
    x.generate_struct(type) -> None -- generate an Unreal struct for the given Python type
    """
    pass

def generate_enum(*args):
    r"""
    x.generate_enum(type) -> None -- generate an Unreal enum for the given Python type
    """
    pass

def get_type_from_class(*args):
    r"""
    x.get_type_from_class(class) -> type -- get the best matching Python type for the given Unreal class
    """
    pass

def get_type_from_struct(*args):
    r"""
    x.get_type_from_struct(struct) -> type -- get the best matching Python type for the given Unreal struct
    """
    pass

def get_type_from_enum(*args):
    r"""
    x.get_type_from_enum(enum) -> type -- get the best matching Python type for the given Unreal enum
    """
    pass

def NSLOCTEXT(*args):
    r"""
    x.NSLOCTEXT(ns, key, source) -> Text -- create a localized Text from the given namespace, key, and source string
    """
    pass

def LOCTABLE(*args):
    r"""
    x.LOCTABLE(id, key) -> Text -- get a localized Text from the given string table id and key
    """
    pass

class ScopedSlowTask(object):
    r"""
    Type used to create and managed a scoped slow task in Python
    """
    def __init__(self, *args, **kwargs):
        pass
    def __enter__(self, *args):
        r"""
        x.__enter__() -> self -- begin this slow task
        """
        pass
    def __exit__(self, *args, **kwargs):
        r"""
        x.__exit__(type, value, traceback) -> None -- end this slow task
        """
        pass
    def make_dialog_delayed(self, *args, **kwargs):
        r"""
        x.make_dialog_delayed(delay, can_cancel=False, allow_in_pie=False) -> None -- creates a new dialog for this slow task after the given time threshold. If the task completes before this time, no dialog will be shown
        """
        pass
    def make_dialog(self, *args, **kwargs):
        r"""
        x.make_dialog(can_cancel=False, allow_in_pie=False) -> None -- creates a new dialog for this slow task, if there is currently not one open
        """
        pass
    def enter_progress_frame(self, *args, **kwargs):
        r"""
        x.enter_progress_frame(work=1.0, desc=Text()) -> None -- indicate that we are to enter a frame that will take up the specified amount of work (completes any previous frames)
        """
        pass
    def should_cancel(self, *args):
        r"""
        x.should_cancel() -> bool -- True if the user has requested that the slow task be canceled
        """
        pass

class ObjectIterator(object):
    r"""
    Type for iterating Unreal Object instances
    """
    def __init__(self, *args, **kwargs):
        pass

class ClassIterator(object):
    r"""
    Type for iterating Unreal class types
    """
    def __init__(self, *args, **kwargs):
        pass

class StructIterator(object):
    r"""
    Type for iterating Unreal struct types
    """
    def __init__(self, *args, **kwargs):
        pass

class TypeIterator(object):
    r"""
    Type for iterating Python types
    """
    def __init__(self, *args, **kwargs):
        pass

class ValueDef(object):
    r"""
    Type used to define constant values from Python
    """
    def __init__(self, *args, **kwargs):
        pass

class PropertyDef(object):
    r"""
    Type used to define UProperty fields from Python
    """
    def __init__(self, *args, **kwargs):
        pass

class FunctionDef(object):
    r"""
    Type used to define UFunction fields from Python
    """
    def __init__(self, *args, **kwargs):
        pass

class _WrapperBase(object):
    r"""
    Base type for all UE4 exposed types
    """
    def __init__(self, *args, **kwargs):
        pass

class _ObjectBase(_WrapperBase):
    r"""
    Type for all UE4 exposed object instances
    """
    def __init__(self, outer=None, name="None"):
        pass
    def _post_init(self, *args):
        r"""
        x._post_init() -> None -- called during Unreal object initialization (equivalent to PostInitProperties in C++)
        """
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> Object -- cast the given object to this Unreal object type
        """
        pass
    @classmethod
    def get_default_object(cls, *args):
        r"""
        X.get_default_object() -> Object -- get the Unreal class default object (CDO) of this type
        """
        pass
    @classmethod
    def static_class(cls, *args):
        r"""
        X.static_class() -> Class -- get the Unreal class of this type
        """
        pass
    def get_class(self, *args):
        r"""
        x.get_class() -> Class -- get the Unreal class of this instance
        """
        pass
    def get_outer(self, *args):
        r"""
        x.get_outer() -> Object -- get the outer object from this instance (if any)
        """
        pass
    def get_typed_outer(self, *args):
        r"""
        x.get_typed_outer(type) -> type() -- get the first outer object of the given type from this instance (if any)
        """
        pass
    def get_outermost(self, *args):
        r"""
        x.get_outermost() -> Package -- get the outermost object (the package) from this instance
        """
        pass
    def get_name(self, *args):
        r"""
        x.get_name() -> str -- get the name of this instance
        """
        pass
    def get_fname(self, *args):
        r"""
        x.get_fname() -> FName -- get the name of this instance
        """
        pass
    def get_full_name(self, *args):
        r"""
        x.get_full_name() -> str -- get the full name (class name + full path) of this instance
        """
        pass
    def get_path_name(self, *args):
        r"""
        x.get_path_name() -> str -- get the path name of this instance
        """
        pass
    def get_world(self, *args):
        r"""
        x.get_world() -> World -- get the world associated with this instance (if any)
        """
        pass
    def modify(self, *args):
        r"""
        x.modify(bool) -> bool -- inform that this instance is about to be modified (tracks changes for undo/redo if transactional)
        """
        pass
    def rename(self, *args, **kwargs):
        r"""
        x.rename(name=None, outer=None) -> bool -- rename this instance
        """
        pass
    def get_editor_property(self, *args, **kwargs):
        r"""
        x.get_editor_property(name) -> object -- get the value of any property visible to the editor
        """
        pass
    def set_editor_property(self, *args, **kwargs):
        r"""
        x.set_editor_property(name, value) -> None -- set the value of any property visible to the editor, ensuring that the pre/post change notifications are called
        """
        pass

class StructBase(_WrapperBase):
    r"""
    Type for all UE4 exposed struct instances
    """
    def __init__(self, *args, **kwargs):
        pass
    def _post_init(self, *args):
        r"""
        x._post_init() -> None -- called during Unreal struct initialization (equivalent to PostInitProperties in C++)
        """
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> struct -- cast the given object to this Unreal struct type
        """
        pass
    @classmethod
    def static_struct(cls, *args):
        r"""
        X.static_struct() -> Struct -- get the Unreal struct of this type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> struct -- copy this Unreal struct
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> struct -- copy this Unreal struct
        """
        pass
    def assign(self, *args):
        r"""
        x.assign(object) -> None -- assign the value of this Unreal struct to value of the given object
        """
        pass
    def to_tuple(self, *args):
        r"""
        x.to_tuple() -> tuple -- break this Unreal struct into a tuple of its properties
        """
        pass
    def get_editor_property(self, *args, **kwargs):
        r"""
        x.get_editor_property(name) -> object -- get the value of any property visible to the editor
        """
        pass
    def set_editor_property(self, *args, **kwargs):
        r"""
        x.set_editor_property(name, value) -> None -- set the value of any property visible to the editor, ensuring that the pre/post change notifications are called
        """
        pass

class EnumBase(_WrapperBase):
    r"""
    Type for all UE4 exposed enum instances
    """
    def __init__(self):
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> enum -- cast the given object to this Unreal enum type
        """
        pass
    @classmethod
    def static_enum(cls, *args):
        r"""
        X.static_enum() -> Enum -- get the Unreal enum of this type
        """
        pass

class _EnumEntry(object):
    def __init__(self, enum, name, value):
        self.enum = enum
        self.name = name
        self.value = value
    def __get__(self, obj, type=None):
        return self
    def __repr__(self):
        return "{0}.{1}".format(self.enum, self.name)
    @property
    def __name__(self):
        return None
    @__name__.setter
    def __name__(self, value):
        pass
    @property
    def __doc__(self):
        return None
    @__doc__.setter
    def __doc__(self, value):
        pass

class DelegateBase(_WrapperBase):
    r"""
    Type for all UE4 exposed delegate instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> struct -- cast the given object to this Unreal delegate type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> delegate -- copy this Unreal delegate
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> struct -- copy this Unreal delegate
        """
        pass
    def is_bound(self, *args):
        r"""
        x.is_bound() -> bool -- is this Unreal delegate bound to something?
        """
        pass
    def bind_delegate(self, *args):
        r"""
        x.bind_delegate(delegate) -> None -- bind this Unreal delegate to the same object and function as another delegate
        """
        pass
    def bind_function(self, *args):
        r"""
        x.bind_function(obj, name) -> None -- bind this Unreal delegate to a named Unreal function on the given object instance
        """
        pass
    def bind_callable(self, *args):
        r"""
        x.bind_callable(callable) -> None -- bind this Unreal delegate to a Python callable
        """
        pass
    def unbind(self, *args):
        r"""
        x.unbind() -> None -- unbind this Unreal delegate
        """
        pass
    def execute(self, *args):
        r"""
        x.execute(...) -> value -- call this Unreal delegate, but error if it's unbound
        """
        pass
    def execute_if_bound(self, *args):
        r"""
        x.execute_if_bound(...) -> value -- call this Unreal delegate, but only if it's bound to something
        """
        pass

class MulticastDelegateBase(_WrapperBase):
    r"""
    Type for all UE4 exposed multicast delegate instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> struct -- cast the given object to this Unreal delegate type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> struct -- copy this Unreal delegate
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> struct -- copy this Unreal delegate
        """
        pass
    def is_bound(self, *args):
        r"""
        x.is_bound() -> bool -- is this Unreal delegate bound to something?
        """
        pass
    def add_function(self, *args):
        r"""
        x.add_function(obj, name) -> None -- add a binding to a named Unreal function on the given object instance to the invocation list of this Unreal delegate
        """
        pass
    def add_callable(self, *args):
        r"""
        x.add_callable(callable) -> None -- add a binding to a Python callable to the invocation list of this Unreal delegate
        """
        pass
    def add_function_unique(self, *args):
        r"""
        x.add_function_unique(obj, name) -> None -- add a unique binding to a named Unreal function on the given object instance to the invocation list of this Unreal delegate
        """
        pass
    def add_callable_unique(self, *args):
        r"""
        x.add_callable_unique(callable) -> None -- add a unique binding to a Python callable to the invocation list of this Unreal delegate
        """
        pass
    def remove_function(self, *args):
        r"""
        x.remove_function(obj, name) -> None -- remove a binding to a named Unreal function on the given object instance from the invocation list of this Unreal delegate
        """
        pass
    def remove_callable(self, *args):
        r"""
        x.remove_callable(callable) -> None -- remove a binding to a Python callable from the invocation list of this Unreal delegate
        """
        pass
    def remove_object(self, *args):
        r"""
        x.remove_object(obj) -> None -- remove all bindings for the given object instance from the invocation list of this Unreal delegate
        """
        pass
    def contains_function(self, *args):
        r"""
        x.contains_function(obj, name) -> bool -- does the invocation list of this Unreal delegate contain a binding to a named Unreal function on the given object instance
        """
        pass
    def contains_callable(self, *args):
        r"""
        x.contains_callable(callable) -> bool -- does the invocation list of this Unreal delegate contain a binding to a Python callable
        """
        pass
    def clear(self, *args):
        r"""
        x.clear() -> None -- clear the invocation list of this Unreal delegate
        """
        pass
    def broadcast(self, *args):
        r"""
        x.broadcast(...) -> None -- invoke this Unreal multicast delegate
        """
        pass

class Name(_WrapperBase):
    r"""
    Type for all UE4 exposed name instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> Name -- cast the given object to this Unreal name type
        """
        pass
    def is_valid(self, *args):
        r"""
        x.is_valid() -> bool -- is this Unreal name valid?
        """
        pass
    def is_none(self, *args):
        r"""
        x.is_none() -> bool -- is this Unreal name set to NAME_None?
        """
        pass

class Text(_WrapperBase):
    r"""
    Type for all UE4 exposed text instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args):
        r"""
        X.cast(object) -> Text -- cast the given object to this Unreal text type
        """
        pass
    @classmethod
    def as_number(cls, *args):
        r"""
        X.as_number(num) -> Text -- convert the given number to a culture correct Unreal text representation
        """
        pass
    @classmethod
    def as_percent(cls, *args):
        r"""
        X.as_percent(num) -> Text -- convert the given number to a culture correct Unreal text percentgage representation
        """
        pass
    @classmethod
    def as_currency(cls, *args):
        r"""
        X.as_currency(val, code) -> Text -- convert the given number (specified in the smallest unit for the given currency) to a culture correct Unreal text currency representation
        """
        pass
    def is_empty(self, *args):
        r"""
        x.is_empty() -> bool -- is this Unreal text empty?
        """
        pass
    def is_empty_or_whitespace(self, *args):
        r"""
        x.is_empty_or_whitespace() -> bool -- is this Unreal text empty or only whitespace?
        """
        pass
    def is_transient(self, *args):
        r"""
        x.is_transient() -> bool -- is this Unreal text transient?
        """
        pass
    def is_culture_invariant(self, *args):
        r"""
        x.is_culture_invariant() -> bool -- is this Unreal text culture invariant?
        """
        pass
    def is_from_string_table(self, *args):
        r"""
        x.is_from_string_table() -> bool -- is this Unreal text referencing a string table entry?
        """
        pass
    def to_lower(self, *args):
        r"""
        x.to_lower() -> Text -- convert this Unreal text to lowercase in a culture correct way
        """
        pass
    def to_upper(self, *args):
        r"""
        x.to_upper() -> Text -- convert this Unreal text to uppercase in a culture correct way
        """
        pass
    def format(self, *args, **kwargs):
        r"""
        x.format(...) -> Text -- use this Unreal text as a format pattern and generate a new text using the format arguments (may be a mapping, sequence, or set of (optionally named) arguments)
        """
        pass

class Array(_WrapperBase):
    r"""
    Type for all UE4 exposed array instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args, **kwargs):
        r"""
        X.cast(type, obj) -> Array -- cast the given object to this Unreal array type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> Array -- copy this Unreal array
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> Array -- copy this Unreal array
        """
        pass
    def append(self, *args):
        r"""
        x.append(value) -> None -- append the given value to the end of this Unreal array (equivalent to TArray::Add in C++)
        """
        pass
    def count(self, *args):
        r"""
        x.count(value) -> integer -- return the number of times that value appears in this this Unreal array
        """
        pass
    def extend(self, *args):
        r"""
        x.extend(iterable) -> None -- extend this Unreal array by appending elements from the given iterable (equivalent to TArray::Append in C++)
        """
        pass
    def index(self, *args, **kwargs):
        r"""
        x.index(value, start=0, stop=len) -> integer -- get the index of the first matching value in this Unreal array, or raise ValueError if missing (equivalent to TArray::IndexOfByKey in C++)
        """
        pass
    def insert(self, *args, **kwargs):
        r"""
        x.insert(index, value) -> None -- insert the given value at the given index in this Unreal array
        """
        pass
    def pop(self, *args):
        r"""
        x.pop(index=len-1) -> value -- remove and return the value at the given index in this Unreal array, or raise IndexError if the index is out-of-bounds
        """
        pass
    def remove(self, *args):
        r"""
        x.remove(value) -> None -- remove the first matching value in this Unreal array, or raise ValueError if missing
        """
        pass
    def reverse(self, *args):
        r"""
        x.reverse() -> None -- reverse this Unreal array in-place
        """
        pass
    def sort(self, *args, **kwargs):
        r"""
        x.sort(cmp=None, key=None, reverse=False) -> None -- stable sort this Unreal array in-place
        """
        pass
    def resize(self, *args):
        r"""
        x.resize(len) -> None -- resize this Unreal array to hold the given number of elements
        """
        pass

class FixedArray(_WrapperBase):
    r"""
    Type for all UE4 exposed fixed-array instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args, **kwargs):
        r"""
        X.cast(type, obj) -> FixedArray -- cast the given object to this Unreal fixed-array type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> FixedArray -- copy this Unreal fixed-array
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> FixedArray -- copy this Unreal fixed-array
        """
        pass

class Set(_WrapperBase):
    r"""
    Type for all UE4 exposed set instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args, **kwargs):
        r"""
        X.cast(type, obj) -> Set -- cast the given object to this Unreal set type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> Set -- copy this Unreal set
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> Set -- copy this Unreal set
        """
        pass
    def add(self, *args):
        r"""
        x.add(value) -> None -- add the given value to this Unreal set if not already present
        """
        pass
    def discard(self, *args):
        r"""
        x.discard(value) -> None -- remove the given value from this Unreal set, or do nothing if not present
        """
        pass
    def remove(self, *args):
        r"""
        x.remove(value) -> None -- remove the given value from this Unreal set, or raise KeyError if not present
        """
        pass
    def pop(self, *args):
        r"""
        x.pop() -> value -- remove and return an arbitrary value from this Unreal set, or raise KeyError if the set is empty
        """
        pass
    def clear(self, *args):
        r"""
        x.clear() -> None -- remove all values from this Unreal set
        """
        pass
    def difference(self, *args):
        r"""
        x.difference(...) -> Set -- return the difference between this Unreal set and the other iterables passed for comparison (ie, all values that are in this set but not the others)
        """
        pass
    def difference_update(self, *args):
        r"""
        x.difference_update(...) -> None -- make this set the difference between this Unreal set and the other iterables passed for comparison (ie, all values that are in this set but not the others)
        """
        pass
    def intersection(self, *args):
        r"""
        x.intersection(...) -> Set -- return the intersection between this Unreal set and the other iterables passed for comparison (ie, values that are common to all of the sets)
        """
        pass
    def intersection_update(self, *args):
        r"""
        x.intersection_update(...) -> None -- make this set the intersection between this Unreal set and the other iterables passed for comparison (ie, values that are common to all of the sets)
        """
        pass
    def symmetric_difference(self, *args):
        r"""
        x.symmetric_difference(other) -> Set -- return the symmetric difference between this Unreal set and another (ie, values that are in exactly one of the sets)
        """
        pass
    def symmetric_difference_update(self, *args):
        r"""
        x.symmetric_difference_update(other) -> None -- make this set the symmetric difference between this Unreal set and another (ie, values that are in exactly one of the sets)
        """
        pass
    def union(self, *args):
        r"""
        x.union(...) -> Set -- return the union between this Unreal set and the other iterables passed for comparison (ie, values that are in any set)
        """
        pass
    def update(self, *args):
        r"""
        x.update(...) -> None -- make this set the union between this Unreal set and the other iterables passed for comparison (ie, values that are in any set)
        """
        pass
    def isdisjoint(self, *args):
        r"""
        x.isdisjoint(other) -> bool -- return True if there is a null intersection between this Unreal set and another
        """
        pass
    def issubset(self, *args):
        r"""
        x.issubset(other) -> bool -- return True if another set contains this Unreal set
        """
        pass
    def issuperset(self, *args):
        r"""
        x.issuperset(other) -> bool -- return True if this Unreal set contains another
        """
        pass

class Map(_WrapperBase):
    r"""
    Type for all UE4 exposed map instances
    """
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def cast(cls, *args, **kwargs):
        r"""
        X.cast(key, value, obj) -> Map -- cast the given object to this Unreal map type
        """
        pass
    def __copy__(self, *args):
        r"""
        x.__copy__() -> Map -- copy this Unreal map
        """
        pass
    def copy(self, *args):
        r"""
        x.copy() -> Map -- copy this Unreal map
        """
        pass
    def clear(self, *args):
        r"""
        x.clear() -> None -- remove all items from this Unreal map
        """
        pass
    @classmethod
    def fromkeys(cls, *args, **kwargs):
        r"""
        X.fromkeys(sequence, value=None) -> Map -- returns a new Unreal map of keys from the sequence using the given value (types are inferred)
        """
        pass
    def get(self, *args, **kwargs):
        r"""
        x.get(key, default=None) -> value -- x[key] if key in x, otherwise default
        """
        pass
    def setdefault(self, *args, **kwargs):
        r"""
        x.setdefault(key, default=None) -> value -- set key to default if key not in x and return the new value of key
        """
        pass
    def pop(self, *args, **kwargs):
        r"""
        x.pop(key, default=None) -> value -- remove key and return its value, or default if key not present, or raise KeyError if no default
        """
        pass
    def popitem(self, *args):
        r"""
        x.popitem() -> pair -- remove and return an arbitrary pair from this Unreal map, or raise KeyError if the map is empty
        """
        pass
    def update(self, *args, **kwargs):
        r"""
        x.update(...) -> None -- update this Unreal map from the given mapping or sequence pairs type or key->value arguments
        """
        pass
    def has_key(self, *args):
        r"""
        x.has_key(k) -> bool -- does this Unreal map contain the given key? (equivalent to k in x)
        """
        pass
    def iteritems(self, *args):
        r"""
        x.iteritems() -> iter -- an iterator over the key->value pairs of this Unreal map
        """
        pass
    def iterkeys(self, *args):
        r"""
        x.iterkeys() -> iter -- an iterator over the keys of this Unreal map
        """
        pass
    def itervalues(self, *args):
        r"""
        x.itervalues() -> iter -- an iterator over the values of this Unreal map
        """
        pass
    def items(self, *args):
        r"""
        x.items() -> iter -- a Python list containing the key->value pairs of this Unreal map
        """
        pass
    def keys(self, *args):
        r"""
        x.keys() -> iter -- a Python list containing the keys of this Unreal map
        """
        pass
    def values(self, *args):
        r"""
        x.values() -> iter -- a Python list containing the values of this Unreal map
        """
        pass
    def viewitems(self, *args):
        r"""
        x.viewitems() -> view -- a set-like view of the key->value pairs of this Unreal map
        """
        pass
    def viewkeys(self, *args):
        r"""
        x.viewkeys() -> view -- a set-like view of the keys of this Unreal map
        """
        pass
    def viewvalues(self, *args):
        r"""
        x.viewvalues() -> view -- a view of the values of this Unreal map
        """
        pass

def register_slate_pre_tick_callback(*args):
    r"""
    x.register_slate_pre_tick_callback(callable) -> _DelegateHandle -- register the given callable (taking a single float) as a pre-tick callback in Slate
    """
    pass

def unregister_slate_pre_tick_callback(*args):
    r"""
    x.unregister_slate_pre_tick_callback(handle) -> None -- unregister the given handle from a previous call to register_slate_pre_tick_callback
    """
    pass

def register_slate_post_tick_callback(*args):
    r"""
    x.register_slate_post_tick_callback(callable) -> _DelegateHandle -- register the given callable (taking a single float) as a pre-tick callback in Slate
    """
    pass

def unregister_slate_post_tick_callback(*args):
    r"""
    x.unregister_slate_post_tick_callback(handle) -> None -- unregister the given handle from a previous call to register_slate_post_tick_callback
    """
    pass

def parent_external_window_to_slate(*args):
    r"""
    x.parent_external_window_to_slate(external_window, parent_search_method=SlateParentWindowSearchMethod.ACTIVE_WINDOW) -> None -- parent the given OS specific external window handle to a suitable Slate window
    """
    pass

class ActorIterator(object):
    r"""
    Type for iterating Unreal actor instances
    """
    def __init__(self, *args, **kwargs):
        pass

class SelectedActorIterator(object):
    r"""
    Type for iterating selected Unreal actor instances
    """
    def __init__(self, *args, **kwargs):
        pass

class ScopedEditorTransaction(object):
    r"""
    Type used to create and managed a scoped editor transaction in Python
    """
    def __init__(self, *args, **kwargs):
        pass
    def __enter__(self, *args):
        r"""
        x.__enter__() -> self -- begin this transaction
        """
        pass
    def __exit__(self, *args, **kwargs):
        r"""
        x.__exit__(type, value, traceback) -> None -- end this transaction
        """
        pass
    def cancel(self, *args):
        r"""
        x.cancel() -> None -- cancel this transaction
        """
        pass

##### Additional Code #####


class _Logger(object):
    def __init__(self, log_func, flush_func):
        self.encoding = "utf-8"
        self.log_func = log_func
        self.flush_func = flush_func
    def write(self, log_text):
        self.log_func(log_text)
    def writelines(self, lines):
        for line in lines:
            self.write(line)
    def flush(self):
        self.flush_func()

sys.stdout = _Logger(log, log_flush)
sys.stderr = _Logger(log_error, log_flush)

def uclass():
    '''decorator used to define UClass types from Python'''
    def _uclass(type):
        generate_class(type)
        return type
    return _uclass
    
def ustruct():
    '''decorator used to define UStruct types from Python'''
    def _ustruct(type):
        generate_struct(type)
        return type
    return _ustruct
    
def uenum():
    '''decorator used to define UEnum types from Python'''
    def _uenum(type):
        generate_enum(type)
        return type
    return _uenum

def uvalue(val, meta=None):
    '''function used to define constant values from Python'''
    return ValueDef(val, meta)
    
def uproperty(type, meta=None, getter=None, setter=None):
    '''function used to define UProperty fields from Python'''
    return PropertyDef(type, meta, getter, setter)

def ufunction(meta=None, ret=None, params=None, override=None, static=None, pure=None, getter=None, setter=None):
    '''decorator used to define UFunction fields from Python'''
    def _ufunction(func):
        return FunctionDef(func, meta, ret, params, override, static, pure, getter, setter)
    return _ufunction
    

