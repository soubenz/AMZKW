const request = require('request');



const scrapingController = {
    run(req, res) {
        let keyword = req.query.keyword;
        let limit = req.query.limit;
        let scrapHost = process.env.SCRAP_HOST;
        let scrapEndpoint = process.env.SCRAP_ENDPOINT;
        let options = {
            url: 'http://' + scrapHost + '/' + scrapEndpoint,
            method: 'POST',
            body: '{"spider_name": "generator","start_requests": true,"keyword":"' + keyword + '", "limit": ' + limit + '}'

        };
        request(options).pipe(res);
    },
    metrics(req, res) {
        let keywords = req.query.keywords;
        let KRevApiKey = process.env.KR_API_KEY;
        let qs = {
            apiKey: KRevApiKey,
            country: "in",


        }
        qs['kw'] = keywords.split(',')
        // qs['kw'] = ['milk', 'java']
        let options = {
            url: 'https://keywordseverywhere.com/service/1/getKeywordData.php',
            method: 'GET',
            qs: qs,



        };
        console.log(request(options).url);
        request(options).pipe(res);
    },

}


module.exports = scrapingController;