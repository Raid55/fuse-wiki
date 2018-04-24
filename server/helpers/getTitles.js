export async function(db, res) {
    return res.reduce((accu, el) => {
        accu.push(el.reduce((accu, el) => {
            accu.push(await db.findTitle(el));
            return accu;
        }, []));
        return accu;
    }, [])
}
