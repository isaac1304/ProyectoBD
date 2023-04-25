from django.db import connection
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseServerError
import cx_Oracle
import io
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tempfile
from reportlab.lib.utils import ImageReader


#Vistas Reporte
def reporte(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_devoluciones')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de devoluciones', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Crear tabla con estilos Bootstrap
    headings = ['Fecha', 'Cliente', 'Producto', 'Factura', 'Monto']
    data = [headings] + [tuple(dato[1:]) for dato in datos]

    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)
    """
    # Crear gráfico de barras
    fig, ax = plt.subplots()
    x = [dato[2] for dato in datos]  # Obtener los nombres de los productos
    y = [dato[4] for dato in datos]  # Obtener los montos de las devoluciones
    ax.bar(x, y)
    ax.set_xlabel('Productos')
    ax.set_ylabel('Monto')
    ax.set_title('Devoluciones por producto')

    # Guardar el gráfico en un archivo temporal
    with tempfile.NamedTemporaryFile(suffix='.png') as tmpfile:
        fig.savefig(tmpfile, bbox_inches='tight')
        tmpfile.seek(0)
        image_data = tmpfile.read()

    # Agregar el archivo al documento PD
    image = ImageReader(image_data)
    elements.append(image)
    """
    doc.build(elements)
    return response

def reporte_ventasxmes(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VENTAS_MENSUALES_COLABORADOR')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de ventas de colaboradores mensuales', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Nombre colaborador', 'Mes', 'Cantidad ventas')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)
    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_diasmasventas(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM DIA_MAX_VENTAS')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de ventas de dias con mas ventas', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Dia', 'Cantidad Ventas')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_ventasxsemana(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VENTAS_SEMANALES_COLABORADOR')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de ventas de colaboradores por semana', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Nombre Colaborador', 'Nombre producto', 'Cantidad')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_productosmasvendidos(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM PRODUCTOS_MAS_VENDIDOS')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de ventas de productos mas vendidos', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Nombre Producto','Cantidad')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_ventasTotalesCategoria(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_ventas_categoria')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de ventas totales por categoria', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Categoria','Vental Total')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_productosBajoInventario(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VISTA_PRODUCTOS_BAJO_INVENTARIO')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de productos con bajo inventario', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Cod Producto','Nombre', 'Stock')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

def reporte_clientesCompras(request):
    # Obtener los datos de la vista de devoluciones
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM VISTA_CLIENTES_COMPRAS')
        datos = cursor.fetchall()

    # Obtener fecha y hora de creación
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Crear el documento con ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el documento con ReportLab
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Agregar título al documento
    estilo_titulo = getSampleStyleSheet()['Heading1']
    estilo_titulo.textColor = colors.HexColor("#F04E23")
    elements.append(Paragraph('Reporte de los clientes y sus compras', estilo_titulo))

    # Agregar fecha y hora de creación
    estilo_fecha = ParagraphStyle(name='fecha', fontName='Helvetica', fontSize=12, textColor=colors.HexColor("#707070"), alignment=1)
    elements.append(Paragraph(fecha_creacion, estilo_fecha))

    # Agregar encabezados de columna
    headings = ('Cedula Cliente','Nombre', 'Fecha', 'Producto', 'Total Pagado')
    data = [headings] + [tuple(dato[0:]) for dato in datos]

    # Crear la tabla y definir su estilo
    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#dee2e6")),
    ]))
    elements.append(t)

    # Cerrar el documento y devolver el archivo
    doc.build(elements)
    return response

#Vistas Reporte cliente con más compras
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
    elements.append(Paragraph('Vista de los colaboradores con más ventas en el periodo de tiempo seleccionado', getSampleStyleSheet()['Heading1']))

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
    elements.append(Paragraph('Vista de los colaboradores con más ventas en el periodo de tiempo seleccionado', getSampleStyleSheet()['Heading1']))

    # Agregar encabezados de columna
    headings = ('Nombre Colaborador', 'Mes', 'Cantidad ventas')
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
    elements.append(Paragraph('Vista de los colaboradores con más ventas en el periodo de tiempo seleccionado', getSampleStyleSheet()['Heading1']))

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
    elements.append(Paragraph('Vista de los colaboradores con más ventas en el periodo de tiempo seleccionado', getSampleStyleSheet()['Heading1']))

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

#Vistas Clientes
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
            messages.error(request, f'Error en la base de datos: HTTP ERROR 500')
            #return HttpResponseServerError()
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

#Vistas Categorias
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

@login_required
def indexProductos(request):
    cursor = connection.cursor()
    productos_cursor = cursor.callfunc('F_LISTAR_PRODUCTOS', cx_Oracle.CURSOR)
    categorias_cursor = cursor.callfunc('F_LISTAR_CATEGORIAS', cx_Oracle.CURSOR)
    print()
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

#Vistas Proveedores
@login_required
def registrarProveedor(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['txtNombre']
            correo = request.POST['txtCorreo']
            telefono = request.POST['txtTelefono']
            direccion = request.POST['txtDireccion']

            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_PROVEEDOR', [nombre, correo, telefono, direccion])
            cursor.close()
            connection.commit()
            connection.close()

            messages.success(request, '¡Proveedor registrado!')
            return redirect('indexProveedores')
        except Exception as e:
            messages.error(request, 'No se pudo registrar el proveedor. Error: {}'.format(str(e)))
    return render(request, 'Proveedores/registrarProveedor.html')

@login_required
def edicionProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request, 'Proveedores/edicionProveedor.html', {'proveedor':proveedor})

@login_required
def editarProveedor(request):
    id_proveedor = request.POST['id_proveedor']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_PROVEEDOR', bool, [id_proveedor, nombre, correo, telefono, direccion])
    cursor.close()

    if resultado:
        messages.success(request, '¡Proveedor actualizado!')
    else:
        messages.error(request, 'No se pudo actualizar el proveedor')

    return redirect('indexProveedores')

@login_required
def eliminarProveedor(request, id_proveedor):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_PROVEEDOR', [id_proveedor])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Proveedor eliminado!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar el proveedor porque tiene registros asociados en otras tablas.')
    return redirect('indexProveedores')

@login_required
def indexProveedores(request):
    cursor = connection.cursor()
    proveedores_cursor = cursor.callfunc('F_LISTAR_PROVEEDORES', cx_Oracle.CURSOR)
    print(proveedores_cursor)
    proveedores = []
    for proveedor in proveedores_cursor:
        proveedores.append({
            'id_proveedor': proveedor[0],
            'nombre': proveedor[1],
            'correo': proveedor[2],
            'telefono': proveedor[3],
            'direccion': proveedor[4],
        })
        #print(proveedores)
    cursor.close()
    connection.close()
    return render(request, 'Proveedores/indexProveedores.html', {'proveedores': proveedores})

#Vistas Sucursales
@login_required
def registrarSucursal(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['txtNombre']
            telefono = request.POST['txtTelefono']
            direccion = request.POST['txtDireccion']
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_SUCURSAL', [nombre, telefono, direccion])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Sucursal registrada!')
            return redirect('indexSucursales')
        except IntegrityError:
            messages.error(request, 'Ya existe una sucursal con este id')
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messages.error(request, f'Error al registrar la sucursal: {error.message}')
        except Exception:
            messages.error(request, f'Error en la base de datos: HTTP ERROR 500')
            #return HttpResponseServerError()
    return render(request, 'Sucursales/indexSucursales.html')

@login_required
def edicionSucursal(request, id_sucursal):
    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request, 'Sucursales/edicionSucursal.html', {'sucursal':sucursal})

@login_required
def editarSucursal(request):
    id_sucursal = request.POST['id_sucursal']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_SUCURSAL', bool, [id_sucursal, nombre, telefono, direccion])
    cursor.close()

    if resultado:
        messages.success(request, '¡Sucursal actualizada!')
    else:
        messages.error(request, 'No se pudo actualizar la sucursal')

    return redirect('indexSucursales')

@login_required
def eliminarSucursal(request, id_sucursal):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_SUCURSAL', [id_sucursal])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Sucursal eliminada!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar la sucursal porque tiene registros asociados en otras tablas.')
    return redirect('indexSucursales')

@login_required
def indexSucursales(request):
    cursor = connection.cursor()
    sucursales_cursor = cursor.callfunc('F_LISTAR_SUCURSALES', cx_Oracle.CURSOR)
    sucursales = []
    for sucursal in sucursales_cursor:
        sucursales.append({
            'id_sucursal': sucursal[0],
            'nombre': sucursal[1],
            'telefono': sucursal[2],
            'direccion': sucursal[3],
        })
    cursor.close()
    connection.close()
    return render(request, 'Sucursales/indexSucursales.html', {'sucursales': sucursales})

#Vista Facturas
@login_required
def registrarFactura(request):
    if request.method == 'POST':
        try:
            cedula_cliente = request.POST.get('cedula_cliente')
            codigo_producto = request.POST.get('codigo_producto')
            id_colaborador = request.POST.get('id_colaborador')
            fecha = date.today()
            total_pagado = request.POST.get('total_pagado')
            precio_unitario = request.POST.get('precio_unitario')
            cantidad = request.POST.get('cantidad')
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_FACTURA', [cedula_cliente, codigo_producto, id_colaborador, fecha, total_pagado, precio_unitario, cantidad])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Factura registrada!')
            return redirect('indexFacturas')
        except IntegrityError:
            messages.error(request, 'Ya existe una factura con este código')
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messages.error(request, f'Error al registrar la factura: {error.message}')
        except Exception:
            messages.error(request, f'Error en la base de datos: HTTP ERROR 500')
            #return HttpResponseServerError()
    return render(request, 'Facturas/indexFacturas.html')

"""
@login_required
def edicionFactura(request, codigo):
    factura = Facturas.objects.get(cod_factura=codigo)
    return render(request, 'Facturas/edicionFactura.html', {'factura': factura})

@login_required
def editarFactura(request):
    codigo = request.POST['cod_factura']
    cedula_cliente = request.POST['cedula_cliente']
    codigo_producto = request.POST['codigo_producto']
    id_colaborador = request.POST['id_colaborador']
    fecha = datetime.date.today()
    total_pagado = request.POST['total_pagado']
    cursor = connection.cursor()
    resultado = cursor.callfunc('F_ACTUALIZAR_FACTURA', bool, [codigo, cedula_cliente, codigo_producto, id_colaborador, fecha, total_pagado])
    cursor.close()
    if resultado:
        messages.success(request, '¡Factura actualizada!')
    else:
        messages.error(request, 'No se pudo actualizar la factura')
    return redirect('indexFacturas')
    path('facturas/edicionFactura/<codigo>', views.edicionFactura, name="edicionFactura"),
    path('editarFactura/', views.editarFactura, name="editarFactura"),
"""

@login_required
def eliminarFactura(request, codigo):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_FACTURA', [codigo])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Factura eliminada!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar la factura porque tiene registros asociados en otras tablas.')
    return redirect('indexFacturas')

@login_required
def indexFacturas(request):
    cursor = connection.cursor()
    facturas_cursor = cursor.callfunc('F_LISTAR_FACTURAS', cx_Oracle.CURSOR)
    productos_cursor = cursor.callfunc('F_LISTAR_PRODUCTOS', cx_Oracle.CURSOR)
    colaboradores_cursor = cursor.callfunc('F_LISTAR_COLABORADORES', cx_Oracle.CURSOR)
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
    facturas = []
    for factura in facturas_cursor:
        facturas.append({
            'cod_factura': factura[0],
            'cedula_cliente': factura[1],
            'codigo_producto': factura[2],
            'id_colaborador': factura[3],
            'fecha': factura[4],
            'total_pagado': factura[5],
            'precio_unitario': factura[6],
            'cantidad': factura[7],
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
    return render(request, 'Facturas/indexFacturas.html', {'facturas': facturas, 'productos': productos, 'colaboradores':colaboradores, 'clientes':clientes})

#Vista Devoluciones
def registrarDevolucion(request):
    if request.method == 'POST':
        try:
            cod_factura = request.POST.get('cod_factura')
            monto_devolucion = request.POST.get('monto_devolucion')
            cursor = connection.cursor()
            cursor.callproc('SP_INSERTAR_DEVOLUCION', [cod_factura, monto_devolucion])
            cursor.close()
            connection.commit()
            connection.close()
            messages.success(request, '¡Devolución registrada!')
            return redirect('indexDevoluciones')
        except cx_Oracle.IntegrityError:
            messages.error(request, 'Ya existe una devolución con este código')
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            messages.error(request, f'Error al registrar la devolución: {error.message}')
        except Exception:
            messages.error(request, f'Error en la base de datos: HTTP ERROR 500')
            #return HttpResponseServerError()
    return render(request, 'Devoluciones/indexDevoluciones.html')

"""
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
    path('devoluciones/edicionDevolucion/<id_devolucion>', views.edicionDevolucion, name="edicionDevolucion"),
    path('editarDevolucion/', views.editarDevolucion, name="editarDevolucion"),
"""

def eliminarDevolucion(request, id_devolucion):
    try:
        cursor = connection.cursor()
        cursor.callproc('SP_ELIMINAR_DEVOLUCION', [id_devolucion])
        cursor.close()
        connection.commit()
        connection.close()
        messages.success(request, '¡Devolución eliminada!')
    except IntegrityError:
        messages.error(request, 'No se puede eliminar la devolución porque tiene registros asociados en otras tablas.')
    return redirect('indexDevoluciones')

def indexDevoluciones(request):
    cursor = connection.cursor()
    facturas_cursor = cursor.callfunc('F_LISTAR_FACTURAS', cx_Oracle.CURSOR)
    devoluciones_cursor = cursor.callfunc('F_LISTAR_DEVOLUCIONES', cx_Oracle.CURSOR)
    facturas = []
    for factura in facturas_cursor:
        facturas.append({
            'cod_factura': factura[0],
            'cedula_cliente': factura[1],
            'codigo_producto': factura[2],
            'id_colaborador': factura[3],
            'fecha': factura[4],
            'total_pagado': factura[5],
            'precio_unitario': factura[6],
            'cantidad': factura[7],
            'estado': factura[8]
        })
    devoluciones = []
    for devolucion in devoluciones_cursor:
        devoluciones.append({
            'id_devolucion': devolucion[0],
            'fecha': devolucion[1],
            'ced_cliente': devolucion[2],
            'cod_producto': devolucion[3],
            'cod_factura': devolucion[4],
            'monto_devolucion': devolucion[5]
        })
    cursor.close()
    connection.close()
    return render(request, 'Devoluciones/indexDevoluciones.html', {'facturas': facturas, 'devoluciones': devoluciones})
