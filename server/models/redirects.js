module.exports = function(sequelize, DataTypes) {
    return sequelize.define("Redirects", {
        source_id: {
            type: DataTypes.INTEGER,
            primaryKey: true
        },
        target_id: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    });
}
