import streamlit as st
from Time import Date
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from Endpoints import Leetcode

def get_columns():
  c = 0

  with open('cols.txt', 'r') as file:
    c = file.read()
    c = int(c.strip())

  return c

def set_columns(col):
  with open('cols.txt', 'w') as file:
    file.write(col)

def get_data():
  COLUMNS = get_columns()
  
  conn = st.experimental_connection('gsheets', type=GSheetsConnection)
  
  data = conn.read(worksheet='II', usecols=list(range(COLUMNS)), ttl=60)
  data.dropna(how='all', inplace=True)

  return conn, data

def fetch_data():
  conn, data = get_data()

  usernames = data['Username']
  curr_count = []

  for username in usernames:
    total = Leetcode(username)
    curr_count.append(total)

  return conn, data, pd.Series(curr_count)

def merge_data():
  conn, existing_data, curr_count = fetch_data()

  date = Date().strip()

  if date in not existing_data.columns:
    set_columns(len(existing_data.columns) + 1)

  existing_data[date] = curr_count

  conn.update(worksheet='II', data=existing_data)

  st.success('Data Fetched and Updated... Please Verify...')

fetch = st.button('Update/Fetch Data')

if fetch:
  merge_data()
  
    
