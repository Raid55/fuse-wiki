const Db = require('../models');
const links = require('../models/links.js');
const redirects = require('../models/redirects.js');
const pages = require('../models/pages.js')
const Sequelize = require('sequelize');

db = new Db(Sequelize, "./fuse.sqlite", links, pages, redirects)

db.sequelize.sync().then(() => {
    dbTest(db);
});

async function dbTest(db){
    te1 = await db.find_incoming(['148201']);
    te2 = await db.find_outgoing(['148201']);
    te3 = await db.find_incoming(['146728', '148191']);
    te4 = await db.find_outgoing(['146728', '148191']);
    console.log(te1);
    console.log(te2);
    console.log(te3);
    console.log(te4);
}
