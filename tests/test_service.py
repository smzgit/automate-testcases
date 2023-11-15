import pytest

from source.service import get_all_users


def test_get_users():
    data = get_all_users()
    assert len(data) > 0


@pytest.mark.xfail
def test_fail_get_users():
    with pytest.raises(Exception):
        data = get_all_users()


def test_something():
    assert bool([]) == False


def test_raise_exp():
    with pytest.raises(Exception):
        1 + '1'


def test_if_none():
    dummy_d = {1: 'smz',2: 'gmz',3: 'yml', }
    data = dummy_d.get(23)
    assert data is None
