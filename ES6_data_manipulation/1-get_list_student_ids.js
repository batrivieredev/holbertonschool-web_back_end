export default function getListStudentIds(list) {
  if (!Array.isArray(list)) {
    return [];
  }

  return students.map((student) => student.id);
}
