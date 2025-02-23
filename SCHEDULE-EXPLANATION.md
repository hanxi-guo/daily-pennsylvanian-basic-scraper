# Explanation of cron expression

My schedule related code is now look like this in [scrape.yaml](https://github.com/hanxi-guo/daily-pennsylvanian-basic-scraper/blob/main/.github/workflows/scrape.yaml "scrape.yaml") file:

```
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron:   "0 14,21 * * *"   
```
Since the cron expression with 5 strings is in form :
- "minute" "hours" "date" "month" "day of week"
- where we could see `*` as *every*
- The hours and minute is defined based on ==UTC+ 0 time==
- The numbers which separated by comma, means we would run this script in UTC 14:00 and 21:00 every day separately
- Thus, the script would run in 9:00 and 16:00 in EST and 10:00 and 17:00 in EDT for Philadelphia every day, every week, every month