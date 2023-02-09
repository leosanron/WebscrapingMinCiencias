select grupos -> 'G' ->> 'Nombre' AS nombre_del_grupo,
grupos -> 'G' ->> 'DatosBasicos' AS Datos_basicos
from ctei
where  grupos -> 'G' ->> 'Nombre' like '%Grupo%'
and id between 5000 and 5100
limit 40;

select grupos -> 'G' ->> 'Nombre' AS nombre_del_grupo,
grupos -> 'G' -> 'DatosBasicos' ->'Líder' AS Datos_basicos
from ctei
where  grupos -> 'G' ->> 'Nombre' like '%Grupo%'
and id between 5000 and 5100
limit 40;
