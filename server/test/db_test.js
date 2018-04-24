const Db = require('../models');
const links = require('../models/links.js');
const redirects = require('../models/redirects.js');
const pages = require('../models/pages.js')
const Sequelize = require('sequelize');
const search = require('../helpers/b_dir_earch.js');
const getTitles = require('../helpers/getTitles.js');

db = new Db(Sequelize, "./fuse.sqlite", links, pages, redirects)

db.sequelize.sync().then(() => {
    console.time('search');
    res = search(db, "", "");
    console.timeEnd('dbTest');
    console.log(res);
    console.log(getTitles(res));
});


