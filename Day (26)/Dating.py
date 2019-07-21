# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:33:45 2019

@author: Sahil
"""

"""

Q2. Code Challenge (Connecting Hearts)


Downlaod Link: http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/Resource.zip

What influences love at first sight? (Or, at least, love in the first four minutes?) This dataset was compiled by Columbia Business School Professors Ray Fisman and Sheena Iyengar for their paper Gender Differences in Mate Selection: Evidence from a Speed Dating Experiment.

Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.


What does a person look for in a partner? (both male and female)


For example: being funny is more important for women than man in selecting a partner! Being sincere on the other hand is more important to men than women.

    What does a person think that their partner would look for in them? Do you think what a man thinks a woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

    Plot Graphs for:
            How often do they go out (not necessarily on dates)?
            In which activities are they interested?
    
    If the partner is from the same race are they more keen to go for a date?
    What are the least desirable attributes in a male partner? Does this differ for female partners?
    How important do people think attractiveness is in potential mate selection vs. its real impact?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('Dating_Data.csv',encoding='windows 1252')   

#dataset = pd.read_csv('Dating_Data.csv',encoding='ISO-8859-1')      #unicode error
#dataset = pd.read_csv('Dating_Data.csv',encoding='utf-8')


dataset.isnull().any(axis=0)  

#dataset = dataset.copy().dropna(how='any',axis = 0)   




"""
#Graph - How often do they go out (not necessarily on dates)?

go out:
How often do you go out (not necessarily on dates)?
	Several times a week=1
	Twice a week=2
	Once a week=3
	Twice a month=4
	Once a month=5
	Several times a year=6
	Almost never=7
"""

go_out = dataset['go_out']
go_out = go_out.dropna()   
go_out_count = go_out.value_counts()
go_out_count.plot.bar()

"""
labels = go_out_count.index
sizes = go_out_count.values
sizes.plot.bar()
plt.pie(sizes,  labels=labels,  autopct='%1.1f%%', startangle=0)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
"""





""" 
#Graph - In which activities are they interested?
How interested are you in the following activities, on a scale of 1-10?
sports: Playing sports/ athletics
tvsports: Watching sports
excersice: Body building/exercising
dining: Dining out
museums: Museums/galleries
art: Art
hiking:  Hiking/camping
gaming: Gaming
clubbing: Dancing/clubbing
reading: Reading
tv: Watching TV
theater: Theater
movies: Movies
concerts: Going to concerts
music: Music
shopping: Shopping
yoga: Yoga/meditation

"""
go_out = dataset['go_out']
go_out = go_out.dropna()   
go_out_count = go_out.value_counts()
go_out_count.plot.bar()
  

