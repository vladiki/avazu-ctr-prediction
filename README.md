	https://www.kaggle.com/c/avazu-ctr-prediction/data

## File descriptions
train - Training set. 10 days of click-through data, ordered chronologically. Non-clicks and clicks are subsampled according to different strategies. 

	https://www.kaggle.com/c/avazu-ctr-prediction/download/train.gz

test - Test set. 1 day of ads to for testing your model predictions. 

	https://www.kaggle.com/c/avazu-ctr-prediction/download/test.gz

sampleSubmission.csv - Sample submission file in the correct format, corresponds to the All-0.5 Benchmark. 

	https://www.kaggle.com/c/avazu-ctr-prediction/download/sampleSubmission.gz

## Data fields
id: ad identifier

click: 0/1 for non-click/click

hour: format is YYMMDDHH, so 14091123 means 23:00 on Sept. 11, 2014 UTC.

C1 -- anonymized categorical variable

banner_pos

site_id

site_domain

site_category

app_id

app_domain

app_category

device_id

device_ip

device_model

device_type

device_conn_type

C14-C21 -- anonymized categorical variables