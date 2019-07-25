// import axios from 'axios';


const API_URL = 'http://localhost:3000'
import database from "@/services/database";
const api = require('axios');
api.defaults.baseURL = 'http://localhost:3000/'
var token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ2YjgzOTdjOGU0NmE3M2ZiMDExMDk2YjUyMDE1YTZlNjZkMDMyZWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20va2V5d29yZC1nZW5lcmF0b3ItOGJmYjkiLCJhdWQiOiJrZXl3b3JkLWdlbmVyYXRvci04YmZiOSIsImF1dGhfdGltZSI6MTU2MzcwNjQ3MiwidXNlcl9pZCI6IlNnenFYcEJ5Q1BYTGdJSDFFUHAxM3RZZXhtRDIiLCJzdWIiOiJTZ3pxWHBCeUNQWExnSUgxRVBwMTN0WWV4bUQyIiwiaWF0IjoxNTYzOTIwMzEyLCJleHAiOjE1NjM5MjM5MTIsImVtYWlsIjoic291YmVuejk0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzb3ViZW56OTRAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.HS6s8KXzvb6ZBKtBkYWbF02q4f7wpGOyiHsPCbUqa74QUIi5HaytBXgwv64wreJK8K7gYWCL3N5DGr-iWMrkfT86MLxPFPctWOre9NXzvfm-djJfUeFOZ-vAf1KShFD4xfHS2aL3BxChG_BIIlV4VifJmK0s_NTpm6WIMPoywf-NUNGV6fpcpM2iegm2aSsmyBQ3vLAfw3xE7JEOqQXco7vNO3IDadnYYB10FQ3hIZ3j39jykAv7GWZciQrmGub3z6B4mO1t0oJvrskNGezUwgPYVLUCOiY9L_CsZFwJY5a48qinxAdugh78r_iVfZeqHRp_eHZt4DKtX8RpwgxymA";
api.defaults.headers.common = {
    'Authorization': `Bearer ${token}`
}
export default api;


// export class APIService {



//     constructor() {

//     }

//     getKeywords(keywords, limit) {
//         const url = '${API_URL}/run';
//         return axios.get(url, {
//             params: {
//                 keywords: keywords

//             }
//         }).then(response => response.data);
//     }

// }