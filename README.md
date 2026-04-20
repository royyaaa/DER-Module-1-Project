# Data Engineering Module 1 Assignment

This repository was created to fulfill the Data Engineering Module 1 assignment at UIII. This project was completed by:
-	**Selvi Oktaviani (05212510001)**
-	**Nikhla Isfa Khuraiya (05212510002)**

## Introduction
The rapid development of digital technology and the increasingly widespread use of smartphones have transformed the way people consume information. Today, individuals tend to spend hours accessing various digital platforms, especially social media and video streaming services such as YouTube. This condition has led to the emergence of a phenomenon known as doomscrolling, which refers to the habit of continuously consuming content without time control.

The phenomenon of doomscrolling not only affects how people use their time but also has the potential to reduce individuals' cognitive quality. One of the impacts that has been increasingly discussed is brainrot, a condition characterized by decreased focus and mental fatigue due to excessive consumption of digital content.

In daily life, this phenomenon can be observed when individuals find it difficult to detach themselves from digital devices, even in situations such as traveling or engaging in social interactions. As a result, individuals become less aware of their surroundings and experience a decline in their ability to concentrate for extended periods.

As this phenomenon continues to grow, various types of content discussing doomscrolling and brainrot have also emerged on YouTube. This indicates an increasing level of public awareness regarding the negative impacts of digital content consumption.

Therefore, this study aims to analyze the level of public awareness of the brainrot and doomscrolling phenomena through the characteristics of YouTube content. By utilizing data from the YouTube Data API, this research will explore patterns such as view counts, user engagement, and the distribution of video publication times to better understand how these topics are developing within society. 

## What Did We Do?
In this project, we aim to analyze public awareness of the brainrot and doomscrolling phenomena by analyzing the trend in the number of brainrot-related videos and their view counts over time. This analysis is intended to provide insights into how significant the level of awareness is regarding the brainrot and doomscrolling phenomena among audiences.

## What Data Did We Use?
The data used in this analysis was collected from YouTube based on specific keywords and regions. Below is the data structure used in this project:
| Variable | Descriptions |
|---------|------------|
| videoId | The unique ID of each video |
| title | The title of the video |
| channel | The channel that published the video |
| views | The number of views of the video |
| like | The number of likes on the video |
| comments | The number of comments on the video |
| publishedAt | The publication date of the video |
| duration | The duration of the video |
| region | Indicates the region where the content is popular or recommended |

The regions used in this project are Indonesia (ID), Malaysia (MY), and Singapore (SG). These regions were selected due to their geographical proximity, as well as similarities in language and cultural context with Indonesia.

The keywords used in this project are "how to stop brainrot","digital detox" "reduce screen time","stop scrolling addiction","doom scrolling". Based on the selected keywords and regions, the total of data were collecting is 1548 data. However, after the data cleaning process, 1314 observations were retained and considered suitable for further analysis.

## How Was the Process Conducted?
The workflow of this project consists of the following steps:
1.	Data Acquisition: Fetching data using the YouTube API.
2.	Data Cleaning: Removing irrelevant content based on video titles and eliminating duplicate data.
3.	Analysis: Conducting a simple Exploratory Data Analysis (EDA).

## Additional Information
Below is the file structure and the location of key components in this project:
1.	Data Fetching Code: project_module1/fetch_data.py (for fetching the data) and project_module1/save_data.py (for saving the data that we have fetched)
2.	Data Cleaning Code: project_module1/preprocess.py
3.	EDA code: project_module1/eda.py
4.  Main code: we do have 2 main code files. The one is for fetching the Data, and the one more is for running the rest. Bot files are stored in main folder. The files names is scripts.py (the main one) and fetch_one.py (the main script for fetching data).
5.  Reports data: Any reports, explanations and findings of this project are available in reports/

## DISCALIMERS
Notably, during project initialization using Cookiecutter Data Science (CCDS), no folder named `src` was generated, despite its common importance in project structure. This is because the current version of CCDS no longer creates a `src` directory by default. Instead, the source code directory is named based on the defined module_name, which in this repository is `project_module1`

## References
Oxford University (2024) ‘Brain rot’ named Oxford Word of the Year 2024. Oxford University Press, Language and Literacy. https://corp.oup.com/news/brain-rot-named-oxford-word-of-the-year-2024/

Özbay, Ö. ‘Brain Rot’ Among University Students in the Digital Age: A Phenomenological Study. Curr Psychiatry Rep 28, 11 (2026). https://doi.org/10.1007/s11920-025-01658-w 
