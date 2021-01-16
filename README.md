<h2 align="center">Meddy Assignment</h2>
<h4 align="center">News Aggregator</h4>

## About The Project

It is news aggregator. It clubs the news from various sources (newsapi,reddit). It returns list of news data having
attribute 'headline','link','source'.

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

### Add more api sources

1. Open directory