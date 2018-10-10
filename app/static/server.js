const $axios = axios.create({
  baseURL: "/elastic",
  timeout: 80000,
  headers: { "Content-Type": "application/json" }
});
