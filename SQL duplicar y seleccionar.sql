CREATE TABLE cteii As select * FROM ctei;

select * FROM cteii;

create table ctei (id INT PRIMARY KEY,grupos jsonb not null);

select * FROM ctei;