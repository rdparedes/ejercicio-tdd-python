
class Ejercicio():

  def obtener_divisores(self, numero):
    return [n for n in range(1, numero) if (numero % n == 0)]

  # def obtener_divisores(self, numero):
    # contador=1
    # divisores=[]
    # while (contador < numero):
    #   if(numero % contador == 0):
    #     divisores.append(contador)
    #   contador+=1
    # return divisores
