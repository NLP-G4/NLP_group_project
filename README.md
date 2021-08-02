# NLP Group Project
### Alberto Puentes, Parker Voit, Tyler Applegate
#### Florence Cohort, 2021_08_03

## Project Summary

### Project Objectives:
> - Deliver a Jupyter Notebook walkthrough, and slide presentation (no more than 5 minutes) that gives a high level overview of our project.
> - Document our planning, process (data aquisition, data preparation, data exploration, data visualizations, statistical testing, modeling, and model evaluation,) as well as all relevent findings and key takeaways from each step.
> - Develop modules (acquire.py, prepare.py, explore.py) to make this process repeatable.
> - Be prepared to answer follow-up questions about our methods, code, findings, model

### Business Goals:
> - Identify which programming language is being used, based upon data scraped from README files
> - Build a Machine Learning classification model that outperforms the baseline model to accuractely predict programming language.
> - Document our process so that it can be presented live, as well as read later like a report.

### Audience:
> - Codeup Data Science (Instructors, Support Staff, and Peers.)

### Deliverables:
> - Final Jupyter Notebook of our report.
> - One or two google slides, with well-labeled data visualizations
> - Live presenation of Jupyter Notebook and slides.
> - A link to the google slides
> - All modules required to replicate our project
> - .csv file that documents our predications along side actual values for programming language.
> - All necessary Jupyter Notebooks to document each stage of the DS Pipeline.

### Project Context:
> - This data was scraped from github, under the topic of 'awesome'
> - 30 README filesw were downloaded in each of the following languages, to give us a data set of 120: (java, python, shell, and HTML)

### Data Dictionary:
|Target|Datatype|Definition|
|:-------|:-------|:----------|

|Feature|Datatype|Description|
|:-------|:-------|:----------|

### Initial Hypothoses:
> - Hypothosis 1 - 
> - $H_0$: 
> - $H_a$: 
> - Hypothosis 2 - 
> - $H_0$: 
> - $H_a$: 
> - Hypothosis 3 - 
> - $H_0$: 
> - $H_a$: 

## Executive Summary

## Stages of DS Pipeline
Plan -> Data Acquisition -> Data Prep -> Exploratory Analysis -> ML Models -> Delivery

### Planning
- [] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [] Acquire data from GitHub and create a series of functions to automate this process. Save the functions in an acquire.py file to import into the Final Report Notebook.
- [] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a series of functions to automate the process, store the functions in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtions.
- []  Clearly define three hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [] Establish a baseline accuracy and document well.
- [] Train three different classification models.
- [] Evaluate models on train and validate datasets.
- [] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [] Create csv file with the index, the actual programming language, and the model's prediction for programming language in our test dataset.
- [] Document conclusions, takeaways, and next steps in the Final Report Notebook.

### Data Acquistion
- [] Store functions that are needed to acquire data from GitHub; make sure the acquire.py module contains the necessary imports to run our code.
- [] The final function will return a pandas DataFrame.
- [] Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- [] Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, `.nunique()`, ...).

### Data Prep

### Exploratory Analysis
- [] Answer key questions, our hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, programming language. 
- [] Run at least 2 statistical tests in data exploration. Document our hypotheses, set an alpha before running the tests, and document the findings well.
- [] Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to programming language (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- [] Summarize our conclusions, provide clear answers to our specific questions, and summarize any takeaways/action plan from the work above.

### ML Models
- [] Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- [] Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters we use.
- [] Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- [] Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- [] Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- [] Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

### Delivery
> - Introduce ourselves and our project goals at the very beginning of my notebook walkthrough.
> - Summarize our findings at the beginning like I would for an Executive Summary. 
> - Walk Codeup Data Science Team through the analysis we did to answer our questions and that lead to our findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers we are analyzing as well as offer insights and recommendations based on our findings.

## How to Reproduce this Project
> - You will need your own env file with credentials for the GitHub, along with these files to recreate our project:
    > - README.md
    > - acquire.py
    > - prepare.py 
    > - explore.py
    > - run the final_report.ipynb notebook