"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with open('north_data/customers_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='QWERasdf0058*')
    try:
        with conn:
            with conn.cursor() as curs:
                counter = 0
                for element in file_reader:
                    if counter == 0:
                        counter += 1
                        continue
                    else:
                        curs.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                     (element[0], element[1], element[2]))
                        counter += 1
    finally:
        conn.close()

with open('north_data/employees_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='QWERasdf0058*')
    try:
        with conn:
            with conn.cursor() as curs:
                counter = 0
                for element in file_reader:
                    if counter == 0:
                        counter += 1
                        continue
                    else:
                        curs.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                     (element[0], element[1], element[2], element[3], element[4], element[5]))
                        counter += 1
    finally:
        conn.close()

with open('north_data/orders_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='QWERasdf0058*')
    try:
        with conn:
            with conn.cursor() as curs:
                counter = 0
                for element in file_reader:
                    if counter == 0:
                        counter += 1
                        continue
                    else:
                        curs.execute("INSERT INTO  orders VALUES (%s, %s, %s, %s, %s)",
                                     (element[0], element[1], element[2], element[3], element[4]))
                        counter += 1
    finally:
        conn.close()

