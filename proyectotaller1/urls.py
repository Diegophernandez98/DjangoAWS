from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('planes_telefonia', views.planes_telefonia, name="planes_telefonia"),
    path('planes_internet/', views.planes_internet, name='planes_internet'),
    path('planes_television/', views.planes_television, name='planes_television'),
    path('planes_internet_cliente/', views.planes_internet_cliente, name='planes_internet_cliente'),
    path('planes_television_cliente/', views.planes_television_cliente, name='planes_television_cliente'),
    path('planes_telefonia_cliente/', views.planes_telefonia_cliente, name='planes_telefonia_cliente'),
    path('resumen_plan_internet/<int:plan_id>/', views.resumen_plan_internet, name='resumen_plan_internet'),
    path('resumen_plan_television/<int:plan_id>/', views.resumen_plan_television, name='resumen_plan_television'),
    path('resumen_plan_telefonia/<int:plan_id>/', views.resumen_plan_telefonia, name='resumen_plan_telefonia'),
    path('planS/', views.planS, name="planS"),
    path('planM/', views.planM, name="planM"),
    path('planL/', views.planM, name="planL"),
    path('planXL/', views.planM, name="planXL"),
    path('registro/', views.registro, name="registro"),
    path('inicioSesion/', views.login_view, name="login"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('confirmar_suscripcion/', views.confirmar_suscripcion, name='confirmar_suscripcion'),
    path('cliente_dashboard/', views.cliente_dashboard, name='cliente_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('editar_perfil/<int:id>/', views.editar_perfil, name="editar_perfil"),
    path('enviar_comentario/', views.enviar_comentario, name="enviar_comentario"),
    path('agregarUsuarios/', views.formUsuario, name="formUsuario"),
    path('agregarPlanInternet/', views.formPlanInternet, name="formPlanInternet"),
    path('agregarPlanTelevision/', views.formPlanTelevision, name="formPlanTelevision"),
    path('agregarPlanTelefonia/', views.formPlanTelefonia, name="formPlanTelefonia"),
    path('listaUsuarios/', views.listaUsuarios, name='listaUsuarios'),
    path('listaPlanesInternet/', views.listaPlanesInternet, name='listaPlanesInternet'),
    path('listaPlanesTelevision/', views.listaPlanesTelevision, name='listaPlanesTelevision'),
    path('listaPlanesTelefonia/', views.listaPlanesTelefonia, name='listaPlanesTelefonia'),
    path('editar_plan_telefonia/<int:id>', views.editar_plan_telefonia, name='editar_plan_telefonia'),
    path('editar_plan_television/<int:id>', views.editar_plan_television, name='editar_plan_television'),
    path('editar_plan_internet/<int:id>', views.editar_plan_internet, name='editar_plan_internet'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('eliminarUsuario/<int:id>', views.eliminarUsuario, name='eliminarUsuario'),
    path('eliminarPlanInternet/<int:id>', views.eliminarPlanInternet, name='eliminarPlanInternet'),
    path('eliminarPlanTelevision/<int:id>', views.eliminarPlanTelevision, name='eliminarPlanTelevision'),
    path('eliminarPlanTelefonia/<int:id>', views.eliminarPlanTelefonia, name='eliminarPlanTelefonia'),
    path('formUsuario/', views.formUsuario, name='formUsuario'),
    path('formPlanTelefonia/', views.formPlanTelefonia, name='formPlanTelefonia'),
    path('formPlanTelevision/', views.formPlanTelevision, name='formPlanTelevision'),
    path('formPlanInternet/', views.formPlanInternet, name='formPlanInternet'),
]