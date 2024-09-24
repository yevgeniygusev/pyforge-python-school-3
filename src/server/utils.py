from rdkit import Chem
from src.server.models.molecules import Molecule, Storage


def substructure_search(mol_storage: Storage, mol_search: str) -> list[Molecule | None]:
    # mols = [Chem.MolFromSmiles(mol.smiles) for mol in mols.get_all_molecules()]

    mol_search = Chem.MolFromSmiles(mol_search)
    mol_matches: list[Molecule | None] = [mol for mol in mol_storage.get_all_molecules() if
                                          Chem.MolFromSmiles(mol.smiles).HasSubstructMatch(mol_search)]

    return mol_matches


# matches = substructure_search(["CCO", "c1ccccc1", "CC(=O)O", "CC(=O)Oc1ccccc1C(=O)O"], "c1ccccc1")
# print(matches)
