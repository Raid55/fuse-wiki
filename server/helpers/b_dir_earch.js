import { NONAME } from 'dns';

const db = require('../models');

module.exports = async function(db, source_id, target_id) {
    // Composed by J.B.Hartman
    // Transpiled by Raid55

    // Setup
    let paths = [];

    // 0 Degrees of Separation
    if (source_id === target_id)
        return("they are teh same m8");

    // 1 Degree of Separation
    let source_1 = await db.findOutgoing([source_id]);
    if (source_1.includes(target_id)) {
        paths.push([source_id, target_id]);
        return paths;
    }

    // 2 Degrees of Separation
    target_1 = await db.findOutgoing([target_id]);
    for (article in source_1) {
        if (target_1.includes(article))
            paths.push([source_id, article, target_id]);
    }
    if (paths)
        return paths;

    // 3 Degress of Separation
    source_2 = await db.findOutgoing([source_1]);
    for (key in source_2) {
        for (article in source_2[key]) {
            if (target_1.includes(article))
                paths.push([source_id, key, article, target_id]);
        }
    }
    if (paths)
        return paths
    
    return paths

}







