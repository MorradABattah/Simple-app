const { Pool } = require('pg');

const pool = new Pool({
  user: 'jenkins',
  host: 'localhost',
  database: 'jenkins',
  password: 'jenkins',
  port: 5432,
});

module.exports = pool;
