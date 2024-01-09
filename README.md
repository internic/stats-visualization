# Statistical visualization dashboard for LiK Household data

## Project Description
This is a statistical visualization dashboard built with Django. It displays various data visualizations such as donut charts, bar charts, and pie charts, focusing on household data, children's education, health measurements, and more.

## Getting Started

### Prerequisites
Before running this project, make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

#### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/internic/stats-visualization.git
cd your-repository
```

#### 2. Create a Virtual Environment

- **For Windows:**
  ```bash
  python -m venv venv
  ```
- **For macOS and Linux:**
  ```bash
  python3 -m venv venv
  ```

#### 3. Activate the Virtual Environment

- **For Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **For macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 4. Install Required Packages
Install all the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Running the Project

Once you have installed all the requirements, you can run the Django development server:

- **For Windows:**
  ```bash
  python manage.py runserver
  ```
- **For macOS and Linux:**
  ```bash
  python3 manage.py runserver
  ```

The server will start at `http://127.0.0.1:8000/` by default. Open this address in your web browser to view the application.
