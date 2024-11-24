const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

// Function to send notifications
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs from the queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message);

  // Mark the job as done
  done();
});
