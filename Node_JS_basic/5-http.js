const http = require('http');
const fs = require('fs');

const args = process.argv.slice(2);
const database = args[0];

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.toString().split('\n');
    const students = lines.slice(1).filter((line) => line.length > 0);
    let message = '';

    message += `Number of students: ${students.length}\n`;

    const fields = {};
    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    for (const [field, names] of Object.entries(fields).sort()) {
      message += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    return message;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const message = countStudents(database);
      res.end(`This is the list of our students\n${message.slice(0, -1)}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  }
});

app.listen(1245);

module.exports = app;
