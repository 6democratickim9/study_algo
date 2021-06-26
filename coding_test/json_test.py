import json
from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import pymysql
import json


item = {
	"item":
		[{
			"id": 42,
			"Qty": 2
		},
                    {
			"id": 43,
			"Qty": 3
		},
                    {
            "id":52,
            "Qty":5
		}]

}
json_data = json.dumps(item) # json 파일로 변형
python_data = json.loads(json_data) # 파이썬 dict 파일로 변형


for a in range(len(python_data["item"])):
    
    print(python_data["item"][a]["id"])
    print(python_data["item"][a]["Qty"])
    item_amounts = python_data["item"][a]["Qty"]
    item_id = python_data["item"][a]["id"]
    conn = pymysql.connect(
        host='multicampus.clhnj2zwdisk.eu-west-2.rds.amazonaws.com', port=3306, user='admin', passwd='master123', db='multicampus', charset='utf8')

    subtraction = "UPDATE Item_info SET Qty=Qty-{} WHERE Item_id='{}'"
    subtraction = subtraction.format(item_amounts,item_id)

    python_data["item"][a]

    print(subtraction)
    cursor = conn.cursor()

    cursor.execute(subtraction)
    conn.commit()
conn.close()


def insert_sales(item,phonenum):
    item = item
    cursor = conn.cursor()
    

    return print("query success")


insert_sales(item,'090-92222-0728')

