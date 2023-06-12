#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0, square; i < num; i++) {
    square = '';
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
