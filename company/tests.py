from django.test import TestCase
from .tools.validate_dpi import validate_dpi
from .tools.validate_nit import validate_nit


class ValidateDpiTestCase(TestCase):
    def test_validate_dpi(self):
        self.assertTrue(validate_dpi("1234567890123"))  # DPI válido
        # DPI inválido (falta un dígito)
        self.assertFalse(validate_dpi("123456789012"))
        # DPI inválido (contiene caracteres no numéricos)
        self.assertFalse(validate_dpi("abcdefghi123"))
        # DPI inválido (dígito de verificación incorrecto)
        self.assertFalse(validate_dpi("1234567890128"))


class NitValidationTestCase(TestCase):
    def test_valid_nit(self):
        # Test valid NITs
        self.assertTrue(validate_nit("3602978-5"))
        self.assertTrue(validate_nit("576937-K"))

    def test_invalid_nit(self):
        # Test invalid NITs
        self.assertFalse(validate_nit("3602978-6"))
        self.assertFalse(validate_nit("12345678-9"))
        self.assertFalse(validate_nit("12345678-K"))
        self.assertFalse(validate_nit("invalid-nit"))

    def test_edge_cases(self):
        # Test edge cases
        self.assertTrue(validate_nit("12345678-K"))
        self.assertTrue(validate_nit("12345678-k"))
        self.assertFalse(validate_nit("12345678-0"))
