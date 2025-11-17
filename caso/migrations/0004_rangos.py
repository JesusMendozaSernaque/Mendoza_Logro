

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caso', '0003_reglas'),
    ]
    

    operations = [
        migrations.CreateModel(
            name='Rangos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('BONIFICACION', 'Bonificación'), ('DESCUENTO', 'Descuento'), ('COMBINADA', 'Combinada')], max_length=20)),
                ('canal_cliente', models.CharField(max_length=50)),
                ('producto_objetivo', models.CharField(max_length=50)),
                ('monto_minimo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monto_maximo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cantidad_minima', models.IntegerField(blank=True, null=True)),
                ('cantidad_maxima', models.IntegerField(blank=True, null=True)),
                ('descuento_porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bonificacion_producto', models.CharField(blank=True, max_length=50, null=True)),
                ('bonificacion_cantidad', models.IntegerField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
    ]
