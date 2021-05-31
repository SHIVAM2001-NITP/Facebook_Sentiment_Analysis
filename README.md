# machine_learning



Facebook-Sentiment analysis in python

Sentiment analysis - It is the automated process of understanding an opinion about a given subject from written or spoken language.
 
Reference: Google
Assume I want to Predict sentiment of a person based on his/her updates on very commonly used social media platform - Facebook.
Individual on an average posts almost 100 status in a year on a social media, we would look at his/her social media profile and predict his/her sentiment by counting number of positive, negative and neutral status updates.
Let’s assume : 80 out of total 100 posts are negative then we can infer that person is not happy person or assume 90 out of total 100 posts are joyful then we can infer that person is a happy person.
Algorithm:
1.	Download all Facebook status updates of a person.
2.	Analyze them by looking at their sentiment of individual status update.
Algorithm is divided in 2 parts
Part A:
1.	Download Facebook data from your account settings (as shown in figure).This will include all the information like comments, likes, posts, etc.
2.	Store the data (on which you want to predict sentiment of a person)in excel file. It is Posts shared by person , in my case.

 
Download Facebook data
Part B:
1.	Import libraries.
Pandas - Provide data structure that are easy for data analysis.
nltk- It is used to process human language and provides sentiment analysis of data considered.
VADER- It not only takes into account the sentiment of a data but also tells it’s intensity i.e. what percent of sentiment is true.
Example :
If statement is : I’m very very happy today.
It’s sentiment intensity would be 90% positive.

 
Python libraries
2. Convert excel sheet to data frame.

 
Parse data in excel sheet
3. Perform Preprocessing of data frames
This is required because there are chances that excel sheet contains some blank fields so we want to remove those fields.

 
Preprocessing
4. Analyze data

 
Predict sentiment scores

 
Output
Conclusion:
We learn how to extract required data from Facebook, and analyze it to predict the sentiment of status updates by using different relevant libraries in python.
