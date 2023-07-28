const pool = require('./dbConfig');
const bcrypt = require('bcrypt');

const username = 'exampleUser';
const password = 'examplePassword';
const hashedPassword = bcrypt.hashSync(password, 10);

pool.query(`
  INSERT INTO users (username, hashedPassword)
  VALUES ($1, $2);
`, [username, hashedPassword], (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('User registered successfully');
  }
});
