const { Pool } = require('pg');

const pool = new Pool({
  user: 'jenkins',
  host: '3.141.10.82',
  database: 'jenkins',
  password: 'jenkins',
  port: 5432,
});

module.exports = pool;
