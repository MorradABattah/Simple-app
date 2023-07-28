const pool = require('./dbConfig');
const bcrypt = require('bcrypt');

const username = 'exampleUser';
const passwordAttempt = 'examplePassword';

pool.query(`
  SELECT hashedPassword
  FROM users
  WHERE username = $1;
`, [username], (err, results) => {
  if (err) {
    console.error(err);
  } else if (results.rows.length > 0) {
    const hashedPassword = results.rows[0].hashedpassword;

    if (bcrypt.compareSync(passwordAttempt, hashedPassword)) {
      console.log('Login successful');
    } else {
      console.log('Password incorrect');
    }
  } else {
    console.log('Username not found');
  }
});
