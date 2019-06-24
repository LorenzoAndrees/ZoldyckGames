from config import *
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(db_zoldyck,postgres,user56))
cur = conn.cursor()

sql = """
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (1, '9290307145', 'Business Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (2, '8312881115', 'Accounting');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (3, '7152677409', 'Services');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (4, '9072631196', 'Business Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (5, '9792643699', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (6, '5777061184', 'Research and Development');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (7, '1163553417', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (8, '4967462448', 'Training');
insert into DEPARTAMENTO (codigo, rut_jefe, area) values (9, '8802202710', 'Engineering');
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Voyatouch', 'Horror|Mystery|Thriller', 1, 1, '1709779586', 1992);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Latlux', 'Drama|Romance', 2, 2, '9893403618', 1998);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Domainer', 'Drama|Western', 3, 3, '6914885583', 2009);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Flexidy', 'Drama', 4, 4, '2163947181', 1994);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Quo Lux', 'Comedy|Romance', 5, 5, '2767111771', 2012);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Greenlam', 'Romance', 6, 6, '6944085003', 2011);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Flowdesk', 'Comedy', 7, 7, '5607306666', 2001);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Y-find', 'Crime|Horror|Thriller', 8, 8, '5168188222', 1995);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Alphazap', 'Comedy|Drama', 9, 9, '9975945694', 2009);
insert into VIDEOJUEGO (nombre, genero, plataforma, dia_lanzamiento, mes_lanzamiento, año_lanzamiento) values ('Stringtough', 'Horror|Thriller', 10, 10, '7726426381', 2000);
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
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('8409607700', 'Sherwood', 'Sales Associate', '$822.33', '58118-2081');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('9337276429', 'Rhodie', 'Staff Accountant III', '$236.82', '42937-703');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('7450977141', 'Anne-marie', 'GIS Technical Architect', '$725.02', '0363-0130');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('9246575792', 'Frankie', 'Biostatistician I', '$386.18', '43199-020');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('2987950659', 'Benjie', 'Analog Circuit Design manager', '$660.20', '57664-371');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('6494021190', 'Bronson', 'Speech Pathologist', '$246.13', '63481-435');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('4790508277', 'Teddie', 'Physical Therapy Assistant', '$767.69', '51532-5400');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('4058619708', 'Sanford', 'Senior Sales Associate', '$207.67', '62032-119');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('4735243070', 'Katha', 'Budget/Accounting Analyst II', '$621.92', '0378-3404');
insert into MOCK_DATA (rut, nombre, profesion, sueldo, codigo_oficina) values ('1469973960', 'Zaneta', 'Structural Analysis Engineer', '$825.49', '53808-0257');
"""
cur.execute(sql)

conn.commit()

cur.close()
conn.close()
