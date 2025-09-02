CREATE DATABASE IF NOT EXISTS traderbot;
USE traderbot;
CREATE TABLE IF NOT EXISTS users (
  email VARCHAR(255) PRIMARY KEY,
  password VARCHAR(32),
  iq_email VARCHAR(255),
  iq_password VARCHAR(255)
  password VARCHAR(32)
);
