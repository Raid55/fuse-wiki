module.exports = function(sequelize, DataTypes) {
    return sequelize.define("links", {
        id: {
            type: DataTypes.INTEGER,
            primaryKey: true
        },
        outgoing_links_count: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        incoming_links_count: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        outgoing_links: {
            type: DataTypes.TEXT,
            allowNull: false
        },
        incoming_links: {
            type: DataTypes.TEXT,
            allowNull: false
        }
    });
}
