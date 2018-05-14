const express = require('express');
const app = express();

app.use(express.static('client/build'));

const port  = process.env.PORT || 3001;
app.listen(port, function () {
  console.log('Fuse.wiki app listening on port ' + port);
})
