Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (3,'Tarjetas Graficas','categorias/grafica-cat.jpg');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (4,'Memorias Ram','categorias/ram-cat.webp');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (5,'Unidades de Almacenamiento','categorias/disk-cat.jpg');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (6,'Fuentes de Poder','categorias/fuente-cat.webp');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (1,'Procesadores','categorias/procesador-cat.webp');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (2,'Placas Madre','categorias/placamadre-cat.jpg');
Insert into CORE_CATEGORIA (ID,NOMBRE,IMAGEN) values (61,'Gabinetes','categorias/gabinete-cat_H10vzna.webp');

Insert into CORE_MARCA (ID,NOMBRE) values (1,'Intel');
Insert into CORE_MARCA (ID,NOMBRE) values (2,'GIGABYTE');
Insert into CORE_MARCA (ID,NOMBRE) values (41,'Kingston');
Insert into CORE_MARCA (ID,NOMBRE) values (42,'ASUS');

Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (41,'ASUS ProArt PA401 Wood Edition','Gabinete ASUS ProArt PA401 Wood Edition, Vidrio Templado, 2x 160mm, 1x 120mm, ATX, Black',129990,2,61,42,'productos/gabinete-asus.png');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (2,'GIGABYTE B650M','Placa Madre GIGABYTE B650M GAMING WIFI, Socket AM5, 2x DDR5, Wi-Fi, Micro-ATX',149990,3,2,2,'productos/placa-amd.png');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (4,'Intel Core i5-12400','Procesador Intel Core i5-12400, 2.5GHz Turbo 4.4GHz, Socket LGA 1700, 6-Core / 12-Threads',299990,5,1,1,'productos/inteli5_Ufcfs9N.jpeg');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (21,'GIGABYTE NVIDIA GeForce RTX 5060','Tarjeta de Video GIGABYTE NVIDIA GeForce RTX 5060 EAGLE OC, 8GB GDDR7, 128-bit, PCI-e 5.0 x8',374990,3,3,2,'productos/video-nvidia.png');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (22,'Kingston Fury Beast 8GB','Memoria RAM DDR4 8GB 3200MT/s Kingston Fury Beast RGB, CL16, DIMM, 1.35V',31990,6,4,41,'productos/ram-fury.jpg');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (23,'Kingston NV3','Unidad SSD Kingston NV3, 1TB, M.2 2280, NVMePCIe 4.0 x4, Lectura 6000MB/s Escritura 4000MB/s',64990,2,5,41,'productos/ssd-kingston.jpg');
Insert into CORE_PRODUCTO (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,CATEGORIA_ID,MARCA_ID,IMAGEN) values (24,'Gigabyte GP-P750BS','Fuente de Poder 750W Gigabyte GP-P750BS, 80 PLUS Bronze, ATX, Color Negro',69990,4,6,2,'productos/fuente-giga.png');

commit;