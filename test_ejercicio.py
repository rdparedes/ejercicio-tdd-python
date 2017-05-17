import unittest
from ejercicio import Ejercicio

class TestEjercicio(unittest.TestCase):

  def setUp(self):
    self.subject = Ejercicio()

  def test_deberia_retornar_divisores(self):
    resultado_esperado_6 = [1, 2, 3]
    resultado_esperado_10 = [1, 2, 5]
    self.assertEqual(resultado_esperado_6, self.subject.obtener_divisores(6))
    self.assertEqual(resultado_esperado_10, self.subject.obtener_divisores(10))

  def test_deberia_retornar_verdadero_si_el_numero_es_perfecto(self):
    self.assertTrue(self.subject.es_perfecto(6))

  def test_deberia_retornar_falso_si_el_numero_no_es_perfecto(self):
    self.assertFalse(self.subject.es_perfecto(7))

  def test_deberia_retornar_solo_numeros_perfectos(self):
    resultado_esperado = [6]
    self.assertEqual(resultado_esperado, self.subject.obtener_perfectos([1, 6, 78, 344]))

  def test_deberia_retornar_vacio_si_el_tipo_no_es_correcto(self):
    self.assertEquals([],self.subject.obtener_perfectos("perfectos"))

  def test_deberia_retornar_verdadero_si_el_numero_es_abundante(self):
    self.assertTrue(self.subject.es_abundante(12))

  def test_deberia_retornar_falso_si_el_numero_no_es_abundante(self):
    self.assertFalse(self.subject.es_abundante(6))

  def test_deberia_retornar_verdadero_si_el_numero_es_deficiente(self):
    self.assertTrue(self.subject.es_deficiente(16))

  def test_deberia_retornar_falso_si_el_numero_no_es_deficiente(self):
    self.assertFalse(self.subject.es_deficiente(6))

  def test_deberia_retornar_verdadero_si_el_numero_es_primo(self):
    self.assertTrue(self.subject.es_primo(5))
    self.assertTrue(self.subject.es_primo(89))

  def test_deberia_retornar_falso_si_el_numero_no_es_primo(self):
    self.assertFalse(self.subject.es_primo(1))
    self.assertFalse(self.subject.es_primo(96))

if __name__ == '__main__':
  unittest.main()