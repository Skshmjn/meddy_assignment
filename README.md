<h2 align="center">Meddy Assignment</h2>
<h4 align="center">News Aggregator</h4>

## About The Project

It is news aggregator. It clubs the news from various sources (newsapi,reddit). It returns list of news data having
attribute 'headline','link','source'.

```bazaar
{"headline":"Police launch search for unknown suspects after 7-year-old boy shot dead in Soweto",
"link":"https://www.news24.com/news24/SouthAfrica/News/police-launch-search-for-unknown-suspects-after-7-year-old-boy-shot-dead-in-soweto-20210116",
"source":"newsapi}"
```

### INSTALLATION :

#### Install locally

1. clone the git repository

```
git clone https://github.com/Skshmjn/meddy_assignment.git
```

2. Create python virtualenv and activate virtualenv

```
python3 -m venv env

source env/bin/activate
```

3. Install redis server

```
sudo apt-get install redis
```

4. Install python dependency using

```
./install_python_dependencies.sh
```

5. Run python fast api server

```
python app.py
```

6. Endpoints are

```
http://0.0.0.0:8000/news/
    
http://0.0.0.0:8000/news?query=<query>>
```

### Add more news api sources

1. Open directory sources in root directory


2. Create a python file to add new news source


3. Create functions to call api and prepare custom response as per our requirement


4. Add configuration in config.py file

   
5. Import function in aggregator.py file and add in source list(without paranthesis)

   
6. Use cache_api decorator to cache your api custom response.
   

7. Add custom cache expiry time for your api in seconds(If no parameter given DEFAULT_API_CACHE_TIME will be used).
   

8. Create custom test case for your api.


9. Use MyLogger to log error or info (not implemented).