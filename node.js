const fs = require('fs');
const readline = require('readline');
const tf = require('@tensorflow/tfjs-node');
const { LinearRegression } = require('ml-regression');

// Data Import
const fileStream = fs.createReadStream('final_Dataset.csv');
const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
});

const arr = [];
rl.on('line', (line) => {
    arr.push(line.split(','));
}).on('close', () => {
    const Y = arr.map(row => parseFloat(row[0]));
    const X = arr.map(row => row.slice(1).map(parseFloat));
    const X_t = tf.tensor2d(X)
    const y = tf.tensor(Y)
});