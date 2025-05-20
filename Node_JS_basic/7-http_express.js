const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 1245;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter(line => line);

    let output = `Number of students: ${students.length}\n`;

    const fields = {};
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count += 1;
      fields[field].names.push(firstName);
    });

    // Sort fields alphabetically
    const sortedFields = Object.keys(fields).sort((a, b) =>
      a.localeCompare(b, undefined, { sensitivity: 'base' })
    );

    sortedFields.forEach(field => {
      const data = fields[field];
      output += `Number of students in ${field}: ${data.count}. List: ${data.names.join(', ')}\n`;
    });

    return output.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const database = process.argv[2];
    const data = await countStudents(database);
    res.set('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${data}`);
  } catch (error) {
    res.set('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(port);

module.exports = app;
