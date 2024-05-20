function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  return array.map(({ id }) => id);
}

export default getListStudentIds;
