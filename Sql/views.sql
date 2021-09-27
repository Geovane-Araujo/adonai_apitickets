--view cidades
create view vw_cidades as
select cidades.id,cidades.nome,estados.uf
from cidades
	inner join estados on estados.codigouf = cidades.idestado