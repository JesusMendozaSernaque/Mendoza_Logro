

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caso', '0002_promocion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reglas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal_cliente', models.CharField(choices=[('MAYORISTA', 'Mayorista'), ('COBERTURA', 'Cobertura'), ('MERCADO', 'Mercado'), ('INSTITUCIONAL', 'Institucional')], max_length=20)),
                ('producto_objetivo', models.CharField(blank=True, help_text='Código del producto objetivo, opcional para promociones por monto', max_length=50, null=True)),
                ('tipo', models.CharField(choices=[('BONIFICACION', 'Bonificación'), ('DESCUENTO', 'Descuento'), ('COMBINADA', 'Combinada')], max_length=12)),
                ('cantidad_minima', models.PositiveIntegerField(blank=True, null=True)),
                ('cantidad_maxima', models.PositiveIntegerField(blank=True, null=True)),
                ('monto_minimo', models.FloatField(blank=True, null=True)),
                ('monto_maximo', models.FloatField(blank=True, null=True)),
                ('bonificacion_producto', models.CharField(blank=True, max_length=50, null=True)),
                ('bonificacion_cantidad', models.PositiveIntegerField(blank=True, null=True)),
                ('descuento_porcentaje', models.DecimalField(blank=True, decimal_places=2, help_text='Porcentaje de descuento, ej. 15.00 para 15%', max_digits=5, null=True)),
            ],
        ),
    ]
