# Robots Analysis for the Daily Pennsylvanian 
The Daily Pennsylvanian's `robots.txt` file is available at [https://www.thedp.com/robots.txt](https://www.thedp.com/robots.txt). 
## Contents of the `robots.txt` file on Feb 23, 2025

``` 
User-agent: *
Crawl-delay: 10
Allow: /

User-agent: SemrushBot
Disallow: / 
``` 
## Explanation
### First paragraph
1. The first paragraph of the `robots.txt` indicates that the website allow all types of user agent but request them to wait 10 seconds between each successive requests
2. The reason of why it ask delay is because the mountains of requests may leading the server load excessive, giving chance for malicious attack
3. The third row explicitly allows all crawlers to access the entire website since it refer to the root repository by `/`

### Second paragraph
1. Besides the first paragraph allowance, the website explicitly block the `SemrushBot` crawler.
2. And it do not allow the crawler access the entire website since it also refer to the root repository by `/`
3. This may because `SemrushBot` is a famous SEO tool and it would lead to useless server resources consumption.


