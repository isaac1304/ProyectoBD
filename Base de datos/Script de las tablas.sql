--Scrip de las tablas de la base de datos
CREATE TABLE CLIENTE (
  CEDULA_CLIENTE NUMBER(11,0) PRIMARY KEY,
  NOMBRE VARCHAR2(50),
  APELLIDO_1 VARCHAR2(50),
  APELLIDO_2 VARCHAR2(50),
  NACIMIENTO DATE,
  CORREO VARCHAR2(100),
  TELEFONO VARCHAR2(20),
  DIRECCION VARCHAR2(100)
);

CREATE TABLE COLABORADORES (
  ID_COLABORADOR NUMBER(11,0) PRIMARY KEY,
  CEDULA_COLABORADOR VARCHAR2(10),
  NOMBRE VARCHAR2(50),
  APELLIDO_1 VARCHAR2(50),
  APELLIDO_2 VARCHAR2(50),
  CORREO VARCHAR2(100),
  TELEFONO VARCHAR2(20),
  PUESTO VARCHAR2(50),
  COL_DIRECCION VARCHAR2(100)
);

CREATE TABLE CATEGORIA (
  ID_CATEGORIA NUMBER(11,0) PRIMARY KEY,
  NOMBRE VARCHAR2(50),
  DESCRIPCION VARCHAR2(100)
);

CREATE TABLE PRODUCTOS (
  COD_PRODUCTO NUMBER(11,0) PRIMARY KEY,
  NOMBRE VARCHAR2(50),
  DESCRIPCION VARCHAR2(100),
  PRECIO NUMBER(10,2),
  STOCK NUMBER(10),
  PRO_ID_CATEGORIA NUMBER(11,0),
  ESTADO VARCHAR2(20),
  CONSTRAINT FK_PRODUCTOS_CATEGORIA FOREIGN KEY (PRO_ID_CATEGORIA) REFERENCES CATEGORIA(ID_CATEGORIA)
);

CREATE TABLE PROVEEDORES (
  ID_PROVEEDOR NUMBER(11,0) PRIMARY KEY,
  NOMBRE VARCHAR2(50),
  CORREO VARCHAR2(100),
  TELEFONO VARCHAR2(20),
  DIRECCION VARCHAR2(100)
);

CREATE TABLE SUCURSALES (
  ID_SUCURSAL NUMBER(11,0) PRIMARY KEY,
  NOMBRE VARCHAR2(50),
  TELEFONO VARCHAR2(20),
  DIRECCION VARCHAR2(100)
);

CREATE TABLE FACTURAS (
  COD_FACTURA NUMBER(11,0) PRIMARY KEY,
  FAC_CED_CLIENTE NUMBER(11,0),
  FAC_COD_PRODUCTO NUMBER(11,0),
  FAC_ID_COLABORADOR NUMBER(11,0),
  FECHA DATE,
  TOTAL_PAGADO NUMBER(10,2),
  PRECIO_UNITARIO NUMBER(10,2),
  CANTIDAD NUMBER(11,0),
  ESTADO NUMBER(1,0) DEFAULT 1,
  CONSTRAINT FK_FACTURA_CLIENTE FOREIGN KEY (FAC_CED_CLIENTE) REFERENCES CLIENTE(CEDULA_CLIENTE),
  CONSTRAINT FK_FACTURA_PRODUCTO FOREIGN KEY (FAC_COD_PRODUCTO) REFERENCES PRODUCTOS(COD_PRODUCTO),
  CONSTRAINT FK_FACTURA_COLABORADOR FOREIGN KEY (FAC_ID_COLABORADOR) REFERENCES COLABORADORES(ID_COLABORADOR)
);

CREATE TABLE DEVOLUCIONES (
  ID_DEVOLUCION NUMBER(11,0) PRIMARY KEY,
  FECHA DATE,
  DEV_CED_CLIENTE NUMBER(11,0),
  DEV_COD_PRODUCTO NUMBER(11,0),
  DEV_COD_FACTURA NUMBER(11,0),
  MONTO_DEVOLUCION NUMBER(10,2),
  CONSTRAINT FK_DEVOLUCION_CLIENTE FOREIGN KEY (DEV_CED_CLIENTE) REFERENCES CLIENTE(CEDULA_CLIENTE),
  CONSTRAINT FK_DEVOLUCION_PRODUCTO FOREIGN KEY (DEV_COD_PRODUCTO) REFERENCES PRODUCTOS(COD_PRODUCTO),
  CONSTRAINT FK_DEVOLUCION_FACTURA FOREIGN KEY (DEV_COD_FACTURA) REFERENCES FACTURAS(COD_FACTURA)
);

CREATE SEQUENCE SEQ_COLABORADORES START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_CATEGORIA START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_PRODUCTOS START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_PROVEEDORES START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_SUCURSALES START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_FACTURAS START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE SEQ_DEVOLUCIONES START WITH 1 INCREMENT BY 1;

ALTER TABLE COLABORADORES
MODIFY ID_COLABORADOR DEFAULT SEQ_COLABORADORES.NEXTVAL;

ALTER TABLE CATEGORIA
MODIFY ID_CATEGORIA DEFAULT SEQ_CATEGORIA.NEXTVAL;

ALTER TABLE PRODUCTOS
MODIFY COD_PRODUCTO DEFAULT SEQ_PRODUCTOS.NEXTVAL;

ALTER TABLE PROVEEDORES
MODIFY ID_PROVEEDOR DEFAULT SEQ_PROVEEDORES.NEXTVAL;

ALTER TABLE SUCURSALES
MODIFY ID_SUCURSAL DEFAULT SEQ_SUCURSALES.NEXTVAL;

ALTER TABLE FACTURAS
MODIFY COD_FACTURA DEFAULT SEQ_FACTURAS.NEXTVAL;

ALTER TABLE DEVOLUCIONES
MODIFY ID_DEVOLUCION DEFAULT SEQ_DEVOLUCIONES.NEXTVAL;

-- Relacion de Colaboradores con Sucursales
ALTER TABLE COLABORADORES ADD COL_ID_SUCURSAL NUMBER(11,0);
ALTER TABLE COLABORADORES ADD CONSTRAINT FK_COLABORADORES_SUCURSALES FOREIGN KEY (COL_ID_SUCURSAL) REFERENCES SUCURSALES(ID_SUCURSAL);

-- Relacion Productos con proveedor
ALTER TABLE PRODUCTOS ADD PRO_ID_PROVEEDOR NUMBER(11,0);
ALTER TABLE PRODUCTOS ADD CONSTRAINT FK_PRODUCTOS_PROVEEDORES FOREIGN KEY (PRO_ID_PROVEEDOR) REFERENCES PROVEEDORES(ID_PROVEEDOR);