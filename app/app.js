const express = require('express') 
const logger = require('node-color-log');

const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World Juan Esteban!')
})


app.get('/math', (req, res) => {
  const { value1, value2, operation } = req.query

  const num1 = parseInt(value1)
  const num2 = parseInt(value2)
  let result = 0

  if (operation === "suma") {
    result = num1 + num2
  } 

  if (operation === "resta") {
    result = num1 - num2
  } 

  res.send(`El resultado es ${result}`)
})

app.listen(port, () => {
  logger
    .color('blue')
    .bold().dim().reverse()
    .log(`Escuchando por el puerto  ${port}`);
})
