const fs = require('fs');

function countStudents(path) {
  try {
    // Read and parse the database file
    const data = fs.readFileSync(path, 'utf8');
    if (!data) {
      throw new Error('Cannot load the database');
    }

    const lines = data.toString().split('\n');
    const students = lines.slice(1).filter(line => line.length > 0);

    if (students.length === 0) {
      throw new Error('Cannot load the database');
    }

    // Log total number of students
    console.log(`Number of students: ${students.length}`);

    // Group students by field
    const fields = {};
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    // Log results for each field (sorted alphabetically)
    Object.keys(fields).sort().forEach(field => {
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
