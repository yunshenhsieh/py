
var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
		printjson(cursor.next());
	}
}

var db = db.getSisterDB("eb102");

db.tmp.drop();

db.tmp.insert({_id:1,x:15});
db.tmp.insert({_id:1,x:25});


var ResultErr = db.runCommand({getLastError:1});
//if(ResultErr.err){
	printjson(ResultErr);
//}






