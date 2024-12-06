
from calendar import day_abbr
from matplotlib.pyplot import xlabel
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


with st.sidebar:
    menu = option_menu(None, ['Main', 'Cool App'], 
    icons =['house', 'building'] )


# a simple method to create some basic features on an SFrame
# def create_count_features(sf):
#     sf['num_images'] = sf['images'].apply(lambda x: len(x))
#     sf['num_links'] = sf['links'].apply(lambda x: len(x))
#     sf['num_tags'] = sf['tags'].apply(lambda x: len(x))
#     sf['num_attr'] = sf['attr'].apply(lambda x: len(x))
#     #sf['num_clean_chars'] = sf['text_clean'].apply(lambda x: len(x))
#     return sf


# # Split links on parts
# def create_link_features(sf):
#     #sf['text_links'] = sf['links'].apply(lambda x: ' '.join(filter(None, '/'.join(x).split('/'))))
#     sf['text_links'] = sf['links'].apply(lambda x: ' '.join(filter(None, re.sub('[^a-zA-Z]', '/', '/'.join(x)).split('/'))))
#     return sf


# # Split image links/paths on parts
# def create_img_features(sf):
#     sf['text_img'] = sf['images'].apply(lambda x: ' '.join(filter(None, re.sub('[^a-zA-Z0-9]', '/', '/'.join(x)).split('/'))))
#     return sf


# # a simple method to clean the text within an html response
# def clean_text(t):
#     ct = t.apply(lambda x: re.sub(r'[\n\t,.:;()\-\/]+', ' ', ' '.join(x)))
#     ct = ct.apply(lambda x: re.sub(r'\s{2,}', ' ', x))
#     ct = ct.apply(lambda x: x.strip())
#     return ct


# def clean_attributes(sf):
#     sf['attr'] = sf['attr'].apply(lambda x: re.sub(r'[^a-zA-Z0-9]+', ' ', x))
#     return sf


# # a wrapper method around the 2 methods above
# def process_dataframe(sf):
#     #sf['text'] = clean_text(sf['text'])
#     sf['title'] = clean_text(sf['title'])
#     sf['header'] = clean_text(sf['header'])
#     sf['meta'] = clean_text(sf['meta'])
#     sf['lists'] = clean_text(sf['lists'])
#     sf['meta_property'] = clean_text(sf['meta_property'])
#     sf['meta_name'] = clean_text(sf['meta_name'])
#     sf['links_visible_text'] = clean_text(sf['links_visible_text'])
#     sf['links_parents'] = sf['links_parents'].apply(lambda x: ' '.join([''] + x).strip())

#     sf = create_count_features(sf)
#     sf = create_link_features(sf)
#     sf = create_img_features(sf)
#     #sf = clean_attributes(sf)
#     return sf