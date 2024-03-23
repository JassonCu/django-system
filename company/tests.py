from django.test import TestCase
from .tools.validate_dpi import validate_dpi

class ValidateDpiTestCase(TestCase):
    def test_validate_dpi(self):
        self.assertTrue(validate_dpi("1234567890123"))  # DPI válido
        self.assertFalse(validate_dpi("123456789012"))  # DPI inválido (falta un dígito)
        self.assertFalse(validate_dpi("abcdefghi123"))  # DPI inválido (contiene caracteres no numéricos)
        self.assertFalse(validate_dpi("1234567890128"))  # DPI inválido (dígito de verificación incorrecto)
