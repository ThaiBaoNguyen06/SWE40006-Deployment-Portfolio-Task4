const express = require("express");

const app = express();

const PORT = process.env.PORT || 3000;
const APP_ENV = process.env.APP_ENV || "Development";

app.get("/", (req, res) => {
  res.send(`
    <h1>SWE40006 Docker Deployment</h1>
    <h2>Task 4.3 - Distinction Level</h2>
    <p>Student: Thai Bao Nguyen</p>
    <p>Environment: ${APP_ENV}</p>
    <p>Container networking is working successfully.</p>
  `);
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`SWE40006 web application running on port ${PORT}`);
  console.log(`Environment: ${APP_ENV}`);
});