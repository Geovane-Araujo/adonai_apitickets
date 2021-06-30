create database adonais1_tickets_0;

create table if not exists pessoa(

	id int AUTO_INCREMENT,
	nome varchar(100),
	foto LONGTEXT,
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
	idusuario int
);

create table if not exists pessoa_clientes(

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

create table if not exists cidades(

	id int AUTO_INCREMENT primary key,
	nome varcahr(160),
	idestado int
);

create table if not exists estados(

	id int AUTO_INCREMENT primary key,
	nome varchar(50),
	uf varchar(2)
);


alter table pessoa_usuario add constraint fk_pessoa_usuario_pessoa foreign key (idpessoa) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_pessoa_usuario foreign key (idatendente) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_pessoa_cliente foreign key (idcliente) references pessoa(id);
alter table atendimentos add constraint fk_atendimentos_atendimento_status foreign key (idstatus) references atendimento_status(id);
alter table atendimento_anexos add constraint fk_atendimento_anexos_atendimento foreign key (idatendimento) references atendimentos(id);
alter table atendimento_anexos add constraint fk_atendimento_anexos_pessoa_usuario foreign key (idusuario) references pessoa(id);
alter table pessoa_clientes add constraint fk_pessoa_clientes_pessoa foreign key (idpessoa) references pessoa(id);
alter table pessoa_endereco add constraint fk_pessoa_endereco_pessoa foreign key (idpessoa) references pessoa(id);
alter table pessoa_endereco add constraint fk_pessoa_endereco_cidades foreign key (idcidade) references cidades(id);
alter table cidades add constraint fk_cidades_estados foreign key (idestado) references estados(id);