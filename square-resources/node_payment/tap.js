const axios = require('axios');

// Make a GET request to the Flask server
axios.get('http://127.0.0.1:5000/post/18')
    .then(response => {
        // Extract the value from the response data
        const value = response.data;

        // Now you can use this value in your Square payment application
        console.log('Value:', value);
        // Example: integrate with your Square payment application logic here
    })
    .catch(error => {
        console.error('Error fetching value:', error);
    });
