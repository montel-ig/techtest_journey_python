# Hello again 

We need assistance! Our fancy planetary database lacks a REST-API. Let's
build one!

Start by *creating a new branch based on master*. Name the branch after
yourself, please (first name will suffice).

Feel free to use any frameworks or libraries you want as long as your 
server runs with `start_server.sh` and uses the database provided by 
`database.py`. The example here is provided with Flask. Feel free to 
extend it if you wish.

The data is planets with a list of moons under them. 
The existing API is very lacking:

```bash
curl 94.237.48.28:8000/planets
["mars", "earth", "uranus"]
```

Build a better one so that one could query the details of a single 
planet. The API should be read-only, so no need for update, delete or
create actions.

After you are satisfied, commit and push your API to your own branch. 
Our CI should deploy your changes and then you should query the details
of Uranus to continue.
