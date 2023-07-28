const pool = require('./dbConfig');

pool.query(`
  CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashedPassword VARCHAR(100) NOT NULL
  );
`, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Users table created successfully');
  }
});
