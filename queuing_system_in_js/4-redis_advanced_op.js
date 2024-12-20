import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Create Hash
const createHash = () => {
  client.hset('HolbertonSchools', 'Portland', '50', redis.print);
  client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
  client.hset('HolbertonSchools', 'New York', '20', redis.print);
  client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
  client.hset('HolbertonSchools', 'Cali', '40', redis.print);
  client.hset('HolbertonSchools', 'Paris', '2', redis.print);
};

// Display Hash
const displayHash = () => {
  client.hgetall('HolbertonSchools', (err, res) => {
    if (err) {
      console.error(`Error fetching hash: ${err.message}`);
    } else {
      console.log(res);
    }
  });
};

// Main operations
createHash();
displayHash();
