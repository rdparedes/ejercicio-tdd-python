import unittest
from ejercicio import Ejercicio

class TestEjercicio(unittest.TestCase):

  def test_deberia_retornar_divisores(self):
    subject = Ejercicio()
    resultado_esperado_6 = [1, 2, 3]
    resultado_esperado_10 = [1, 2, 5]
    self.assertEqual(resultado_esperado_6, subject.obtener_divisores(6))
    self.assertEqual(resultado_esperado_10, subject.obtener_divisores(10))

  def test_should_fail(self):
    print("Slin rompió el build")
    self.assertEqual(1, 2)

if __name__ == '__main__':
  unittest.main()
