const http = require('http');
const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    lines.shift();

    const students = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (firstname && field) {
        totalStudents += 1;
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }
    });

    let output = `Number of students: ${totalStudents}\n`;
    for (const [field, names] of Object.entries(students)) {
      output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    resolve(output);
  });
});

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];
    countStudents(database)
      .then((data) => {
        res.write('This is the list of our students\n');
        res.end(data.slice(0, -1));
      })
      .catch((error) => {
        res.write('This is the list of our students\n');
        res.end(error.message);
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
