import pubchempy as pcp
from resourcemanage import Resource_Manager
import json

# a somewhat unnecessary wrapper for pubchem.py
# CAS numbers fall in the 'name' category on pubchem, so they are searched as names
# you could also search by the common name or any other synonym, however CAS numbers
# should return more consistent results
rm = Resource_Manager()


def get_compound(CAS):
    compound_list = pcp.get_compounds(CAS, "name")
    # TODO throw error if list size is greater than 1
    if len(compound_list) > 1:
        raise ValueError(
            "Multiple compounds with this name have been found, please input a more specific name or CAS number"
        )
    compound = compound_list[0]
    return compound


def fill_in(id):
    body = rm.get_item(id)
    compound = get_compound(body["title"])
    CAS = body["title"]
    # TODO I'd like a more reliable way to get CAS than relying on human input
    if (
        "Autofilled" in body["tags"]
        or id <= 300
        or body["category_title"] not in ["Polymer", "Chemical Compound"]
    ):
        return

    metadata = json.loads(body["metadata"])
    metadata["extra_fields"]["SMILES"]["value"] = compound.isomeric_smiles
    metadata["extra_fields"]["Full name"]["value"] = compound.iupac_name
    metadata["extra_fields"]["CAS"]["value"] = CAS

    body = {
        "title": compound.synonyms[0],
        "body": "",
        "rating": 5,
        "tags": ["Autofilled"],
        "metadata": json.dumps(metadata),
    }
    rm.change_item(id, body)
