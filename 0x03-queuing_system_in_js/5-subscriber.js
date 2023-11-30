// Import required modules
import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Handle connection events
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel "holberton school channel"
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(`Message received on channel ${channel}: ${message}`);

  // Unsubscribe and quit if the message is "KILL_SERVER"
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});