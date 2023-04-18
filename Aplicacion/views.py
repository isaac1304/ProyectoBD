from django.db import connection
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseServerError
import cx_Oracle

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

#Vistas Reporte

def reporte(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_devoluciones')
        datos = cursor.fetchall()

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Agregar título al documento
    elements.append(Paragraph('Vista de las devoluciones con información del cliente, el producto y la factura', getSampleStyleSheet()['Heading1']))

    # Agregar tabla con estilos Bootstrap
    headings = ['Fecha', 'Cliente', 'Producto', 'Factura', 'Monto']
    data = [headings] + [tuple(dato[1:]) for dato in datos]
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#212529'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), 'white'),
        ('TEXTCOLOR', (0, 1), (-1, -1), 'black'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, '#dee2e6'),
    ]))
    elements.append(t)

    # Agregar un espacio en blanco antes del final del documento
    elements.append(Paragraph('<br/><br/><br/><br/>', getSampleStyleSheet()['Normal']))

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response


def reporte_ventasxmes(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VENTAS_MENSUALES_COLABORADOR')
        datos = cursor.fetchall()

    # Generar el reporte con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Agregar título al documento
    elements.append(Paragraph('Reporte de ventas de colaboradores mensuales', getSampleStyleSheet()['Heading1']))

    # Agregar encabezados de columna
    headings = ('Nombre colaborador', 'Mes', 'Cantidad ventas')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#7f7f7f'),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (1, 1, 1)),
        ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ])
    table.setStyle(style)
    elements.append(table)

    # Agregar un espacio en blanco antes del final del documento
    elements.append(Paragraph('<br/><br/><br/><br/>', getSampleStyleSheet()['Normal']))

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_diasmasventas(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM DIA_MAX_VENTAS')
        datos = cursor.fetchall()

    # Generar el reporte con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Agregar título al documento
    elements.append(Paragraph('Reporte de dias con mas ventas', getSampleStyleSheet()['Heading1']))

    # Agregar encabezados de columna
    headings = ('Dia', 'Cantidad Ventas')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#7f7f7f'),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (1, 1, 1)),
        ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ])
    table.setStyle(style)
    elements.append(table)

    # Agregar un espacio en blanco antes del final del documento
    elements.append(Paragraph('<br/><br/><br/><br/>', getSampleStyleSheet()['Normal']))

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_ventasxsemana(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VENTAS_SEMANALES_COLABORADOR')
        datos = cursor.fetchall()

    # Generar el reporte con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Agregar título al documento
    elements.append(Paragraph('Reporte de ventas de colaboradores por semana', getSampleStyleSheet()['Heading1']))

    # Agregar encabezados de columna
    headings = ('Nombre Colaborador', 'Nombre producto', 'Cantidad')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#7f7f7f'),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (1, 1, 1)),
        ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ])
    table.setStyle(style)
    elements.append(table)

    # Agregar un espacio en blanco antes del final del documento
    elements.append(Paragraph('<br/><br/><br/><br/>', getSampleStyleSheet()['Normal']))

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_productosmasvendidos(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM PRODUCTOS_MAS_VENDIDOS')
        datos = cursor.fetchall()

    # Generar el reporte con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Agregar título al documento
    elements.append(Paragraph('Reporte de productos mas vendidos', getSampleStyleSheet()['Heading1']))

    # Agregar encabezados de columna
    headings = ('Nombre Producto','Cantidad')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#7f7f7f'),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (1, 1, 1)),
        ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ])
    table.setStyle(style)
    elements.append(table)

    # Agregar un espacio en blanco antes del final del documento
    elements.append(Paragraph('<br/><br/><br/><br/>', getSampleStyleSheet()['Normal']))

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

#Vistas de Login y Registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'inicio/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales invalidas')
    form = UserLoginForm()
    return render(request, 'inicio/login.html', {'form': form})

@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('login')

#Vista perfil
@login_required
def user_profile(request):
    return render(request, 'inicio/perfil.html')

#Vista inicio
def home(request):
    return render(request, "index.html")

#Vistas Cursos
@login_required
def indexCursos(request):
    listaCursos = Curso.objects.all()
    return render(request, "Cursos/gestionCursos.html", {"cursos": listaCursos})

@login_required
def registrarCurso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.create(nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('indexCursos')

@login_required
def ediccionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'Cursos/ediccionCurso.html', {'curso':curso})

@login_required
def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso editado!')
    return redirect('indexCursos')

@login_required
def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso eliminado!')
    return redirect('indexCursos')

#Vistas de Cliente
@login_required
def registrarCliente(request):
    if request.method == 'POST':
        try:
            cedula = request.POST['txtCedula']
            nombre = request.POST['txtNombre']
            apellido1 = request.POST['txtApellido1']
            apellido2 = request.POST['txtApellido2']
            nacimiento = request.POST['txtNacimiento']
            correo = request.POST['txtCorreo']
            telefono = request.POST['txtTelefono']
            direccion = request.POST['txtDireccion']

            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_CLIENTE', [cedula, nombre, apellido1, apellido2, nacimiento, correo, telefono, direccion])
            cursor.close()
            connection.commit()
            connection.close()

            messages.success(request, '¡Cliente registrado!')
            return redirect('indexClientes')
        except IntegrityError:
            messages.error(request, 'Ya existe un cliente con esta cédula')
        except Exception:
            return HttpResponseServerError()

    return render(request, 'Clientes/indexClientes.html')

@login_required
def edicionCliente(request, cedula_cliente):
    cliente = Cliente.objects.get(cedula_cliente=cedula_cliente)
    nacimiento = datetime.strftime(cliente.nacimiento, "%Y-%m-%d")
    return render(request, 'Clientes/edicionCliente.html', {'cliente':cliente, 'nacimiento': nacimiento})

@login_required
def editarCliente(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtApellido1']
    apellido2 = request.POST['txtApellido2']
    nacimiento = request.POST['txtNacimiento']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_CLIENTE', bool, [cedula, nombre, apellido1, apellido2, nacimiento, correo, telefono, direccion])
    cursor.close()

    if resultado:
        messages.success(request, '¡Cliente actualizado!')
    else:
        messages.error(request, 'No se pudo actualizar el cliente')

    return redirect('indexClientes')

@login_required
def eliminarCliente(request, cedula_cliente):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_CLIENTE', [cedula_cliente])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Cliente eliminado!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar el cliente porque tiene registros asociados en otras tablas.')
    return redirect('indexClientes')

@login_required
def indexClientes(request):
    cursor = connection.cursor()
    clientes_cursor = cursor.callfunc('F_LISTAR_CLIENTES', cx_Oracle.CURSOR)

    clientes = []
    for cliente in clientes_cursor:
        clientes.append({
            'cedula_cliente': cliente[0],
            'nombre': cliente[1],
            'apellido_1': cliente[2],
            'apellido_2': cliente[3],
            'nacimiento': cliente[4],
            'correo': cliente[5],
            'telefono': cliente[6],
            'direccion': cliente[7]
        })

    cursor.close()
    connection.close()

    return render(request, 'Clientes/indexClientes.html', {'clientes': clientes})

# Vistas Colaboradores
@login_required
def registrarColaborador(request):
    if request.method == 'POST':
        try:
            cedula = request.POST['txtCedula']
            nombre = request.POST['txtNombre']
            apellido1 = request.POST['txtApellido1']
            apellido2 = request.POST['txtApellido2']
            correo = request.POST['txtCorreo']
            telefono = request.POST['txtTelefono']
            puesto = request.POST['txtPuesto']
            direccion = request.POST['txtDireccion']
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_COLABORADOR', [cedula, nombre, apellido1, apellido2, correo, telefono, puesto, direccion])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Colaborador registrado!')
            return redirect('indexColaboradores')
        except IntegrityError:
            messages.error(request, 'Ya existe un colaborador con esta cédula')
        except Exception:
            return HttpResponseServerError()
    return render(request, 'Colaboradores/indexColaboradores.html')

@login_required
def edicionColaborador(request, id_colaborador):
    colaborador = Colaboradores.objects.get(id_colaborador=id_colaborador)
    return render(request, 'Colaboradores/edicionColaborador.html', {'colaborador':colaborador})

@login_required
def editarColaborador(request):
    id_colaborador = request.POST['id_colaborador']
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtApellido1']
    apellido2 = request.POST['txtApellido2']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    puesto = request.POST['txtPuesto']
    direccion = request.POST['txtDireccion']

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_COLABORADOR', bool, [id_colaborador, cedula, nombre, apellido1, apellido2, correo, telefono, puesto, direccion])
    cursor.close()

    if resultado:
        messages.success(request, '¡Colaborador actualizado!')
    else:
        messages.error(request, 'No se pudo actualizar el colaborador')

    return redirect('indexColaboradores')

@login_required
def eliminarColaborador(request, id_colaborador):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_COLABORADOR', [id_colaborador])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Colaborador eliminado!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar el colaborador porque tiene registros asociados en otras tablas.')
    return redirect('indexColaboradores')

@login_required
def indexColaboradores(request):
    cursor = connection.cursor()
    colaboradores_cursor = cursor.callfunc('F_LISTAR_COLABORADORES', cx_Oracle.CURSOR)
    colaboradores = []
    for colaborador in colaboradores_cursor:
        colaboradores.append({
            'id_colaborador': colaborador[0],
            'cedula_colaborador': colaborador[1],
            'nombre': colaborador[2],
            'apellido_1': colaborador[3],
            'apellido_2': colaborador[4],
            'correo': colaborador[5],
            'telefono': colaborador[6],
            'puesto': colaborador[7],
            'col_direccion': colaborador[8],
        })
    cursor.close()
    connection.close()
    return render(request, 'Colaboradores/indexColaboradores.html', {'colaboradores': colaboradores})

#Vistas Categoria
@login_required
def registrarCategoria(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['txtNombre']
            descripcion = request.POST['txtDescripcion']
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_CATEGORIA', [nombre, descripcion])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Categoría registrada!')
            return redirect('indexCategorias')
        except IntegrityError:
            messages.error(request, 'Ya existe una categoría con este id')
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messages.error(request, f'Error al registrar la categoría: {error.message}')
        except Exception:
            messages.error(request, f'Error en la base de datos: HTTP ERROR 500')
            #return HttpResponseServerError()
    return render(request, 'Categorias/indexCategorias.html')

@login_required
def edicionCategoria(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    return render(request, 'Categorias/edicionCategoria.html', {'categoria':categoria})

@login_required
def editarCategoria(request):
    id_categoria = request.POST['id_categoria']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_CATEGORIA', bool, [id_categoria, nombre, descripcion])
    cursor.close()

    if resultado:
        messages.success(request, '¡Categoría actualizada!')
    else:
        messages.error(request, 'No se pudo actualizar la categoría')

    return redirect('indexCategorias')

@login_required
def eliminarCategoria(request, id_categoria):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_CATEGORIA', [id_categoria])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Categoría eliminada!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar la categoría porque tiene registros asociados en otras tablas.')
    return redirect('indexCategorias')

@login_required
def indexCategorias(request):
    cursor = connection.cursor()
    categorias_cursor = cursor.callfunc('F_LISTAR_CATEGORIAS', cx_Oracle.CURSOR)
    categorias = []
    for categoria in categorias_cursor:
        categorias.append({
            'id_categoria': categoria[0],
            'nombre': categoria[1],
            'descripcion': categoria[2],
        })
    cursor.close()
    connection.close()
    return render(request, 'Categorias/indexCategorias.html', {'categorias': categorias})

#Vistas Productos
@login_required
def indexProductos(request):
    cursor = connection.cursor()
    productos_cursor = cursor.callfunc('F_LISTAR_PRODUCTOS', cx_Oracle.CURSOR)
    categorias_cursor = cursor.callfunc('F_LISTAR_CATEGORIAS', cx_Oracle.CURSOR)
    categorias = []
    for categoria in categorias_cursor:
        categorias.append({
            'id_categoria': categoria[0],
            'nombre': categoria[1],
            'descripcion': categoria[2],
        })
    productos = []
    for producto in productos_cursor:
        productos.append({
            'cod_producto': producto[0],
            'nombre': producto[1],
            'descripcion': producto[2],
            'precio': producto[3],
            'stock': producto[4],
            'pro_id_categoria': producto[5],
            'estado': producto[6],
        })
    cursor.close()
    connection.close()
    return render(request, 'Productos/indexProductos.html', {'productos': productos, 'categorias': categorias})

@login_required
def registrarProducto(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['txtNombre']
            descripcion = request.POST['txtDescripcion']
            precio = request.POST['txtPrecio']
            stock = request.POST['txtStock']
            pro_id_categoria  = request.POST.get('cmbCategoria')
            #pro_id_categoria = request.POST['cmbCategoria']
            estado = request.POST['cmbEstado']
            print(request.POST)
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_PRODUCTO', [nombre, descripcion, precio, stock, pro_id_categoria, estado])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Producto registrado!')
            return redirect('indexProductos')
        except Exception as e:
            print(e)
            messages.error(request, 'No se pudo registrar el producto')
    return render(request, 'Productos/registrarProducto.html')

@login_required
def edicionProducto(request, cod_producto):
    producto = Productos.objects.get(cod_producto=cod_producto)
    producto.precio = str(producto.precio).replace(',', '.')
    cursor = connection.cursor()
    categorias_cursor = cursor.callfunc('F_LISTAR_CATEGORIAS', cx_Oracle.CURSOR)
    categorias = []
    for categoria in categorias_cursor:
        categorias.append({
            'id_categoria': categoria[0],
            'nombre': categoria[1],
            'descripcion': categoria[2],
        })
    return render(request, 'Productos/edicionProducto.html', {'producto': producto, 'categorias': categorias})

@login_required
def editarProducto(request):
    cod_producto = request.POST['cod_producto']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['txtStock']
    pro_id_categoria = request.POST['cmbCategoria']
    estado = request.POST['cmbEstado']
    

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_PRODUCTO', bool, [cod_producto, nombre, descripcion, precio, stock, pro_id_categoria, estado])
    cursor.close()
    if resultado:
        messages.success(request, '¡Producto actualizado!')
    else:
        messages.error(request, 'No se pudo actualizar el producto')

    return redirect('indexProductos')

@login_required
def eliminarProducto(request, cod_producto):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_PRODUCTO', [cod_producto])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Producto eliminado!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar el producto porque tiene registros asociados en otras tablas.')
    return redirect('indexProductos')











#Proveedores
def registrarProveedor(request):
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']
    proveedor = Proveedores.objects.create(nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)
    messages.success(request, '¡Proveedor registrado!')
    return redirect('indexProveedores')

def edicionProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request, 'Proveedores/edicionProveedor.html', {'proveedor':proveedor})

def editarProveedor(request):
    id_proveedor = request.POST['id_proveedor']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.correo = correo
    proveedor.telefono = telefono
    proveedor.direccion = direccion
    proveedor.save()

    messages.success(request, '¡Proveedor editado!')
    return redirect('indexProveedores')

def eliminarProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('indexProveedores')

def indexProveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'Proveedores/indexProveedores.html', {'proveedores':proveedores})

#Sucursales
def registrarSucursal(request):
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    sucursal = Sucursales.objects.create(nombre=nombre, telefono=telefono, direccion=direccion)

    messages.success(request, '¡Sucursal registrada!')
    return redirect('indexSucursales')

def edicionSucursal(request, id_sucursal):
    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request, 'Sucursales/edicionSucursal.html', {'sucursal':sucursal})

def editarSucursal(request):
    id_sucursal = request.POST['txtIdSucursal']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre = nombre
    sucursal.telefono = telefono
    sucursal.direccion = direccion
    sucursal.save()

    messages.success(request, '¡Sucursal editada!')
    return redirect('indexSucursales')

def eliminarSucursal(request, id_sucursal):
    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()

    messages.success(request, '¡Sucursal eliminada!')
    return redirect('indexSucursales')

def indexSucursales(request):
    sucursales = Sucursales.objects.all()
    return render(request, 'Sucursales/indexSucursales.html', {'sucursales':sucursales})

#Facturas
def indexFacturas(request):
    facturas = Facturas.objects.all()
    return render(request, 'Facturas/indexFacturas.html', {'facturas': facturas})

def registrarFactura(request):
    if request.method == 'POST':
        cedula_cliente = request.POST['cedula_cliente']
        codigo_producto = request.POST['codigo_producto']
        id_colaborador = request.POST['id_colaborador']
        fecha = request.POST['fecha']
        total_pagado = request.POST['total_pagado']

        factura = Facturas.objects.create(fac_ced_cliente=cedula_cliente, fac_cod_producto=codigo_producto,
                                        fac_id_colaborador=id_colaborador, fecha=fecha, total_pagado=total_pagado)

        messages.success(request, '¡Factura registrada!')
        return redirect('indexFacturas')
    else:
        return render(request, 'Facturas/registrarFactura.html')

def edicionFactura(request, codigo):
    factura = Facturas.objects.get(cod_factura=codigo)
    return render(request, 'Facturas/edicionFactura.html', {'factura':factura})

def editarFactura(request):
    if request.method == 'POST':
        codigo = request.POST['cod_factura']
        cedula_cliente = request.POST['cedula_cliente']
        codigo_producto = request.POST['codigo_producto']
        id_colaborador = request.POST['id_colaborador']
        fecha = request.POST['fecha']
        total_pagado = request.POST['total_pagado']

        factura = Facturas.objects.get(cod_factura=codigo)
        factura.fac_ced_cliente = cedula_cliente
        factura.fac_cod_producto = codigo_producto
        factura.fac_id_colaborador = id_colaborador
        factura.fecha = fecha
        factura.total_pagado = total_pagado
        factura.save()

        messages.success(request, '¡Factura editada!')
        return redirect('indexFacturas')
    else:
        return render(request, 'Facturas/editarFactura.html')

def eliminarFactura(request, codigo):
    factura = Facturas.objects.get(cod_factura=codigo)
    factura.delete()
    messages.success(request, '¡Factura eliminada!')
    return redirect('indexFacturas')

def indexFacturas(request):
    facturas = Facturas.objects.all()
    return render(request, 'Facturas/indexFacturas.html', {'facturas':facturas})

#Devoluciones
def registrarDevolucion(request):
    fecha = request.POST['fecha']
    dev_ced_cliente_id = request.POST['dev_ced_cliente_id']
    dev_cod_producto_id = request.POST['dev_cod_producto_id']
    dev_cod_factura_id = request.POST['dev_cod_factura_id']
    monto_devolucion = request.POST['monto_devolucion']

    devolucion = Devoluciones.objects.create(
        fecha=fecha,
        dev_ced_cliente_id=dev_ced_cliente_id,
        dev_cod_producto_id=dev_cod_producto_id,
        dev_cod_factura_id=dev_cod_factura_id,
        monto_devolucion=monto_devolucion
    )
    messages.success(request, '¡Devolución registrada!')
    return redirect('indexDevoluciones')

def edicionDevolucion(request, codigo):
    devolucion = Devoluciones.objects.get(id_devolucion=codigo)
    return render(request, 'Devoluciones/edicionDevolucion.html', {'devolucion': devolucion})

def editarDevolucion(request):
    codigo = request.POST['codigo']
    fecha = request.POST['fecha']
    dev_ced_cliente_id = request.POST['dev_ced_cliente_id']
    dev_cod_producto_id = request.POST['dev_cod_producto_id']
    dev_cod_factura_id = request.POST['dev_cod_factura_id']
    monto_devolucion = request.POST['monto_devolucion']

    devolucion = Devoluciones.objects.get(id_devolucion=codigo)
    devolucion.fecha = fecha
    devolucion.dev_ced_cliente_id = dev_ced_cliente_id
    devolucion.dev_cod_producto_id = dev_cod_producto_id
    devolucion.dev_cod_factura_id = dev_cod_factura_id
    devolucion.monto_devolucion = monto_devolucion
    devolucion.save()

    messages.success(request, '¡Devolución editada!')
    return redirect('indexDevoluciones')

def eliminarDevolucion(request, codigo):
    devolucion = Devoluciones.objects.get(id_devolucion=codigo)
    devolucion.delete()
    messages.success(request, '¡Devolución eliminada!')
    return redirect('indexDevoluciones')

def indexDevoluciones(request):
    devoluciones = Devoluciones.objects.all()
    return render(request, 'Devoluciones/indexDevoluciones.html', {'devoluciones':devoluciones})
