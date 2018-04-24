const path       = require('path');
const cors       = require('cors');
const morgan     = require('morgan');
const express    = require('express');
const favicon    = require('serve-favicon');
const bodyParser = require('body-parser');

//Importing routes
const { api } = require('./routes');

//express app
const app = express();

// Allow CORS
app.use(cors())

// Serve static assets
app.use(express.static(path.resolve(__dirname, '..', 'client', 'build')));
// Serving favicon
// app.use(favicon(__dirname + '/public/favicon-16x16.png'));

//body parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

//Morgan logger//
app.use(morgan("........................................"));
app.use(morgan(':user-agent'));
app.use(morgan('[:date[clf]]'));
app.use(morgan('":method | :url | HTTP/:http-version"'));
app.use(morgan(':status | :res[content-length] | :response-time ms'));
app.use(morgan('........................................'));
app.use(morgan(' '));
//end of logger info//

// React route
app.get("*", (req, res) => {
    res.sendFile(path.resolve(__dirname, '..', 'client', 'build', 'index.html'));
})

// Applying Routes
app.use('/api/v1', api);


module.exports = app;
