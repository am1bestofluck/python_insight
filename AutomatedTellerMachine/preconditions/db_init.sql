# sozdaem bazy
DROP SCHEMA IF EXISTS terminals;
CREATE SCHEMA `terminals`;
use `terminals`;

CREATE TABLE cards(id SERIAL, card_number CHAR(16),
	PRIMARY KEY(id));
CREATE TABLE card_balances (id SERIAL, card_id BIGINT UNSIGNED, balance DECIMAL(12,2),
	PRIMARY KEY(id),FOREIGN KEY (card_id) REFERENCES cards(id) );
CREATE TABLE pins(id SERIAL, card_id BIGINT UNSIGNED, pin BIGINT, 
	PRIMARY KEY(id),FOREIGN KEY (card_id) REFERENCES cards(id));
CREATE TABLE terminal_units (id SERIAL,number TINYINT, location TINYTEXT, balance DECIMAL(12,2), PRIMARY KEY(id));