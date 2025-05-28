--liquibase formatted sql
--changeset "Rick Haffey":"0001"
--comment Set up opentelemetry access

create user opentelemetry WITH
    password 'opentelemetry'
    NOCREATEDB
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    NOBYPASSRLS
;

grant select on pg_stat_database to opentelemetry;
grant pg_monitor to opentelemetry;

create extension if not exists pg_stat_statements;

alter user opentelemetry set search_path to opentelemetry,public,pg_catalog;

--rollback drop user if exists opentelemetry;
--rollback drop extension if exists pg_stat_statements;
