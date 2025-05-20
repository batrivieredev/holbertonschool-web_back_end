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

    Object.entries(fields).forEach(([field, data]) => {
      output += `Number of students in ${field}: ${data.count}. List: ${data.names.join(', ')}\n`;
    });

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const database = process.argv[2];
    const data = await countStudents(database);
    res.send(`This is the list of our students\n${data}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(port);

module.exports = app;
