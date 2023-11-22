-- Custom script for setting up the MySQL test environment for AirBnB_clone_v2 project

-- Create a new testing database with a unique name
CREATE DATABASE IF NOT EXISTS hbnb_clone_test_db;

-- Create a unique user for testing purposes
CREATE USER IF NOT EXISTS 'hbnb_clone_tester'@'localhost' IDENTIFIED BY 'clone_test_pwd';

-- Grant minimal necessary privileges to the test user on the test database
GRANT SELECT, INSERT, UPDATE, DELETE ON hbnb_clone_test_db.* TO 'hbnb_clone_tester'@'localhost';

-- Apply the privileges
FLUSH PRIVILEGES;
