# ![](https://github.com/BlakeWallace/AWS) AWS
#### 05/30/2025

---

<a id='creators'></a>

## Creators
  
[Blake Wallace](https://www.linkedin.com/in/blake-wallace)  

---

## Contents in README
[Creators](#creators)  
[Problem Statement](#problem-statement)  
[Contents in Project Repo](#repo-content)  
[Data Dictionary](#data-dictionary)  
[Executive Summary](#executive-summary)  
[Known Issues](#known-issues)  
[Future iterations/next steps](#next-steps)  
[Data Sources](#data-sources)  
[Sources](#sources)

---

<a id='problem-statement'></a>

## Problem Statement

#### Data Scinece Question

Work through the book Mastering Machine Learning on AWS.  

#### Project Objective

1. Explore Amazon Web Services (AWS)  
1. Build Machine Learning Models and run them through AWS  

#### Current Tasks

1. Complete Chapter 2, training a Document Classification algorithm.  
    1. Train six machine learning models for compairson (Three trained, three remaining to train)  
        1. Trained models:  
            1. Naive Bayes'  
            1. Logistic Regression  
            1. k-Nearest Neighbors  
        1. Models to train:  
            1. Classification and Regression Tree  
            1. Random Forest  
            1. Support Vector Machine
    1. Lift the document classifier into Amazon Web Services  
        1. Run the notebook through Sagemaker
        1. 

---

<a id='repo-content'></a>

## Contents in Project Repo
1. [Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes](https://github.com/BlakeWallace/Exploring_AWS/tree/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes)  
    1. [Data](https://github.com/BlakeWallace/Exploring_AWS/tree/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/data)  
        1. [location_of_data.md](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/data/location_of_data.md) 
        1. [democrats.csv](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/data/democrats.csv)
        1. [republicans.csv](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/data/republicans.csv)
        1. [text_data.csv](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/data/text_data.csv)
    1. Functions Used Throughout  
        1. [bnaivebayes.py](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/bnaivebayes.py)  
        1. [datacleaning.py](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/datacleaning.py)  
        1. [readtextfunctions.py](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/readtextfunctions.py)  
    1. Data Cleaning  
        1. [sentence_tokenization.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/sentence_tokenization.ipynb)  
        1. [pos_tagging.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/pos_tagging.ipynb)  
    1. Main Work  
        1. [document_classification.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/document_classification.ipynb)  
    1. Side Work
        1. [Classification_and_the_NB_Algorithm.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/Classification_and_the_NB_Algorithm.ipynb)  
        1. [collect_text_data.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Ch2_Classifying_Twitter_Feeds_with_Naive_Bayes/collect_text_data.ipynb)  
1. [.gitignore](https://github.com/BlakeWallace/Exploring_AWS/blob/master/.gitignore)  
1. [README.md](https://github.com/BlakeWallace/Exploring_AWS/blob/master/README.md)  
1. [aws_ml_setup.ipynb](https://github.com/BlakeWallace/Exploring_AWS/blob/master/aws_ml_setup.ipynb)  
1. [order_of_building_aws_account.md](https://github.com/BlakeWallace/Exploring_AWS/blob/master/order_of_building_aws_account.md)  
---

<a id='data-dictionary'></a>

## Data Dictionary

#### NOTE: THIS IS INACURATE, AND DOES NOT MATCH THE INFORMATION IN THE CURRENT REPO!
A few notes regarding the primary dataset used for modeling:
1. The primary dataset for analysis to answer the data science questions is labeled [data_for_analysis](https://github.com/BlakeWallace/Project_Pigskin/blob/master/Data/data_for_analysis.csv).  
1. When reading through a notebook, any data that is put into this dataset is labeled `'stuff_to_keep'`.  Once this point is reached inside a notebook, the data that follows is munged, cleaned, engineered, or explored to be included in the primary dataset for analysis.  In all cases the data is later renamed to be included to the [data_for_analysis](https://github.com/BlakeWallace/Project_Pigskin/blob/master/Data/data_for_analysis.csv) dataset.

**Our primary [data_for_analysis](https://github.com/BlakeWallace/Exploring_AWS/blob/master/Data/data_for_analysis.csv) will be displayed in the following table.  At the moment, this is a template data table that is not currently holding any relevant data for this project.**

<div align="left"> 
    
|Feature (Bin #)|Description|
|---|---|
file_name|Name of .wav Audio File
class|Emergency or Non-Emergency
emergency_type|Description of Situation
origin|Broadcastify or YouTube
good_exception|Whether or not Speech Detection API detected audio or not
audio_recognition|Speech-to-Text of the Audio Clip
tempogram_#|Tempo
spectral_contrast_#|Spectral Contrast
chroma_cens_#|Chroma Feature Normalized
spectral_centroid|Spectral Centroid
spectral_band|Spectral Bandwidth
spectral_flat|Spectral Flatness
rolloff|Spectral Rolloff
chroma_cqt_#|Chroma Continuous Q Transform
tonnetz_#|Tonnetz
contrast_#|Spectral Contrast
mel_#|Mel Scale
chroma_stft_#|Chroma Short Time Fourier Transform
mfcc_#|Mel Frequency Cepstrum
preds|Model Prediction of Class

</div>

---

<a id='executive-summary'></a>

## Executive Summary



---

<a id='known-issues'></a>

## Known Issues



---

<a id='next-steps'></a>

## Future iterations/next steps



---

<a id='data-sources'></a>

## Data Sources

1. [Text Classification on Emails](https://www.kaggle.com/datasets/dipankarsrirag/topic-modelling-on-emails)   
  
---

<a id='sources'></a>

## Sources

