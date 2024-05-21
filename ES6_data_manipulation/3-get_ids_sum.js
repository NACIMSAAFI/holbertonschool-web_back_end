function getStudentIdsSum(list) {
  return list.reduce((accumulator, current) => accumulator + current.id, 0);
}

export default getStudentIdsSum;
