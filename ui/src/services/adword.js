const AdwordsUser = require('node-adwords').AdwordsUser;

let user = new AdwordsUser({
 developerToken: '8nH5Q-0ZabpOshboLmoGhw', //your adwords developerToken
     userAgent: 'INSERT_COMPANY_NAME_HERE', //any company name
     clientCustomerId: '553-689-7327', //the Adwords Account id (e.g. 123-123-123)
    client_id: '401250063060-6rknjaa479p4h6u6mld5urcnpj1rs8cc.apps.googleusercontent.com', //this is the api console client_id
    client_secret: '03v9Cbn4t6svgFk8ntErP89y',
    refresh_token: '1/9bqtiM-wjKvuQr_qK-JIqb3jua3a9vKRVTngr9HDTvk'
});


export default user;