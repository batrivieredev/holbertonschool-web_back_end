const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
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

    // Sort fields alphabetically and display results
    const sortedFields = Object.keys(fields).sort((a, b) =>
      a.localeCompare(b, undefined, { sensitivity: 'base' })
    );

    sortedFields.forEach(field => {
      const data = fields[field];
      console.log(
        `Number of students in ${field}: ${data.count}. List: ${data.names.join(', ')}`
      );
    });

    return Promise.resolve(); // Explicitly return a resolved promise
  } catch (error) {
    return Promise.reject(new Error('Cannot load the database'));
  }
}

module.exports = countStudents;
