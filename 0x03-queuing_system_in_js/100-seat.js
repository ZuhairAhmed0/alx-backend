// Redis
// Create a Redic client:

// Create a function reserveSeat, that will take into argument number, and set the key available_seats with the number
// Create a function getCurrentAvailableSeats, it will return the current number of available seats (by using promisify for Redis)
// When launching the application, set the number of available to 50
// Initialize the boolean reservationEnabled to true - it will be turn to false when no seat will be available
// Kue queue
// Create a Kue queue

// Server
// Create an express server listening on the port 1245. (You will start it via: npm run dev 100-seat.js)
// Create a route GET /available_seats that will return the number of remaining seats (via getCurrentAvailableSeats)
// Create a route POST /reserve_seat that will reserve a seat
// It will take into argument the userId and the number of seats to reserve
// It will call the reserveSeat function

