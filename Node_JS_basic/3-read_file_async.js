const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.toString().split('\n');
    const students = lines.slice(1).filter((line) => line.length > 0);

    if (!students.length) {
      throw new Error('Cannot load the database');
    }

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    for (const [field, names] of Object.entries(fields).sort()) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
