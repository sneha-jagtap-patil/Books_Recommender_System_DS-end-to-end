# from books_recommender.logger import log

# log.logging.info("Starting the books recommender system application.")

import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException



class Recommendation:
    def __init__(self,app_config = AppConfiguration()):
        try:
            self.recommendation_config= app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    
    def fetch_poster(self,suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
            final_rating =  pickle.load(open(self.recommendation_config.final_rating_serialized_objects,'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]: 
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url
        
        except Exception as e:
            raise AppException(e, sys) from e
        
