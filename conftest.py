import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.server.api.molecules import mol_storage

from src.server.models.molecules import Molecule, Storage

mol_storage.add_molecule(Molecule(name='aspirin', smiles='CC(=O)Oc1ccccc1C(=O)O'))
mol_storage.add_molecule(Molecule(name='test', smiles='CC(=O)O'))


@pytest.fixture(scope='function')
def api_client() -> TestClient:
    return TestClient(app)


@pytest.fixture()
def mol_storage_db() -> Storage:
    return mol_storage
