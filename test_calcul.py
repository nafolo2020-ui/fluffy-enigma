import pytest

from calcul import appliquer_remise


def test_remise_simple():
    assert appliquer_remise(100, 20) == 80.0


def test_sans_remise():
    assert appliquer_remise(59.90, 0) == 59.9


def test_pourcentage_invalide():
    with pytest.raises(ValueError):
        appliquer_remise(100, 150)