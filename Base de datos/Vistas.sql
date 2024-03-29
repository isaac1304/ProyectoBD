--Vista de las devoluciones con información del cliente, el producto y la factura
CREATE OR REPLACE VIEW vista_devoluciones AS 
SELECT d.ID_DEVOLUCION, d.FECHA, c.NOMBRE AS CLIENTE, p.NOMBRE AS PRODUCTO, f.COD_FACTURA, d.MONTO_DEVOLUCION 
FROM DEVOLUCIONES d 
JOIN CLIENTE c ON d.DEV_CED_CLIENTE = c.CEDULA_CLIENTE 
JOIN PRODUCTOS p ON d.DEV_COD_PRODUCTO = p.COD_PRODUCTO 
JOIN FACTURAS f ON d.DEV_COD_FACTURA = f.COD_FACTURA;

SELECT * FROM vista_devoluciones;

--Vista de las facturas con información del cliente, el producto y el colaborador
CREATE OR REPLACE VIEW vista_facturas AS 
SELECT f.COD_FACTURA, c.NOMBRE AS CLIENTE, p.NOMBRE AS PRODUCTO, col.NOMBRE AS COLABORADOR, f.FECHA, f.TOTAL_PAGADO 
FROM FACTURAS f 
JOIN CLIENTE c ON f.FAC_CED_CLIENTE = c.CEDULA_CLIENTE 
JOIN PRODUCTOS p ON f.FAC_COD_PRODUCTO = p.COD_PRODUCTO 
JOIN COLABORADORES col ON f.FAC_ID_COLABORADOR = col.ID_COLABORADOR;

SELECT * FROM vista_facturas;

--Vista de ventas totales por categoría
CREATE OR REPLACE VIEW VISTA_VENTAS_CATEGORIA AS
SELECT 
  C.NOMBRE AS CATEGORIA,
  SUM(F.TOTAL_PAGADO) AS VENTAS_TOTALES
FROM 
  CATEGORIA C
  JOIN PRODUCTOS P ON C.ID_CATEGORIA = P.PRO_ID_CATEGORIA
  JOIN FACTURAS F ON P.COD_PRODUCTO = F.FAC_COD_PRODUCTO
GROUP BY 
  C.NOMBRE;

SELECT * FROM vista_ventas_categoria;
  
--Vista de productos con bajo inventario
CREATE OR REPLACE  VIEW VISTA_PRODUCTOS_BAJO_INVENTARIO AS
SELECT 
  P.COD_PRODUCTO,
  P.NOMBRE,
  P.STOCK
FROM 
  PRODUCTOS P
WHERE 
  P.STOCK < 5;

SELECT * FROM vista_productos_bajo_inventario;

--Vista de ventas por producto y fecha
CREATE OR REPLACE VIEW VISTA_VENTAS_PRODUCTO_FECHA AS
SELECT 
  P.COD_PRODUCTO, 
  P.NOMBRE, 
  F.FECHA,
  SUM(F.TOTAL_PAGADO) AS VENTAS_TOTALES
FROM 
  PRODUCTOS P 
  JOIN FACTURAS F ON P.COD_PRODUCTO = F.FAC_COD_PRODUCTO
GROUP BY 
  P.COD_PRODUCTO, 
  P.NOMBRE, 
  F.FECHA;
  
SELECT * FROM vista_ventas_producto_fecha;

--Vista de clientes y sus compras
CREATE OR REPLACE  VIEW VISTA_CLIENTES_COMPRAS AS
SELECT 
  C.CEDULA_CLIENTE, 
  C.NOMBRE,
  F.FECHA,
  P.NOMBRE AS PRODUCTO,
  F.TOTAL_PAGADO
FROM 
  CLIENTE C 
  JOIN FACTURAS F ON C.CEDULA_CLIENTE = F.FAC_CED_CLIENTE
  JOIN PRODUCTOS P ON F.FAC_COD_PRODUCTO = P.COD_PRODUCTO;

SELECT * FROM vista_clientes_compras;

--Vista de ventas por mes y producto
CREATE OR REPLACE  VIEW VENTAS_MENSUALES_PRODUCTOS AS
SELECT TO_CHAR(FECHA, 'YYYY-MM') AS MES,
       NOMBRE AS NOMBRE_PRODUCTO,
       SUM(TOTAL_PAGADO) AS TOTAL_VENTAS
FROM FACTURAS
JOIN PRODUCTOS ON FACTURAS.FAC_COD_PRODUCTO = PRODUCTOS.COD_PRODUCTO
GROUP BY TO_CHAR(FECHA, 'YYYY-MM'), NOMBRE;

SELECT * FROM ventas_mensuales_productos;

--Vista de clientes con más compras
CREATE OR REPLACE  VIEW CLIENTES_CON_MAS_COMPRAS AS
SELECT CLIENTE.CEDULA_CLIENTE,
       CLIENTE.NOMBRE,
       CLIENTE.APELLIDO_1,
       CLIENTE.APELLIDO_2,
       COUNT(FACTURAS.COD_FACTURA) AS NUM_COMPRAS
FROM CLIENTE
JOIN FACTURAS ON CLIENTE.CEDULA_CLIENTE = FACTURAS.FAC_CED_CLIENTE
GROUP BY CLIENTE.CEDULA_CLIENTE, CLIENTE.NOMBRE, CLIENTE.APELLIDO_1, CLIENTE.APELLIDO_2
ORDER BY NUM_COMPRAS DESC;

SELECT*FROM CLIENTES_CON_MAS_COMPRAS;

--Vista de clientes con menos compras, tambien se puede con mas compras y mostrar a los tres principales
CREATE OR REPLACE VIEW VISTA_CLIENTES_MENOS_COMPRAS AS
SELECT CEDULA_CLIENTE, NOMBRE, APELLIDO_1, APELLIDO_2, CORREO, TELEFONO, COUNT(*) AS CANTIDAD_COMPRAS
FROM CLIENTE
WHERE CEDULA_CLIENTE IN (
  SELECT FAC_CED_CLIENTE
  FROM FACTURAS
  GROUP BY FAC_CED_CLIENTE
  ORDER BY COUNT(*) DESC
  FETCH FIRST 3 ROWS ONLY
)
GROUP BY CEDULA_CLIENTE, NOMBRE, APELLIDO_1, APELLIDO_2, CORREO, TELEFONO
ORDER BY CANTIDAD_COMPRAS ASC;

SELECT * FROM vista_clientes_menos_compras;

--Vista de clientes con mas compras
CREATE OR REPLACE VIEW VISTA_CLIENTES_MAS_COMPRAS AS
SELECT CEDULA_CLIENTE, NOMBRE, APELLIDO_1, APELLIDO_2, CORREO, TELEFONO, COUNT(*) AS CANTIDAD_COMPRAS
FROM CLIENTE
WHERE CEDULA_CLIENTE IN (
  SELECT FAC_CED_CLIENTE
  FROM FACTURAS
  GROUP BY FAC_CED_CLIENTE
  ORDER BY COUNT(*) DESC
  FETCH FIRST 3 ROWS ONLY
)
GROUP BY CEDULA_CLIENTE, NOMBRE, APELLIDO_1, APELLIDO_2, CORREO, TELEFONO
ORDER BY CANTIDAD_COMPRAS DESC;

SELECT * FROM vista_clientes_mas_compras;

--Vista para Reporte de Producto Mas Vendido
CREATE OR REPLACE VIEW PRODUCTOS_MAS_VENDIDOS AS
SELECT p.NOMBRE AS NOMBRE_PRODUCTO, COUNT(*) AS CANTIDAD_VENTAS
FROM FACTURAS f
INNER JOIN PRODUCTOS p ON f.FAC_COD_PRODUCTO = p.COD_PRODUCTO
GROUP BY p.NOMBRE
ORDER BY COUNT(*) DESC
FETCH FIRST 4 ROWS ONLY;

select * from PRODUCTOS_MAS_VENDIDOS;

--Vista para filtrar las ventas del colaborador por semana
CREATE OR REPLACE VIEW VENTAS_SEMANALES_COLABORADOR AS
SELECT c.NOMBRE AS NOMBRE_COLABORADOR, p.NOMBRE AS NOMBRE_PRODUCTO, 
       COUNT(*) AS CANTIDAD_VENTAS
FROM FACTURAS f
INNER JOIN PRODUCTOS p ON f.FAC_COD_PRODUCTO = p.COD_PRODUCTO
INNER JOIN COLABORADORES c ON f.FAC_ID_COLABORADOR = c.ID_COLABORADOR
WHERE TRUNC(f.FECHA) >= TRUNC(SYSDATE) - 7
GROUP BY c.NOMBRE, p.NOMBRE
ORDER BY COUNT(*) DESC;

select * from VENTAS_SEMANALES_COLABORADOR;

--Vista para filtrar las ventas del colaborador por mes
CREATE OR REPLACE VIEW VENTAS_MENSUALES_COLABORADOR AS
SELECT c.NOMBRE AS NOMBRE_COLABORADOR,
       TO_CHAR(f.FECHA, 'YYYY-MM') AS MES,
       COUNT(*) AS CANTIDAD_VENTAS
FROM FACTURAS f
INNER JOIN COLABORADORES c ON f.FAC_ID_COLABORADOR = c.ID_COLABORADOR
WHERE TRUNC(f.FECHA, 'MONTH') = TRUNC(SYSDATE, 'MONTH') -- Ventas del mes actual
GROUP BY c.NOMBRE, TO_CHAR(f.FECHA, 'YYYY-MM')
ORDER BY c.NOMBRE, TO_CHAR(f.FECHA, 'YYYY-MM');

select * from VENTAS_MENSUALES_COLABORADOR;

--Vista para ver el dia en el que se realizaron mas ventas
CREATE OR REPLACE VIEW DIA_MAX_VENTAS AS
SELECT TO_CHAR(FECHA, 'DD-MON-YYYY') AS DIA, COUNT(*) AS CANTIDAD_VENTAS
FROM FACTURAS
GROUP BY TO_CHAR(FECHA, 'DD-MON-YYYY')
ORDER BY COUNT(*) DESC
FETCH FIRST 1 ROWS ONLY;

select * from DIA_MAX_VENTAS;