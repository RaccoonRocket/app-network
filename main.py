from flask import Flask, render_template
import psycopg2, redis

app = Flask(__name__) 

def conn_pg():
    pg = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="password", 
        host="172.20.0.3", 
        port="5432"
    )
    return pg

def conn_r():
    return redis.Redis(host='172.20.0.2', port='6379', decode_responses=True)


@app.route("/")
def hello_world():
    try:
        r = conn_r()
        r.flushdb()
    except:
        print("Error connecting to redis")
    return render_template('index.html')


@app.route('/cities')
def read_count():
    pair = 'cities:count'
    r = conn_r()
    redisCount = r.get(pair)
    if redisCount:
        res = redisCount + " cities in BRA (from redis)"
        return render_template('cities.html', value=res)

    pg = conn_pg()
    cur = pg.cursor()
    cur.execute("SELECT COUNT(*) FROM city WHERE countrycode = 'BRA'")
    pgCount = cur.fetchone()[0]

    res = str(pgCount) + " cities in BRA (from postgres)"
    r.set(pair, pgCount)

    return render_template('cities.html', value=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
