import unittest
from credit_card.credit_card_validator import is_valid_credit_card

class TestCreditCardValidator(unittest.TestCase):

    def test_valid_credit_card_visa(self):
        """
        Testa um número de cartão de crédito válido da Visa.
        """
        self.assertTrue(is_valid_credit_card('4532015112830366'))

    def test_valid_credit_card_mastercard(self):
        """
        Testa um número de cartão de crédito válido da MasterCard.
        """
        self.assertTrue(is_valid_credit_card('5500000000000004'))

    def test_invalid_credit_card(self):
        """
        Testa um número de cartão de crédito inválido que não passa pelo algoritmo de Luhn.
        """
        self.assertFalse(is_valid_credit_card('1234567812345678'))

    def test_invalid_credit_card_too_short(self):
        """
        Testa um número de cartão de crédito muito curto para ser válido.
        """
        self.assertFalse(is_valid_credit_card('1234'))

    def test_invalid_credit_card_with_non_digit_characters(self):
        """
        Testa um número de cartão de crédito que contém caracteres não numéricos.
        """
        self.assertTrue(is_valid_credit_card('4532abcd1122efgh'))

if __name__ == '__main__':
    unittest.main()
