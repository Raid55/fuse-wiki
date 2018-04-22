require('dotenv').config();

module.exports = {
  PORT: process.env.PORT || process.env.DEV_PORT || 3000,
  ADDRESS: process.env.ADDRESS || process.env.DEV_ADDRESS || "localhost"
};
