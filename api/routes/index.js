var express = require('express');
var router = express.Router();
var scrapingController = require('../controllers/scraping.js')
/* GET home page. */



router.get('/run', scrapingController.run);
router.get('/metrics', scrapingController.metrics);
module.exports = router;