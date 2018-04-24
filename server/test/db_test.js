const db = require('../models');
const links = require('../models/links.js');
const redirects = require('../models/redirects.js');
const pages = require('../models/pages.js')
const Sequelize = require('sequelize');
const search = require('../helpers/b_dir_earch.js');
// const getTitles = require('../helpers/getTitles.js');

db.sequelize.sync().then( async () => {
    console.time('search');
    res = await search(db, "2731583", "25414");
    console.timeEnd('search');
    console.log(res, "arr");
    // for (arr of res) {
    //     console.log(arr);
    //     for (id of arr) {
    //         console.log(id);
    //         console.log("aayayay", await db.findTitle(id), "LOLOLOLO")
    //     }
    // }
    title = await db.findTitles(res)
    console.log(title);
});


// sqlite> select id from pages where title="Adolf_Hitler"
// 2731583
// sqlite> select id from pages where title="Jews";
// 25955086
// sqlite> select id from pages where title="Religion";
// 25414
