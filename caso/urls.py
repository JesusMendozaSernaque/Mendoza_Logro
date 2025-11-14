from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluarPromocionAPIView, EvaluarAPIView 
from .views import CoreScaleViewSet, Caso4ViewSet
from .views import ReglaViewSet
from .views import RangosViewSet 

router = DefaultRouter()
router.register(r'escalas', CoreScaleViewSet, basename='escalas')
router.register(r'caso4', Caso4ViewSet, basename='caso4')
router.register(r'rangos', RangosViewSet, basename='rangos') 
router.register(r'reglas', ReglaViewSet, basename='reglas')


urlpatterns = [
    path('evaluar/', EvaluarAPIView.as_view(), name='evaluar'),
    path('evaluar-promocion/', EvaluarPromocionAPIView.as_view(), name='evaluar_promocion'),
    path('', include(router.urls)),
]
