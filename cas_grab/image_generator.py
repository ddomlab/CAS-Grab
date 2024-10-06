from rdkit import Chem
from rdkit.Chem import Draw


def generate_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    return img
