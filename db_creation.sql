create table usuario (
	cod_usuario int primary key,
	handle varchar(255),
	id_discord bigint,
	id_telegram bigint
);

create table meme (
	cod_meme int primary key,
	texto_meme varchar(2048)
);

create table caga_pau (
	contagem int primary key
);

insert into caga_pau values(45);

create or replace function getNextCodMeme() returns trigger as
$$
declare
	last_meme int default 0;
	qtd_meme int default 0;
begin
	qtd_meme := (select count(*) from meme);
	if qtd_meme > 0 then
		last_meme := (select max(cod_meme) from meme);
	new.cod_meme := last_meme+1;
	return new;
end;
$$
language plpgsql;

drop trigger if exists getNextCodMeme on meme;
create trigger getNextCodMeme before insert on meme
for each row execute procedure getNextCodMeme();
