export default function concatArrays(array1, array2, string) {
  const array3 = array1.concat(array2);
  const words = string.split('');
  for (const word of words) {
    array3.push(word);
  }
  return array3;
}
