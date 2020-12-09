import pymysql, os, json

# read JSON file which is in the next parent folder
file = os.path.abspath('C:/Users/wongb/Desktop/record.json')
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = 'PassRoot_2',db = 'userinfo')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    name = validate_string(item.get("name", None))
    temp_celsius = validate_string(item.get("temp_celsius", None))
    DateTime = validate_string(item.get("DateTime", None))

    cursor.execute("INSERT INTO temps (name,    temp_celsius,    DateTime) VALUES (%s,    %s,    %s)", (name,    temp_celsius,    DateTime))
con.commit()
con.close()
