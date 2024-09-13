import json


class Processor:
    def __init__(self):
        self.registry: Registry = Registry()

    ### Actions ###
    def open_page():
        raise NotImplementedError

    def archive_item():
        raise NotImplementedError

    def batch_action():
        raise NotImplementedError

    def clear():
        raise NotImplementedError

    def assosciate():
        raise NotImplementedError

    ###   ###
    commands: dict = {
        "open": open_page,
        "archive": archive_item,
        "batch": batch_action,
        "clear": clear,
        "assosciate": assosciate,
    }

    def register(self, input: str):
        if input == "batch":
            self.registry.toggle_batch()
        elif input.isdigit():
            self.registry.add_id(
                int(input)
            )  # add the integer id to the registry, if it isn't in batch mode, it will simply replace the old id in the reigstry with the new one
        elif input in self.commands:
            self.registry.action = input
        else:
            raise ValueError(
                "Input not processed, please check spelling/formatting and try again, or use a QR Code"
            )

    def from_json(self, input: str):
        data = json.loads(input).to_dict()
        for key in data:
            if key in self.commands:
                self.register(key)

    def from_human(input: str):
        raise NotImplementedError


class Registry:
    def __init__(self):
        self.id_registry: list[int] = []
        self.action: str = ""
        self.is_batch: bool = False

    def toggle_batch(self):
        self.is_batch = not self.is_batch  # toggle batch mode
        if not self.is_batch:  # if you just turned off batch mode
            self.id_registry = [
                self.id_registry[-1]
            ]  # make the list have one element, the most recently added

    def add_id(self, id: int):
        self.id_registry.append(id)
        if not self.is_batch:
            self.id_registry = [
                self.id_registry[-1]
            ]  # if batch mode is not on, make sure the list is one long
