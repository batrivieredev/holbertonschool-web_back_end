import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const path = process.argv[2];

    readDatabase(path)
      .then((studentsByField) => {
        const fields = Object.keys(studentsByField).sort((a, b) => a.localeCompare(b));
        let response = 'This is the list of our students\n';

        fields.forEach((field) => {
          response += `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}\n`;
        });

        return res.status(200).send(response.slice(0, -1));
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    const path = process.argv[2];

    return readDatabase(path)
      .then((studentsByField) => {
        const students = studentsByField[major] || [];
        return res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
