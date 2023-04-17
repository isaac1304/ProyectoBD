CREATE OR REPLACE FUNCTION F_LISTAR_SUCURSALES
RETURN SYS_REFCURSOR
AS
  V_CURSOR SYS_REFCURSOR;
BEGIN
  OPEN V_CURSOR FOR
    SELECT * FROM SUCURSALES;
    
  RETURN V_CURSOR;
END F_LISTAR_SUCURSALES;
/

CREATE OR REPLACE PROCEDURE SP_INSERTAR_SUCURSAL (
    P_NOMBRE VARCHAR2,
    P_TELEFONO VARCHAR2,
    P_DIRECCION VARCHAR2
)
AS
BEGIN
    INSERT INTO SUCURSALES (NOMBRE, TELEFONO, DIRECCION)
    VALUES (P_NOMBRE, P_TELEFONO, P_DIRECCION);
    COMMIT;
END SP_INSERTAR_SUCURSAL;
/

CREATE OR REPLACE FUNCTION F_ACTUALIZAR_SUCURSAL(
  P_ID_SUCURSAL NUMBER,
  P_NOMBRE VARCHAR2,
  P_TELEFONO VARCHAR2,
  P_DIRECCION VARCHAR2
) RETURN BOOLEAN
IS
  V_ACTUALIZADO BOOLEAN := FALSE;
BEGIN
  UPDATE SUCURSALES SET
    NOMBRE = P_NOMBRE,
    TELEFONO = P_TELEFONO,
    DIRECCION = P_DIRECCION
  WHERE ID_SUCURSAL = P_ID_SUCURSAL;

  IF SQL%ROWCOUNT = 1 THEN
    V_ACTUALIZADO := TRUE;
  END IF;

  RETURN V_ACTUALIZADO;
EXCEPTION
  WHEN OTHERS THEN
    RETURN FALSE;
END F_ACTUALIZAR_SUCURSAL;
/

CREATE OR REPLACE PROCEDURE SP_ELIMINAR_SUCURSAL (
    P_ID_SUCURSAL NUMBER
)
AS
BEGIN
    DELETE FROM SUCURSALES
    WHERE ID_SUCURSAL = P_ID_SUCURSAL;
    COMMIT;
END SP_ELIMINAR_SUCURSAL;
/

CREATE OR REPLACE PACKAGE PK_SUCURSALES AS
  FUNCTION F_LISTAR_SUCURSALES RETURN SYS_REFCURSOR;
  FUNCTION F_ACTUALIZAR_SUCURSAL(P_ID_SUCURSAL NUMBER, P_NOMBRE VARCHAR2, P_TELEFONO VARCHAR2, P_DIRECCION VARCHAR2) RETURN BOOLEAN;
  PROCEDURE SP_INSERTAR_SUCURSAL(P_ID_SUCURSAL NUMBER, P_NOMBRE VARCHAR2, P_TELEFONO VARCHAR2, P_DIRECCION VARCHAR2);
  PROCEDURE SP_ELIMINAR_SUCURSAL(P_ID_SUCURSAL NUMBER);
END PK_SUCURSALES;
/

CREATE TABLE AUDITORIA_SUCURSAL (
  ID_SUCURSAL NUMBER(11,0),
  NOMBRE VARCHAR2(50),
  TELEFONO VARCHAR2(20),
  DIRECCION VARCHAR2(100),
  OPERACION VARCHAR2(6),
  FECHA_OPERACION DATE
);

CREATE OR REPLACE TRIGGER TRG_SUCURSAL_INSERT
AFTER INSERT ON SUCURSALES
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_SUCURSAL (ID_SUCURSAL, NOMBRE, TELEFONO, DIRECCION, OPERACION, FECHA_OPERACION)
  VALUES (:NEW.ID_SUCURSAL, :NEW.NOMBRE, :NEW.TELEFONO, :NEW.DIRECCION, 'INSERT', SYSDATE);
END;
/

CREATE OR REPLACE TRIGGER TRG_SUCURSAL_UPDATE
AFTER UPDATE ON SUCURSALES
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_SUCURSAL (ID_SUCURSAL, NOMBRE, TELEFONO, DIRECCION, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.ID_SUCURSAL, :OLD.NOMBRE, :OLD.TELEFONO, :OLD.DIRECCION, 'UPDATE', SYSDATE);
END;
/

CREATE OR REPLACE TRIGGER TRG_SUCURSAL_DELETE
AFTER DELETE ON SUCURSALES
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA_SUCURSAL (ID_SUCURSAL, NOMBRE, TELEFONO, DIRECCION, OPERACION, FECHA_OPERACION)
  VALUES (:OLD.ID_SUCURSAL, :OLD.NOMBRE, :OLD.TELEFONO, :OLD.DIRECCION, 'DELETE', SYSDATE);
END;
/