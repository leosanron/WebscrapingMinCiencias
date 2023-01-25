select grupos -> 'G' ->> 'Nombre' AS nombre_del_grupo
from ctei
where  grupos -> 'G' ->> 'Nombre' like '%Grupo%'
and id between 5000 and 5100
limit 40;