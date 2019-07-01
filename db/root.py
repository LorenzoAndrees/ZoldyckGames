from config import *
import psycopg2
conn = psycopg2.connect(
            host = "localhost",
            database = "db_zoldyck",
            user = "postgres",
            password = "user56")

cur = conn.cursor()

sql="""
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (1, '9290307145', 'Diseño');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (2, '8312881115', 'Game Tester');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (3, '7152677409', 'Marketing');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (4, '5777061184', 'Producción');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (5, '9792643699', 'Programación');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (6, '5777061184', 'Traducción');
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Voyatouch', 'MULTIPLATAFORMA', 'Simulación', 25, 5, 2009, 100000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Latlux', 'MULTIPLATAFORMA', 'Acción', 12, 9, 2019, 200000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Domainer', 'SWITCH', 'Disparos', 1, 7, 2017, 300000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Flexidy', 'PC', 'Sigilo', 21, 6, 2019, 250000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Quo Lux', 'PS4', 'Estrategia', 25, 8, 2012, 590000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Greenlam', 'SWITCH', 'Plataformas', 1, 2, 2011, 500000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Flowdesk', 'MULTIPLATAFORMA', 'Battle Royale', 2, 6, 2013, 200000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Y-find', 'MULTIPLATAFORMA','Carreras', 8, 10, 2011, 50000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Alphazap', 'PC', 'Survival Horror', 22, 10, 2008, 273000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Stringtough', 'PS4', 'Rol', 31, 6, 2015, 846500);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Digrod', 'SWITCH', 'Simulación', 13, 8, 2013, 100000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Nitronicle', 'XBOX ONE', 'Acción', 21, 5, 2004, 200000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Junctice', 'PC', 'Disparos', 7, 10, 2013, 300000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Boval', 'PS4', 'Sigilo', 2, 2, 2019, 250000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Visalum', 'SWITCH', 'Estrategia', 22, 8, 2013, 590000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Nash', 'MULTIPLATAFORMA', 'Plataformas', 9, 9, 2018, 500000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Dotone', 'PS4', 'Battle Royale', 6, 2, 2012, 200000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Panvet', 'SWITCH', 'Carreras', 18, 4, 2014, 50000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Tot', 'PS4', 'Survival Horror', 25, 5, 2007, 273000);
insert into VIDEOJUEGO (nombre, plataforma, genero, dia_lanzamiento, mes_lanzamiento, anio_lanzamiento, precio) values ('Lansite', 'MULTIPLATAFORMA', 'Rol', 8, 4, 2010, 846500);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Electronic Arts', 'US', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Valve', 'US', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Sony Interactive Entertainment', 'US', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Xbox Game Studios', 'US', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Nintendo', 'JP', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Ubisoft', 'FR', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Konami', 'JP', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('SEGA', 'JP', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('505 Games', 'IT', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Capcom', 'JP', true);
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('8409607700', 'Sherwood', 'Sales Associate', 822, '58118-2081');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9337276429', 'Rhodie', 'Staff Accountant III', 789, '42937-703');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('7450977141', 'Anne-marie', 'GIS Technical Architect', 725, '0363-0130');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9246575792', 'Frankie', 'Biostatistician I', 560, '43199-020');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('2987950659', 'Benjie', 'Analog Circuit Design manager', 660, '57664-371');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('6494021190', 'Bronson', 'Speech Pathologist', 578, '63481-435');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4790508277', 'Teddie', 'Physical Therapy Assistant', 767, '51532-5400');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4058619708', 'Sanford', 'Senior Sales Associate', 807, '62032-119');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4735243070', 'Katha', 'Budget/Accounting Analyst II', 470, '0378-3404');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('1469973960', 'Zaneta', 'Structural Analysis Engineer', 825, '53808-0257');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('8409477700', 'Finley', 'Sales Associate', 865, '58118-2081');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9338376429', 'Gunner', 'Staff Accountant III', 543, '42937-703');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('6850977141', 'Jakob', 'GIS Technical Architect', 749, '0363-0130');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9290575792', 'Alvin', 'Biostatistician I', 686, '43199-020');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('2952950659', 'Josue', 'Analog Circuit Design manager', 688, '57664-371');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('6491121190', 'Darian', 'Speech Pathologist', 946, '63481-435');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4798808277', 'Misael', 'Physical Therapy Assistant', 467, '51532-5400');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4058609708', 'Emmanuel', 'Senior Sales Associate', 707, '62032-119');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4735243160', 'Damaris', 'Budget/Accounting Analyst II', 621, '0378-3404');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('1469973560', 'Eve', 'Structural Analysis Engineer', 815, '53808-0257');
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('8409607700', 1);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9337276429', 2);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('7450977141', 3);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9246575792', 4);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('2987950659', 5);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('6494021190', 6);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4790508277', 1);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4058619708', 2);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4735243070', 3);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('1469973960', 4);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('8409477700', 5);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9338376429', 6);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('6850977141', 1);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9290575792', 2);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('2952950659', 3);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('6491121190', 4);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4798808277', 5);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4058609708', 6);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4735243160', 1);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('1469973560', 2);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Electronic Arts', 'Quo Lux', 31, 8, 2012);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Valve', 'Junctice', 9, 10, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Sony Interactive Entertainment', 'Y-find', 10, 10, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Valve', 'Greenlam', 3, 2, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Electronic Arts', 'Digrod', 15, 8, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Ubisoft', 'Y-find', 12, 9, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Capcom', 'Digrod', 16, 8, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Xbox Game Studios', 'Flowdesk', 8, 6, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Nintendo', 'Voyatouch', 27, 5, 2009);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Konami', 'Quo Lux', 3, 9, 2012);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('505 Games', 'Visalum', 24, 8, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Ubisoft', 'Greenlam', 5, 2, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('505 Games', 'Y-find', 12, 9, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('SEGA', 'Greenlam', 6, 2, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Xbox Game Studios', 'Voyatouch', 28, 5, 2009);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Capcom', 'Y-find', 21, 1, 1998);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Electronic Arts', 'Voyatouch', 30, 5, 2009);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('SEGA', 'Flowdesk', 10, 6, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Valve', 'Tot', 27, 5, 2007);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, anio_compra) values ('Sony Interactive Entertainment', 'Lansite', 13, 4, 2010);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('1469973960', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9246575792', 'Voyatouch', 25, 4, 2009);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4735243070', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4058619708', 'Greenlam', 1, 1, 2011);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('6494021190', 'Y-find', 8, 9, 2011);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('2987950659', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('8409607700', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('7450977141', 'Voyatouch', 25, 4, 2009);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9337276429', 'Voyatouch', 25, 4, 2009);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4790508277', 'Y-find', 8, 9, 2011);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('1469973960', 'Digrod', 13, 7, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('8409477700', 'Nitronicle', 21, 4, 2004);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9338376429', 'Digrod', 13, 7, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('6850977141', 'Dotone', 6, 1, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9290575792', 'Junctice', 7, 9, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('2952950659', 'Junctice', 7, 9, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('6491121190', 'Visalum', 22, 7, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4798808277', 'Dotone', 6, 1, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4058609708', 'Tot', 25, 4, 2007);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4735243160', 'Lansite', 8, 3, 2010);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('8409477700', 'Flowdesk', 2, 5, 2013);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9246575792', 'Panvet', 18, 3, 2014);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('8409477700', 'Nash', 9, 8, 2018);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4790508277', 'Boval', 2, 1, 2019);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4058609708', 'Stringtough', 31, 5, 2015);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('1469973960', 'Alphazap', 22, 9, 2008);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('2987950659', 'Flexidy', 21, 5, 2019);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('9290575792', 'Domainer', 1, 6, 2017);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, anio_plazo) values('4798808277', 'Latlux', 12, 8, 2019);

"""
cur.execute(sql)
conn.commit()
cur.close()
conn.close()