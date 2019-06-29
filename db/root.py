from config import *
import psycopg2

conn = psycopg2.connect(database="db_zoldyck",user="postgres",password="user56",port=5432)
cur = conn.cursor()

sql = """
insert into "DEPARTAMENTO" (codigo, rut_jefe, area) values (1, '9290307145', 'Business Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (2, '8312881115', 'Accounting');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (3, '7152677409', 'Services');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (4, '9072631196', 'Business Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (5, '9792643699', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (6, '5777061184', 'Research and Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (7, '1163553417', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (8, '4967462448', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (9, '8802202710', 'Engineering');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (10, '584123669', 'Marketing');
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Voyatouch', 'Horror|Mystery|Thriller', 1, 1, 5, 1992, 100000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Latlux', 'Drama|Romance', 2, 2, 7, 1998, 200000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Domainer', 'Drama|Western', 3, 3, 5, 2009, 300000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Flexidy', 'Drama', 4, 4, 6, 1994, 250000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Quo Lux', 'Comedy|Romance', 5, 5, 8, 2012, 590000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Greenlam', 'Romance', 6, 6, 2, 2011, 500000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Flowdesk', 'Comedy', 7, 7, 10, 2001, 200000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Y-find', 'Crime|Horror|Thriller', 8, 8, 10, 1995, 50000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Alphazap', 'Comedy|Drama', 9, 9, 2, 2009, 273000);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento, precio) values ('Stringtough', 'Horror|Thriller', 10, 10, 1, 2000, 846500);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Halvorson, Cremin and Buckridge', 'SE', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Wilkinson-Nicolas', 'FR', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Rogahn Inc', 'MY', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Ratke Inc', 'ID', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Powlowski, Feil and Windler', 'GR', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Ruecker, Brakus and Dicki', 'PT', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Cremin LLC', 'FR', true);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Lesch Group', 'KP', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Toy LLC', 'CN', false);
insert into DISTRIBUIDORA (nombre, ubicacion, estado_contrato) values ('Hessel, Schoen and Pouros', 'JM', true);
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('8409607700', 'Sherwood', 'Sales Associate', '$822.33', '58118-2081');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9337276429', 'Rhodie', 'Staff Accountant III', '$236.82', '42937-703');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('7450977141', 'Anne-marie', 'GIS Technical Architect', '$725.02', '0363-0130');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('9246575792', 'Frankie', 'Biostatistician I', '$386.18', '43199-020');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('2987950659', 'Benjie', 'Analog Circuit Design manager', '$660.20', '57664-371');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('6494021190', 'Bronson', 'Speech Pathologist', '$246.13', '63481-435');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4790508277', 'Teddie', 'Physical Therapy Assistant', '$767.69', '51532-5400');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4058619708', 'Sanford', 'Senior Sales Associate', '$207.67', '62032-119');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('4735243070', 'Katha', 'Budget/Accounting Analyst II', '$621.92', '0378-3404');
insert into EMPLEADO (rut, nombre, profesion, sueldo, codigo_oficina) values ('1469973960', 'Zaneta', 'Structural Analysis Engineer', '$825.49', '53808-0257');
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('8409607700', 1);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9337276429', 2);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('7450977141', 3);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('9246575792', 4);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('2987950659', 5);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('6494021190', 6);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4790508277', 7);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4058619708', 8);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('4735243070', 9);
insert into TRABAJAN (rut_empleado, codigo_departamento) values ('1469973960', 10);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Powlowski, Feil and Windler', 'Quo Lux', 18, 5, 1995);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Ruecker, Brakus and Dicki', 'Greenlam', 2, 6, 2001);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Rogahn Inc', 'Y-find', 7, 7, 2010);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Lesch Group', 'Greenlam', 10, 10, 2005);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Lesch Group', 'Voyatouch', 9, 12, 2000);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Toy LLC', 'Y-find', 21, 1, 1998);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Toy LLC', 'Voyatouch', 13, 5, 2013);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Hessel, Schoen and Pouros', 'Flowdesk', 20, 4, 2017);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Toy LLC', 'Voyatouch', 27, 2, 2011);
insert into COMPRAN (nombre_distribuidora, nombre_videojuego, dia_compra, mes_compra, año_compra) values ('Toy LLC', 'Quo Lux', 26, 11, 1994);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('1469973960', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('9246575792', 'Voyatouch', 25, 4, 1992);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('4735243070', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('4058619708', 'Greenlam', 1, 1, 2011);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('6494021190', 'Y-find', 8, 9, 1995);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('2987950659', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('8409607700', 'Quo Lux', 25, 7, 2012);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('7450977141', 'Voyatouch', 25, 4, 1992);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('9337276429', 'Voyatouch', 25, 4, 1992);
insert into PRODUCEN (rut_empleado, nombre_videojuego, dia_plazo, mes_plazo, año_plazo) values('4790508277', 'Y-find', 8, 9, 1995);


"""
cur.execute(sql)

conn.commit()

cur.close()
conn.close()
