from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reglas, Rangos
from .models import Caso4, CoreScale, Promocion, Reglas
from .serializers import Caso4Serializer, CoreScaleSerializer, ReglasSerializer
from .serializers import EvaluarPromocionSerializer
from .serializers import RangosSerializer, EvaluarPromocionInputSerializer, PromocionAplicadaSerializer

class Caso4ViewSet(viewsets.ModelViewSet):
    queryset = Caso4.objects.all()
    serializer_class = Caso4Serializer


class CoreScaleViewSet(viewsets.ModelViewSet):
    queryset = CoreScale.objects.all()
    serializer_class = CoreScaleSerializer

class ReglaViewSet(viewsets.ModelViewSet):
    queryset = Reglas.objects.all()
    serializer_class = ReglasSerializer

class RangosViewSet(viewsets.ModelViewSet):
    queryset = Rangos.objects.all()
    serializer_class = RangosSerializer

class EvaluarPromocionAPIView(APIView):
    def post(self, request):
        serializer = EvaluarPromocionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        promociones_aplicadas = []

        for promo in Promocion.objects.filter(canal_cliente=data["canal"]):
            for prod in data["productos"]:
                if promo.producto_objetivo == prod["codigo"]:
                    if promo.cantidad_minima and prod["cantidad"] >= promo.cantidad_minima:
                        if not promo.cantidad_maxima or prod["cantidad"] <= promo.cantidad_maxima:
                            if promo.tipo == 'BONIFICACION':
                                promociones_aplicadas.append({
                                    "tipo": "BONIFICACION",
                                    "producto": promo.bonificacion_producto,
                                    "cantidad": promo.bonificacion_cantidad
                                })
                            elif promo.tipo == 'DESCUENTO':
                                promociones_aplicadas.append({
                                    "tipo": "DESCUENTO",
                                    "porcentaje": float(promo.descuento_porcentaje)
                                })
                            elif promo.tipo == 'COMBINADA':
                                promociones_aplicadas.append({
                                    "tipo": "BONIFICACION",
                                    "producto": promo.bonificacion_producto,
                                    "cantidad": promo.bonificacion_cantidad
                                })
                                promociones_aplicadas.append({
                                    "tipo": "DESCUENTO",
                                    "porcentaje": float(promo.descuento_porcentaje)
                                })

            if promo.monto_minimo and data["monto_total"] >= promo.monto_minimo:
                if not promo.monto_maximo or data["monto_total"] <= promo.monto_maximo:
                    if promo.tipo == 'BONIFICACION':
                        promociones_aplicadas.append({
                            "tipo": "BONIFICACION",
                            "producto": promo.bonificacion_producto,
                            "cantidad": promo.bonificacion_cantidad
                        })
                    elif promo.tipo == 'DESCUENTO':
                        promociones_aplicadas.append({
                            "tipo": "DESCUENTO",
                            "porcentaje": float(promo.descuento_porcentaje)
                        })
                    elif promo.tipo == 'COMBINADA':
                        promociones_aplicadas.append({
                            "tipo": "BONIFICACION",
                            "producto": promo.bonificacion_producto,
                            "cantidad": promo.bonificacion_cantidad
                        })
                        promociones_aplicadas.append({
                            "tipo": "DESCUENTO",
                            "porcentaje": float(promo.descuento_porcentaje)
                        })

        return Response({
            "promociones_aplicadas": promociones_aplicadas
        })


class EvaluarAPIView(APIView):
    def post(self, request):
        serializer = EvaluarPromocionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        promociones_aplicadas = []

        # Caso 11 y 12: Evaluar promociones por canal, producto y cantidad mínima/máxima
        for promo in Reglas.objects.filter(canal_cliente=data["canal"]):
            for prod in data["productos"]:
                if promo.producto_objetivo == prod["codigo"]:
                    # Caso 12: rango cantidad mínima y máxima
                    cantidad = prod["cantidad"]
                    if promo.cantidad_minima and cantidad < promo.cantidad_minima:
                        continue
                    if promo.cantidad_maxima and cantidad > promo.cantidad_maxima:
                        continue
                    
                    # Aplicar según tipo
                    if promo.tipo == 'BONIFICACION':
                        promociones_aplicadas.append({
                            "tipo": "BONIFICACION",
                            "producto": promo.bonificacion_producto,
                            "cantidad": promo.bonificacion_cantidad
                        })
                    elif promo.tipo == 'DESCUENTO':
                        promociones_aplicadas.append({
                            "tipo": "DESCUENTO",
                            "porcentaje": float(promo.descuento_porcentaje)
                        })
                    elif promo.tipo == 'COMBINADA':
                        promociones_aplicadas.append({
                            "tipo": "BONIFICACION",
                            "producto": promo.bonificacion_producto,
                            "cantidad": promo.bonificacion_cantidad
                        })
                        promociones_aplicadas.append({
                            "tipo": "DESCUENTO",
                            "porcentaje": float(promo.descuento_porcentaje)
                        })

        # Caso 13: Evaluar promociones por monto total mínimo y máximo
        for promo in Reglas.objects.filter(canal_cliente=data["canal"]):
            if promo.monto_minimo and data["monto_total"] < promo.monto_minimo:
                continue
            if promo.monto_maximo and data["monto_total"] > promo.monto_maximo:
                continue

            if promo.tipo == 'BONIFICACION':
                promociones_aplicadas.append({
                    "tipo": "BONIFICACION",
                    "producto": promo.bonificacion_producto,
                    "cantidad": promo.bonificacion_cantidad
                })
            elif promo.tipo == 'DESCUENTO':
                promociones_aplicadas.append({
                    "tipo": "DESCUENTO",
                    "porcentaje": float(promo.descuento_porcentaje)
                })
            elif promo.tipo == 'COMBINADA':
                promociones_aplicadas.append({
                    "tipo": "BONIFICACION",
                    "producto": promo.bonificacion_producto,
                    "cantidad": promo.bonificacion_cantidad
                })
                promociones_aplicadas.append({
                    "tipo": "DESCUENTO",
                    "porcentaje": float(promo.descuento_porcentaje)
                })

        return Response({
            "promociones_aplicadas": promociones_aplicadas
        }, status=status.HTTP_200_OK) # type: ignore