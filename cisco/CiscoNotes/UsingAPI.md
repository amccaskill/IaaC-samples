 Implement robust REST API error handling for timeouts and rate limits

 Implement control flow of consumer code for unrecoverable REST API errors

 Identify ways to optimize API usage through HTTP cache controls
    application optimizations - 
        application response times
        lower bandwidth
        lower  processing time
        lower utilization

    HTTP caching is a process that stores copies of resources and serves them to reduce the amount of network traffic and the load of the servers. HTTP requests are completed in less time.

    HTTP caches in common use today are typically limited to caching responses to GET, 
    many caches simply decline other methods and use only the URI as the primary cache key
    Caching may be implemented at different places at the client browser, proxy server, web server (local), or API gateway
    
    Freshness - cache content uses expiration timer or validation check (Etags strong/weak)
        ETag: Unique identifier (version)
        Validation: Last Modified
        HTTP Conditional Requests - 
            If-None-Match
            If-Unmodified-Since
            Cache-Control HTTP header
                no-store - disable caching (you can only choose one either no-store or no-cache)
                no-cache- caching allowed stored response must be validated first before using
                max-age - valid time (seconds)
                public - anyone can cache
                private - can be cached locally only (you can only choose one either public or private)

    when designing API for cache effectiveness:
        URL should be consistent that to the same resource.
        Common Libraries for static content
        use cache control functions (max age values etc..)
        don't refresh files that haven't change
    when designing endpoints for cache effectiveness:
        Use "Get" correctly it is the method that is cached
        POST/PUT/DELETE limited circumstances
        Different URL for different resources
        authorization info should be in authorization header

    

    HTTP compression
        Benefits - faster response time and less throughput utilization
        HTTP "Accept-Encoding" header - Used to list types of compression algorithms 
            compress, deflate, gzip, and bzip2
        HTTP "Content-Encoding" header - Uses this header if the responding server decides to use one of the compression techniques




## Construct an application that consumes a REST API that supports pagination
    Pagination - the process of dividing data into multple pages
        Offset
            the value of the pages that should be skip.
            latency when dealing with large offset values.
            GET /items?offset=196&limit=40
        Page-Based
            Basic method for pagination responses from the API.
            GET /events?page=50
            GET /events?per_page=60&page=5

        Cursor or Keyset/Seek
            index or field value that results should be shown after 
            GET /items?limit=10&after=82653
        Static
            predefine set of results parameters.
            The static technique supports caching most efficiently
            GET /items?limit=20&page=40
            
    You can query the REST API to provide additional information (metadata) in the HTTP headers responses.
        The "link" method is use by some API such at the Cisco Webex API
        With this metadata provided, (first, last, previous, and next) the client does not have to construct 
        its own URLs for requesting additional resources but can (and should) use the URL provided in the Link header.
    
    The link can be parsed or extracted by using a utility like the Python 
    requests_utils_parse_header_links method. 
    The headers also sometimes contain additional metadata such as total records, current record number, etc..



## Describe the steps in the OAuth2 three-legged authorization code grant flow
    Open standards distributed authorization protocol
    OAuth allows an end user to authorize an application to access to a third-party service without sharing their credentials with the application

    Resource owner: The end user
    Resource server: Node with the protected resources
    Client: The APPLICATION that requests access to the resource owner's data
    Authorization server: Confirms identity and issues tokens (could be the same as the resource server.)


        The end user authenticates then authorizes the application (Oauth server application)

        The application issues OAuth tokens to the third-party application

        The Third-party service presents the OAuth token to access a protected resource rather than user credentials


    Two Legged (Flow) Authorization
        authentication request without the end user.  Used mostly with API communication.
        Client Credentials grant: Obtain an access token without a user
            1.  client application authenticates with the authorization server and requests an access token
               HTTP request:
                    POST /token HTTP/1.1
                    Host: server.purple.com
                    Content-Type: application/x-www-form-urlencoded
                    grant_type=client_credentials 
                    client_id=alpofiutmh4dkjmi
                    client_secret=24653uygt5slkujredr2

            2.  The authorization server will then authenticate the request and (if valid) will issue an access token including any additional parameters:
                HTTP response:
                    HTTP/1.1 200 OK 
                    Content-Type: application/json;charset=UTF-8 
                    Cache-Control: no-store 
                    Pragma: no-cache 
                    { 
                    "access_token":"3ZJIKEOXYDLEYJM”,
                    "token_type":"purple",
                    "expires_in":1200, 
                    "demo_parameter":"blue_value“ 
                    }






            




    Three Legged (Flow) Authorization
        authentication with end user and browser.
        Authorization Code grant: Exchange an authorization code for an access token

            1.  Sends the credentials and receives the auth code(authorization grant code/token are short term)

            2.  Sends the Authorization code for an (access) Token (access token are longer term - has expiration)
                                Distributed environments often have different servers sending the access tokens vs. the grant code/token.

            3. Client uses the access token and gets granted access to the protected resources.
                                The user/browser never has access to the access token only the client(application)

            Detailed steps:
                    1.  user wants to login to samplesite.com opens the app, and clicks the "Log in to Yahoo.com"

                         Sample request:
                            GET https://accounts.yahoo.com/o/oauth2/v2/auth?
                            response_type=code&
                            scope=https%3A//www.yahooapis.com/auth/coolsite?
                            client_id=98766542.apps.yahoousercontent.com&
                            state=random_custom_string&
                            redirect_uri=https://oauth.samplesite.com/cb

                        Response type: Sent to the server to indicate the desired grant type; must be "code."
                        Scope: Used to limit access only to resources the application needs (optional).
                        Client identifier: Obtained during the client registration process.  
                        The owner of the client site must register with the resource owner and be approved for a unique client-id.    
                        State: Any string value to maintain state between the authorization request and response. It will be included in the redirection URL and may be used to protect against attacks such as cross-site request forgery (CSRF).
                         Redirection URI: Where the user is redirected after completing the authorization. The value must match redirect URIs (uniform resource identifiers) established during the client registration process.

                    2.  If the resource owner grants access, the authorization server redirects the user's browser back to the client using the redirection URI:
                                https://oauth.samplesite.com/cb?code=JDKLSIRFVBGT
                                state=sample_unique_custom_string&scope=https%3A//www.yahooapis.com/auth/catalog
                        
                         If the resource owner does not grant access, the response contains an error message:
                                https://oauth.samplesite.com/cb?error=access_denied&
                                state=sample_unique_string

                   3.   The application exchanges the authorization code for the access token by making a POST (or GET) request to the authorization server
                               POST /token HTTP/1.1
                                Host: oauth2.yahooapis.com
                                grant_type=authorization_code&
                                client_id=98765213.apps.yahoousercontent.com&
                                client_secret=your_client_secret&
                                code=JDKLSIRFVBGT
                                redirect_uri=https://oauth.samplesite.com/cb 

                    4.  If/When the Authentication Server validates the code it responds with the code.
                                HTTP/1.1 200 OK
                                Content-Type: application/json;charset=UTF-8
                                {
                                "access_token":"UKL/KlkkhjQSDsd4xQ",
                                "token_type":"Bearer",
                                "expires_in":3600,
                                "refresh_token":"36JKOUEFBGTDtvg",
                                }
