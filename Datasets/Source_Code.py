# imports 
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


# parse the data files as html to datasets.
with open("Datasets/2008_honda_accord", "r", encoding="utf-8", errors="ignore") as file:
    honda_accord_2008_file = file.read()
    
with open("Datasets/2009_honda_accord", "r" , encoding="utf-8", errors="ignore") as file:
    honda_accord_2009_file = file.read()
    
with open("Datasets/2009_hyundai_sonata", "r", encoding="utf-8", errors="ignore") as file:
    hyundai_sonata_2009_file = file.read()
    
with open("Datasets/2009_toyota_corolla", "r", encoding="utf-8", errors="ignore") as file:
    toyota_corolla_2009_file = file.read()


#exclusion criteria in reading the file
def is_excluded(tag):
    return tag.name != 'docno'



# send honda accord 2008 data frame to notebook
def send_honda_accord_2008_data():
    
    honda_accord_2008_dict = {} # dictionary to house the data  
    
    Honda_accord_2008_soup = BeautifulSoup(honda_accord_2008_file, 'html.parser')  #read the file as HTML
    unique_tags = set(tag.name for tag in Honda_accord_2008_soup.find_all(is_excluded)) # get the unique tags

    # Loop through the unique tags
    for tag_name in unique_tags:
        tag_instances = Honda_accord_2008_soup.find_all(tag_name)         # Find all instances of the tag
        tag_data = [tag.get_text() for tag in tag_instances] # get tag content and store it in a list
        honda_accord_2008_dict[tag_name] = tag_data # Store the data in the dictionary

    # Create a DataFrame from the dictionary
    honda_df_08 = pd.DataFrame(honda_accord_2008_dict)

    # return data
    return honda_df_08 



# send honda accord 2009 data frame to notebook
def send_honda_accord_2009_data():   
    
    honda_accord_2009_dict = {} # dictionary to house the data
    
    Honda_accord_2009_soup = BeautifulSoup(honda_accord_2009_file, 'html.parser') #read the file as HTML
    unique_tags = set(tag.name for tag in Honda_accord_2009_soup.find_all(is_excluded)) # get the unique tags
    
    # Loop through the unique tags
    for tag_name in unique_tags:
        tag_instances = Honda_accord_2009_soup.find_all(tag_name)         # Find all instances of the tag
        tag_data = [tag.get_text() for tag in tag_instances] # get tag content and store it in a list
        honda_accord_2009_dict[tag_name] = tag_data # Store the data in the dictionary

    # Create a DataFrame from the dictionary
    honda_df_09 = pd.DataFrame(honda_accord_2009_dict)

    # return data
    return honda_df_09
    
    

# send hyundai sonata 2009 data frame to notebook
def send_hyundai_sonata_2008_data():
        
    hyundai_sonata_2009_dict = {} # dictionary to house the data
    
    hyundai_sonata_2009_soup = BeautifulSoup(hyundai_sonata_2009_file, 'html.parser') #read the file as HTML
    unique_tags = set(tag.name for tag in hyundai_sonata_2009_soup.find_all(is_excluded)) # get the unique tags
    
    # Loop through the unique tags
    for tag_name in unique_tags:
        
        tag_instances = hyundai_sonata_2009_soup.find_all(tag_name)         # Find all instances of the tag
        tag_data = [tag.get_text() for tag in tag_instances] # get tag content and store it in a list
        hyundai_sonata_2009_dict[tag_name] = tag_data # Store the data in the dictionary

    # Create a DataFrame from the dictionary
    hyundai_sonata_df_09 = pd.DataFrame(hyundai_sonata_2009_dict)

    # return data
    return hyundai_sonata_df_09 
      
      

# send toyota corolla 2009 data frame to notebook
def send_toyota_corolla_2009_data(): 
    
    toyota_corolla_2009_dict = {} # dictionary to house the data
    
    toyota_corolla_2009_soup = BeautifulSoup(toyota_corolla_2009_file, 'html.parser') #read the file as HTML
    unique_tags = set(tag.name for tag in toyota_corolla_2009_soup.find_all(is_excluded)) # get the unique tags
    
    # Loop through the unique tags
    for tag_name in unique_tags:
        
        tag_instances = toyota_corolla_2009_soup.find_all(tag_name)         # Find all instances of the tag
        tag_data = [tag.get_text() for tag in tag_instances] # get tag content and store it in a list
        toyota_corolla_2009_dict[tag_name] = tag_data # Store the data in the dictionary

    # Create a DataFrame from the dictionary
    toyota_corolla_df_09 = pd.DataFrame(toyota_corolla_2009_dict)

    # return data
    return toyota_corolla_df_09 
    