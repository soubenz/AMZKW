const request = require('request');
const AdwordsUser = require('node-adwords').AdwordsUser;



const scrapingController = {
    run(req, res) {
        let keyword = req.query.keyword;
        let type = req.query.type;
        let limit = req.query.limit;
        let scrapHost = process.env.SCRAP_HOST;
        let scrapEndpoint = process.env.SCRAP_ENDPOINT;
        let options = {
            url: 'http://' + scrapHost + '/' + scrapEndpoint,
            method: 'POST',
            body: '{"spider_name":"' + type + '", "start_requests": true, "keyword": "' + keyword + '", "limit": ' + limit + '}'

        };
        request(options).pipe(res);
    },
    metrics(req, res) {
        let keywords = req.query.keywords;
        console.log(keywords);
        let KRevApiKey = process.env.KR_API_KEY;
        let qs = {
            apiKey: KRevApiKey,
            country: "in",


        }
        qs['kw'] = keywords
        // qs['kw'] = ['milk', 'java']
        let options = {
            url: 'https://keywordseverywhere.com/service/1/getKeywordData.php',
            method: 'GET',
            qs: qs,



        };
        console.log(request(options).url);
        request(options).pipe(res);
    },
    adword(req, res) {

        let user = new AdwordsUser({
            developerToken: '8nH5Q-0ZabpOshboLmoGhw', //your adwords developerToken
            userAgent: 'INSERT_COMPANY_NAME_HERE', //any company name
            clientCustomerId: '553-689-7327', //the Adwords Account id (e.g. 123-123-123)
            client_id: '767473147886-u2icc23qlpmdhistbq1bi9stgk56vvqb.apps.googleusercontent.com', //this is the api console client_id
            client_secret: 'PmBZqm1d4n7e5LmD8zYzbMS7',
            refresh_token: '1/mGm-IWYfefXWzgbCPuHmKkkvmEQU7_oXRs8Gqw5FCnv0DLBqO-Z_Hu1JRX6WHDBn'
        });

        let campaignService = user.getService('CampaignService', 'v201809')

        //create selector
        let selector = {
            fields: ['Id', 'Name'],
            ordering: [{
                field: 'Name',
                sortOrder: 'ASCENDING'
            }],
            paging: {
                startIndex: 0,
                numberResults: 100
            }
        }

        campaignService.get({
            serviceSelector: selector
        }, (error, result) => {
            res.send(error, result);
        })
        }}


module.exports = scrapingController;