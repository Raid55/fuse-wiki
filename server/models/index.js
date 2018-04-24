const Sequelize = require('sequelize');
// importing models
const links = require('./links.js');
const pages = require('./pages.js');
const redirects = require('./redirects.js');

class Database {
    constructor(Sequelize, db_path, Links, Pages, Redirects) {
        this.Sequelize = Sequelize;
        this.Op = this.Sequelize.Op;
        this.sequelize = new Sequelize('none', 'none', 'none', {
            dialect: 'sqlite',
            storage: db_path
        });

        this.Links = this.sequelize.import("links", Links);
        this.Pages = this.sequelize.import("pages", Pages);
        this.Redirects = this.sequelize.import("redirects", Redirects);
    }

    // takes in an array of ids and returns dict with
    // key as id and value as array of outgoing ids
    async findOutgoing(arr) {
        return await this.Links.findAll({
            attributes: ["id", "outgoing_links"],
            where: {
                id: {
                    [this.Op.or]: arr
                }
            }
        })
        .then(links => {
            if (links.length == 1)
                return links[0].dataValues.outgoing_links.split("|");
            else
                return links.reduce((accu, el) => {
                    accu[el.dataValues.id] = el.dataValues.outgoing_links.split("|");
                    return accu;
                }, {});
        })
    }

    // takes in an array of ids and returns dict with
    // key as id and value as array of incoming ids
    async findIncoming(arr) {
        return await this.Links.findAll({
            attributes: ["id", "incoming_links"],
            where: {
                id: {
                    [this.Op.or]: arr
                }
            }
        })
        .then(links => {
            if (links.length == 1)
                return links[0].dataValues.incoming_links.split("|");
            else
                return links.reduce((accu, el) => {
                    accu[el.dataValues.id] = el.dataValues.incoming_links.split("|");
                    return accu;
                }, {});
        });
    }

    async findTitle(id) {
        return await this.Pages.findAll({
            attributes: ["title"],
            where: {
                id: id
            }
        })
        .then(page => {
            return page[0].dataValues.title;
        });
    }

}

// Creating the Database connection
module.exports = new Database(Sequelize, "./fuse.sqlite", links, pages, redirects);
