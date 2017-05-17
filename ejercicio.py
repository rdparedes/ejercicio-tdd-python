
class Ejercicio():

  def obtener_divisores(self, numero):
    return [n for n in range(1, numero) if (numero % n == 0)]

  def es_perfecto(self, numero):
    divisores = self.obtener_divisores(numero)
    return (numero == sum(divisores))

  def es_abundante(self, numero):
    divisores = self.obtener_divisores(numero)
    return (numero < sum(divisores))

  def es_deficiente(self, numero):
    divisores = self.obtener_divisores(numero)
    return (numero > sum(divisores))

  def es_primo(self, numero):
    divisores = [n for n in range(1, numero + 1) if (numero % n == 0)]
    return (len(divisores) == 2)

  def obtener_perfectos(self, lista_numeros):
    try:
      return [n for n in lista_numeros if self.es_perfecto(n)]
    except TypeError:
      return []

  # def obtener_divisores(self, numero):
    # contador=1
    # divisores=[]
    # while (contador < numero):
    #   if(numero % contador == 0):
    #     divisores.append(contador)
    #   contador+=1
    # return divisores
