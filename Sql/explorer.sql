--menu cliente
insert into dynamic(route, query,tablebase) values('mnu_cliente','select pessoa.id,
	   pessoa.nome,
       pessoa_endereco.endereco,
       pessoa_endereco.bairro,
       pessoa_endereco.numero,
       cidades.nome,
       estados.uf
from pessoa_clientes
	inner join pessoa on pessoa.id = pessoa_clientes.idpessoa
    inner join pessoa_endereco on pessoa.id = pessoa_endereco.idpessoa
    inner join cidades on pessoa_endereco.idcidade = cidades.id
    inner join estados on cidades.idestado = estados.id
','pessoa_clientes')
--expl cidade

insert into dynamic(route, query,tablebase) values('expl_cidades','select * from vw_cidades','vw_cidades')

