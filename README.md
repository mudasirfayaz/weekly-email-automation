# Weekly Email Automation ✉️

> A Python automation script that sends a motivational quote every Monday via email. Perfect for inspiring your friends, team, or yourself at the start of the week.

<br/>

## ✨ Features

- Sends HTML-styled motivational quotes on every Monday via email.
- Uses Simple Mail Transfer Protocol (SMTP) with secure App Passwords.
- Runs on PythonAnywhere via scheduled tasks.
- Supports multiple recipients via `recipients.txt`.

<br/>

## 🛠️ Prerequisites

- Python 3.8+
- Email account with App Password enabled
- Libraries:
  ```bash
  pip install -r requirements.txt
  ```

<br/>

## Setup Instructions

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/weekly-email-automation.git
cd weekly-email-automation
```

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

<br/>

**3. Prepare `.env` File**

Create a .env file with:

```bash
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
```

> [!NOTE]
> For Gmail, you must enable 2FA and create an App Password.<br/> [Google’s Guide on App Passwords](https://support.google.com/accounts/answer/185833?hl=en)

This script works with most email providers that support SMTP.  
Simply update the `.env` file with the correct `SMTP_SERVER` value.

| Provider              | SMTP Server           |
| --------------------- | --------------------- |
| **Gmail**             | `smtp.gmail.com`      |
| **Yahoo Mail**        | `smtp.mail.yahoo.com` |
| **Outlook / Hotmail** | `smtp.office365.com`  |
| **Zoho Mail**         | `smtp.zoho.com`       |
| **Proton Mail**       | `mail.protonmail.com` |

💡 **Tip:** Always keep your credentials safe by storing them in `.env` and never committing that file to GitHub.

<br/>

**4. Add Quotes and Recipients**

- Add new quotes or update existing ones in `quotes.txt` (one per line).
- Add recipient emails in `recipients.txt` (one per line).

<br/>

**5. Run Locally**

```bash
python main.py
```

<br/>

## Deployment on PythonAnywhere

> This script is designed to run on PythonAnywhere so you don’t need to keep your PC on.

**Step 1: Create a PythonAnywhere Account**

- Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com) and sign up for a free account.
- Log in to your dashboard.

<br/>

**Step 2: Upload Your Files**

- Go to the Files tab.
- Upload:
  - `main.py`
  - `quotes.txt`
  - `recipients.txt`
  - `.env` (upload it too, it will remain private)
- Ensure they are all in the same directory, for example:

```bash
/home/yourusername/monday-motivation-emailer
```

<br/>

**Step 3: Install Dependencies**

- Go to the Consoles tab → Start a Bash console.
- Run:

```bash
pip install --user python-dotenv
```

<br/>

**Step 4: Test the Script**

- In the Bash console, run:

```bash
python3 main.py
```

- If it’s Monday, it should send an email.
- (To test on other days, temporarily remove the Monday check in `main.py`.)

<br/>

**Step 5: Schedule the Script**

- Go to the Tasks tab → Add a New Scheduled Task.
- Set it to run every Monday at your preferred time (e.g., 09:00).
- Command to run:

```bash
python3 /home/yourusername/monday-motivation-emailer/main.py
```

- Click Create.

> Your script will now automatically send motivation emails every Monday at the scheduled time.

<br/>

### Video Reference

📺 Watch one of thes these PythonAnywhere scheduling tutorials:<br/>
**[Schedule Python Tasks on PythonAnywhere](https://youtu.be/C6NThuZiLjU?si=ln-5VVFCx4Urlf5N)**<br/>
**[How to Schedule python script on PythonAnywhere](https://youtu.be/yaChrGcSIo4?si=JtT9GqmSREBPvEVQ)**<br/>

> These videos shows how to upload files and set scheduled jobs step-by-step.

<br/>

## Security Note

> [!WARNING]
> Never upload `.env` to GitHub — it contains your credentials.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
