#!/usr/bin/env python
# coding: utf-8

# In[340]:


# Add the dependencies.
import pandas as pd
import os 
import numpy as np


# In[341]:


# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")


# In[342]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[343]:


student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[344]:


#school_data_complete_df: is a combinded data set that has 9th grade at Thomas High reading and math scores
#school_data_complete: is a combinded data set that has nan for reading and math scores of 9th grade at Thomas High
#merge school and student data sets
school_data_complete = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[345]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[346]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[347]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[348]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[349]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[350]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[351]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[352]:


# Determine data types for the school DataFrame.
school_data_df.dtypes


# In[353]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[354]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[355]:


# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
student_data_df.head()


# In[356]:


#school_data_complete_df: is a combinded data set that has 9th grade at Thomas High reading and math scores
#school_data_complete: is a combinded data set that has nan for reading and math scores of 9th grade at Thomas High
#switch reading scores to nan for 9th grades at Thomas High School
df = school_data_complete
mask = (df['school_name']=="Thomas High School" ) & (df['grade']=="9th")
mask
df['reading_score'] = np.where(mask, np.nan, df['reading_score'])
df['reading_score'].mean()


# In[357]:


(df['grade']=="9th")


# In[358]:


df.tail(10)


# In[359]:


#switch math scores to nan for 9th grades at Thomas High School
df['math_score'] = np.where(mask, np.nan, df['math_score'])
df['math_score'].mean()


# In[360]:


#school_data_complete_df: is a combinded data set that has 9th grade at Thomas High reading and math scores
#school_data_complete: is a combinded data set that has nan for reading and math scores of 9th grade at Thomas High
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[361]:


# Get the total number of students.
student_count = school_data_complete_df["Student ID"].count()
student_count


# In[362]:


# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# In[363]:


# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# In[364]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[365]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[366]:


# Calculate the average reading score. With nan substitutted.
average_reading_score_nan = school_data_complete["reading_score"].mean()
average_reading_score_nan


# In[367]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[368]:


# Calculate the average math score. With nan substitutted.
average_math_score_nan = school_data_complete["math_score"].mean()
average_math_score_nan


# In[369]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[370]:


# Get all the students who are passing math in a new DataFrame. With nan substitutted.
passing_math_nan = school_data_complete[school_data_complete["math_score"] >= 70]


# In[371]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]


# In[372]:


# Get all the students that are passing reading in a new DataFrame. With nan substitutted.
passing_reading_nan = school_data_complete[school_data_complete["reading_score"] >= 70]


# In[373]:


# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()

print(passing_math_count)
print(passing_reading_count)


# In[374]:


# Calculate the number of students passing math. With nan substitutted.
passing_math_count_nan = passing_math_nan["student_name"].count()

# Calculate the number of students passing reading. With nan substitutted.
passing_reading_count_nan = passing_reading_nan["student_name"].count()

print(passing_math_count_nan)
print(passing_reading_count_nan)


# In[375]:


# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100

print(passing_math_percentage)
print(passing_reading_percentage)


# In[376]:


# Calculate the percent that passed math. With nan subsitutted.
passing_math_percentage_nan = passing_math_count_nan / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage_nan = passing_reading_count_nan / float(student_count) * 100

print(passing_math_percentage_nan)
print(passing_reading_percentage_nan)


# In[377]:


# Calculate the overall passing percentage.
overall_passing_percentage = (passing_math_percentage + passing_reading_percentage ) / 2

print(overall_passing_percentage)


# In[378]:


# Calculate the overall passing percentage.
overall_passing_percentage_nan = (passing_math_percentage_nan + passing_reading_percentage_nan ) / 2

print(overall_passing_percentage_nan)


# In[379]:


# Adding a list of values with keys to create a new DataFrame.Creating the district summary.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[380]:


# Adding a list of values with keys to create a new DataFrame. Creating the district summary with nan substitutted.
district_summary_df_nan = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score_nan,
          "Average Reading Score": average_reading_score_nan,
          "% Passing Math": passing_math_percentage_nan,
         "% Passing Reading": passing_reading_percentage_nan,
        "% Overall Passing": overall_passing_percentage_nan}])
district_summary_df_nan


# In[381]:


# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100


# In[382]:


passing_math_count = 29370
total_student_count = 39170


# In[383]:


# Call the function.
passing_math_percent(passing_math_count, total_student_count)


# In[384]:


# Using the format() function.
my_grades = [92.34, 84.56, 86.78, 98.32]

for grade in my_grades:
    print("{:.0f}".format(grade))


# In[385]:


# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]


# In[386]:


# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]


# In[387]:


# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[388]:


district_summary_df


# In[389]:


# Determine the school type.
school_types = school_data_df.set_index(["school_name"])["type"]
school_types


# In[390]:


# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(school_types)
df


# In[391]:


# Calculate the total student count.
per_school_counts = school_data_df["size"]
per_school_counts


# In[392]:


# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# In[393]:


# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts


# In[394]:


# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget


# In[395]:


# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[396]:


# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]
student_school_math


# In[397]:


# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages


# In[398]:


# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages


# In[399]:


# Calculate the average math scores with nan substituted 
per_school_averages = school_data_complete.groupby(["school_name"]).mean()
per_school_averages


# In[400]:


# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]


# In[401]:


# Calculate the average test scores. With nan substitutted
per_school_math_nan = school_data_complete.groupby(["school_name"]).mean()["math_score"]

per_school_reading_nan = school_data_complete.groupby(["school_name"]).mean()["reading_score"]


# In[402]:


# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
per_school_passing_math.head()


# In[403]:


# Calculate the passing scores by creating a filtered DataFrame. With nan substituted 
per_school_passing_math_nan = school_data_complete[(school_data_complete["math_score"] >= 70)]

per_school_passing_reading_nan = school_data_complete[(school_data_complete["reading_score"] >= 70)]
per_school_passing_math_nan.tail()


# In[404]:


# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading


# In[405]:


# Calculate the number of students passing math and passing reading by school.With nan substituted 
per_school_passing_math_nan = per_school_passing_math_nan.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading_nan = per_school_passing_reading_nan.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading_nan


# In[406]:


# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
per_school_passing_math


# In[407]:


# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math_nan = per_school_passing_math_nan / per_school_counts * 100

per_school_passing_reading_nan = per_school_passing_reading_nan / per_school_counts * 100
per_school_passing_math_nan


# In[408]:


# Calculate the overall passing percentage.
per_overall_passing_percentage = (per_school_passing_math + per_school_passing_reading ) / 2
per_overall_passing_percentage


# In[409]:


# Calculate the overall passing percentage. With nan substitutted
per_overall_passing_percentage_nan = (per_school_passing_math_nan + per_school_passing_reading_nan ) / 2
per_overall_passing_percentage_nan


# In[410]:


# Adding a list of values with keys to create a new DataFrame. Creating the school summary.

per_school_summary_df = pd.DataFrame({
             "School Type": school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.tail()


# In[411]:


# Adding a list of values with keys to create a new DataFrame. Creating the school summary with nan substitutted.

per_school_summary_df = pd.DataFrame({
             "School Type": school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math_nan,
           "Average Reading Score": per_school_reading_nan,
           "% Passing Math": per_school_passing_math_nan,
           "% Passing Reading": per_school_passing_reading_nan,
           "% Overall Passing": per_overall_passing_percentage_nan})
per_school_summary_df.tail()


# In[412]:


# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# Display the data frame
per_school_summary_df.head()


# In[413]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[414]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[415]:


# Create a grade level DataFrames.
ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]

tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]

eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]

twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]
ninth_graders


# In[416]:


# Group each school Series by the school name for the average math score.
ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]

tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]

eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]

twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_grade_math_scores


# In[417]:


# Group each school Series by the school name for the average reading score.
ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]

tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]

eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]

twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]
twelfth_grade_reading_scores


# In[418]:


# Combine each Series for average math scores by school into single DataFrame.
math_scores_by_grade = pd.DataFrame({
               "9th": ninth_grade_math_scores,
               "10th": tenth_grade_math_scores,
               "11th": eleventh_grade_math_scores,
               "12th": twelfth_grade_math_scores})

math_scores_by_grade.head()


# In[419]:


# Combine each Series for average reading scores by school into single DataFrame.
reading_scores_by_grade = pd.DataFrame({
              "9th": ninth_grade_reading_scores,
              "10th": tenth_grade_reading_scores,
              "11th": eleventh_grade_reading_scores,
              "12th": twelfth_grade_reading_scores})

reading_scores_by_grade.head()


# In[420]:


# Format each grade column.
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)

math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)

math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)

math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)

# Make sure the columns are in the correct order.
math_scores_by_grade = math_scores_by_grade[
            ["9th", "10th", "11th", "12th"]]

# Remove the index name.
math_scores_by_grade.index.name = None
# Display the DataFrame.
math_scores_by_grade.head()


# In[421]:


# Format each grade column.
reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:,.1f}".format)

reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:,.1f}".format)

reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:,.1f}".format)

reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:,.1f}".format)

# Make sure the columns are in the correct order.
reading_scores_by_grade = reading_scores_by_grade[
             ["9th", "10th", "11th", "12th"]]

# Remove the index name.
reading_scores_by_grade.index.name = None
# Display the data frame.
reading_scores_by_grade.head()


# In[422]:


# Get the descriptive statistics for the per_school_capita.
per_school_capita.describe()


# In[423]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)


# In[424]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)


# In[425]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)


# In[426]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[427]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 630, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[428]:


# Establish the spending bins and group names.
spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]


# In[429]:


# Categorize spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)

per_school_summary_df


# In[430]:


# Calculate averages for the desired columns.
spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]


# In[431]:


# Calculate the overall passing percentage.
overall_passing_percentage = (spending_passing_math + spending_passing_reading) / 2  


# In[432]:


# Assemble into DataFrame.
spending_summary_df = pd.DataFrame({
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing": overall_passing_percentage})

spending_summary_df


# In[433]:


# Formatting
spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)

spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)

spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)

spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)

spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)

spending_summary_df


# In[434]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[435]:


# Categorize spending based on the bins.
per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], size_bins, labels=group_names)

per_school_summary_df.head()


# In[436]:


# Calculate averages for the desired columns.
size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

size_overall_passing = (size_passing_math + size_passing_reading) / 2


# In[437]:


# Assemble into DataFrame.
size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

size_summary_df


# In[438]:


# Formatting.
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)

size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)

size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)

size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)

size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)

size_summary_df


# In[439]:


# Calculate averages for the desired columns. 
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]

type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]

type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]

type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]

type_overall_passing = (type_passing_math + type_passing_reading) / 2


# In[440]:


# Assemble into DataFrame.
type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

type_summary_df


# In[441]:


# Formatting
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)

type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)

type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)

type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)

type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)

type_summary_df


# In[442]:


#Analysis Questions 
# 1. After removing the selected data from the data set the percentage of students passing each subject slightly declined (no change greater than 1.5%). As well as a slight decline in the average reading and math scores.
# 2. The removal of the selected data affected only Thomas High School in the school summary.
# 3. After removing the 9th grade reading and math scores from Thomas High School the performance of the school barely changed. The average reading and math score at Thomas High changed less than one percent when the 9th grade reading and math scores were removed. The number of students who passed reading and math at Thomas High each decreased by 28%. 
# 4. Math and reading scores cross-referenced with any other variable will be affected. Thomas High School will rank significantly lower than it does with the 9th grade scores in the analysis. In turn other schools scores will look as if they are inflated.

