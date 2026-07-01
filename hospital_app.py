import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Smart Hospital Navigator", page_icon="🏥")

st.title("🏥smart hospital navigator")

@st.cache_resource
def load_model(:
  with open("Hospital_Model.pkl", "rb") as: f
    return pickle.load(f)

bundle = load_model()

model = bundle['model']
scaler = bundle['scaler']
features = bundle['features']
cols_to_scale = bundle['cols_to_scale']
depr_map_inv = bundle['depr_map_inv']
gender_map = bundle['gender_map']
temperature_map = bundle['temperqature_map']
hr_map = bundle['hr_map']
dur_map = bundle['dur_map']
cc_map = bundle['cc_map']
