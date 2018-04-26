module.exports = async function(db, res) {
    console.log(res);
    return await res.reduce(async (acu, el) => {
        let ret = el.reduce(async (accu, el) => {
            let rett = await db.findTitle(el);
            console.log(1, accu);
            console.log(2, rett)
            accu.push(rett);
            return accu;
        }, [])
        console.log(3, ret);
        console.log(4, acu);
        acu.push(ret);
        return acu;
    }, [])
}
