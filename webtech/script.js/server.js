const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
app.use(express.static('public'));
app.use(bodyParser.json());

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

app.post('/send-emails', async (req, res) => {
  const { subject, message, recipients } = req.body;
  const results = [];

  for (const { name, email } of recipients) {
    const personalizedMessage = message.replace('{{name}}', name);

    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: email,
      subject,
      text: personalizedMessage,
    };

    try {
      await transporter.sendMail(mailOptions);
      results.push({ email, status: 'sent' });
    } catch (error) {
      results.push({ email, status: 'failed', error: error.message });
    }
  }

  res.json(results);
});

app.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
