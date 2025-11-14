from rest_framework import serializers
from .models import Caso4, CoreScale, Reglas, Rangos

class Caso4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Caso4
        fields = '__all__'

class CoreScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreScale
        fields = '__all__'

class ReglasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglas
        fields = '__all__'

class ProductoSerializer(serializers.Serializer):
    codigo = serializers.CharField()
    cantidad = serializers.IntegerField()

class EvaluarPromocionSerializer(serializers.Serializer):
    canal = serializers.CharField()
    productos = ProductoSerializer(many=True)
    monto_total = serializers.DecimalField(max_digits=10, decimal_places=2)

class ProductoInputSerializer(serializers.Serializer):
    codigo = serializers.CharField()
    cantidad = serializers.IntegerField(min_value=1)

class EvaluarSerializer(serializers.Serializer):
    canal = serializers.CharField()
    productos = ProductoInputSerializer(many=True)
    monto_total = serializers.FloatField(min_value=0)

class RangosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rangos
        fields = '__all__'

class ProductoInputSerializer(serializers.Serializer):
    codigo = serializers.CharField()
    cantidad = serializers.IntegerField()
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)

class EvaluarPromocionInputSerializer(serializers.Serializer):
   canal = serializers.CharField()
   productos = ProductoInputSerializer(many=True)


class PromocionAplicadaSerializer(serializers.Serializer):
    tipo = serializers.CharField()
    promocion = serializers.CharField()
    descuento_porcentaje = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    bonificacion_producto = serializers.CharField(required=False)
    bonificacion_cantidad = serializers.IntegerField(required=False)