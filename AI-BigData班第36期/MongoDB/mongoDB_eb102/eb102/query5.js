
var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

var db = db.getSisterDB("eb102");

db.test.drop();

var user = {name:'Austin',age:30}; db.test.insert(user);
user.name = 'Zooooooo'; user.age = 25; db.test.insert(user);
user.name = 'Justin'; user.age = 29; db.test.insert(user);

user.name = 'Hopper'; user.age = 27; db.test.insert(user);
user.name = 'Alan'; user.age = 35; db.test.insert(user);
user.name = 'Lisa'; user.age = 35; db.test.insert(user);

var cursor = db.test.find();
//var cursor = db.test.find().limit(3);

// var cursor1 = db.test.find({}).limit(3).sort({age:-1});
//  print(cursor1)
// var cursor2 = db.test.find({}).sort({age:-1}).limit(3);
//  print(cursor2)


//var cursor = db.test.find({},{name:1,_id:0,age:1}).sort({name:-1,age:-1});
// var cursor = db.test.find({},{age:1,_id:0,name:1}).sort({age:-1,name:-1});

showCursorItems(cursor);
