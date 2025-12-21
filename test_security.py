import unittest
from security import validar_password  # Encara no existeix

class TestSecurity(unittest.TestCase):
    def test_password_curta(self):
        self.assertFalse(validar_password("abc"))  # Massa curta

    def test_password_llarga(self):
        self.assertTrue(validar_password("contrasenya_llarga"))

if __name__ == "__main__":
    unittest.main()
