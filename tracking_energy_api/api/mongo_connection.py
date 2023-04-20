from decouple import config
PASSWORD = config("PASSWORD")
uri = "mongodb+srv://ja683:"+PASSWORD+"@cluster0.l2in6rm.mongodb.net/ManHaysHack"
