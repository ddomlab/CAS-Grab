from backend.resourcemanage import Resource_Manager
import printer.generate_label

rm = Resource_Manager()
lg = printer.generate_label.LabelGenerator()

for item in rm.get_items(size=100):
    id = item.to_dict()["id"]
    filenames = []
    for file in rm.get_uploaded_files(id):
        filenames.append(file.to_dict()["real_name"])
        if file.to_dict()["real_name"] == "labels.pdf":
            rm.delete_upload(id, file.id)
    if "label.pdf" not in filenames:
        lg.add_item(id)
        lg.write_labels()
        rm.upload_file(id, lg.path)
