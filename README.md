# NLP Group Project
### Alberto Puentes, Parker Voit, Tyler Applegate
#### Florence Cohort, 2021_08_03
​
## Project Summary
​
The goal of this project was to try and identify which programming language was used in a GitHub repository by scraping their respective readme.md files and constructing a classification model that would 'accurately' predict the programming language.  We focused on repositories we knew utilized one of the following languages: a) JavaScript, b) Python, c) HTML or d) Shell.  After having scraped the readme.md contents of 120 repositories (30 per language), we prepared the data and, explored single word, bigram and trigram frequencies.  Throughout the exploration process we tried to identify key stop words and various word groupings that would enable our models to best predict the programming language.  In the end, we relied on IDF word rankings and culled scores below a determined threshold from our general dataframe.  The resulting culled data significantly improved our model performance.  Despite a clear overfit on our train dataset, our validation and test scores still showed our model outperforming the benchmark by 15-32%. 
​
In the end, it was our distance based models that outperformed the other classication models.  We found that the decision based classification models weren't flexible enough to weight their decisions across all of our selected languages.  The distance based algorithms did a much better job of performing across all target languages.  We chose and tested our K Nearest Neighbors classification model giving us 'accuracy' scores of 84%, 60% on our train and validate sets and a 43% accuracy score our our final test.  
​
### Project Objectives:
> - Deliver a Jupyter Notebook walkthrough, and slide presentation (no more than 5 minutes) that gives a high level overview of our project.
> - Document our planning, process (data aquisition, data preparation, data exploration, data visualizations, statistical testing, modeling, and model evaluation,) as well as all relevent findings and key takeaways from each step.
> - Develop modules (acquire.py, prepare.py, explore.py) to make this process repeatable.
> - Be prepared to answer follow-up questions about our methods, code, findings, model
​
### Business Goals:
> - Identify which programming language is being used, based upon data scraped from README files
> - Build a Machine Learning classification model that outperforms the baseline model to accuractely predict programming language.
> - Document our process so that it can be presented live, as well as read later like a report.
​
### Audience:
> - Codeup Data Science (Instructors, Support Staff, and Peers.)
​
### Deliverables:
> - Final Jupyter Notebook of our report.
> - One or two google slides, with well-labeled data visualizations
> - Live presenation of Jupyter Notebook and slides.
> - A link to the google slides
> - All modules required to replicate our project
> - .csv file that documents our predications along side actual values for programming language.
> - All necessary Jupyter Notebooks to document each stage of the DS Pipeline.
​
​
### Data Dictionary:
|Target|Datatype|Definition|
|:-------|:-------|:----------|
|language|object|Programming Language of README files: 'shell', 'python', 'JavaScript', 'html'|
​
|Feature|Datatype|Description|
|:-------|:-------|:----------|
|repo|object|literal url of the repository|
|readme_contents|object|the original contents of the README file|
|cleaned_readme_contents|object|the contents of the README file after going through 'basic_clean' function|
|stemmed_readme_contents|object|the contents of the README file after going through 'basic_clean' and 'stem' functions|
|lemmatized_readme_contents|object|the contents of the README file after going through 'basic_clean' and 'lemmatize' functions|
​
## Stages of DS Pipeline
Plan -> Data Acquisition -> Data Prep -> Exploratory Analysis -> ML Models -> Delivery
​
### Planning
- [x] Create README.md with data dictionary, project and business goals.
- [x] Acquire data from GitHub and create a series of functions to automate this process. Save the functions in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a series of functions to automate the process, store the functions in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtions.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [] Create csv file with the index, the actual programming language, and the model's prediction for programming language in our test dataset.
- [] Document conclusions, takeaways, and next steps in the Final Report Notebook.
​
### Data Acquistion
- [x] Identify 120 target GitHub repositories; 30 for each of our selected languages. 
- [x] Scrape readme.md contents from each of our selected GitHub repositiory and create a series of functions to automate this process. Save the functions in an acquire.py file to import into the Final Report Notebook.
- [x] The final function will return a pandas DataFrame.
- [x] Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- [x] Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, `.nunique()`, ...).
​
### Data Preparation
- [x] After initial exploration, drop null values and any observations containing foreign language.
- [x] Perform an initial prep that includes:
    * a basic cleaning that lower cased all words, normalized character encoding and removed any non alpha-numeric strings
    * identify and removed stopwords
    * utilized regex to remove noisy html language
    * Tok Tok tokenization, Porter stemming, and Word Net lemmatization of all data strings
- [x] Split data into train, validate, and test sets, stratified on the target variable 'language'
- [x] Document Key Findings & Takeaways, as well as possible routes to take after MVP / First Iteration
​
### Exploratory Analysis
- [x] Answer key questions and figure out the features that can be used in a classification model to best predict the target variable, programming language. 
- [x] Create visualizations of word, bigram and trigram frequencies. The goal is to identify features that clearly relate to a specific programming language (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- [x] Summarize our conclusions, provide clear answers to our specific questions, and summarize any takeaways/action plan from the work above.
- [x] Document further data preparation steps to be looked into after MVP / first iteration through the DS pipeline
​
### ML Models
- [x] Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- [x] Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters we use.
- [x] Compare evaluation metrics across all models and evaluate using our validate sets.
- [x] Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information?  Are there any alternative feature selection processes that could 
- [x] Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- [x] Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
​
### Delivery
> - Introduce ourselves and our project goals at the very beginning of my notebook walkthrough.
> - Summarize our findings at the beginning like I would for an Executive Summary. 
> - Walk Codeup Data Science Team through the analysis we did to answer our questions and that lead to our findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers we are analyzing as well as offer insights and recommendations based on our findings.
​
## Conclusions & Next Steps
​
​
## How to Reproduce this Project
> - You will need your own env file with credentials for the GitHub, along with these files to recreate our project:
    > - README.md
    > - acquire.py
    > - prepare.py 
    > - explore.py
    > - run the final_report.ipynb notebook
> - Libraries requiring install:
    > - Markdown
    > - BeautifulSoup
    > - Pandas
    > - Scikit-Learn
    > - NLTK
    > - 