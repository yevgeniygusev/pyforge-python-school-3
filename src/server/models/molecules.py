from pydantic import BaseModel


class IdCounter:
    latest_id = 0

    @classmethod
    def assign_id(cls) -> int:
        cls.latest_id += 1
        return cls.latest_id


class Molecule(BaseModel):
    id: int | None = None
    smiles: str | None = None
    name: str | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = IdCounter.assign_id()


class Storage:
    def __init__(self):
        self.molecules: dict[int, Molecule] = dict()

    def add_molecule(self, mol: Molecule):
        self.molecules[mol.id] = mol

    def get_all_molecules(self) -> list[Molecule]:
        return list(self.molecules.values())

    def get_mol_by_id(self, mol_id: int) -> Molecule:
        return self.molecules[mol_id]
