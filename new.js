const regression = require('regression');

// Sample dataset
const data = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
];

// Separate input features (X) and target variable (Y)
const X = data.map(row => [row[0]]);
const Y = data.map(row => row[1]);

// Create a linear regression model
const result = regression.linear(X, Y);

// Print the regression result
console.log('Regression Result:', result);

// Make predictions using the regression model
const newInput = 6;
const predictedOutput = result.predict(newInput);
console.log(`Prediction for input ${newInput}: ${predictedOutput}`);