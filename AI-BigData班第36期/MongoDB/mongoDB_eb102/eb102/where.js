db = connect("localhost:27017/eb102");

var showCursorItems = function(cursor){
    while (cursor.hasNext()) {
        printjson(cursor.next());
    }
}

db.food2.drop()

db.food2.insert({apple:6,banana:2,peach:2});

db.food2.insert({apple:5,spinach:30,watermelon:6,cccc:78, aaaaa:16})

print("---------------------------------")
cursor = db.food2.find({$where:function(){
    // print("=================================")
    for(var current in this){
        for(var other in this){
            // print(">>>>>>>------>current:"+this[current]+" other:"+this[other]);
            if(current != other && this[current] == this[other]){
                return true;
            }
        }
    }
    return false;
}});
showCursorItems(cursor);

// print("--------------------------------------")
//cursor = db.food2.find( {watermelon : {$exists:true}, $where:'this.watermelon >= 3 && this.apple > 3'} )
//cursor = db.food2.find("this.apple > 4")
//showCursorItems(cursor);

// cursor = db.food2.find({$where:function(){
//  var count = 0;
//  for(var current in this){
//      count++;
//      if(count >= 6){
//          return true;
//      }       
//  }
//  return false;
// }});
// showCursorItems(cursor);


// cursor = db.food2.find({$where:function(){
//  var sum = 0;
//  for(var current in this){
//      //print("current:"+current)
//      if(current != '_id'){
//          sum = sum + this[current];
//          if(sum > 40){
//              return true;
//          }
//      }   
//  }
//  return false;
// }});
// showCursorItems(cursor);