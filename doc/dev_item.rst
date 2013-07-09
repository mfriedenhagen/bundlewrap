.. _dev_item:

============================
Creating your own item types
============================

Step 1: Create an item module
-----------------------------

Create a new file called ``/your/blockwart/repo/items/foo.py``. You can use this as a template::

    from blockwart.items import Item, ItemStatus

    class Foo(Item):
        """
        A foo.
        """
        BUNDLE_ATTRIBUTE_NAME = "foo"
        DEPENDS_STATIC = []
        ITEM_ATTRIBUTES = {
            'attribute': "default value",
        }
        ITEM_TYPE_NAME = "foo"

        def ask(self):
        	"""
        	Returns a string asking the user if this item should be
        	implemented.
        	"""
            return ""

        def fix(self):
            """
            ConfigItems override this to do their work.
            """
            raise NotImplementedError

        def get_status(self):
            """
            Returns an ItemStatus instance describing the current status of
            the item on the actual node. Must not be cached.
            """
            return ItemStatus(
                correct=True,
                description="No description available.",
                status_info={},
            )

        def validate_attributes(self, attributes):
            """
            Raises blockwart.exceptions.BundleError if something is amiss with
            the user-specified attributes.
            """
            pass



Step 2: Define attributes
-------------------------

``BUNDLE_ATTRIBUTE_NAME`` is the name of the variable defined in a bundle module that holds the items of this type. If your bundle looks like this::

   foo = { {...] }

...then you should put ``BUNDLE_ATTRIBUTE_NAME = "foo"`` here.


``DEPENDS_STATIC`` is a list of hard-wired dependencies for all intances of your item. For example, all services inherently depend on all packages (because you can't start the service without installing its package first). Most of the time, this will be a wildcard dependency on a whole type of items, not a specific one::

    DEPENDS_STATIC = ["file:/etc/hosts", "user:"]  # depends on /etc/hosts and all users


``ITEM_ATTRIBUTES`` is a dictionary of the attributes users will be able to configure for your item. For files, that would be stuff like owner, group, and permissions. Every attribute (even if it's mandatory) needs a default value, ``None`` is totally acceptable::

    ITEM_ATTRIBUTES = {'attr1': "default1"}

``ITEM_TYPE_NAME`` sets the first part of an items ID. For the file items, this is "file". Therefore, file ID look this this: ``file:/path``. The second part is the name a user assigns to your item in a bundle. Example::

    ITEM_TYPE_NAME = "foo"

Step 3: Implement methods
-------------------------