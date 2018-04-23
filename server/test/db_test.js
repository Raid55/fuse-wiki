const db = require('./models');
const Op = db.Sequelize.Op;

db.sequelize.sync().then(() => {
    test = db.Links.findAll(
        where: {
            attributes: ['incoming_links_count', 'incoming_link'],
            id: {
                [Op.contains]: ["1080220"]
            } 
        }
    )

    console.log(test);
});
