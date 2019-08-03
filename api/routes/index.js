var express = require('express');
var router = express.Router();
var scrapingController = require('../controllers/scraping.js')
/* GET home page. */



router.get('/run', scrapingController.run);
router.get('/metrics', scrapingController.metrics);
router.get('/adword', scrapingController.adword);
module.exports = router;