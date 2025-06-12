[Text Classification on Emails](https://www.kaggle.com/datasets/dipankarsrirag/topic-modelling-on-emails)  


This is the script that was used to download and show where the data is located.
```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("dipankarsrirag/topic-modelling-on-emails")

print("Path to dataset files:", path)
```
Output: `Path to dataset files: /Users/blakewallace/.cache/kagglehub/datasets/dipankarsrirag/topic-modelling-on-emails/versions/1`

There are four classes of data in the dataset: Crime (1100), Entertainment (1053), Politics (3001), Science (4000).  

When initially exploring the data it was discovered that the many of the instances in the data in the Entertainment folder are identical to the instances in the Crime folder.  An attempt at creating a classifier that includes these two sets fails, since there is so much data overlap between the sets.  In essence, we decide to completely remove the Entertainment set from consideration in our models.  An analysis of the overlap between sets is included in the notebook `Classification_and_the_NB_Algorithm`.

