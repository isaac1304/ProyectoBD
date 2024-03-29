/as sysdba
ALTER SESSION SET "_ORACLE_SCRIPT"= TRUE;

DROP USER PROYECTO CASCADE;

CREATE USER PROYECTO IDENTIFIED BY "P4$$woRD"
DEFAULT TABLESPACE "USERS"
TEMPORARY TABLESPACE "TEMP";
ALTER USER PROYECTO QUOTA UNLIMITED ON USERS;
GRANT CREATE SESSION TO PROYECTO;
GRANT "RESOURCE" TO PROYECTO;
ALTER USER PROYECTO DEFAULT ROLE "RESOURCE";

GRANT DBA TO PROYECTO;
GRANT CREATE VIEW TO PROYECTO;