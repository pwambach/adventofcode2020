const list = require('fs')
  .readFileSync(require('path').join(__dirname, '/input'), 'utf8')
  .split('\n')
  .map(n => Number(n.trim()));

// prettier-ignore
list.forEach(x =>
  list.forEach(y =>
      x + y === 2020 && console.log(x, y, x * y)
  )
);
