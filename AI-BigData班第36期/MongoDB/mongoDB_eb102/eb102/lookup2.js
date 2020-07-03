var db = db.getSisterDB("eb102");

var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

db.lookup_product.drop();
db.lookup_color.drop();

var product1 = { "_id" : 1, "item" : "ABC1", sizes: [ "S", "M", "L"]}
var product2 = { "_id" : 2, "item" : "ABC2", sizes: [ "S", "M"] }
db.lookup_product.insert([product1,product2])

var color1 = {"_id": 1, size:"S", color: "blue"}
var color2 = {"_id": 2, size:"S", color: "red"}
var color3 = {"_id": 3, size:"M", color: "blue"}
var color4 = {"_id": 4, size:"M", color: "green"}
var color5 = {"_id": 5, size:"L", color: "black"}
db.lookup_color.insert([color1,color2,color3,color4,color5]);


var cursor = db.lookup_product.aggregate(
	[
     {$unwind: "$sizes"}
	 ,
	{
		$lookup:
        {
          from: "lookup_color",
          localField: "sizes",
          foreignField: "size",
          as: "colors"
        }
	}
	,
    {
   	  $project:{
        "_id":0,
        "colors._id":0,
        "colors.size":0
      }
    }
  ] 
)
showCursorItems(cursor);
