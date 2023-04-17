CREATE OR REPLACE FUNCTION F_LISTAR_PRODUCTOS
RETURN SYS_REFCURSOR
AS
  V_CURSOR SYS_REFCURSOR;
BEGIN
  OPEN V_CURSOR FOR
    SELECT * FROM PRODUCTOS;
    
  RETURN V_CURSOR;
END F_LISTAR_PRODUCTOS;
/

CREATE OR REPLACE PROCEDURE SP_INSERTAR_PRODUCTO (
    P_NOMBRE VARCHAR2,
    P_DESCRIPCION VARCHAR2,
    P_PRECIO NUMBER,
    P_STOCK NUMBER,
    P_PRO_ID_CATEGORIA NUMBER,
    P_ESTADO VARCHAR2
)
AS
BEGIN
    INSERT INTO PRODUCTOS (NOMBRE, DESCRIPCION, PRECIO, STOCK, PRO_ID_CATEGORIA, ESTADO)
    VALUES (P_NOMBRE, P_DESCRIPCION, P_PRECIO, P_STOCK, P_PRO_ID_CATEGORIA, P_ESTADO);
    COMMIT;
END SP_INSERTAR_PRODUCTO;
/

CREATE OR REPLACE FUNCTION F_ACTUALIZAR_PRODUCTO(
  P_COD_PRODUCTO NUMBER,
  P_NOMBRE VARCHAR2,
  P_DESCRIPCION VARCHAR2,
  P_PRECIO NUMBER,
  P_STOCK NUMBER,
  P_PRO_ID_CATEGORIA NUMBER,
  P_ESTADO VARCHAR2
) RETURN BOOLEAN
IS
  V_ACTUALIZADO BOOLEAN := FALSE;
BEGIN
  UPDATE PRODUCTOS SET
    NOMBRE = P_NOMBRE,
    DESCRIPCION = P_DESCRIPCION,
    PRECIO = P_PRECIO,
    STOCK = P_STOCK,
    PRO_ID_CATEGORIA = P_PRO_ID_CATEGORIA,
    ESTADO = P_ESTADO
  WHERE COD_PRODUCTO = P_COD_PRODUCTO;

  IF SQL%ROWCOUNT = 1 THEN
    V_ACTUALIZADO := TRUE;
  END IF;

  RETURN V_ACTUALIZADO;
EXCEPTION
  WHEN OTHERS THEN
    RETURN FALSE;
END F_ACTUALIZAR_PRODUCTO;
/

CREATE OR REPLACE PROCEDURE SP_ELIMINAR_PRODUCTO (
    P_COD_PRODUCTO NUMBER
)
AS
BEGIN
    DELETE FROM PRODUCTOS
    WHERE COD_PRODUCTO = P_COD_PRODUCTO;
    COMMIT;
END SP_ELIMINAR_PRODUCTO;
/

CREATE OR REPLACE PACKAGE PK_PRODUCTOS AS
  FUNCTION F_LISTAR_PRODUCTOS RETURN SYS_REFCURSOR;
  PROCEDURE SP_INSERTAR_PRODUCTO(
    P_COD_PRODUCTO NUMBER,
    P_NOMBRE VARCHAR2,
    P_DESCRIPCION VARCHAR2,
    P_PRECIO NUMBER,
    P_STOCK NUMBER,
    P_PRO_ID_CATEGORIA NUMBER,
    P_ESTADO VARCHAR2
  );
  FUNCTION F_ACTUALIZAR_PRODUCTO(
    P_COD_PRODUCTO NUMBER,
    P_NOMBRE VARCHAR2,
    P_DESCRIPCION VARCHAR2,
    P_PRECIO NUMBER,
    P_STOCK NUMBER,
    P_PRO_ID_CATEGORIA NUMBER,
    P_ESTADO VARCHAR2
  ) RETURN BOOLEAN;
  PROCEDURE SP_ELIMINAR_PRODUCTO(P_COD_PRODUCTO NUMBER);
END PK_PRODUCTOS;
/

CREATE TABLE AUDITORIA_PRODUCTO (
  COD_PRODUCTO NUMBER(11,0),
  NOMBRE VARCHAR2(50),
  DESCRIPCION VARCHAR2(100),
  PRECIO NUMBER(10,2),
  STOCK NUMBER(10),
  PRO_ID_CATEGORIA NUMBER(11,0),
  ESTADO VARCHAR2(20),
  OPERACION VARCHAR2(6),
  FECHA_OPERACION DATE
);

CREATE OR REPLACE TRIGGER TRG_PRODUCTO_INSERT
AFTER INSERT ON PRODUCTOS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_PRODUCTO (COD_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, PRO_ID_CATEGORIA, ESTADO, OPERACION, FECHA_OPERACION)
  VALUES (:NEW.COD_PRODUCTO, :NEW.NOMBRE, :NEW.DESCRIPCION, :NEW.PRECIO, :NEW.STOCK, :NEW.PRO_ID_CATEGORIA, :NEW.ESTADO, 'INSERT', SYSDATE);
END;
/

CREATE OR REPLACE TRIGGER TRG_PRODUCTO_UPDATE
AFTER UPDATE ON PRODUCTOS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_PRODUCTO (COD_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, PRO_ID_CATEGORIA, ESTADO, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.COD_PRODUCTO, :OLD.NOMBRE, :OLD.DESCRIPCION, :OLD.PRECIO, :OLD.STOCK, :OLD.PRO_ID_CATEGORIA, :OLD.ESTADO, 'UPDATE', SYSDATE);
END;
/

CREATE OR REPLACE TRIGGER TRG_PRODUCTO_DELETE
AFTER DELETE ON PRODUCTOS
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_PRODUCTO (COD_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, PRO_ID_CATEGORIA, ESTADO, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.COD_PRODUCTO, :OLD.NOMBRE, :OLD.DESCRIPCION, :OLD.PRECIO, :OLD.STOCK, :OLD.PRO_ID_CATEGORIA, :OLD.ESTADO, 'DELETE', SYSDATE);
END;
/
