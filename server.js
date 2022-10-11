// Loads the configuration from config.env to process.env
require('dotenv').config({ path: './config.env' });

var express = require('express');
var bodyParser = require('body-parser');
var MongoClient = require('mongodb').MongoClient;

var app = express();
var port = 3012;
var db;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true}))

app.post('/artists', function (req, res) {
  var artist = {
    name: req.body.name
    };

    db.collection('artists').insert(artist, function (err, result) {
      if (err) {
        console.log(err);
        res.sendStatus(500);
        }
        res.send(artist)
      })
//    res.send(artist);
  })

app.put('/artists/:id', function (req, res) {
  var artist = artists.find(function (artist) {
    return artist.id === Number(req.params.id)
  });
    artists.name = req.body.name;
    res.sendStatus(200);
  })

app.delete('/artists/:id', function (req, res) {
  var artist = artists.filter(function (artist) {
    return artist.id !== Number(req.params.id)
  });
    res.sendStatus(200);
  })

MongoClient.connect('mongodb+srv://valstan:nitro2000@postopus.qjxr9.mongodb.net/postopus?retryWrites=true&w=majority',
                    function (err, database) {
  if (err) {
    return console.log(err);
  }
  db = database;
  app.listen(port, function () {
    console.log('API app started');
  })
})