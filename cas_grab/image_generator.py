from rdkit import Chem
from rdkit.Chem import Draw


def generate_image(smiles) -> str:
    mol = Chem.MolFromSmiles(smiles)
    filename = "RDKitImage.png"
    Draw.MolToFile(mol, "tmp/" + filename)
    return filename
