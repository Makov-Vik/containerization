const { faker } = require('@faker-js/faker');
const randomEmail = faker.internet.email();

console.log('Another person who became a millionaire in this world:')
console.log(
  faker.fake('{{name.lastName}}, {{name.firstName}} {{name.suffix}}')
);
console.log('Write to him to congratulate: ', randomEmail);