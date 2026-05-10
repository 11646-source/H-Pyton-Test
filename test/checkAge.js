// checkAge.js

export default function checkAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 18) {
      resolve('Access granted');
    } else {
      reject('Access denied');
    }
  });
}
