module.exports = function(sequelize, DataTypes) {
    return sequelize.define("pages", {
        id: {
            type: DataTypes.INTEGER,
            primaryKey: true
        },
        title: {
            type: DataTypes.TEXT,
            allowNull: false
        },
        is_redirect: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    });
}
