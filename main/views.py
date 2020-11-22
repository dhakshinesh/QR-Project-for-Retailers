from django.shortcuts import render
import psycopg2

# Create your views here.
def index(request):
    """ Fetch the Data Base """
    conn = psycopg2.connect(database="d7vu2qberk3khb", user="khvziiwdidbcus",
                                    password="a30b1259b978d1ef24ae8bd6c9d942f3cf951062f4ccd7136aa785499f10b3cd", host="ec2-54-152-40-168.compute-1.amazonaws.com", port="5432")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from product_details"
    cursor.execute(postgreSQL_select_Query)
    result = cursor.fetchall()
    return render(request, "DB.html", result)