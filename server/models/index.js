const Sequelize = require('sequelize');
let sequelize = new Sequelize('sqlite:./fuse.sqlite');


module.exports = {
    // Sequelize
    Sequelize: Sequelize,
    sequelize: sequelize,
    // Models
    Links: sequelize.import(__dirname + '/links.js'),
    Pages: sequelize.import(__dirname + '/page.js'),
    Redirects: sequelize.import(__dirname + '/redirects.js')
}
