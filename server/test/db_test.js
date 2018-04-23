const Db = require('../models');
const links = require('../models/links.js');
const redirects = require('../models/redirects.js');
const pages = require('../models/pages.js')
const Sequelize = require('sequelize');

db = new Db(Sequelize, "./fuse.sqlite", links, pages, redirects)

db.sequelize.sync().then(() => {
    db.test(["20845297"]).then((res) => {
        console.log(res);
    })
});
