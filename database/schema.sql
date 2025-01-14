CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    role VARCHAR(255),
    company VARCHAR(255),
    status VARCHAR(20)  -- "Yes", "No", or "Pending"
);

