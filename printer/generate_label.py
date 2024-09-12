from blabel import LabelWriter
from resourcemanage import Resource_Manager
import json


class LabelGenerator:
    def __init__(self):
        self.label_writer = LabelWriter(
            "printer/label.html", default_stylesheets=("printer/style.css",)
        )  # TODO: platform agnostic paths'=
        self.records = []
        self.rm = Resource_Manager()

    # records  = [
    #     dict(sample_id="s01", name="Sample 1"),
    #     dict(sample_id="s02", name="Sample 2")
    # ]

    def add_item(self, id: int):
        item: dict = self.rm.get_item(id)
        metadata: dict = json.loads(item["metadata"])

        room_checked: str = "--"
        loc_checked: str = "--"

        ## handles errors if location or room are left blank
        try:
            room_checked = metadata["extra_fields"]["Room"]["value"]
        except KeyError:
            pass
        try:
            loc_checked = metadata["extra_fields"]["Location"]["value"]
        except KeyError:
            pass

        self.records.append(
            dict(
                id_num=id,
                name=item["title"],
                room=room_checked,
                loc=loc_checked,
                date=item["_date"],
            )
        )

    def write_labels(self):
        self.label_writer.write_labels(self.records, target="qrcode_and_label.pdf")
        self.records = []
