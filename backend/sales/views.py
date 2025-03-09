from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import sqlite3
import pymysql
import psycopg2
import re
from django.conf import settings

class ExecuteQueryAPIView(APIView):
    def post(self, request):
        data = request.data
        db_type = data.get("db")
        user_prompt = data.get("query")  # This can be raw SQL or natural language
        print(f"Database type: {db_type}")
        print(f"Original query: {user_prompt}")

        if not user_prompt:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

        # If the query is in English, convert it to SQL using OpenAI API
        if not user_prompt.strip().lower().startswith(("select", "insert", "update", "delete")):
            sql_query = self.convert_to_sql(user_prompt, db_type)
            
            if isinstance(sql_query, str) and sql_query.startswith("Error"):
                return Response({"error": sql_query}, status=status.HTTP_400_BAD_REQUEST)
        else:
            sql_query = user_prompt

        try:
            def sqllite3(sql_query):
                print("Sid",sql_query)
                conn = sqlite3.connect("db.sqlite3")
                cursor = conn.cursor()
                cursor.execute(sql_query)
                
                if sql_query.strip().lower().startswith("select"):
                    column_names = [description[0] for description in cursor.description]
                    rows = cursor.fetchall()
                    formatted_results = [dict(zip(column_names, row)) for row in rows]
                    results = formatted_results
                else:
                    results = [{"affected_rows": cursor.rowcount}]
                    conn.commit()
                
                conn.close()
                return results  
            
            def mysql(sql_query):
                conn = pymysql.connect(host="localhost", user="root", password="0531", database="mysql_db_sales", port=3306)
                cursor = conn.cursor()
                cursor.execute(sql_query)
                
                if sql_query.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                else:
                    results = [{"affected_rows": cursor.rowcount}]
                    conn.commit()
                
                conn.close()
                return results
            
            def postgresql(sql_query):
                conn = psycopg2.connect(dbname="postgres_db_sales", user="postgres", password="0531", host="localhost", port=5432)
                cursor = conn.cursor()
                cursor.execute(sql_query)
                
                if sql_query.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                else:
                    results = [{"affected_rows": cursor.rowcount}]
                    conn.commit()
                
                conn.close()
                return results
            
            if db_type == "SQLite3":
                results = sqllite3(sql_query)
            elif db_type == "MYSQL":
                results = mysql(sql_query)
            elif db_type == "PostgreSQL":
                results = postgresql(sql_query)
                
            elif db_type == "Global":
                global_results = []

                for specific_db, query in sql_query.items():
                    try:
                        if specific_db == "SQLite3":
                            result = sqllite3(query)
                        elif specific_db == "MYSQL":
                            result = mysql(query)
                        elif specific_db == "PostgreSQL":
                            result = postgresql(query)

                        # Ensure the result structure is a list of tuples
                        if isinstance(result, list) and all(isinstance(row, tuple) for row in result):
                            global_results.extend(result)  # Append tuples directly
                        else:
                            global_results.append(tuple(result) if isinstance(result, list) else (result,))

                    except Exception as e:
                        global_results.append((f"Error in {specific_db}: {str(e)}",))

                print("Final Global Results:", global_results)

                return Response({
                    "status": "success",
                    "sql_queries": sql_query,
                    "data": global_results  # Ensure it matches the required list-of-tuples format
                }, status=status.HTTP_200_OK)

                
            else:
                return Response({"error": "Invalid database type"}, status=status.HTTP_400_BAD_REQUEST)
            
            if db_type == "Global":
                pass

            else:
                print(results)
                final_results = results
            
            return Response({
                "status": "success", 
                "sql_query": sql_query, 
                "data": final_results
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)










    def convert_to_sql(self, user_prompt, db_type):
        try:
            table_mapping = {
                "SQLite3": "sales_data_sqlite_fixed",
                "MYSQL": "mysql_salesdata",
                "PostgreSQL": "postgres_salesdata"
            }
            
            client = OpenAI(api_key='''''')
            
            if db_type == "Global":
                queries = {}
                
                for specific_db, table_name in table_mapping.items():
                    system_prompt = (
                        f"You are an expert SQL generator for {specific_db} databases. "
                        f"Convert the user query into a valid SQL statement using the table '{table_name}'. "
                        "Return ONLY the SQL query with no additional text, explanation, or markdown formatting."
                    )
                    
                    completion = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Convert this into {specific_db} SQL query: {user_prompt}"}
                        ]
                    )
                    
                    sql_query = completion.choices[0].message.content.strip()
                    sql_query = re.sub(r"^(SQL|sql):\s*", "", sql_query)
                    queries[specific_db] = sql_query
                
                print(f"Generated database-specific queries: {queries}")
                return queries
            
            elif db_type in table_mapping:
                table_name = table_mapping[db_type]
                system_prompt = (
                    f"You are an expert SQL generator for {db_type} databases. "
                    f"Convert the user query into a valid SQL statement using the table '{table_name}'. "
                    "Return ONLY the SQL query with no additional text, explanation, or markdown formatting."
                )
                
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Convert this into {db_type} SQL query: {user_prompt}"}
                    ]
                )
                
                sql_query = completion.choices[0].message.content.strip()
                sql_query = re.sub(r"^(SQL|sql):\s*", "", sql_query)
                return sql_query
            else:
                return f"Error: Invalid database type '{db_type}'"
        except Exception as e:
            return f"Error generating SQL: {str(e)}"
