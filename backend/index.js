const express = require('express');
const app = express();

app.get('/api/courses', (req, res) => {
    res.send('Hello world!');
})

app.listen(8000, () => {
    console.log('Backend listening on port 8000!');
})
