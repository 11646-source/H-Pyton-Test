export function getMessage() {
  return Promise.resolve('Hello world');
}

getMessage().then(console.log);
