function createInt8TypedArray(length, position, value) {
  // Check if the position is within the valid range
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const dataView = new DataView(buffer);
  dataView.setInt8(position, value);

  return dataView;
}

export default createInt8TypedArray;
