const cluster = require('cluster');
const fs = require('fs');
const express = require('express');
const https = require('https');
const http = require('http');
const morgan = require('morgan');

// get number of CPUS for cluster
const numCPUs = require('os').cpus().length;

// keys for SSL
const certificate  = fs.readFileSync('/etc/letsencrypt/live/fuse.wiki/fullchain.pem', 'utf8');
const privateKey = fs.readFileSync('/etc/letsencrypt/live/fuse.wiki/privkey.pem', 'utf8');

// declare our express object and cert object
const app = express();
const options = {cert: certificate,
                 key: privateKey};

// serve React's static and user helmet
app.use(require('helmet')());
app.use(function(req, res, next) {
  if (req.secure) {
    next();
  } else {
    res.redirect('https://' + req.headers.host + req.url);
  }
});
app.use(morgan('combined'))
app.use(express.static('client/build'));


// run the server
if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  // Fork workers.
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on('exit', (worker, code, signal) => {
    console.log(`worker ${worker.process.pid} died`);
  });
} else {
  // Workers can share any TCP connection
  // In this case it is an HTTP server
  https.createServer(options, app).listen(443);
  http.createServer(app).listen(80);
  console.log(`Worker ${process.pid} started`);
}


//https.createServer(options, app).listen(443);
//http.createServer(app).listen(80);
//console.log('Fuse.wiki app running... on port <TODO> ');
