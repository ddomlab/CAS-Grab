# right now i intend to create a class with a few methods to control
# resources (add/delete/edit) here, if this gets too complicated i may decide to
# split it into seperate files

# this contains mostly code written by Connor found in Python_Scripts.zip in the Onedrive.
# i am mostly writing wrappers and making the code a little more abstract and generally usable

import config


class Resource_Manager:
    def __init__(self):
        self.itemsapi = config.load_items_api()

    def create_item(self, category, body_dict):
        response = self.itemsapi.post_item_with_http_info(
            body={
                "category_id": category,
                "tags": ["API Test", "Example Tag"],
            }  # TODO remove/abstract tags
        )
        locationHeaderInResponse = response[2].get("Location")
        print(f"The newly created item is here: {locationHeaderInResponse}")
        item_id = int(locationHeaderInResponse.split("/").pop())
        self.change_item(item_id, body_dict)

    # TODO  search by long id

    def change_item(self, id, body_dict):
        self.itemsapi.patch_item(id, body=body_dict)

    def get_item(self, id):
        return self.itemsapi.get_item(id).to_dict()

    def get_items(self):
        return self.itemsapi.read_items().to_dict()
