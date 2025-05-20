import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  if (!filePath) {
    reject(new Error('Cannot load the database'));
  }

  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const students = {};
    const lines = data.split('\n');
    const fileLines = lines.filter((line) => line.trim().length > 0);
    const studentsLines = fileLines.slice(1);

    if (studentsLines.length === 0) {
      resolve(students);
      return;
    }

    studentsLines.forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (field && firstName) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstName);
      }
    });

    resolve(students);
  });
});

export default readDatabase;
