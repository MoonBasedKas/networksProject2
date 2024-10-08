Difficulties
-----
A massive difficulty I had when working on this project was 
getting multiple sockets to connect to a singular server. The main 
reason is because we need to create a new port for each connection.
Afterwards if we try reading each socket we need the packets to arrive 
in order of sockets. However, using select.select() we can fix this 
the major error I ran into was I had my socket array and address array 
set with the wrong variable names so I was trying to use select.select()
on my addresses rather than my sockets. After that I needed to add in a 
timeout as it would never stop waiting. Afterwards it was fine.