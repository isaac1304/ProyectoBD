from . import views
from django.urls import path, include

urlpatterns = [
    #Inicio
    path('', views.home, name="index"),
    
    #Rutas Clientes
    path('clientes/', views.indexClientes, name="indexClientes"),
    path('registrarCliente/', views.registrarCliente, name="registrarCliente"),
    path('clientes/edicionCliente/<cedula_cliente>', views.edicionCliente, name="edicionCliente"),
    path('editarCliente/', views.editarCliente, name="editarCliente"),
    path('clientes/eliminarCliente/<cedula_cliente>', views.eliminarCliente, name="eliminarCliente"),
    
    #Rutas Colaboradores
    path('colaboradores/', views.indexColaboradores, name="indexColaboradores"),
    path('registrarColaborador/', views.registrarColaborador, name="registrarColaborador"),
    path('colaboradores/edicionColaborador/<id_colaborador>', views.edicionColaborador, name="edicionColaborador"),
    path('editarColaborador/', views.editarColaborador, name="editarColaborador"),
    path('colaboradores/eliminarColaborador/<id_colaborador>', views.eliminarColaborador, name="eliminarColaborador"),
    
    #Rutas Categoria
    path('categorias/', views.indexCategorias, name="indexCategorias"),
    path('registrarCategoria/', views.registrarCategoria, name="registrarCategoria"),
    path('categorias/edicionCategoria/<id_categoria>', views.edicionCategoria, name="edicionCategoria"),
    path('editarCategoria/', views.editarCategoria, name="editarCategoria"),
    path('categorias/eliminarCategoria/<id_categoria>', views.eliminarCategoria, name="eliminarCategoria"),
    
    #Rutas Productos
    path('productos/', views.indexProductos, name="indexProductos"),
    path('registrarProducto/', views.registrarProducto, name="registrarProducto"),
    path('productos/edicionProducto/<cod_producto>', views.edicionProducto, name="edicionProducto"),
    path('editarProducto/', views.editarProducto, name="editarProducto"),
    path('productos/eliminarProducto/<cod_producto>', views.eliminarProducto, name="eliminarProducto"),
    
    #Rutas Proveedores
    path('proveedores/', views.indexProveedores, name="indexProveedores"),
    path('registrarProveedor/', views.registrarProveedor, name="registrarProveedor"),
    path('proveedores/edicionProveedor/<id_proveedor>', views.edicionProveedor, name="edicionProveedor"),
    path('editarProveedor/', views.editarProveedor, name="editarProveedor"),
    path('proveedores/eliminarProveedor/<id_proveedor>', views.eliminarProveedor, name="eliminarProveedor"),

    #Rutas Sucursales
    path('sucursales/', views.indexSucursales, name="indexSucursales"),
    path('registrarSucursal/', views.registrarSucursal, name="registrarSucursal"),
    path('sucursales/edicionSucursal/<id_sucursal>', views.edicionSucursal, name="edicionSucursal"),
    path('editarSucursal/', views.editarSucursal, name="editarSucursal"),
    path('sucursales/eliminarSucursal/<id_sucursal>', views.eliminarSucursal, name="eliminarSucursal"),

    #Rutas Facturas
    path('facturas/', views.indexFacturas, name="indexFacturas"),
    path('registrarFactura/', views.registrarFactura, name="registrarFactura"),
    path('facturas/eliminarFactura/<codigo>', views.eliminarFactura, name='eliminarFactura'),

    #Rutas Devoluciones
    path('devoluciones/', views.indexDevoluciones, name="indexDevoluciones"),
    path('registrarDevolucion/', views.registrarDevolucion, name="registrarDevolucion"),
    path('devoluciones/eliminarDevolucion/<id_devolucion>', views.eliminarDevolucion, name="eliminarDevolucion"),
    
    #Rutas de login y registro 
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('perfil/', views.user_profile, name='perfil'),
    path('logout/', views.user_logout, name='logout'),
    
    #Ruta reporte
    path('reporte/', views.reporte, name='reporte'),
    path('reporte2/', views.reporte_ventasxmes, name='reporte2'),
    path('reporte3/', views.reporte_diasmasventas, name='reporte3'),
    path('reporte4/', views.reporte_ventasxsemana, name='reporte4'),
    path('reporte5/', views.reporte_productosmasvendidos, name='reporte5'),
    path('reporte6/', views.reporte_ventasTotalesCategoria, name='reporte6'),
    path('reporte7/', views.reporte_productosBajoInventario, name='reporte7'),
    path('reporte8/', views.reporte_clientesCompras, name='reporte8'),

]