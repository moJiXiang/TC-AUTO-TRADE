const Huobi = require('huobi')

let huobi = new Huobi({
  serectKey:'7298cea4-e6f9bef9-deb69529-92199', 
  accessKey:'7be44a0a-5fac8dca-7afc15a8-b1936'})

huobi.getAccountInfo()
.then(data => console.log(data))
.catch(err => console.log(err))