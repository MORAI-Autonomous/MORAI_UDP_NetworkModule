[![MORAILog](./docs/MORAI_Logo.png)](https://www.morai.ai)
===
# MORAI - Network Module example (UDP)

This is an example of sending and receiving UDP data in `MORAI SIM: Drive`  
For more details, please refer to the MORAI manual.  
Link : https://help-morai-sim.scrollhelp.site/

```
├── lib                
│    ├── define          # UDP network - Protocol configure
│    └── network         # UDP network manager class│    
│
├── EgoNetwork           
│    ├── CmdControl      # Ego Vehicle Control Command
│    ├── Publisher       # UDP Protocol received from the MOARI SIM related to Ego
│    └── Subscriber      # UDP Protocol send to the MOARI SIM related to Ego
│
├── Sensor              
│
└── Etc

```

# Requirement

- python >= 3.7
