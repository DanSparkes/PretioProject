# PretioProject
The high-level goal of this mini-project to make a simple server-side integration with our API that avoids issues with cross-domain restrictions, and automatically detects the country of the user.

    Setup a simple web server using Flask that does the following:
       - Responds to the endpoint /ad
       - Translates the client's IP address into a two-letter country code
       - Makes an HTTP request to the Pretio API and parses the result
       - Returns HTML, with the creative URL from the ad response templated in as the src attribute for a fullscreen iframe.

