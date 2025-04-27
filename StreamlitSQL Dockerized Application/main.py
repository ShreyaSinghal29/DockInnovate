import streamlit as st
import psycopg2

# Modern and cleaner CSS styling
st.markdown("""
    <style>
        body {
            background-color: #eef2f7;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            color: #222;
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            margin-top: 10px;
        }
        .subtitle {
            color: #555;
            font-size: 24px;
            margin-bottom: 30px;
            text-align: center;
        }
        .card {
            background: #fff;
            border-radius: 12px;
            padding: 20px 30px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .data {
            font-size: 19px;
            line-height: 1.7;
            color: #333;
        }
        .data span {
            color: #1e90ff;
            font-weight: bold;
        }
        .error, .success, .warning {
            font-size: 18px;
            font-weight: 500;
            text-align: center;
            margin-top: 20px;
        }
        .error { color: #e74c3c; }
        .success { color: #27ae60; }
        .warning { color: #f39c12; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🚀 Streamlit + PostgreSQL Deployment</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Running inside Docker Containers</div>", unsafe_allow_html=True)

# Database credentials
DB_HOST = "postgres_container"   # Name of PostgreSQL container
DB_NAME = "testdb"                # Database name
DB_USER = "shreya"                # Username
DB_PASSWORD = "secret"            # Password

def fetch_data():
    """Connects to PostgreSQL and retrieves passenger data."""
    try:
        st.write("🔗 Establishing database connection...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        st.markdown("<div class='success'>✅ Connected Successfully!</div>", unsafe_allow_html=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passengers;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        st.markdown(f"<div class='error'>❌ Error: {str(e)}</div>", unsafe_allow_html=True)
        return []

# Fetching data from database
data = fetch_data()

# Displaying data
if data:
    st.subheader("📋 Retrieved Passenger Data:")
    for row in data:
        st.markdown(f"""
            <div class="card">
                <p class="data">
                🆔 <strong>ID:</strong> <span>{row[0]}</span><br>
                🧑 <strong>Name:</strong> <span>{row[1]}</span><br>
                📍 <strong>Location:</strong> <span>{row[2]}</span>
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<div class='warning'>⚠️ No records found in the passengers table.</div>", unsafe_allow_html=True)
