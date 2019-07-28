

const API_URL = 'http://localhost:3000'

import qs from "qs";
const api = require('axios');
api.defaults.baseURL = API_URL;
api.defaults.paramsSerializer = params => {
        return qs.stringify(params)
}
export default api;

