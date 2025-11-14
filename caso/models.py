from django.db import models # type: ignore

#Caso 1, 2, 3 y 4
class Caso4(models.Model):
    Caso_TYPES = [
        ('BONUS_VOLUME', 'Bonificación por volumen'),
        ('BONUS_AMOUNT', 'Bonificación por monto'),
        ('DISCOUNT_VOLUME', 'Descuento por volumen'),
    ]
    CUSTOMER_CHANNELS = [
        ('MAYORISTA', 'Mayorista'),
        ('COBERTURA', 'Cobertura'),
        ('MERCADO', 'Mercado'),
        ('INSTITUCIONAL', 'Institucional'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=Caso_TYPES)
    channel = models.CharField(max_length=20, choices=CUSTOMER_CHANNELS)
    product_code = models.CharField(max_length=50)
    quantity_required = models.PositiveIntegerField(null=True, blank=True)
    amount_required = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bonus_products = models.JSONField(null=True, blank=True)  # [{"code": "VO010B", "qty": 2}]
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_scaled = models.BooleanField(default=False)  # NUEVO: Indica si la regla es escalonada

    def __str__(self):
        return self.name

# NUEVO: Modelo para escalas de descuento por volumen
class CoreScale(models.Model):
    core = models.ForeignKey(Caso4, related_name='scales', on_delete=models.CASCADE)
    min_qty = models.PositiveIntegerField()
    max_qty = models.PositiveIntegerField(null=True, blank=True)  # null = sin límite superior
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        max_label = f"{self.max_qty}" if self.max_qty else "más"
        return f"{self.core.name}: {self.min_qty} - {max_label} => {self.discount_percentage}%"
#Caso 5,6,7 pendiente

class Rangos(models.Model):
    TIPO_CHOICES = [
    ('BONIFICACION', 'Bonificación'),
    ('DESCUENTO', 'Descuento'),
    ('COMBINADA', 'Combinada'),
]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    canal_cliente = models.CharField(max_length=50)
    producto_objetivo = models.CharField(max_length=50)
    monto_minimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cantidad_minima = models.IntegerField(null=True, blank=True)
    cantidad_maxima = models.IntegerField(null=True, blank=True)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bonificacion_producto = models.CharField(max_length=50, null=True, blank=True)
    bonificacion_cantidad = models.IntegerField(null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
#Caso 8,9 y 10
class Promocion(models.Model):
    TIPO_CHOICES = [
        ('BONIFICACION', 'Bonificación'),
        ('DESCUENTO', 'Descuento'),
        ('COMBINADA', 'Combinada'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    canal_cliente = models.CharField(max_length=50)
    producto_objetivo = models.CharField(max_length=20)
    monto_minimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cantidad_minima = models.IntegerField(null=True, blank=True)
    cantidad_maxima = models.IntegerField(null=True, blank=True)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bonificacion_producto = models.CharField(max_length=20, null=True, blank=True)
    bonificacion_cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

#Caso 11,12 y 13
class Reglas(models.Model):
    TIPOS_PROMOCION = [
        ('BONIFICACION', 'Bonificación'),
        ('DESCUENTO', 'Descuento'),
        ('COMBINADA', 'Combinada'),
    ]

    CANALES = [
        ('MAYORISTA', 'Mayorista'),
        ('COBERTURA', 'Cobertura'),
        ('MERCADO', 'Mercado'),
        ('INSTITUCIONAL', 'Institucional'),
    ]

    canal_cliente = models.CharField(max_length=20, choices=CANALES)
    producto_objetivo = models.CharField(max_length=50, blank=True, null=True,
                                         help_text="Código del producto objetivo, opcional para promociones por monto")
    tipo = models.CharField(max_length=12, choices=TIPOS_PROMOCION)

    cantidad_minima = models.PositiveIntegerField(blank=True, null=True)
    cantidad_maxima = models.PositiveIntegerField(blank=True, null=True)

    monto_minimo = models.FloatField(blank=True, null=True)
    monto_maximo = models.FloatField(blank=True, null=True)

    # Campos para bonificación
    bonificacion_producto = models.CharField(max_length=50, blank=True, null=True)
    bonificacion_cantidad = models.PositiveIntegerField(blank=True, null=True)

    # Campo para descuento (porcentaje)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                               help_text="Porcentaje de descuento, ej. 15.00 para 15%")

    def __str__(self):
        return f"{self.get_tipo_display()} para {self.canal_cliente} - Producto: {self.producto_objetivo or 'General'}"