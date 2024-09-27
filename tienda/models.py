from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    imagen = models.URLField(max_length=200)  # Puedes dejarlo por si decides usarlo

    def __str__(self):
        return self.nombre
