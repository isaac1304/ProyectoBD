DELETE FROM CLIENTE;
TRUNCATE TABLE CLIENTE;

EXEC sp_insertar_cliente (1, 'Juan', 'Pérez', 'García', TO_DATE('1990/01/01', 'yyyy/mm/dd'), 'juanperez@gmail.com', '1234567890', 'Calle 1, Ciudad 1');

EXEC sp_insertar_cliente (2, 'María', 'González', 'Hernández', TO_DATE('1995/05/05', 'yyyy/mm/dd'), 'mariagonzalez@gmail.com', '2345678901', 'Calle 2, Ciudad 2');

EXEC sp_insertar_cliente (3, 'Pedro', 'Rodríguez', 'López', TO_DATE('1985/03/15', 'yyyy/mm/dd'), 'pedrorodriguez@gmail.com', '3456789012', 'Calle 3, Ciudad 3');

EXEC sp_insertar_cliente (4, 'Luis', 'Martínez', 'Sánchez', TO_DATE('1992/08/20', 'yyyy/mm/dd'), 'luismartinez@gmail.com', '4567890123', 'Calle 4, Ciudad 4');

EXEC sp_insertar_cliente (5, 'Ana', 'López', 'García', TO_DATE('1993/06/25', 'yyyy/mm/dd'), 'analopez@gmail.com', '5678901234', 'Calle 5, Ciudad 5');

EXEC sp_insertar_cliente (6, 'Jorge', 'García', 'Martínez', TO_DATE('1988/12/10', 'yyyy/mm/dd'), 'jorgegarcia@gmail.com', '6789012345', 'Calle 6, Ciudad 6');

EXEC sp_insertar_cliente (7, 'Laura', 'González', 'Sánchez', TO_DATE('1994/07/30', 'yyyy/mm/dd'), 'lauragonzalez@gmail.com', '7890123456', 'Calle 7, Ciudad 7');

EXEC sp_insertar_cliente (8, 'Carlos', 'Martínez', 'González', TO_DATE('1980/04/12', 'yyyy/mm/dd'), 'carlosmartinez@gmail.com', '8901234567', 'Calle 8, Ciudad 8');

EXEC sp_insertar_cliente (9, 'Marta', 'Hernández', 'Pérez', TO_DATE('1987/10/05', 'yyyy/mm/dd'), 'martahernandez@gmail.com', '9012345678', 'Calle 9, Ciudad 9');

EXEC sp_insertar_cliente (10, 'Sofía', 'García', 'López', TO_DATE('1991/02/28', 'yyyy/mm/dd'), 'sofiagarcia@gmail.com', '0123456789', 'Calle 10, Ciudad 10');

EXEC sp_insertar_cliente (11, 'Julio', 'Pérez', 'García', TO_DATE('1989/09/15', 'yyyy/mm/dd'), 'julioperez@gmail.com', '1234567890', 'Calle 11, Ciudad 11');

EXEC sp_insertar_cliente (12, 'Lucía', 'González', 'Hernández', TO_DATE('1997/03/20', 'yyyy/mm/dd'), 'luciagonzalez@gmail.com', '2345678901', 'Calle 12, Ciudad 12');

EXEC sp_insertar_cliente (13, 'Alberto', 'Rodríguez', 'López', TO_DATE('1993/06/10', 'yyyy/mm/dd'), 'albertorodriguez@gmail.com', '3456789012', 'Calle 13, Ciudad 13');

EXEC sp_insertar_cliente (14, 'Carolina', 'Martínez', 'Sánchez', TO_DATE('1986/11/25', 'yyyy/mm/dd'), 'carolinamartinez@gmail.com', '4567890123', 'Calle 14, Ciudad 14');

EXEC sp_insertar_cliente (15, 'Luis', 'Fernández', 'García', TO_DATE('1992/08/18', 'yyyy/mm/dd'), 'luisfernandez@gmail.com', '5678901234', 'Calle 15, Ciudad 15');

EXEC sp_insertar_cliente (16, 'Ana', 'López', 'González', TO_DATE('1995/05/07', 'yyyy/mm/dd'), 'analg@gmail.com', '6789012345', 'Calle 16, Ciudad 16');

EXEC sp_insertar_cliente (17, 'Juan', 'García', 'Pérez', TO_DATE('1984/02/22', 'yyyy/mm/dd'), 'juangarcia@gmail.com', '7890123456', 'Calle 17, Ciudad 17');

EXEC sp_insertar_cliente (18, 'María', 'Hernández', 'González', TO_DATE('1990/09/03', 'yyyy/mm/dd'), 'mariahernandez@gmail.com', '8901234567', 'Calle 18, Ciudad 18');

---------------------------------------------------------------------------------------------------------------------------------------
DELETE FROM COLABORADORES;
TRUNCATE TABLE COLABORADORES;

EXEC sp_insertar_colaborador ('1234567890', 'Juan', 'Pérez', 'García', 'juan.perez@ejemplo.com', '555-1234', 'Gerente de Tienda', 'Calle 1, Ciudad 1');

EXEC sp_insertar_colaborador ('2345678901', 'María', 'López', 'González', 'maria.lopez@ejemplo.com', '555-2345', 'Encargado de Ventas', 'Calle 1, Ciudad 1');

EXEC sp_insertar_colaborador ('3456789012', 'Pedro', 'González', 'Sánchez', 'pedro.gonzalez@ejemplo.com', '555-3456', 'Técnico de Soporte', 'Calle 1, Ciudad 1');

EXEC sp_insertar_colaborador ('4567890123', 'Ana', 'Ramírez', 'Jiménez', 'ana.ramirez@ejemplo.com', '555-4567', 'Vendedor', 'Calle 1, Ciudad 1');

EXEC sp_insertar_colaborador ('5678901234', 'Carlos', 'Díaz', 'Martínez', 'carlos.diaz@ejemplo.com', '555-5678', 'Técnico de Reparación', 'Calle 2, Ciudad 2');

EXEC sp_insertar_colaborador ('6789012345', 'Sofía', 'Álvarez', 'Hernández', 'sofia.alvarez@ejemplo.com', '555-6789', 'Vendedor', 'Calle 2, Ciudad 2');

EXEC sp_insertar_colaborador ('7890123456', 'Diego', 'Gómez', 'Gutiérrez', 'diego.gomez@ejemplo.com', '555-7890', 'Gerente de Tienda', 'Calle 2, Ciudad 2');

EXEC sp_insertar_colaborador ('8901234567', 'Laura', 'Martínez', 'Sánchez', 'laura.martinez@ejemplo.com', '555-8901', 'Encargado de Ventas', 'Calle 2, Ciudad 2');

EXEC sp_insertar_colaborador ('9012345678', 'Javier', 'Pérez', 'Fernández', 'javier.perez@ejemplo.com', '555-9012', 'Técnico de Soporte', 'Calle 2, Ciudad 2');

EXEC sp_insertar_colaborador ('0123456789', 'Marcela', 'Sánchez', 'Álvarez', 'marcela.sanchez@ejemplo.com', '555-0123', 'Vendedor', 'Calle 3, Ciudad 3');

EXEC sp_insertar_colaborador ('1234567890', 'Gabriel', 'Hernández', 'Ramírez', 'gabriel.hernandez@ejemplo.com', '555-1234', 'Técnico de Reparación', 'Calle 3, Ciudad 3');

EXEC sp_insertar_colaborador ('2345678901', 'Ana', 'González', 'García', 'ana.gonzalez@ejemplo.com', '555-2345', 'Vendedor', 'Calle 3, Ciudad 3');

EXEC sp_insertar_colaborador ('3456789012', 'Sofía', 'Castro', 'Jiménez', 'sofia.castro@ejemplo.com', '555-3456', 'Gerente de Tienda', 'Calle 4, Ciudad 4');

EXEC sp_insertar_colaborador ('4567890123', 'Mario', 'Vargas', 'García', 'mario.vargas@ejemplo.com', '555-4567', 'Encargado de Ventas', 'Calle 4, Ciudad 4');

EXEC sp_insertar_colaborador ('5678901234', 'Lucía', 'Pérez', 'Sánchez', 'lucia.perez@ejemplo.com', '555-5678', 'Técnico de Soporte', 'Calle 4, Ciudad 4');

EXEC sp_insertar_colaborador ('6789012345', 'Juan', 'Gutiérrez', 'Fernández', 'juan.gutierrez@ejemplo.com', '555-6789', 'Vendedor', 'Calle 5, Ciudad 5');

EXEC sp_insertar_colaborador ('7890123456', 'Ana', 'Martínez', 'Álvarez', 'ana.martinez@ejemplo.com', '555-7890', 'Técnico de Reparación', 'Calle 5, Ciudad 5');

EXEC sp_insertar_colaborador ('8901234567', 'María', 'Fernández', 'Hernández', 'maria.fernandez@ejemplo.com', '555-8901', 'Vendedor', 'Calle 5, Ciudad 5');

---------------------------------------------------------------------------------------------------------------
DELETE FROM PROVEEDORES;
TRUNCATE TABLE PROVEEDORES;

EXEC sp_insertar_proveedor ('Juan Pérez', 'juanperez@example.com', '2222-2222', 'San José, Costa Rica');

EXEC sp_insertar_proveedor ('María Fernández', 'mariafernandez@example.com', '3333-3333', 'Heredia, Costa Rica');

EXEC sp_insertar_proveedor ('Luis Sánchez', 'luissanchez@example.com', '4444-4444', 'Cartago, Costa Rica');

EXEC sp_insertar_proveedor ('Ana Solano', 'anasolano@example.com', '5555-5555', 'Alajuela, Costa Rica');

EXEC sp_insertar_proveedor ('Jorge Castillo', 'jorgecastillo@example.com', '6666-6666', 'Limón, Costa Rica');

EXEC sp_insertar_proveedor ('Silvia Ramírez', 'silviaramirez@example.com', '7777-7777', 'Puntarenas, Costa Rica');

EXEC sp_insertar_proveedor ('Pedro Rojas', 'pedrorojas@example.com', '8888-8888', 'San José, Costa Rica');

EXEC sp_insertar_proveedor ('Carmen Chacón', 'carmenchacon@example.com', '9999-9999', 'Heredia, Costa Rica');

EXEC sp_insertar_proveedor ('Javier Araya', 'javieraraya@example.com', '1111-1111', 'Cartago, Costa Rica');

EXEC sp_insertar_proveedor ('Lucía Campos', 'luciacampos@example.com', '2222-2222', 'Alajuela, Costa Rica');

EXEC sp_insertar_proveedor ('Ricardo Umaña', 'ricardoumana@example.com', '3333-3333', 'Limón, Costa Rica');

EXEC sp_insertar_proveedor ('Mariana Jiménez', 'marianajimenez@example.com', '4444-4444', 'Puntarenas, Costa Rica');

EXEC sp_insertar_proveedor ('Eduardo Castro', 'eduardocastro@example.com', '5555-5555', 'San José, Costa Rica');

EXEC sp_insertar_proveedor ('Carolina Solís', 'carolinasolis@example.com', '6666-6666', 'Heredia, Costa Rica');

EXEC sp_insertar_proveedor ('Diego Hernández', 'diegohernandez@example.com', '7777-7777', 'Cartago, Costa Rica');

EXEC sp_insertar_proveedor ('Fabiola Ugalde', 'fabiolaugalde@example.com', '8888-8888', 'Alajuela, Costa Rica');

EXEC sp_insertar_proveedor ('Andrés Esquivel', 'andresesquivel@example.com', '9999-9999', 'Limón, Costa Rica');

EXEC sp_insertar_proveedor ('Verónica Fernández', 'veronicafernandez@example.com', '1111-1111', 'Puntarenas, Costa Rica');

EXEC sp_insertar_proveedor ('Gustavo Quesada', 'gustavoquesada@example.com', '2222-2222', 'San José, Costa Rica');

EXEC sp_insertar_proveedor ('Ana Martínez', 'anamartinez@example.com', '3333-3333', 'Heredia, Costa Rica');

EXEC sp_insertar_proveedor ('Juan Vargas', 'juanvargas@example.com', '4444-4444', 'Cartago, Costa Rica');

------------------------------------------------------------------------------------------------------------
DELETE FROM SUCURSALES;
TRUNCATE TABLE SUCURSALES;

EXEC sp_insertar_sucursal ('Sucursal San José', '2222-2222', 'San José, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Alajuela', '3333-3333', 'Alajuela, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Heredia', '4444-4444', 'Heredia, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Cartago', '5555-5555', 'Cartago, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Guanacaste', '6666-6666', 'Guanacaste, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Puntarenas', '7777-7777', 'Puntarenas, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Limón', '8888-8888', 'Limón, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal San Carlos', '9999-9999', 'San Carlos, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Desamparados', '1010-1010', 'Desamparados, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Escazú', '1111-1111', 'Escazú, Costa Rica');

EXEC sp_insertar_sucursal ('Sucursal Tibás', '1212-1212', 'Tibás, Costa Rica');

-------------------------------------------------------------------------------------------------------
DELETE FROM CATEGORIA;
TRUNCATE TABLE CATEGORIA;

EXEC sp_insertar_categoria ('Hardware', 'Productos físicos como placas base, procesadores, tarjetas gráficas, discos duros, etc.');

EXEC sp_insertar_categoria ('Software', 'Programas, sistemas operativos, aplicaciones, etc.');

EXEC sp_insertar_categoria ('Periféricos', 'Dispositivos externos como teclados, ratones, monitores, impresoras, etc.');

EXEC sp_insertar_categoria ('Accesorios', 'Productos adicionales como cables, adaptadores, ventiladores, fuentes de poder, etc.');

-------------------------------------------------------------------------------------------------------------------------------------------
DELETE FROM PRODUCTOS;
TRUNCATE TABLE PRODUCTOS;

EXEC sp_insertar_producto ('Placa madre ASUS ROG Strix Z390-E Gaming', 'Placa madre de alta gama para procesadores Intel', 450.99, 20, 1, 'Disponible');

EXEC sp_insertar_producto ('Procesador Intel Core i9-11900K', 'Procesador de gama alta para gaming y aplicaciones exigentes', 619.99, 15, 1, 'Disponible');

EXEC sp_insertar_producto ('Tarjeta gráfica NVIDIA GeForce RTX 3080', 'Tarjeta gráfica de última generación para gaming y renderizado', 1199.99, 10, 1, 'Agotado');

EXEC sp_insertar_producto ('Microsoft Windows 10 Pro', 'Sistema operativo de Microsoft para usuarios profesionales', 199.99, 50, 2, 'Disponible');

EXEC sp_insertar_producto ('Adobe Photoshop CC 2022', 'Software de edición de imágenes y diseño gráfico', 20.99, 100, 2, 'Disponible');

EXEC sp_insertar_producto ('Teclado mecánico Corsair K100 RGB', 'Teclado mecánico con retroiluminación LED RGB', 199.99, 25, 3, 'Disponible');

EXEC sp_insertar_producto ('Monitor ASUS TUF Gaming VG279QM', 'Monitor gaming de alta frecuencia de actualización', 399.99, 15, 3, 'Disponible');

EXEC sp_insertar_producto ('Cable HDMI 2.1 de 2 metros', 'Cable HDMI de alta velocidad y ancho de banda para video y audio', 14.99, 100, 4, 'Disponible');

EXEC sp_insertar_producto ('Fuente de poder modular Corsair RM850x', 'Fuente de poder con certificación 80 PLUS Gold y cableado modular', 179.99, 20, 4, 'Disponible');

EXEC sp_insertar_producto ('Mouse gamer Logitech G502 HERO', 'Mouse gaming con sensor óptico avanzado y pesos ajustables', 79.99, 30, 3, 'Disponible');

EXEC sp_insertar_producto ('Auriculares inalámbricos Sony WH-1000XM4', 'Auriculares con cancelación de ruido y alta calidad de sonido', 349.99, 10, 3, 'Disponible');

EXEC sp_insertar_producto ('Router Wi-Fi ASUS RT-AX86U', 'Router Wi-Fi de alta velocidad y cobertura para gaming y streaming', 259.99, 5, 1, 'Disponible');

EXEC sp_insertar_producto ('Disco duro externo Western Digital Passport 4 TB', 'Disco duro externo portátil con conexión USB 3.0 y 4 TB de capacidad', 119.99, 8, 1, 'Disponible');

EXEC sp_insertar_producto ('Proyector BenQ MH733', 'Proyector de alta resolución y brillo para presentaciones y cine en casa', 699.99, 3, 2, 'Disponible');

EXEC sp_insertar_producto ('Impresora láser HP Color LaserJet Pro MFP M277dw', 'Impresora multifunción láser con conexión Wi-Fi y NFC', 399.99, 6, 2, 'Disponible');

EXEC sp_insertar_producto ('Mochila para laptop SwissGear SA1923', 'Mochila para laptop con compartimentos acolchados y resistentes al agua', 79.99, 20, 4, 'Disponible');

EXEC sp_insertar_producto ('Teclado mecánico Corsair K95 RGB Platinum XT', 'Teclado gaming mecánico con retroiluminación RGB y teclas programables', 199.99, 15, 3, 'Disponible');

EXEC sp_insertar_producto ('Monitor gaming Alienware AW3418DW', 'Monitor ultrawide para gaming con resolución WQHD y tasa de refresco de 120 Hz', 999.99, 5, 2, 'Disponible');

EXEC sp_insertar_producto ('Laptop MSI GS65 Stealth Thin', 'Laptop gaming delgada y ligera con procesador Intel Core i7 y tarjeta gráfica NVIDIA', 1699.99, 3, 4, 'Disponible');

EXEC sp_insertar_producto ('Altavoces Bluetooth Bose SoundLink Revolve', 'Altavoces portátiles con sonido de 360 grados y conectividad Bluetooth', 199.99, 10, 3, 'Disponible');

EXEC sp_insertar_producto ('Cámara fotográfica Sony Alpha a7 III', 'Cámara mirrorless con sensor de fotograma completo y enfoque automático de alta velocidad', 1999.99, 2, 2, 'Disponible');

EXEC sp_insertar_producto ('Tablet Apple iPad Pro de 12,9 pulgadas', 'Tablet con pantalla Retina y procesador A12X Bionic', 999.99, 7, 4, 'Disponible');

EXEC sp_insertar_producto ('Smartwatch Garmin Forerunner 945', 'Reloj deportivo con GPS, sensor de frecuencia cardíaca y funciones avanzadas de entrenamiento', 599.99, 5, 4, 'Disponible');

EXEC sp_insertar_producto ('Kit de realidad virtual Oculus Quest 2', 'Sistema de realidad virtual inalámbrico con controladores Touch y gráficos de alta resolución', 399.99, 4, 2, 'Disponible');

EXEC sp_insertar_producto ('Procesador Intel Core i9-11900K', 'Procesador de 11ª generación para desktop con 8 núcleos y 16 hilos', 599.99, 8, 1, 'Disponible');

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
DELETE FROM FACTURAS;
TRUNCATE TABLE FACTURAS;

EXEC sp_insertar_factura (2, 2, 8, TO_DATE('2023/04/16', 'yyyy/mm/dd'), 250.99);

EXEC sp_insertar_factura (5, 8, 5, TO_DATE('2023/04/15', 'yyyy/mm/dd'), 599.99);

EXEC sp_insertar_factura (12, 11, 11, TO_DATE('2023/04/14', 'yyyy/mm/dd'), 129.99);

EXEC sp_insertar_factura (1, 1, 18, TO_DATE('2023/04/13', 'yyyy/mm/dd'), 299.99);

EXEC sp_insertar_factura (8, 16, 4, TO_DATE('2023/04/12', 'yyyy/mm/dd'), 159.99);

EXEC sp_insertar_factura (3, 3, 16, TO_DATE('2023/04/11', 'yyyy/mm/dd'), 99.99);

EXEC sp_insertar_factura (13, 19, 6, TO_DATE('2023/04/10', 'yyyy/mm/dd'), 599.99);

EXEC sp_insertar_factura (7, 26, 3, TO_DATE('2023/04/09', 'yyyy/mm/dd'), 1199.99);

EXEC sp_insertar_factura (15, 24, 12, TO_DATE('2023/04/08', 'yyyy/mm/dd'), 499.99);

EXEC sp_insertar_factura (4, 27, 9, TO_DATE('2023/04/07', 'yyyy/mm/dd'), 239.99);

EXEC sp_insertar_factura (5, 1, 10, TO_DATE('2022-02-01', 'YYYY-MM-DD'), 1500);

EXEC sp_insertar_factura (6, 2, 11, TO_DATE('2022-02-02', 'YYYY-MM-DD'), 2000);

EXEC sp_insertar_factura (7, 3, 12, TO_DATE('2022-02-03', 'YYYY-MM-DD'), 2500);

EXEC sp_insertar_factura (8, 4, 13, TO_DATE('2022-02-04', 'YYYY-MM-DD'), 3000);

EXEC sp_insertar_factura (9, 5, 14, TO_DATE('2022-02-05', 'YYYY-MM-DD'), 3500);

EXEC sp_insertar_factura (6, 15, TO_DATE('2022-02-06', 'YYYY-MM-DD'), 4000);

EXEC sp_insertar_factura (11, 7, 16, TO_DATE('2022-02-07', 'YYYY-MM-DD'), 4500);

EXEC sp_insertar_factura (12, 8, 17, TO_DATE('2022-02-08', 'YYYY-MM-DD'), 5000);

EXEC sp_insertar_factura (13, 9, 18, TO_DATE('2022-02-09', 'YYYY-MM-DD'), 5500);

EXEC sp_insertar_factura (14, 26, 6, TO_DATE('2022-02-10', 'YYYY-MM-DD'), 6000);
------------------------------------------------------------------------------------------------------------------------------
DELETE FROM DEVOLUCIONES;
TRUNCATE TABLE DEVOLUCIONES;

EXEC sp_insertar_devolucion (TO_DATE('2022-01-01', 'YYYY-MM-DD'), 5, 10, 3, 50.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-02', 'YYYY-MM-DD'), 12, 18, 7, 25.50);

EXEC sp_insertar_devolucion (TO_DATE('2022-03-03', 'YYYY-MM-DD'), 4, 4, 6, 10.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-04-04', 'YYYY-MM-DD'), 8, 21, 9, 75.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-05-05', 'YYYY-MM-DD'), 16, 5, 15, 12.99);

EXEC sp_insertar_devolucion (TO_DATE('2022-06-06', 'YYYY-MM-DD'), 3, 1, 4, 50.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-07-07', 'YYYY-MM-DD'), 14, 12, 10, 35.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-08-08', 'YYYY-MM-DD'), 6, 7, 5, 20.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-09-09', 'YYYY-MM-DD'), 11, 24, 19, 100.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-10-10', 'YYYY-MM-DD'), 7, 9, 3, 30.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-01', 'YYYY-MM-DD'), 10, 8, 11, 50.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-02', 'YYYY-MM-DD'), 14, 12, 17, 80.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-05', 'YYYY-MM-DD'), 9, 5, 10, 20.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-06', 'YYYY-MM-DD'), 3, 3, 6, 30.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-10', 'YYYY-MM-DD'), 8, 2, 4, 15.00);

EXEC sp_insertar_devolucion (TO_DATE('2022-02-12', 'YYYY-MM-DD'), 7, 20, 14, 100.00);

