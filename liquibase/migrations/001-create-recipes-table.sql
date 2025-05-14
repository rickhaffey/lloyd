--liquibase formatted sql
--changeset "Rick Haffey":"0001"
--comment Create table: recipes

create table if not exists recipes(
  id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name varchar(255) NOT NULL
);

--rollback drop table if exists recipes;
