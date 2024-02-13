#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.lenght === 0) {
  console.log('undefined is undefined');
} else if (argv.lenght === 1) {
  console.log(argv[0] + ' is undefined ');
} else {
  console.log(argv[0] + ' is ' + argv[1]);
}
