CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    enabled BOOLEAN DEFAULT TRUE
);

INSERT INTO users (username, password, enabled) VALUES ('user', 'pass', TRUE);
INSERT INTO users (username, password, enabled) VALUES ('admin', 'admin123', TRUE);
