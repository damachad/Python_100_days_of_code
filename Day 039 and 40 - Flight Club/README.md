# Flight Club ✈️
Flight Club is a Python project that uses APIs to get flight data, helping you find the best flight deals based on your preferences. 
It utilizes the [Tequila Kiwi API](https://partners.kiwi.com/our-solutions/tequila/) for flight search and provides notifications through SMS and email when a low-price alert is triggered.

It uses a Google sheet with the cities you are interested in visiting, the IATA code from these cities, and the lowest price for a flight there.   
![image](https://github.com/damachad/Python_100_days_of_code/assets/128734978/f793e907-24d6-48b3-8582-4293e445a228)
   
The list of users to be contacted via email when a flight deal is found is also present on another page of the same sheet.   
To manage the data present in this sheet, the [Sheety API](https://sheety.co/) is used.   

## Notes
- The default departure city is set to London (but can be changed).
- If no direct flights are found to the searched destination, it looks for flights with one stop.
- The body of the email contains the flight's: price, city of departure and respective airport, city of arrival and airport, date of departure, and date of return. If the flight is not direct, it also includes the
number of stops and where they are.
