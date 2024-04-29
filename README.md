# Text_to_SQL_using_Gemini


## Installation

### 1. Clone the repository
```bash
git clone git@github.com:darsh1234/Text_to_SQL_using_Gemini.git
```

### 2. create and activate environment
``` bash 
conda create -n text2sql python=3.10 -y 
```

``` bash 
conda activate text2sql 
```

### 3. install depenedencies
``` bash 
pip install -r requirements.txt
```

### 4. set envrionment variables
#### Create a .env file in the root directory and add your Google Gemini API credentials as follows:
```ini
GOOGLE_API_KEY = ""
```

### 5. To change the database configuration:
#### Edit SQLlite.py and run it to createa database to query
``` bash 
python SQLlite.py
```

### 6. Run the website and open local host:
``` bash 
streamlit run app.py
```
#### Input the text to retrieve data from the database
