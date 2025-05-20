const http = require('http');
const fs = require('fs');

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

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const output = countStudents(process.argv[2]);
      res.end(`This is the list of our students\n${output}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
