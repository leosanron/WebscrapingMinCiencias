with data As (SELECT grupos->'G'->>'Nombre'as nombre,jsonb_each(grupos->'G'->'Artículos publicados') as "Articulos"
FROM ctei
where grupos->'G'->>'Artículos publicados'  like '%grupos%')

select * from data