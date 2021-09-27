create database adonais1_tickets_0;

create table if not exists pessoa(

	id int AUTO_INCREMENT,
	nome varchar(100),
	foto LONGTEXT,
    cnpjcpf varchar(14),
    rgie varchar(15),
    datanascimento date,
	constraint id_pessoa primary key (id)
);

create table if not exists pessoa_usuario(

	id int AUTO_INCREMENT primary key,
	login varchar(40),
	senha varchar(40),
	idpessoa int
);

create table if not exists atendimento_status(

	id int AUTO_INCREMENT primary key,
	descricao varchar(40)
);

create table if not exists atendimentos(

	id int AUTO_INCREMENT primary key,
	titulo varchar(70),
	idatendente int,
	idstatus int,
	datainicio TIMESTAMP,
	datafim TIMESTAMP,
	dataprevisao TIMESTAMP,
	idcliente int,
	descricao longtext
);

create table if not exists atendimento_anexos(

	id int AUTO_INCREMENT primary key,
	idatendimento int,
	datainclusao timestamp,
    descricao varchar(70),
	idusuario int
);

create table if not exists pessoa_clientes(

	id int AUTO_INCREMENT primary key,
	idpessoa int,
	fantasia varchar(70)
);

create table if not exists pessoa_empresa(

	id int AUTO_INCREMENT primary key,
	idpessoa int,
	fantasia varchar(70)
);

create table if not exists pessoa_endereco(

	id int AUTO_INCREMENT primary key,
	endereco varchar(160),
	bairro varchar(70),
	complemento varchar(70),
	numero varchar(12),
	cep varchar(8),
	idcidade int,
	idpessoa int
);

create table if not exists pessoa_telefone(

	id int AUTO_INCREMENT primary key,
	idpessoa int,
	fone varchar(14),
    tipo int
);

create table if not exists pessoa_email(

	id int AUTO_INCREMENT primary key,
	idpessoa int,
	email varchar(14),
    tipo int
);

create table if not exists cidades(

    id int AUTO_INCREMENT primary key,
    idestado int,
    ibge int,
    nome varchar(70)
);

create table if not exists estados(

    id int AUTO_INCREMENT primary key,
    nome varchar(50),
    codigouf int UNIQUE,
    uf char(2),
    regiao int
);

create table dynamic(

    id int AUTO_INCREMENT primary key,
    route varchar(70),
    query text,
    tablebase varchar(70)
);


alter table pessoa_usuario add constraint fk_pessoa_usuario_pessoa foreign key (idpessoa) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_pessoa_usuario foreign key (idatendente) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_pessoa_cliente foreign key (idcliente) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_atendimento_status foreign key (idstatus) references atendimento_status(id);
alter table atendimento_anexos add constraint fk_atendimento_anexos_atendimento foreign key (idatendimento) references atendimentos(id);
alter table atendimento_anexos add constraint fk_atendimento_anexos_pessoa_usuario foreign key (idusuario) references pessoa(id);
alter table pessoa_clientes add constraint fk_pessoa_clientes_pessoa foreign key (idpessoa) references pessoa(id);
alter table pessoa_empresa add constraint fk_pessoa_empresa_pessoa foreign key (idpessoa) references pessoa(id);
alter table pessoa_endereco add constraint fk_pessoa_endereco_pessoa foreign key (idpessoa) references pessoa(id);
alter table pessoa_endereco add constraint fk_pessoa_endereco_cidades foreign key (idcidade) references cidades(id);
alter table cidades add constraint fk_cidades_estados foreign key (idestado) references estados(CodigoUf);
alter table pessoa_telefone add constraint fk_pessoa_telefone foreign key (idpessoa) references pessoa(id);
alter table pessoa_email add constraint fk_pessoa_email foreign key (idpessoa) references pessoa(id);


insert into pessoa(id,nome) values(-10,'Administrador');
insert into pessoa_usuario values(0,'admin','1234',-10);
insert into pessoa(id, nome,cnpjcpf) values(0,'Empresa Padrão','00000000000000');
insert into pessoa_empresa(idpessoa,fantasia) values(1,'Empresa Padrão');


CREATE USER 'adonais1_admin'@'localhost' IDENTIFIED BY 'Adonai1816';
GRANT ALL PRIVILEGES ON * . * TO 'adonais1_admin'@'localhost';