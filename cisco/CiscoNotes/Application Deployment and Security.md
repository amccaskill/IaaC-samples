


## Diagnose a CI/CD pipeline failure (such as missing dependency, incompatible versions of components, and failed tests)

    CI/CD -method to frequently deliver apps to customers by introducing automation and testing to the
    integration and delivery/deployment process.
    
    CI - Continous Integration - Changes on a branch trigger (pipeline) build, test, and merged to the repository
    
    CD - Continous Delivery - Changes to an app are push to the repository or test environment.
    
    CD - Continous Deployment - Changes pass from the repository or test environment to production.
            Issues stem from:      
                    1. Missing dependencies (requirements.txt or pip)
                    2. Incompatible versions (requirements.txt or pip)
                    3. Failed unit or integration tests (unit tests)
## Integrate an application into a prebuilt CD environment leveraging Docker and Kubernetes
 
     automated container management - Kubernetes (K8s)
     declarative and automation functions
    
     Kubernetes offers services such as the following:
        Service discovery and load balancing
        Storage orchestration
        Automated rollouts and rollbacks
        Automatic bin packing
        Self-healing
        Secret and configuration management

    Components
        Kubernetes master node - global decisions for cluster  detects and responds to events from worker nodes
                API Server - Front End (control plane)
                Controller Manager - daemon that controls the state of the cluster.  maintains desired state:   
                        replicaton controller - ensure the correct number of nodes and replicate if neccessary  
                        endpoint controller  - 
                        namespace controller
                        service account controller
                etcd - Key-Value store (cluster config)
                Scheduler - Determines which worker node and resource requirements

    Worker Node (clustered)
            kublet - ensure that containers are in a pod, ensures health 
            kube-proxy - Network proxy ensure network rules are followed
            Container Runtime - software platform that runs below pods/container  (containerNERD, Docker, etc..)

    Docker has two options for containers to store files in the host machine so that the files are persisted
    even after the container stops—volumes and bind mounts:

    Containers that "bind mount" to storage or file.  storage or files that bind to containers 
        can be modified by a docker process or non docker process
    Containers that use "volumes" for storage or file. should only be modified by the dockers process
    On a user‐defined bridge network, containers can resolve each other by name or alias 

## Describe the benefits of continuous testing and static code analysis in a CI
                Code Linting (static analysis)
                        command line tool, this makes it easy to integrate with CI/CD
                        Integrate with IDE
                Software Testing:
                        Types:
                                Functional - test the function of some portion of the code.  example testing communication between two microservices. Python "unittest" framework for analysis that goes down the smallest modules of code.
                                Non -Functional -  test how well your application scales.  example load testing. simulating traffic to the application.
                                Security test - test the ability of the application against different types of attacks.
## Describe the tenets of the "12-factor app"
    Factor I: Codebase - One codebase tracked in revision control, many deploys.
    Factor II: Dependencies - Explicitly declare and isolate dependencies.
    Factor III: Configuration. Store the configuration in the environment
    Factor IV:  Backing Services. Treat backing services as attached resources.
    Factor V: Build, Release, Run.  Strictly separate build and run stages.
    Factor VI: Processes. Execute the app as one or more stateless processes.
    Factor VII: Port Binding. Export services via port binding.
    Factor VIII: Concurrency.  Scale out via the process model.
    Factor IX: Disposability. Maximize robustness with fast startup and graceful shutdown.
    Factor X: Dev/Prod Parity. Keep development, staging, and production as similar as possible
    Factor XI: Logs. Treat logs as event streams
    Factor XII: Admin Processes. Run admin/management tasks as one‐off processes.

## Describe an effective logging strategy for an application
    Logs are a very efficient component of the application observability framework. 
    For effective logging, the messages should be structured and consistance. 
    timestamps and log levels.

    Centralize logging - software agents (daemons) sometimes used.  centralize server
    Distributed logging - distributed nodes for logs. 1st process (ie format) then distribute logs over many servers
    Distributed tracing - allows you to track the progress of a request from src to dst
        Collector agent to log connector (forwarder) to storage and indexer
    One time source is used to avoid inacurracies.
    logging error should be handled.
    
    

    Syslog Serverity Levels:
        "Emacewnid" Emergency-Alert-Critical-Error-Warning-Informational-Notification
        "Every Apple Can End Weak Ideas Now"


## Implement mitigation strategies for OWASP threats (such as XSS, CSRF, and SQL injection)
    CSRF - Basically a man in the middle attack - attacker can trick you into getting your session cookies.
            use your cookies to authenticate to the site.
            mitigate - same site cookie attribute 
                        CSRF tokens can be generated on the server (each session or request)
                        Per-request tokens are more secure than per-session. (Flask-WTF)
                            CSRF tokens should not be transmitted using cookies.

    XSS - exploit the user (browser) trust of the server.  Malicous code imbedded with valid code delivered from 
            websites into the browser then executed locally.
            a form of injection type. Executes scripts in the victim's browser
        mitigate - encode (escaping) Separate untrusted data from active browser content. or sanitized (filter) before inputing code.
                    var sanitizer = new HtmlSanitizer(); and python's html.escape()function are an examples
    SQL injection - user supplied input queries a dynamic database. allowing a user to potentially 
                    elevate priviledges, alter data, and the list goes on..
        mitigate - Prepared Statements_Parameterized Queries [sqlite3_prepare()]
                        This technique should be used in place of dynamic queries. 
                        The developer has to define the all the SQL code. DB can tell between code & data now.
                    Stored Procedures
                    Allow-list input validation - sometimes parimeterized queries aren't adequte  
                                                    blacklist or whitelist commands
                    Escaping all user supplied input - use to escape user input prior to query. 
                                                        Least effective of the methods and mostly used on legeacy code


## Explain data privacy concerns related to storage and transmission of data
    Data privacy
        Health Insurance Portability and Accountability Act (HIPAA)
        Electronic Communications Privacy Act (ECPA)
        Children's Online Privacy Protection Act (COPPA)
    General Data Protection Regulation (GDPR) - rules governing the transfer of personal data outside the EU and EEA 
                                                    it applies to Europe and to any other country
                                                    that wants to provide services to individuals within the EU.


## Identify the secret storage approach relevant to a given scenario
    don't use same password for prod, test or dev
    use sso and MFA when possible
    
    store a secret in an environment variables:
    from dot_env import load_dotenv
    load_dotenv()
    ACCESS_USER=os.environ["ENV_ACCESS_USER"]
    ACCESS_SECRET=os.environ["ENV_ACCESS_SECRET"]
    result= API_call (url, user=ACCESS_USER, password=ACCESS_SECRET)

    secrets can be stored in a single centralized DB
    Access can be API or GUI based Store tokens, secrets, keys and certificates
    AWS IAM can be used to grant instances access services.  
    API gateways can be useds as proxies.

## Configure application‐specific SSL certificates

## Describe how end‐to‐end encryption principles apply to APIs
    TLS
    Mutual TLS
    IPSec
    API Gateway is a reverse proxy/load-balancer for a group of API nodes.
    Cloud connections should use TLS due to traffic being clear text prior to entering the FW.
    Service Mesh - used between microservices.  Provides a centralize proxy, policy, routing and AAA services.
    Containers Firewall - integrated FW inside a container.  Currently doesn't have parity with new FW. (soon?)

    public‐key cryptography allows security across public internet. uses digital signitures to verify identity.
    Public key - openly distributed. used to encrypt messages only. (asymmetrical)
    Private key - kept hidden.  used to decrypt messages.
    Digital signitures - AKA private key signing. the message signing can only be decrypted by the public key
                        Thus verifing the owner of the private key.

    PKI
    the heart of the process start with the CA (trusted 3rd party)
    CA certifies ownership of key pairs (certificates)
    CA root is a self signed public key and everyone trust it's digital signing.
    Modern browser has the CA public key pre-install

    systems or websites owners need to enroll with the CA to verify identity:
        1st generate a CSR (signing request)
            CSR contain the public key, and system/organization details
        2nd the CSR valids the information and generates a certificate 
            The certificate has system ID info along with the digital signiture (private key signing) of the CA
            Certificate revocation lists (CRLs) and Online Certificate Status Protocol (OCSP) are used to control status.

    PKI can be set up hierarchically. An intermediate CA certificate is a subordinate certificate issued by the
    root CA specifically to issue end‐entity server certificates. The result is a trust‐chain that begins at the
    trusted root CA, through the intermediate, and finally ending with the certificate issued to the end user.
    Such certificates are called chained root certificates.
    Intermediate CAs provide added flexibility, reliability, and security. Different subordinate CAs may have
    different policies. As there's no need to issue certificates directly from the CA root certificate, the CA
    may be kept offline all the time (with rare exceptions of issuing intermediate CAs) to prevent security
    accidents. In large networks using CRLs in multiple tiers, the CA helps to control their size.
    When using intermediate certificates, the client needs to know the whole certificate chain to verify the
    validity of an SSL certificate. An effective way to inform the client of the whole chain is using certificate
    bundles that contain an identity certificate along with all the intermediate certificates.
        
    TLS encrypted session procedure (handshake)
        1st client sends a request to the server (client hello).
        The request includes TLS version, cipher suites and a string of random bytes known as the "client random."
        
        2nd the server sends a reply (server hello).
        sends server's certificate, chosen cipher, and server‐generated "server random" string of bytes.

        3rd (Authentication) the client verifies the server's SSL certificate with the certificate authority that issued it.

        4th (Premaster secret) The client sends one more random string of bytes, known as the "premaster
        secret." It is encrypted with the public key from the certificate and can only be decrypted by the
        server.

        5th Session keys: Both the client and server generate session keys from the client random, the
        server random, and the premaster secret. They should arrive at the same results.

        6th Client is ready: The client sends a "finished" message that is encrypted with a session key.
        
        7th Server is ready: The server sends a "finished" message that is encrypted with a session key.
    


        

