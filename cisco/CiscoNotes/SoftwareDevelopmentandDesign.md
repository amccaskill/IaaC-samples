# Software Development and Design

    Distributed applications 
        Front end and back end in the distributed applications design 
        The front end is the client side of the application stack that processes on your computer (browser)  it takes input from the client.
        Some of the back‐end functionality may be offloaded to the front end for efficiency and speed.
        The back end is the part of the application that processes requests, executes business logic, and
        stores information.
    
    Load Balancing
        load balancing is a way to efficiently distribute incoming requests across web servers.
        Different techniques:
            application or network type:
                HTTP host or path (variables, context based)
                IP address and port (context less)
            SSL offloading
            compression
            
    modular application design
        Modular design makes it easier to reuse application components and to work on specific components independently.  Project work may be broken
        down into smaller independent projects. Modules encapsulates data and functionality to hide complexity. Modules can have dependencies on other modules.
        horizontally (out/in) means adding and removing more nodes and distributing
        traffic across them (usually using a load-balancer).
        
    Traditional monolithic applications are tightly coupled. Scaling vertically (up/down) means adding or removing resources to the same single
    node (CPU, memory, or storage).
    
## application design considering high-availability and resiliency 
    On-premise-hybrid-cloud
    Availability is the degree to which a system is in an operable state, expressed as a percentage of uptime
    over a period of time
        Elimination of single points of failure
        Detection of failures as they occur
        Reliable failover
    Resilience is the ability to provide and maintain an acceptable level of service in the face of unexpected
    faults and challenges to a normal operation.
    Fan out and use the quickest response:
    Fail fast
    Circuit breaker
    Retries
    Fallback mechanisms
    Asynchronous communication
    Timeouts
    Parameter checking 
    resiliency attempts to survive through the failure with error handling and recovery
    high availability's goal is to detect and work around the failure by replacing a broken component.
    
## Evaluate an application design considering latency and rate limiting
    Application and OS latency
    Network and cable latency
    physical distance
    
    pagination (optimized data size of requests and lazy loading)
    CDN - Content Delivery Network (caching info local to client) (reduces physical distance)
    Choosing correct protocols (UDP vs TCP)
    rate‐limiting techniques
        HTTP 429 Too Many Requests
            token bucket
            backoff timers
            
## Evaluate an application design and implementation considering maintainability
    Planning is important for achieving maintainable software, adhere to existing good practices and strategies while planning your application.
    modular design - easier to maintain components
    Object Oriented Design - 
    Version Control - 
    naming conventon - 
    Software configuration management - version and configuation control. Build and enviroment management. Bug management.
    Coding standards
    
    
    S.O.L.I.D principles
        Single responsibility principle
        Open‐closed principle
        Liskov's substitution principle
        Interface segregation principle
        Dependency inversion principle
           
       Implementation:
            Consistent code is one of the foundation of good coding
            Common Toolset and Shared Libraries
            Documentation
            Properly Commented Code
            Continuous Integration
            Automatic Testing
         
## Evaluate an application design considering scalability and modularity
    Decomposability: Decomposability is a scale of how easy it is to break down a problem into subproblems
    Composability: The idea of composability is to produce software from reusable modules.
    Understandability: Easier to understand in smaller chunks
    Continuity: Over time the code base will work better with smaller changes and specialized skill for individual modules. 
    Protection: A security issue or error on one module doesn't effect other modules directly.
                Each module communicates over API - details are not known by other modules
    Testability: Able to test individual modules without effecting the entire code base.
        
    Scalability -  adding resources to support increased workolad.
        Vertical - single node to add resource(monolithic)
        Horizontal - multiple nodes to distribute workload across multiple resources (containers)
        Hybrid - These two approaches can also be combined. Hybrid scaling is often implemented 
                    as an autoscaling solution that uses predictive and reactive
                    scaling to optimize performance. Predictive scaling analyzes patterns to figure out 
                    the predicted resource usage for a time period and
                    accordingly scales the resources horizontally. Since these predictions will never be 
                    100 percent correct, vertical scalability is used
                    reactively, when the current resources are insufficient to handle the predicted workload 
        Scalability improves handling larger amounts of work in multiple dimensions:
            Functional scalability: Do more without disrupting existing services.
            Geographical scalability: Stay effective while expanding geographically.
            Load scalability: Increase load on individual components.
            Administrative scalability: Support more users or tenants.
            Generation scalability: Be able to adapt to newer components.
            Heterogenous scalability: Be able to adapt to different vendors.

            
## Evaluate an application design and implementation considering observability
    observability is the property of a system that tells you how well the internal state of a 
    system can be understood from the knowledge of its external outputs
    
    Can be challanging and complicated to observe applications due to the modern distributed nature.
    Three main sections:
    Logs - While most programming languages support information output in the form of print() or log() functions, 
        this is often not enough for anything beyond the most basic applications.
        That is where logging frameworks come in. They standardize and simplify the logging process, log storage, and analysis. 
        Some frameworks (like log4j are widely used in the industry and well documented.
        Logging frameworks are usually straightforward to integrate into your code, 
        and typically consist of a logger class with some parameters that is fed log messages or can intercept and 
        format messages that are sent to the console.
    Metrics
        numerical measurements recorded by the application over intervals of time. Metrics are best suited to trigger alerts.
    Tracing
        Brings visibility into the life of a request across the systems.
    Monitoring
    
    When building an application, observability must be taken into consideration both at a high and a low level. High-level observability is often included as
    a nonfunctional requirement of the system and is a part of the application design. Low-level observability is included in the implementation phase of the
    development.
    Consider the following when designing:
    Status of application components.
    Health checks on external systems.
    Operational status of services.
    User triggered actions.
    Hardware status and load.
    Consider the following when implementing:
    Programming language-specific logging.
    Function results.
    Transaction and query statuses.
    API responses.
    
    Diagnose problems with an application given logs related to an event
        The most important part of logging in a distributed architecture is proper log aggregation. The inherent problem of logging in a distributed architecture
        is that it uses different systems that tend to present data in different formats. You might end up with different logs on each component of your
        application, meaning you could have to go through many servers or containers and know how logging works on each subsystem to get the whole picture. Being
        able to aggregate logs in a centralized location, ideally as close to real time as possible, allows you to easily and swiftly troubleshoot problems, do
        some additional analysis, and isolate anomalies.
        The logs in a distributed environment always have to be aggregated on a centralized logging component, since manually connecting to all the application
        components, and then opening and reading all their individual logs would be impractical. The goal of distributed logging is to give you one place where you
        can find all the logs.



## Evaluate choice of database types with respect to application requirements
    relational - 
        SQL databases are best suited for storing and querying structured data. Data is stored in tables, The rows are called records. 
        Relational (SQL querying lanuage) are not effective at real time application support. Main attributes are rigid and well known.
        
    document -
        designed for storing, retrieving and managing document-oriented information, 
        also known as semi-structured database an example of an "No SQL" database.
        *document databases are a subclass of key-value databases*

    
    graph - 
        database that is focused on relationships between data. It is based on graph theory
        and consists of a set of node and edge objects.  Nodes represent entities or instances.
        Edge objects represent the line that connect nodes.  Graph databases are always implemented with 
        another type of database to store the data.
    
    columnar - 
        Just like relational data is stored in tables but queried by the columns. ideal for fast querying specific data 
        but not for whole record reads or writes of certain types. (Amazon Redshift - Datawarehouse)
        
    Key‐value -
        Data records are stored with a unique key and a value. No restrictions on format and the focus is on simplicity, speed, and scale.  
        Examples are Redis and AWS DynamoDB.
   
    time series - 
        specifically built for handling metrics, events, or measurements that
        are time‐stamped. great for data lifecycle management and data summarization
        examples are InfluxDB and AWS Timestream
    
    
    
    Atomic: 
         Guarantees the database performs all updates or none. rollback to original state
    Consistency: 
         Guarantees that a transaction can only transition the database from one valid state to another.(Doesn’t mean the transaction was correct)
    Isolation:  
        Guarantees that concurrent execution of transactions leaves the database in the same state that would have been obtained if the 
        transactions were executed sequentially
    Durability: 
        Guarantees that once a transaction has been committed, it will remain committed, it will remain committed even in the case of a system failure.
        This usually means that completed transactions (or their effects) are recorded in non-volatile memory.
        
    The BASE model is an alternative to ACID:
        Basically available - 
            Any data request should receive a response, but that response may
            indicate a failure or changing state, as opposed to the requested data.
        Soft state - 
            A system may be in a changing state until consistency is reached.
        Eventual consistency - 
            Data may vary in value until the system reaches a consistent state.
            
    CAP theorem
        A distributed database (multiple nodes) can only ensure two of the folwing three:
            Consistency: 
                Every read receives the most recent write or an error.
            Availability: 
                Every request receives a (non‐error) response, without the guarantee that it
                contains the most recent write.
            Partition tolerance: 
            The database continues to operate even if an arbitrary number of messages
            were dropped (or delayed) by the network between nodes.


## Explain architectural patterns 
    monolithic  -
        self‐contained and has little or no interaction with other software
    services oriented -
        application components provide services to other components through a communication protocol over a network.
        Enterprise Service Bus (ESB) is a centralized component that performs integration to back‐end services,
        translates their (often incompatible) data models, protocols, and technologies, and makes these 
        available as service interfaces for applications
        uses SOAP/HTML, REST,gRPC.
           
        
           Service reference autonomy 
           Service location transparency
           Service abstraction 
           Service autonomy
           Service statelessness
        
    microservices -
        variant of the service‐oriented architecture. Services are fine‐grained units focused on doing
        just one thing, whereas with SOA, services are much bigger and complicated
        ‐ Modularity makes the application easier to understand, develop, test, and maintain.
        
        Microservices are easily scalable; because they are implemented and deployed independently of
        each other, each can be scaled individually if overloaded.
        Microservices enable distributed development, where small autonomous teams develop,
        deploy, and maintain their respective services independently.
        Microservices can be implemented using different programming languages, databases,
        hardware, and software environments, depending on what fits best.
        On the downside, this architecture introduces additional complexity and new problems to deal with,
        such as network latency, message format design, load balancing, and fault tolerance, which all have to
        be addressed at scale. Performance is affected due to increased overhead and network latency.
        
    event driven -
        The event‐driven architecture (EDA) is based on the production of, detection of, consumption of, and 
        reaction to events. An event can be defined as "a significant change in state."
        What is produced, published,propagated, detected, or consumed is an asynchronous message called the event notification, 
        and not the event itself, as events do not travel (they just occur). However, the term event is often used to 
        denote the notification message itself.
        
        event creators produce events and know what events occurred. Event 
        consumers/processors are affected by events and process them according to their logic. 
        Event notifications are transported from the event creators to the event consumers via event channels. 
        Event notifications are asynchronous and may trigger when resources are not available to respond to them, 
        so EDA also provides storage for them until resources become available in the form of an event queue
        
        Event‐driven architecture consists of two main topologies: mediator and broker. The mediator topology
        is commonly used when there is a need to orchestrate multiple steps within an event through a central
        mediator, whereas the broker topology is used to chain events and responses together directly
        

## Utilize advanced version control operations with Git
    There are three core components/areas of a Git project: 
        working directory - 
            regular directory on your local computer's file system.
        staging area (or index) - 
            'Git add' to file move here from working directory
        local repository - 
            'Git commit' to move file here from staging area.
            
        Remote repository - 
            'Git push' to move file here from local respository
            
    Git has two data structures:
        mutable index (stage-cache) - 
            contains information about the working directory and the next revision to be committed
        
        non-mutable index
            append‐only object database
            
            A tree object is the equivalent of a directory. contains a list of filenames
            
            A blob (binary large object) is the content of a file. 
            Blobs have no proper filename, timestamps,or other metadata 
            (internally, a blob's name is a hash of its content)
            
                       
            commit object links tree objects together into history.
            
        ‐ Merge: 
            Retains all changes to the merged branch and the complete history.
        ‐ Rebase: 
            Maintains a cleaner, linear revision history since merged commits 
            are appended at the end of the target branch. 
            Conflicts may occur more often than in the merge method, 
            and they need to be resolved immediately.
            
        - reset: 
            It undoes some or all changes made with the "git add" and "git commit" commands. 
            It does up to three operations:
                    Move the branch pointer.
                    Update the staging area with the contents of the specified snapshot
                    Update the working directory with the contents of the specified snapshot
                    
                    git rest soft - it just moves the branch's pointer
                    git reset mixed -  moves the branch's pointer and updates the staging area
                    git resert hard -  moves the branch's pointer and updates the staging and working areas
                    
                    git reset works specifying specific files (git reset --soft requirements.txt)         
                    
                    git checkout <branch>
                        Used to switch between branches.
                        makes the "HEAD" point to a target branch
                        updates files in the working directory and in the staging area to match a branch's latest snapshot.
                        
                        git stash 
                            Used when you are not ready commit is not ready but want to switch branches.
                            
                    git revert - 
                        undo changes but maintain revision history, or changes are 
                        pushed to a public repository so you cannot undo them with the reset/checkout commands.
                        
                            git revert vs git reset:
                            With git revert, the "HEAD"/branch pointers move forward (with new commit), and the previous history is intact.
                            With git reset, the "HEAD"/branch pointers move back, and history might be wiped.
                            
                            git checkout vs git reset:
                            The command git checkout is safer because it preserves modified content of the working directory, 
                            whereas git reset --hard just replaces all the files without checking.
                            The command git reset moves the branch pointer, 
                            whereas git checkout moves the "HEAD" pointer and keeps all the branch pointers untouched.
                        
    
            Git commands:  
            git init
            git checkout -b branch
            git merge - # fast forward (if no changes to the master)
            Handling merge conflict
                Accept Both
                Compare side by side
                Accept current changes - keep master changes
                Accept incoming changes - accept the Branch changes
            git checkout  when specifying a file rolls file back to last commit.
            git reset unstages commit.
        
            git reset head~2
            git reset 4482 --soft
            git reset head~2 --mixed (default) (unstaged)
            git reset head~2 --soft (staged)
            git reset head~2 --hard (delete all files)



## Explain the concepts of release packaging and dependency management
    Software code consist of multiple files (modules if you will).  The modules together form the package.  The environment and dependencies need managment.
        Package format: source distribution that has a structure and package dependencies. compressed archive with metadata.
        Package manager: Package Installer for Python (PIP)
        Repository: central ecosystem storage for package retrieval (https://pypi.org)
        
        Example is to create a virtual environment
        install all the needed libraries 
            python3 -m venv bestcode
            source bestcode/bin/activate
            
            install the needed libraries the use the "pip freeze > requirements.txt"
            On the target system use the "install -r requirement.txt"
            
        Another fresh approach would be to packaged sdist into a Docker container


## Construct a sequence diagram that includes API calls

    Sequence diagrams, sometimes called UML diagrams, are diagrams that depict interactions between different entities in a time-ordered fashion. They are used to model and visualize the flow of information through your system, allowing you to troubleshoot and document your logic. Sequence diagrams are used both in design and analysis and are one of the most popular techniques for dynamic modeling (creating models that change over time).

    Sequence diagrams are based on Unified Modeling Language (UML), a modeling language used in the field of software engineering to visualize the design of a system. In addition to sequence diagrams, UML supports a wide variety of diagrams and offers solutions for visualization of many software-related concepts—classes, components, objects, deployments, packages, profiles, activities, states, timing, use cases, and more. The sequence diagram is one of the most used visualization tools, along the class diagram.

    Plant UML (https://plantuml.com/sequence‐diagram )
    docker containter with plant UML image:
    docker run -d -p 8080:8080 plantuml/plantuml-server:tomcat
    

       Participants are the individual components that interact with others within the model. Participants use the notation of “ObjectName:className"   Participant roles include:
       
    Actor is the user or users of the application. However, an actor can also be, for example, a shop customer, bank account holder, external API service, and much more.
    Boundaries represent MVC views and are responsible for interaction with external actors, such as a form on the user interface.
 
    Control objects represent MVC controllers and manage the flow of interactions between boundaries and entities. They manage the processing and execution of the commands coming from a system boundary.
 
    Entity is an object that represents some meaningful chunk of system data

    Synchronous message:
    Return message:
    Asynchronous message:
    Lost message:
    Found message:
    Create message:
    Delete message:
    Self-Message:
    opt: simple IF statement
    alt: IF..THEN...ELSE clause
    Loop: FOR loop
    Par: to show things are executed in parallel
    

