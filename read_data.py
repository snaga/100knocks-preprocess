import pandas as pd
import numpy as np


df_customer = pd.read_csv('data/customer.csv',
                          dtype={
                              'customer_id': str,
                              'customer_name': str,
                              'gender_cd': str,
                              'age': np.int64,
                              'postal_cd': str,
                              'address': str,
                              'application_store_cd': str,
                              'application_date': str,
                              'status_cd': str},
                          parse_dates=['birth_day'])

df_customer['birth_day'] = df_customer['birth_day'].dt.date

df_category = pd.read_csv('data/category.csv', dtype=str)

df_product = pd.read_csv('data/product.csv',
                         dtype={
                             'product_cd': str,
                             'category_major_cd': str,
                             'category_medium_cd': str,
                             'category_small_cd': str,
                             'unit_price': np.float64,
                             'unit_cost': np.float64})

df_receipt = pd.read_csv('data/receipt.csv',
                         dtype={
                             'sales_ymd': np.int64,
                             'sales_epoch': np.int64,
                             'store_cd': str,
                             'receipt_no': np.int64,
                             'receipt_sub_no': np.int64,
                             'customer_id': str,
                             'product_cd': str,
                             'quantity': np.int64,
                             'amount': np.int64})

df_store = pd.read_csv('data/store.csv',
                       dtype={
                           'store_cd': str,
                           'store_name': str,
                           'prefecture_cd': str,
                           'prefecture': str,
                           'address': str,
                           'address_kana': str,
                           'tel_no': str,
                           'longitude': np.float64,
                           'latitude': np.float64,
                           'floor_area': np.float64})

df_geocode = pd.read_csv('data/geocode.csv',
                         dtype={
                             'postal_cd': str,
                             'prefecture': str,
                             'city': str,
                             'town': str,
                             'street': str,
                             'address': str,
                             'full_address': str,
                             'longitude': np.float64,
                             'latitude': np.float64})
