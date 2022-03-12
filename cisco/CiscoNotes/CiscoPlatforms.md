# Webex
        Chatbot
            the chatbot will listen from a specific webhook URL for notifications
                Execute code based on notifications.
                The webhook must have the Webex access token to communicate with Webex API
                The webhook URL is called after a specific event occurs inside Webex
                The calls only notify that some event has occurred.  You must design a event handler to make a call to the Webex API to query for further data.



# Firepower (device management)
# Meraki
        ## Use Meraki Dashboard APIs to enable an SSID
                    If message starts with ('/meraki') the webhook application will make some API calls to the Meraki API server.  If not, the application will just post a confirmation that a message was received.

            location:
                Scanning API delivers location of WiFi and bluetooth devices.  It uses the physical location of  wireless access points and the probes from the client devices.
                the Meraki cloud sends the data in the form json data via HTTP POST to a specified destination server. The posts occur every minute for each AP.
                The destination server must have the secret 'Validator' code to validate your application with Meraki Cloud. (It is included in every POST request)

              
# intersight
        A cloud based management (SaaS) for Cisco UCS and Hyperflex servers.  Intersight communicates via REST API to the systems bases off the OpenAPI Specification.  
        This allows intersight to scale over multiple datacenters.
        Intersight provides a rich query language based on the OData standard. The query language is represented using URL query parameters for GET requests. 
        The query component is indicated by the first question mark ("?") character and terminated by a number sign ("#") character or by the end of the URL. 
        Query tags use key : value pairs ( key eq 'Site' and t/value eq 'Orlando')
                GET /api/v1/compute/RackUnits?$filter=Name eq 'ADMCGJA2'
                GET /api/v1/compute/RackUnits?$filter=Model ne 'UCSC-C340-M5SN'
                GET /api/v1/compute/PhysicalSummaries

# UCS server API
        Cisco UCS Manager XML API
        Management Information Tree or Management information Model
         - operations on single objects or object hierarchy - transactional: rollback if not successful.
        physical and logical components of the Cisco UCS are represented in a hierarchical management information model
        administrative or operational state
        Structure:
            sys
            parent/child nodes
            MO (managed object) or (node) with (distinguished name)
        UCS fabric interconnect houses the DME (data management engine) 


# DNA center API
        Site Health - area and building
        Network Health - information on devices
        Client Health - client type wired or wireless
        REST API - user login with credentials, then API token is granted (X-Auth-Token)
# AppDynamics
        agent and controllers
        looks at everyline of code in the application
        baseline config automatically discovered via transactions
        controllers updated by agents in real time
        monitors and anaylizes the performance and behavior of the application, infrastructure, and database.
        automatically maps the toplogy and transactions for visualization to aid in troubleshooting. 
        
        AppDynamics platform API
                Controller API
                Analytics API
                Database API
                Application Agent instrumentation API
                Cloud Connector API
# Custom Dashboards
        TIG 
        Telegraph - Cisco MDT input - ingestion
        InfluxDB - TimeSeries DB
        Grafana - Display
        
        ELK
        Elatasearch - ingestion
        LogStash - TimeSeries DB
        Kibana - Display
        
        Telemetry - SNMP, NetFlow, syslogs, etc
        MDT - Model Driven Telemetry - uses the YANG model
                support gRPC
        Pull - Dial in
        Push - Dial out