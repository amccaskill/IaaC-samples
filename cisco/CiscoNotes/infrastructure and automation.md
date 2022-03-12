## Explain considerations of model‐driven telemetry (including data consumption and data storage)
    Model‐driven telemetry (MDT)
        sending YANG model data to a repository.
    There are three entities:
        Publisher: Node that sends YANG object data
        Subscriber: Node that requests for a set of YANG object data
        Collector/Reciever: Node that collects the YANG object data - reciever/subscriber could be same node.

    Subscribtion stipulates that data is pushed from the pub to sub. also detail (format, rate- change or continuous)
    Types of subscriptions:
        dynamic - Clients dailin good until session is broken - NETCONF, gNMI are used as transport.
        configured - CLI based dailout -  good until reconfigured. - gRPC is used as transport.

## Utilize RESTCONF to configure a network device, including interfaces, static routes, and VLANs (IOS XE only)

    RESTCONF uses HTTPS and uses JSON or XML encoding format. 
    The Network Configuration protocol uses XML and SSH (830) which is stateful (connection oriented).


    YANG is a data modeling language used to model configuration and
    state data.  YANG does not define the actual data but the data element types and allowed values, 
    their structures, and the relationships between them.
    YANG models the hierarchical organization of data as a tree in which each node has a name and either a
    value or a set of child nodes. YANG mandates the specific interactions between elements.

    YANG models can be broken down into modules and submodules.  A model's module is allowd to import or export 
    external modules from other sources. 

    YANG data models can describe constraints to be enforced on the data, restricting the presence or value
    of nodes based on the presence or value of other nodes in the hierarchy.
    When building the YANG tree, you use a module as the base unit. It contains a collection of related
    definitions and consists of three types of statements: module header statements, "revision" statements,
    and definition statements.

    Yang
    YANG defines four main types of data nodes for data modeling used in the definition statements:

        leaf node:
            contains simple data like an integer or a string. 
            It has exactly one value of a particular type, and no child nodes.
    
        Leaf‐list nodes: 
            A sequence of leaf nodes with exactly one value of a particular type per leaf.

         Container Nodes:
            used to group related nodes in a subtree. 
            It has only child nodes and no value and may contain 
            any number of child nodes of any type (including leafs, lists, containers, and leaf-lists).

        List Nodes
            A sequence of list entries. Each entry is like a structure or a record instance, 
            and is uniquely identified by the values of its key leafs. 
            A list can define multiple keys and may contain any number of child nodes of any 
            type (including leafs, lists, containers etc.).

        data types:
            Build in

            Common data types ietf-yang-types and ietf-inet-types (import ietf-inet-types)

            Derived Types (typedef)
                RFC 7950:
                                    YANG Example:
                    
                         typedef percent {
                           type uint8 {
                             range "0 .. 100";
                           }
                         }
                    
                         leaf completed {
                           type percent;
                         }
                    
                       XML Encoding Example:
                    
                         <completed>20</completed>
                

    Cisco IOS XE devices support native, IETF, OpenConfig, and tail‐f YANG models
    Enable RESTCONF:
        CAT9K(config)#ip http secure-server
        CAT9K(config)#ip http authentication local
        CAT9K(config)#restconf
        

        CAT9K#show platform software yang-management process
        confd : Running
        nesd : Running
        syncfd : Running
        ncsshd : Not Running
        dmiauthd : Running
        nginx : Running
        ndbmand : Running
        pubd : Running
        gnmib : Not Running

##  Construct a workflow to configure network parameters with: Ansible Playbook and Puppet manifest

        Ansible -  Four major files are the core:
                        CONFIGURATION - global variables 
                        INVENTORY - inventory of resources /etc/ansible/hosts
                        HOST-VAR/GROUP-VAR - variables of the inventory
                        PLAYBOOK

                        configuration file which will be searched for in the following order:
                            
                            ANSIBLE_CONFIG (environment variable if set)
                            
                            ansible.cfg (in the current directory)
                            
                            ~/.ansible.cfg (in the home directory)
                            
                            /etc/ansible/ansible.cfg
        Puppet -
                inventory.yml file for inventory of resources
                Puppetfile - specifies the modules in use (ciso_ios module, ntp module,)

## Identify a configuration management solution to achieve technical and business requirements

        
        Config Management - manage changes, status and inventory of systems.

        Network Orchestration - Provisioning 
                policy‐driven approach to automation

        IaC - uses Config Managment and Orchstration

        Terraform- Provisioning Network Orchestration - build from the ground up
                    immutable - resources have to be DESTROYED then recreated.
                    Use Ansible or Puppet to manage the config (changing ACL or adding OSPF area)

        Declarative (Functional) versus Imperative (Procedural)
            Procedural:
                Anisble is procedural (mostly) you have to "order of operations" with the steps.
                Be careful because you if you want to change config you need to delete the config resource first.
                Legacy devices tend to be CLI -> procedural (order of operations and cummulative(stale config)) 
                
            Declarative:
                Terraform
                Define the desired state, and the system executes what needs to happen to achieve that desired state
                Be careful you can easily wipe production config if you mistakly not define service or resource
                NETCONF - Operation Replace
                RESTCONF - HTTP method PUT
                PUPPET is DECLARATIVE like terraform

        PUSH VS PULL solution
            Ansible - Push agentless - software only on client
            Puppet - Pull (newer software is push)
                software agents (on the node) gather facts and send them to a master node.
                node will request a catalog and when the master node sends the catalog is determine it config.
                node will send a report to the master node to confirm changes.
            
        NETCONF stateful, xml. config store, config lock, etc.. better if need to apply all config at once
        RESTCONF stateless, json (capable of xml)

        CICD
            CD continous deployment - fully automated to production nodes
            CD continous delivery - delivered to the "test" environment first. 
                                    Manual intervention is needed to deploy into production
                                    (push request from the test branch into the main branch)
                                    Once the request is approved the process starts again
                                    Build, test then deploy into production.


 ## Describe how to host an application on a network device (including Catalyst 9000 and Cisco IOx-enabled devices)
                    
                Reason for hosting app on nework devices.
                    AI/ML technologies
                    Distributed Processing
                    Security - able to analyze traffic closer to the edge before traversing
                    IoT - bring cloud and processing closer to edge
                    install software agents on net devices.  ( use puppet instead of puppet/proxy)
                    Business agility
                    Bandwidth reduction - no need for all traffic to saturate uplinks
                IOx software:
                        Catalysis 9K - x86 CPU multi-thread, docker container base application hosting
                                        Secure environment and Resource isolation from the switch. 
                                        data is auto 256K encryption
                                        use DNA center to automate
                                        120GB removal storage
                        Cisco ISR and ASR



            Application Deployment:
                only supports docker containers. Apps must be packaged as TAR files:
                    docker save iox_app -o iox_app.tar
                    app-hosting appid iox_app
                    app-vnic appGigabitEthernet trunk
                    vlan 5000 guest-interface 0
                    ip address x.x.x.x netmask x.x.x.x
                    app-default-gateway x.x.x.x guest-interface 0
                    app-resource docker
                    run-opts 1
                    
                    
                    Deploy - app-hosting install appid iox_app package flash:iperf3.tar
                    Activate - app-hosting activate appid iox_app
                    Start - app-hosting start appid iox_app
                    Stop - app-hosting stop appid iox_app
                    Deactivate - app-hosting deactivate appid iox_app
                    Uninstall - app-hosting uninstall appid iox_app
                    show app-hosting list



                    
        
   