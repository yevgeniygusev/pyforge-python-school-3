from pytest_unordered import unordered
from fastapi.testclient import TestClient
from src.server.models.molecules import Molecule, Storage


def test__get_root(api_client: TestClient):
    response = api_client.get('/')
    assert response.status_code == 200


def test__get_molecules(api_client: TestClient):
    response = api_client.get('/molecules')
    assert response.status_code == 200
    assert response.json() == unordered(
        [
            {'id': 1, 'name': 'aspirin', 'smiles': 'CC(=O)Oc1ccccc1C(=O)O'},
            {'id': 2, 'name': 'test', 'smiles': 'CC(=O)O'},
        ]
    )


def test__get_molecule_by_id(api_client: TestClient):
    response = api_client.get('/molecules/2')
    assert response.status_code == 200
    assert response.json() == {'id': 2, 'name': 'test', 'smiles': 'CC(=O)O'}


def test__search_molecule_by_smiles(api_client: TestClient):
    response = api_client.get('/molecules/search/c1ccccc1')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'aspirin', 'smiles': 'CC(=O)Oc1ccccc1C(=O)O'}]


def test__add_molecule(api_client: TestClient, mol_storage_db: Storage):
    response = api_client.post('/molecules', json={'name': 'test_mol', 'smiles': 'CC(=O)Oc1ccccc1C(=O)O'})
    assert response.status_code == 200
    assert response.json() == {'id': 3, 'name': 'test_mol', 'smiles': 'CC(=O)Oc1ccccc1C(=O)O'}

    assert len(mol_storage_db.get_all_molecules()) == 3

    new_mol: Molecule = mol_storage_db.get_mol_by_id(3)
    assert new_mol.id == 3
    assert new_mol.name == 'test_mol'
    assert new_mol.smiles == 'CC(=O)Oc1ccccc1C(=O)O'
