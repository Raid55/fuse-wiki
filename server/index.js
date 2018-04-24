const server = require('./app');
// env vars
const { PORT, ADDRESS } = require('./config');
// db imports
const db = require('./models');


db.sequelize.sync().then((err) => {
    server.listen(PORT, () => {
        console.log(`Web server starting...`);
        console.log(`App listening at ${ADDRESS}:${PORT}`);
        console.log('...\n');
    });
});
