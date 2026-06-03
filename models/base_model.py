#!/usr/bin/python3
"""Defines the BaseModel class for all AirBnB clone models.

Every model in this project (User, Place, State, City, Amenity, Review)
will inherit from BaseModel. That way, they all share the same id,
timestamps, and serialization behavior without us rewriting it six times.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Parent class for all models.

    Handles three core responsibilities:
      1. Giving every object a unique id and timestamps.
      2. Converting itself to/from a dictionary (for JSON storage).
      3. Registering itself with the storage engine when created.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        There are TWO ways this gets called:

        (a) Fresh creation — someone typed `create BaseModel` in the
            console. No kwargs are passed, so we generate a new id,
            set timestamps, and tell storage about ourselves.

        (b) Reload from JSON — the storage engine is rebuilding objects
            from file.json on startup. kwargs contains all the saved
            attributes, so we just set them on the instance. We do NOT
            re-register with storage because the object is already
            tracked.

        *args is in the signature but unused — the project spec says
        to ignore positional args. We only care about named ones.
        """
        if kwargs:
            # Case (b): rebuilding from a saved dictionary.
            for key, value in kwargs.items():
                # __class__ is metadata for storage, not a real attribute.
                # Skip it so we don't end up with self.__class__ = "BaseModel".
                if key == "__class__":
                    continue
                # Timestamps were saved as ISO strings — convert back to
                # datetime objects so we can do math on them later.
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # Case (a): brand new object.
            # uuid4() gives us a random, globally-unique id. We convert
            # to str because JSON can't serialize UUID objects directly.
            self.id = str(uuid4())
            # Both timestamps start equal — they'll diverge once save()
            # is called and updated_at gets refreshed.
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Tell the storage engine "hey, track this new object".
            # Import is inside the method to avoid circular imports:
            # storage imports BaseModel, BaseModel imports storage. If
            # we did it at the top of the file, Python would error out.
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return the official string format: [ClassName] (id) {dict}.

        This is what gets printed by the console's `show` command, and
        it's the format the grader expects. type(self).__name__ gives
        us the actual subclass name (e.g. "User", not "BaseModel") when
        called on a subclass instance.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """Mark this object as updated and persist all objects to disk.

        Two things happen here:
          1. Refresh updated_at so we have a record of the change.
          2. Tell storage to write everything to file.json.

        Note: storage.save() writes ALL tracked objects, not just this
        one. That's fine — it keeps the storage layer simple.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return a JSON-serializable dictionary of this instance.

        JSON can't handle datetime objects directly, so we convert
        timestamps to ISO-format strings. We also add a __class__ key
        so that when we reload from file, we know which class to
        rebuild (BaseModel? User? Place?).

        We copy __dict__ instead of returning it directly — otherwise
        modifying the returned dict would mutate the actual object,
        which is a sneaky bug we don't want.
        """
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result