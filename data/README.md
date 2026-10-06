# Data

The raw file is not stored in this repository. Download it from Kaggle:

**Gojek App Reviews Bahasa Indonesia** by ucupsedaya
https://www.kaggle.com/datasets/ucupsedaya/gojek-app-reviews-bahasa-indonesia

Use `GojekAppReviewV4.0.0-V4.9.3_Cleaned.csv` and put it at
`data/raw/GojekAppReviewV4.0.0-V4.9.3_Cleaned.csv`.

```bash
kaggle datasets download -d ucupsedaya/gojek-app-reviews-bahasa-indonesia -p data/raw --unzip
```

225,002 Google Play reviews with five columns: reviewer name, review text, star rating,
timestamp and installed app version. The notebook drops the reviewer name on load.
