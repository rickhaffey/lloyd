--liquibase formatted sql
--changeset "Rick Haffey":"0002"
--comment Create user: lloyd_api

create user lloyd_api WITH
    password 'lloyd_api'
    nocreatedb
    nocreaterole
    noinherit
    noreplication
    nobypassrls
;

--rollback drop user if exists lloyd_api;
