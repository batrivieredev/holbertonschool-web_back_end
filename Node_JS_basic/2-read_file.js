const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter(line => line); // Remove header and empty lines

    if (!students.length) {
      throw new Error('Cannot load the database');
    }

    console.log(`Number of students: ${students.length}`);

    // Group students by field
    const fields = {};
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count += 1;
      fields[field].names.push(firstName);
    });

    // Display results for each field
    Object.entries(fields).forEach(([field, data]) => {
      console.log(
        `Number of students in ${field}: ${data.count}. List: ${data.names.join(', ')}`
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
