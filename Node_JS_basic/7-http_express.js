const express = require('express');
const fs = require('fs');

const app = express();

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    if (!data) {
      throw new Error('Cannot load the database');
    }

    const lines = data.toString().split('\n');
    const students = lines.slice(1).filter(line => line.length > 0);

    if (students.length === 0) {
      throw new Error('Cannot load the database');
    }

    let output = `Number of students: ${students.length}\n`;

    // Group students by field
    const fields = {};
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    // Add results for each field (sorted alphabetically)
    Object.keys(fields).sort().forEach(field => {
      output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    });

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  try {
    const output = countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${output}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
