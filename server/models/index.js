// const Sequelize = require('sequelize');
// let sequelize = new Sequelize('sqlite:./fuse.sqlite');


// module.exports = {
//     // Sequelize
//     Sequelize: Sequelize,
//     sequelize: sequelize,
//     // Models
//     Links: sequelize.import(__dirname + '/links.js'),
//     Pages: sequelize.import(__dirname + '/page.js'),
//     Redirects: sequelize.import(__dirname + '/redirects.js')
// }

class db {
    constructor(Sequelize, db_path, Links, Pages, Redirects) {
        self.Sequelize = Sequelize;
        self.Op = self.Sequelize.Op;
        self.sequelize = new Sequelize(`sqlite:${db_path}`);
        self.Links = self.sequelize.import(Links);
        self.Pages = self.sequelize.import(Pages);
        self.Redirects = self.sequelize.import(Redirects);
    }
    // ["20845297"]
    function test(arr) {
        db.Links.findAll({
            attributes: ["outgoing_links"],
            where: {
                id: {
                    [self.Op.or]: arr
                }
            }
        })
        .then((links) => {
            return links.map(obj => {
                return obj.dataValues.outgoing_links.split("|");
            })
        })
    }
}

module.exports = db;
