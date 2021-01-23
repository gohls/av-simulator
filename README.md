#### Vehicle Simulator Documentation:

The vehicle simulator (vSim) serves as a testing method of the WeGo TaaS Platform. It additionally functions as a command center of the autonomous vehicles. There are 3 main feature (4 counting "exit") of the vSim. The menu options will printed to the screen at program start. From there vSim user input is reqired. Here are the options:



**1. Start TaaS Serivce** 

```
An automated process whereby any outstanding orders are sequentially initiated
```

This option will essential start the automated process of intiating orders. In more technical detail, it will intiate a process whereby it requests all vehicles that are *available* in the vehicle database on the supply side server (at this time we are only concered about *available* vehicles since those will be the vehicles to fullfill the order - however, say a emergency action is required on the non-available vehicle, it would not be difficult to implement a function that could pull all vehicle and then add functionality to override its current operation). Given this information, it will filter out which have a pending orders. Then is a sequenial order the vSim will GET a routing transcript from the supply side mapping API. It will use this routing information to run down the route in real time. This process will repeat itself, until all pending orders are carried out.



**2. Pending Orders** 

```
Prints a report of any outstanding orders
```

"Pending Orders" is essential just that. As in the "Start TaaS" option, this follow the same logic of pulling all the *available* vehicles. And of those vehicle a function will filter only the vehicle's that have a order pending. This order will then be displayed on the screen for the vSim operator to see. 



**3. Go Here** 

```
Send an autonomous vehicle "anywhere" with this command
```

"Go Here" is a clever way to test the TaaS platform, but also a useful function to send vehicles to areas as seen beneficial or necessary. In other words, it allows a vSim operator give an address, select from the *available* vehicles pull from the database, and the vehicle will go to the given location. Note, this can be used to send it to random areas and see how the vehicle performs and if there are any issues will updating its status and current location back to the supply side server. 



**4. Exit**

```
Graceful exit
```

Easy peasy lemon squeezy - it just gracefully exit the program! (keyboard interrupt should be avoided)



#### **Lastly** 

The interaction with the vSim should be straight forward. It is able to manage input mistakes by the user as well as handle errors with grace (unit tested). Overall, the functionally is kept to core features, so its easy to use while yet still valuable tool to use for testing or for the purpose of a command center/interface of autonomous vehicles. More features in the future won't be difficult to add such as rerouting. 

 

** available in this context relates to the status given in the database