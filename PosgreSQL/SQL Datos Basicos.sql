select grupos -> 'G' ->> 'DatosBasicos' AS Datos_basicos
from ctei
where  grupos -> 'G' ->> 'Nombre' like '%Grupo%'
and id between 5000 and 5100
limit 40;