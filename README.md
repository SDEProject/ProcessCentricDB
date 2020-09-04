# ProcessCentricDB
The Process Centric DB layer forwards all requests related to the internal database. 
Indeed, it forwards the HTTP requests to the Business Logic DB layer choosing the correct path. 
The path changes based on the type of the operation, such as save, retrieve and delete. 

The information about the API are available in the [Wiki page](https://github.com/SDEProject/ProcessCentricDB/wiki).

You can test Travelando project using [Travelando bot](http://t.me/TravelandoBot). 

The bot is able to understand the following sentences:

**Search**
* Select the hotels in [Trento] where you can check-in [at 14.30 o'clock].
* Get the [easiest] mountain path [without equipment required].
* Give me the position of the [bike] shops.
* Give me the list of [local traditional] shops in [Alto Adige].

**Save**
* Can you please save the [search]?
* Can you please save the [first] result?
* Save the [search]
* Save the [first] result

**Retrieve**
* Give me all [results]
* Give me the [first] result
* Give me the [hotel] result
* Give me the [first] [hotel] result
* Give me the [local traditional] shop results
* Give me the [first] [local traditional] shop result
* Give me the mountain path results with [easy] as difficulty

**Delete**
* Delete all [results]
* Delete the [first] result
* Delete the [hotel] result
* Delete the [first] [hotel] result
* Delete the [local traditional] shop results
* Delete the [first] [local traditional] shop result
* Delete the mountain path results with [easy] as difficulty
* Delete the [result] with id [1]

_Note: you can sobstitute all word in the square brackets with other values_
