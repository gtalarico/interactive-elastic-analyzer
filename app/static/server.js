const $axios = axios.create({
  baseURL: "/elastic/",
  timeout: 5000,
  headers: { "Content-Type": "application/json" }
});

// $axios.interceptors.response.use(
//   function(response) {
//     return response;
//   },
//   function(error) {
//     // Handle Error
//     console.log(error);
//     return Promise.reject(error);
//   }
// );
