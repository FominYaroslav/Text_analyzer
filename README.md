# Text analyzer
Analysis of the occurrence's frequency of words in text

# To start:
 To start, project requires python3 to be installed on you PC.
 1. Create virtual environment: python -m venv <virtual_env_name>
 2. Activate virtual environment
 3. Install packages from requirements.txt: pip install -r requirements.txt
 4. Do migrations in DB: python manage.py migrate
 5. For setting value of "high" and "low" frequency execute (optional): SET LOW_RATE_LIMIT=<VALUE>;  SET HIGH_RATE_LIMIT=<VALUE>
 6. Start app: python manage.py runserver
 7. Open in browser "localhost:8000

