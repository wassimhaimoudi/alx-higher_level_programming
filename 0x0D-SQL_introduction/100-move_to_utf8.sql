-- This script converts hbtn_0c_0 database to UFT8 (uft8mb4, collate uft8b4_unicode_ci) in your mySQL server.
-- Compounents to be converted:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
