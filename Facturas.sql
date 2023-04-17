CREATE OR REPLACE FUNCTION F_LISTAR_FACTURAS
RETURN SYS_REFCURSOR
AS
  V_CURSOR SYS_REFCURSOR;
BEGIN
  OPEN V_CURSOR FOR
    SELECT * FROM FACTURAS;
    
  RETURN V_CURSOR;
END F_LISTAR_FACTURAS;

CREATE OR REPLACE PROCEDURE SP_INSERTAR_FACTURA (
    P_COD_FACTURA NUMBER,
    P_FAC_CED_CLIENTE NUMBER,
    P_FAC_COD_PRODUCTO NUMBER,
    P_FAC_ID_COLABORADOR NUMBER,
    P_FECHA DATE,
    P_TOTAL_PAGADO NUMBER
)
AS
BEGIN
    INSERT INTO FACTURAS (COD_FACTURA, FAC_CED_CLIENTE, FAC_COD_PRODUCTO, FAC_ID_COLABORADOR, FECHA, TOTAL_PAGADO)
    VALUES (P_COD_FACTURA, P_FAC_CED_CLIENTE, P_FAC_COD_PRODUCTO, P_FAC_ID_COLABORADOR, P_FECHA, P_TOTAL_PAGADO);
    COMMIT;
END SP_INSERTAR_FACTURA;

CREATE OR REPLACE FUNCTION F_ACTUALIZAR_FACTURA(
  P_COD_FACTURA NUMBER,
  P_FAC_CED_CLIENTE NUMBER,
  P_FAC_COD_PRODUCTO NUMBER,
  P_FAC_ID_COLABORADOR NUMBER,
  P_FECHA DATE,
  P_TOTAL_PAGADO NUMBER
) RETURN BOOLEAN
IS
  V_ACTUALIZADO BOOLEAN := FALSE;
BEGIN
  UPDATE FACTURAS SET
    FAC_CED_CLIENTE = P_FAC_CED_CLIENTE,
    FAC_COD_PRODUCTO = P_FAC_COD_PRODUCTO,
    FAC_ID_COLABORADOR = P_FAC_ID_COLABORADOR,
    FECHA = P_FECHA,
    TOTAL_PAGADO = P_TOTAL_PAGADO
  WHERE COD_FACTURA = P_COD_FACTURA;

  IF SQL%ROWCOUNT = 1 THEN
    V_ACTUALIZADO := TRUE;
  END IF;

  RETURN V_ACTUALIZADO;
EXCEPTION
  WHEN OTHERS THEN
    RETURN FALSE;
END F_ACTUALIZAR_FACTURA;

CREATE OR REPLACE PROCEDURE SP_ELIMINAR_FACTURA (
    P_COD_FACTURA NUMBER
)
AS
BEGIN
    DELETE FROM FACTURAS
    WHERE COD_FACTURA = P_COD_FACTURA;
    COMMIT;
END SP_ELIMINAR_FACTURA;

CREATE OR REPLACE PACKAGE PK_FACTURACION IS
  FUNCTION F_LISTAR_CLIENTES RETURN SYS_REFCURSOR;
  PROCEDURE SP_INSERTAR_CLIENTE (
    P_CEDULA_CLIENTE NUMBER,
    P_NOMBRE VARCHAR2,
    P_APELLIDO_1 VARCHAR2,
    P_APELLIDO_2 VARCHAR2,
    P_NACIMIENTO DATE,
    P_CORREO VARCHAR2,
    P_TELEFONO VARCHAR2,
    P_DIRECCION VARCHAR2
  );
  FUNCTION F_ACTUALIZAR_CLIENTE(
    P_CEDULA_CLIENTE NUMBER,
    P_NOMBRE VARCHAR2,
    P_APELLIDO_1 VARCHAR2,
    P_APELLIDO_2 VARCHAR2,
    P_NACIMIENTO DATE,
    P_CORREO VARCHAR2,
    P_TELEFONO VARCHAR2,
    P_DIRECCION VARCHAR2
  ) RETURN BOOLEAN;
  PROCEDURE SP_ELIMINAR_CLIENTE (
    P_CEDULA_CLIENTE NUMBER
  );
END PK_FACTURACION;

CREATE TABLE AUDITORIA_FACTURAS (
  COD_FACTURA NUMBER(11,0),
  FAC_CED_CLIENTE NUMBER(11,0),
  FAC_COD_PRODUCTO NUMBER(11,0),
  FAC_ID_COLABORADOR NUMBER(11,0),
  FECHA DATE,
  TOTAL_PAGADO NUMBER(10,2),
  OPERACION VARCHAR2(6),
  FECHA_OPERACION DATE
);

CREATE OR REPLACE TRIGGER TRG_FACTURA_INSERT
AFTER INSERT ON FACTURAS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_FACTURAS (COD_FACTURA, FAC_CED_CLIENTE, FAC_COD_PRODUCTO, FAC_ID_COLABORADOR, FECHA, TOTAL_PAGADO, OPERACION, FECHA_OPERACION)
  VALUES (:NEW.COD_FACTURA, :NEW.FAC_CED_CLIENTE, :NEW.FAC_COD_PRODUCTO, :NEW.FAC_ID_COLABORADOR, :NEW.FECHA, :NEW.TOTAL_PAGADO, 'INSERT', SYSDATE);
END;

CREATE OR REPLACE TRIGGER TRG_FACTURA_UPDATE
AFTER UPDATE ON FACTURAS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_FACTURAS (COD_FACTURA, FAC_CED_CLIENTE, FAC_COD_PRODUCTO, FAC_ID_COLABORADOR, FECHA, TOTAL_PAGADO, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.COD_FACTURA, :OLD.FAC_CED_CLIENTE, :OLD.FAC_COD_PRODUCTO, :OLD.FAC_ID_COLABORADOR, :OLD.FECHA, :OLD.TOTAL_PAGADO, 'UPDATE', SYSDATE);
END;

CREATE OR REPLACE TRIGGER TRG_FACTURA_DELETE
AFTER DELETE ON FACTURAS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_FACTURAS (COD_FACTURA, FAC_CED_CLIENTE, FAC_COD_PRODUCTO, FAC_ID_COLABORADOR, FECHA, TOTAL_PAGADO, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.COD_FACTURA, :OLD.FAC_CED_CLIENTE, :OLD.FAC_COD_PRODUCTO, :OLD.FAC_ID_COLABORADOR, :OLD.FECHA, :OLD.TOTAL_PAGADO, 'DELETE', SYSDATE);
END;