--liquibase formatted sql
--changeset "Rick Haffey":"0002"
--comment Seed table: recipes


insert into recipes (name) values
('Manhattan'),
('Martini'),
('Boston Cocktail'),
('Cuba Libre'),
('Margarita'),
('Bloody Mary'),
('Old Fashioned'),
('Bees Knees');

--rollback truncate table recipes;
