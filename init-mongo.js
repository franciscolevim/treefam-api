db.auth('root', 'jerais1234')
db = db.getSiblingDB('family_tree')

db.createUser({
	user: 'admintf',
	pwd: 'admin1234',
	roles: [
	{
      role: 'root',
      db: 'admin',
    },
  ],
});

db.user.drop()
db.user.insertMany([
		{
			'name': 'levbono',
			'password': 'password1234',
			'email': 'levbono@mail.com'
		}
	]);