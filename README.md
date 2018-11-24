# Web Scrape Google Places using Google Place API

In this post, we are going to discuss how to use Google Places API to extract nearby places for your work-related projects.

To start with you have to access https://cloud.google.com/ and create an account for yourself and then access console and click on start a project and navigate to credentials and generate an API Token Key. This API Key is used in the request URL.

The Nearby places are searched through values called types (eg- if you want to search for atms the type should be atm) different types can be found in onhttps://developers.google.com/places/supported_types

Code Attached 

At a time Google response is limited to 20 results per page and at the same time if the result is stored in the 2nd page it gives you a next_page_token key which has to be passed in the URL. Since the response is limited per page we pass a time.sleep call to delay the response by a 5 Seconds this is to ensure that the response doesn’t flag you an error saying Your API limit is exceeded the reason is that the API takes time to load the next page but in this span of time, the query which is passed hits the API .At last CSV file is saved in the path defined. You can also pass different values of types through a list within the function.




