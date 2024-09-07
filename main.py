import pubchempy as pcp
from resourcemanage import Resource_Manager

# a somewhat unnecessary wrapper for pubchem.py
# CAS numbers fall in the 'name' category on pubchem, so they are searched as names
# you could also search by the common name or any other synonym, however CAS numbers
# should return more consistent results
rm = Resource_Manager()


def get_compound(CAS):
    compound_list = pcp.get_compounds(CAS, "name")
    # TODO throw error if list size is greater than 1
    compound = compound_list[0]
    return compound
