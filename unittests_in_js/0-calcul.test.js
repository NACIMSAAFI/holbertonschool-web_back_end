// 0-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round and sum when one argument is a decimal', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round both arguments and return the sum', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should correctly round 1.5 upwards', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });

  it('should handle zero as an input', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
});
