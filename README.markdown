# Naughty or Nice

This is a simple web app written in Python using Flask.  It's main
point is simply to give me a chance to play with Python (and Flask)
some.  I guess it's secondary point is fun.  The idea is that (once I
write a frontend), you'll be able to go to the site, enter a twitter
username, and then be told how 'naughty' that person has been lately
on twitter.  (Where 'naughty' will have something to do with how often
they use 'dirty' words.  Where that list is fairly arbitrary. :smile:)

The backend of the system (this portion) is responsible for routing
virtually all requests to a static html page (where a JavaScript based
frontend does most of the work).  The only real heavy lifing is at the
`/api/naughty_count/<username>' endpoint.

```sh
$ curl localhost:5000/api/naughty_count/charlietanksley
{"username": "charlietanksley", "naughty_count": 8}
$ curl localhost:5000/api/naughty_count/dhh
{"username": "dhh", "naughty_count": 4}
```

You can see I'm naughtier than [DHH](https://twitter.com/dhh).  (I
found this surprising.)
