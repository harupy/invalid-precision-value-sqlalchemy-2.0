CREATE DATABASE testdb;
GO

USE testdb;

CREATE LOGIN testuser
    WITH PASSWORD = 'Test*password1';
GO

CREATE USER testuser FOR LOGIN testuser;
GO

ALTER ROLE db_owner
    ADD MEMBER testuser;
GO
