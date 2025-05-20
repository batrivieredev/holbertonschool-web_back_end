const fs = require('fs');

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  if (!filePath) {
    reject(new Error('Cannot load the database'));
    return;
  }

  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.toString().split('\n');
    const students = lines
      .filter((line) => line.length > 0 && line.includes(','))
      .slice(1);

    const fields = {};
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (firstname && field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    resolve(fields);
  });
});

module.exports = readDatabase;
