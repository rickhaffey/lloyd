--liquibase formatted sql
--changeset "Rick Haffey":"0001"
--comment Create table: foo

create table if not exists foo(
  id int,
  name varchar(50)
);

--rollback drop table if exists foo;
