import re
from .validator import Validator

# BASED ON
# https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf


class CpfValidator(Validator):
    @classmethod
    def validate(self, cpf: str) -> bool:
        # Validaate format
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Get cpf numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Validade length
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validade first digit
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validade second digit
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True
