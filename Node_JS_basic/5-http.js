const http = require('http');
const fs = require('fs').promises;

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

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const database = process.argv[2];
      const data = await countStudents(database);
      res.end(`This is the list of our students\n${data}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
