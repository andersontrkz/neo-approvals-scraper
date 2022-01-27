import pytest
from src.cleaners.cleaner import Cleaner

# BASED ON *
# https://docs.pytest.org/en/6.2.x/parametrize.html


@pytest.mark.parametrize('name, expected', [
    ('MICHELLE BANKS I', 'MICHELLE BANKS'),
    ('MICHELLE BANKS II', 'MICHELLE BANKS'),
    ('MICHELLE BANKS III', 'MICHELLE BANKS'),
    ('MICHELLE BANKS IV', 'MICHELLE BANKS'),
    ('MICHELLE BANKS V', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Dr.', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Sr.', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Mr.', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Jr.', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Mrs.', 'MICHELLE BANKS'),
    ('MICHELLE BANKS Miss', 'MICHELLE BANKS'),
    ('MICHELLE BANKS MD', 'MICHELLE BANKS'),
    ('MICHELLE BANKS DDS', 'MICHELLE BANKS'),
    ('MICHELLE BANKS DVM', 'MICHELLE BANKS'),
    ('MICHELLE BANKS PhD', 'MICHELLE BANKS')
])
def test_blacklist_cleaning(name, expected):
    assert Cleaner.name_cleaning(name) == expected


@pytest.mark.parametrize('name, expected', [
    ('MICHELLE BANKS ', 'MICHELLE BANKS'),
    (' MICHELLE BANKS', 'MICHELLE BANKS'),
    ('  MICHELLE BANKS', 'MICHELLE BANKS'),
    ('MICHELLE BANKS  ', 'MICHELLE BANKS'),
    ('   MICHELLE BANKS   ', 'MICHELLE BANKS')
])
def test_strip_cleaning(name, expected):
    assert Cleaner.name_cleaning(name) == expected


@pytest.mark.parametrize('name, expected', [
    ('michelle BANKS', 'MICHELLE BANKS'),
    ('MICHELLE banks', 'MICHELLE BANKS'),
    ('MiChElLe BaNkS', 'MICHELLE BANKS'),
    ('mIcHeLlE bAnKs', 'MICHELLE BANKS'),
    ('michelle banks', 'MICHELLE BANKS')
])
def test_case_cleaning(name, expected):
    assert Cleaner.name_cleaning(name) == expected


@pytest.mark.parametrize('name, expected', [
    ('MÍCHELLE ANUGNOR', 'MICHELLE ANUGNOR'),
    ('MICHÉLLE ANUGNOR', 'MICHELLE ANUGNOR'),
    ('MICHELLE ÀNUGNOR', 'MICHELLE ANUGNOR'),
    ('MICHELLE ANUGNÓR', 'MICHELLE ANUGNOR'),
    ('MICHELLE ÃNUGNOR', 'MICHELLE ANUGNOR'),
    ('MICHÊLLE ANUGNOR', 'MICHELLE ANUGNOR'),
    ('MICHELLE ANUGNÖR', 'MICHELLE ANUGNOR'),
    ('MICHELLE ÀNUGNÖR', 'MICHELLE ANUGNOR'),
    ('MÍCHELLÈ ANUGNÖR', 'MICHELLE ANUGNOR'),
    ('MÍCHÈLLE ÃNÙGNÖR', 'MICHELLE ANUGNOR')
])
def test_accents_cleaning(name, expected):
    assert Cleaner.name_cleaning(name) == expected


@pytest.mark.parametrize('cpf, expected', [
    ('098.765.432-11', '09876543211'),
    (' 098.765.432-11', '09876543211'),
    ('098.765.432-11 ', '09876543211'),
    ('  098.765.432-11   ', '09876543211'),
    ('*098.765.432-11', '09876543211')
])
def test_cpf_cleaning(cpf, expected):
    assert Cleaner.cpf_cleaning(cpf) == expected


@pytest.mark.parametrize('name, expected', [
    ('90.70', 90.7),
    ('90.7', 90.7),
    (' 90.70', 90.7),
    ('90.70 ', 90.7),
    ('   90.70  ', 90.7),
    ('84.63', 84.63),
    ('84.63', 84.63),
    (' 84.63', 84.63),
    ('84.63 ', 84.63),
    ('   84.63  ', 84.63)
])
def test_score_cleaning(name, expected):
    assert Cleaner.score_cleaning(name) == expected
