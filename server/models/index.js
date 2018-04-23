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
        this.Sequelize = Sequelize;
        this.Op = this.Sequelize.Op;
        this.sequelize = new Sequelize(`sqlite:${db_path}`);
        this.Links = this.sequelize.import("links", Links);
        this.Pages = this.sequelize.import("pages", Pages);
        this.Redirects = this.sequelize.import("redirects", Redirects);
    }
    // ["20845297"]
    async test(arr) {
        this.Links.findAll({
            attributes: ["outgoing_links"],
            where: {
                id: {
                    [this.Op.or]: arr
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
