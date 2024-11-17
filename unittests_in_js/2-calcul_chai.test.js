// 2-calcul_chai.test.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  // Test cases for 'SUM'
  it('should return an int number', () => {
    expect(calculateNumber('SUM', 2.3, 3.1)).to.be.a('number');
  });
  it('should return sum of num', () => {
    expect(calculateNumber('SUM', 2.2, 2.8)).to.deep.equal(5);
  });
  it('should return sum', () => {
    expect(calculateNumber('SUM', 1, 3)).to.deep.equal(4);
  });
  it('sum of nums', () => {
    expect(calculateNumber('SUM', 1, 1)).to.deep.equal(2);
  });
  it('return sum of nums', () => {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.deep.equal(5);
  });
  it('sum', () => {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.deep.equal(6);
  });
  it('sum negative numbers', () => {
    expect(calculateNumber('SUM', -2, -2)).to.deep.equal(-4);
  });
  it('sum with negative decimals', () => {
    expect(calculateNumber('SUM', -1.3, -4.5)).to.deep.equal(-5);
  });
  it('sum decimals rounding up', () => {
    expect(calculateNumber('SUM', 0.4, 0.6)).to.deep.equal(1);
  });
  it('sum decimals rounding down', () => {
    expect(calculateNumber('SUM', 0.4, 0.2)).to.deep.equal(0);
  });

  // Test cases for 'SUBTRACT'
  it('should return subtraction of num', () => {
    expect(calculateNumber('SUBTRACT', 2.2, 2.8)).to.deep.equal(0);
  });
  it('should return subtraction', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.deep.equal(-2);
  });
  it('subtraction of numbers', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.deep.equal(-3);
  });
  it('return subtraction of numbers', () => {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.deep.equal(-3);
  });
  it('subtraction', () => {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.deep.equal(-2);
  });
  it('subtraction of negative numbers', () => {
    expect(calculateNumber('SUBTRACT', -2, -2)).to.deep.equal(0);
  });
  it('subtraction with negative decimals', () => {
    expect(calculateNumber('SUBTRACT', -1.3, -4.5)).to.deep.equal(3);
  });
  it('subtraction decimals rounding up', () => {
    expect(calculateNumber('SUBTRACT', 0.4, 0.6)).to.deep.equal(-1);
  });
  it('subtraction decimals rounding down', () => {
    expect(calculateNumber('SUBTRACT', 0.4, 0.2)).to.deep.equal(0);
  });

  // Test cases for 'DIVIDE'
  it('should return division of numbers', () => {
    expect(calculateNumber('DIVIDE', 2.2, 2.8)).to.deep.equal(1);
  });
  it('should return division', () => {
    expect(calculateNumber('DIVIDE', 1, 3)).to.deep.equal(0.3333333333333333);
  });
  it('division of numbers', () => {
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.deep.equal(0.25);
  });
  it('return division of numbers', () => {
    expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.deep.equal(0.25);
  });
  it('division', () => {
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.deep.equal(0.5);
  });
  it('division of negative numbers', () => {
    expect(calculateNumber('DIVIDE', -2, -2)).to.deep.equal(1);
  });
  it('division with negative decimals', () => {
    expect(calculateNumber('DIVIDE', -1.3, -4.5)).to.deep.equal(0.25);
  });
  it('division decimals rounding down', () => {
    expect(calculateNumber('DIVIDE', 0.4, 0.6)).to.deep.equal(0);
  });
  it('division by zero should return "Error"', () => {
    expect(calculateNumber('DIVIDE', 0.4, 0)).to.deep.equal('Error');
  });
  it('division main case', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.deep.equal(0.2);
  });
  it('division by zero edge case', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.deep.equal('Error');
  });
});
