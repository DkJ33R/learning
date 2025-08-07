// Date

// Explicame que hace la funcion Date y como se usa
// La funcion Date es una funcion que se encarga de crear un objeto de tipo fecha y hora.
// La fecha y hora se pueden crear de diferentes maneras.

// Ejemplo de como se usa la funcion Date
const date = new Date()
console.log(date)

// Ejemplo de como se usa la funcion Date con un string
const date2 = new Date('2025-01-01')
console.log(date2)

// Ejemplo de como se usa la funcion Date con un numero
const date3 = new Date(2025, 0, 1)
console.log(date3)

const date4 = new Date(2025, 0, 1, 12, 12, 12)
console.log(date4.getHours())