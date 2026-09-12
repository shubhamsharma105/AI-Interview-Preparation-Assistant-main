# AI Interview Preparation Assistant

An AI-powered web application designed to help users practice
interviews, receive answer evaluations, generate interview reports, and
review previous interview attempts.

## Features

-   **Interview Practice:** Start an interview and answer questions.
-   **Interview Engine:** Manages the interview flow and questions.
-   **Answer Evaluation:** Evaluates candidate answers and provides
    feedback.
-   **Report Generation:** Creates an interview report based on
    performance.
-   **Interview History:** Stores interview data in an SQLite database.
-   **View History:** Allows users to review previous interview
    attempts.
-   **HTML Templates:** Provides web pages for the application
    interface.

## Project Structure

``` text
AI-Interview-Preparation-Assistant/
│
├── app.py
├── database.py
├── evaluation_engine.py
├── interview_engine.py
├── report_generator.py
├── view_history.py
├── requirements.txt
├── .gitattributes
│
├── database/
│   └── interview.db
│
├── templates/
│   ├── index.html
│   ├── interview.html
│   └── report.html
│
└── __pycache__/
```

## File Description

  -----------------------------------------------------------------------
  File / Folder                       Description
  ----------------------------------- -----------------------------------
  `app.py`                            Main application file and entry
                                      point.

  `database.py`                       Handles database connection and
                                      data storage.

  `evaluation_engine.py`              Contains logic for evaluating
                                      interview answers.

  `interview_engine.py`               Controls interview questions and
                                      interview flow.

  `report_generator.py`               Generates interview performance
                                      reports.

  `view_history.py`                   Displays previously saved interview
                                      records.

  `requirements.txt`                  Lists the Python packages required
                                      by the project.

  `database/interview.db`             SQLite database used to store
                                      interview information.

  `templates/index.html`              Home page of the application.

  `templates/interview.html`          Interview page.

  `templates/report.html`             Report page.
  -----------------------------------------------------------------------

## Technologies Used

-   Python
-   HTML
-   SQLite
-   Flask or Python web framework used by the application
-   Jinja2 HTML templates
-   Python packages listed in `requirements.txt`

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Open the project folder

``` bash
cd AI-Interview-Preparation-Assistant
```

### 3. Create a virtual environment

On Windows:

``` bash
python -m venv venv
```

Activate it:

``` bash
venv\Scripts\activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

## How to Run

Run the main application file:

``` bash
python app.py
```

If the project uses Flask, the terminal will display a local address
similar to:

``` text
http://127.0.0.1:5000/
```

Open that address in your browser.

> If your project uses a different web framework or port, follow the
> command configured in `app.py`.

## How to Use

1.  Open the application in your browser.
2.  Start an interview.
3.  Read each interview question.
4.  Submit your answer.
5.  Review the evaluation and feedback.
6.  Complete the interview.
7.  View the generated report.
8.  Open interview history to review previous attempts.

## Database

The project uses SQLite to store interview records.

The database file is located at:

``` text
database/interview.db
```

The database may contain information such as:

-   Interview questions
-   Candidate answers
-   Evaluation scores
-   Feedback
-   Interview reports
-   Previous interview attempts

## Requirements

Make sure Python is installed on your computer.

Check your Python version:

``` bash
python --version
```

Install all project dependencies using:

``` bash
pip install -r requirements.txt
```

## Future Enhancements

-   Add user login and registration.
-   Add more job roles and question categories.
-   Improve AI-based answer evaluation.
-   Add charts for interview performance.
-   Add resume analysis.
-   Add personalized study recommendations.
-   Add PDF report download.
-   Deploy the application online.
-   Add automated tests.

## Contributing

Contributions are welcome.

1.  Fork the repository.
2.  Create a new branch.
3.  Make your changes.
4.  Test the application.
5.  Create a pull request.

## License

This project is created for educational and learning purposes.

## Author

**Your Name**

GitHub: `https://github.com/shubhamsharma105`

------------------------------------------------------------------------

If you find this project useful, consider giving the repository a star.
