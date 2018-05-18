CREATE TABLE Imagens (
 imagem varchar(45),
 PRIMARY KEY(imagem)
 );

CREATE TABLE Usuario (
 idUser integer,
 PRIMARY KEY (idUser),
 nomeUser varchar(45),
 emailUser varchar(45),
 cpfUser varchar(45),
 contatoUser varchar(45),
 senhaUser varchar(6),
 imagem varchar(45) REFERENCES Imagens(imagem));

 CREATE TABLE CampanhasPerdidos (
 idCampanhasPerdidos integer,
 PRIMARY KEY(idCampanhasPerdidos),
 idUser integer REFERENCES Usuario (idUser),
 statusCampanhasPerdidos varchar(45),
 dataNascimento date,
 nomeDesaparecido varchar(45),
 idadeDesaparecido varchar(45),
 sexoDesaparecido varchar(45),
 olhosDesaparecido varchar(45),
 racaDesaparecido varchar(45),
 cabeloDesaparecido varchar(45),
 dataDesaparecimento date,
 dataCampanha date,
 bo varchar(45),
 descricao varchar(165)
 );

  CREATE TABLE AttLocalizacaoCampanhasPerdidos (
 idCampanhasPerdidos integer REFERENCES CampanhasPerdidos(idCampanhasPerdidos),
 longitude integer,
 latitude integer,
 PRIMARY KEY(idCampanhasPerdidos, longitude, latitude),
 attData date,
 attBairro varchar(45)
 );
	 
 CREATE TABLE CampanhasPerdidos_Imagens (
 idCampanhasPerdidos integer REFERENCES CampanhasPerdidos(idCampanhasPerdidos),
 imagem varchar(45) REFERENCES Imagens(imagem),
 PRIMARY KEY(idCampanhasPerdidos, imagem)
 );
 
 CREATE TABLE Notificacoes (
 idNotificacao integer,
 idUsuario integer REFERENCES Usuario(idUser),
 idCampanhasPerdidos integer REFERENCES CampanhasPerdidos(idCampanhasPerdidos),
 descricao varchar(165),
 dataAtt date,
 PRIMARY KEY(idNotificacao)
 );
 
 CREATE TABLE CampanhasSalvas (
 idUsuario integer REFERENCES Usuario(idUser),
 idCampanhasPerdidos integer REFERENCES CampanhasPerdidos(idCampanhasPerdidos),
 PRIMARY KEY(idUsuario, idCampanhasPerdidos)
 );
 
	 
