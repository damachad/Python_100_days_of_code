# ISS overhead notifier 🛰️
This program uses [APIs](https://en.wikipedia.org/wiki/API) to check if it is nighttime where the user is located (based on the latitude and longitude provided) and if the [ISS](https://en.wikipedia.org/wiki/International_Space_Station) is passing over that location.
If this is true, it sends an email to the user, notifying them that the ISS is passing their location so they can see it.   
**Note:** This program runs an infinite loop that checks these conditions every 60 seconds.
