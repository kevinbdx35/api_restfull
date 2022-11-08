import pytest

from src.api.models.users import User
from src.api.repositories.generic_repository import GenericRepository
from src.api.utils.database import db


def test_save(start):
    user = User('Quiroule', 'Pierre', 'pierre@nasa.gov', '123456')
    repot = GenericRepository()
    repot.save(user)
    assert isinstance(user.uid, int)


def test_find_all(start):
    user = User('Banner', 'Bruce', 'hulk@avengers.fr', 'green')
    repot = GenericRepository()
    repot.find_all(User)
    assert user.last_name == 'Banner'
    assert user.first_name == 'Bruce'
    assert user.email == 'hulk@avengers.fr'
    assert user.password == 'green'


def test_find_by_id(start):
    user = User('America', 'Captain', 'captain@avengers.fr', 'usa')
    repot = GenericRepository()
    user.uid = repot.find_by_id(User, key_id=2)
    assert user.uid is not None


def test_find_by_email(start):
    user = User('Man', 'Iron', 'iron@avengers.fr', 'azerty')
    repot = GenericRepository()
    repot.find_by_email(User, email='iron@avengers.fr')
    assert user.email == 'iron@avengers.fr'
