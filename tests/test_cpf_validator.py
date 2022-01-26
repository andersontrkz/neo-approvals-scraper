import pytest
from src.validators.cpf_validator import CpfValidator


@pytest.mark.parametrize('cpf, expected', [
    ('012.347.586-44', True),
    ('012.354.768-71', True),
    ('876.520.413-17', True),
    ('876.541.230-35', True),
    ('876.543.012-35', True),
    ('178.422.117-11', False),
    ('000.000.046-71', False),
    ('111.111.111-11', False),
    ('999.999.999-99', False),
    ('012.347.586-49', False),
])
def test_cpf_validator(cpf, expected):
    assert CpfValidator.validate(cpf) == expected
