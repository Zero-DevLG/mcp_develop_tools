import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import pymysql
from pymysql.cursors import DictCursor
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()


# Crea instancia de MCP 
app = FastMCP("company-db-server")

# Conexión base de datos
def get_db_connection():
    conn = pymysql.connect(
        host = os.environ.get("DB_HOST"),
        port = int(os.environ.get("DB_PORT")),
        user = os.environ.get("DB_USER"),
        password = os.environ.get("DB_PASSWORD"),
        database = os.environ.get("DB_DATABASE"),
        cursorclass=DictCursor
    )
    return conn

@app.tool
def list_expenses(limit: int = 5) -> List[Dict[str, Any]]:
    """Listar gastos"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            """
            SELECT id, uid, operator_id, operator_account_id,expense_user_id,created_at
            FROM expenses
            ORDER By id
            LIMIT %s
            """,(limit,))
        rows = cursor.fetchall()
        
        expenses = []
        
        for row in rows:
            expenses.append({
                "id":                   row['id'],
                "uid":                  row['uid'],
                "operator_id":          row['operator_id'],
                "operator_account":     row['operator_account_id'],
                "expense_user_id":      row['expense_user_id'],
                "created_at":            str(row['created_at'])
            })
            
        cursor.close()
        conn.close()
        
        return expenses
    except Exception as e:
        raise RuntimeError(f"Error al obtener los gastos: {e}") from e

if __name__ == "__main__":
    app.run(transport="sse", host="0.0.0.0", port=3000)