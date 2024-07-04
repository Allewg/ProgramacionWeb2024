from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='jpg/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return '/static/jpg/producto1.jpg'  # Puedes definir una imagen por defecto o manejar el caso sin imagen

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)

    class Meta:
        db_table = 'categoria'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='categoria_pk')
        ]

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ciudad'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='ciudad_pk')
        ]

class Cliente(models.Model):
    rut_cliente = models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    appaterno_cliente = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_nac = models.DateField()
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cliente'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='cliente_pk')
        ]

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=50)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comuna'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='comuna_pk')
        ]

class Departamento(models.Model):
    nombre_depto = models.CharField(max_length=50)

    class Meta:
        db_table = 'departamento'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='departamento_pk')
        ]

class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    ingrediente = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)
    forma_pago = models.ForeignKey('FormaPago', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detalle_venta'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='detalle_venta_pk')
        ]

class Dificultad(models.Model):
    nombre_dificultad = models.CharField(max_length=50)

    class Meta:
        db_table = 'dificultad'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='dificultad_pk')
        ]

class Empleado(models.Model):
    nombre_emp = models.CharField(max_length=50)
    appaterno_emp = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    sueldo_base = models.IntegerField()
    fecha_ini_contrato = models.DateField()
    fecha_fin_contrato = models.DateField(null=True, blank=True)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleado'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='empleado_pk')
        ]

class FormaPago(models.Model):
    nombre_forma_pago = models.CharField(max_length=50)

    class Meta:
        db_table = 'forma_pago'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='forma_pago_pk')
        ]

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=1000)
    precio = models.IntegerField()
    stock = models.IntegerField()
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingrediente'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='ingrediente_pk')
        ]

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=50)

    class Meta:
        db_table = 'marca'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='marca_pk')
        ]

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=50)

    class Meta:
        db_table = 'pais'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='pais_pk')
        ]

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    class Meta:
        db_table = 'provincia'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='provincia_pk')
        ]

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    minutos_preparacion = models.IntegerField()
    foto_receta = models.BinaryField()
    pasos_preparacion = models.CharField(max_length=1000)
    porciones = models.IntegerField()
    dificultad = models.ForeignKey('Dificultad', on_delete=models.CASCADE)

    class Meta:
        db_table = 'receta'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='receta_pk')
        ]

class Region(models.Model):
    nombre_region = models.CharField(max_length=50)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)

    class Meta:
        db_table = 'region'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='region_pk')
        ]

class Relation8(models.Model):
    ingrediente = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'relation_8'
        constraints = [
            models.UniqueConstraint(fields=['ingrediente', 'categoria'], name='relation_8_pk')
        ]

class Venta(models.Model):
    fecha_venta = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'venta'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='venta_pk')
        ]
