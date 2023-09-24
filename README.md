# Mongo Database Service
We had some bugs integrating Mongo directly into our Rails app, so we decided to create a Back-end API that handles all requests to the DB and returns the results from the Mongo query.
This API has 3 modules which are: user, education, and experience. Each of these modules supports a 'query' and a 'create' operation that get data from or create data in the MongoDB database. You can query this API like so:

```
GET https://tailor-mongo-back-end-c176f21f8caf.herokuapp.com/<module>/query?user-id=<USER-ID>
POST 'https://tailor-mongo-back-end-c176f21f8caf.herokuapp.com/<module>/create (with an attached JSON)
```
