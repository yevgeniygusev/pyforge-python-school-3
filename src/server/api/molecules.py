from fastapi import FastAPI, APIRouter, HTTPException
from contextlib import asynccontextmanager
from src.server.models.molecules import Molecule, Storage
from src.server.utils import substructure_search

router = APIRouter(prefix='/molecules')

mol_storage = Storage()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global mol_storage
    mol_storage.add_molecule(Molecule(name='aspirin', smiles='CC(=O)Oc1ccccc1C(=O)O'))
    mol_storage.add_molecule(Molecule(name='test', smiles='CC(=O)O'))
    yield

    del mol_storage


@router.get("/")
def get_all_molecules():
    return mol_storage.get_all_molecules()


@router.get("/{mol_id}")
def get_molecule(mol_id: int):
    if mol_id not in mol_storage.molecules.keys():
        raise HTTPException(status_code=404, detail=f"Molecule with id {mol_id} not found")
    return mol_storage.get_mol_by_id(mol_id)


@router.get("/search/{smiles}")
def search_molecule(smiles: str):
    return substructure_search(mol_storage, smiles)


@router.post("/")
def add_molecule(molecule: Molecule):
    mol_storage.add_molecule(molecule)
    return molecule
