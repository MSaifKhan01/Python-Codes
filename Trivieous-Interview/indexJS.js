
// 1) Promises


// function Fetch(){
//     return new Promise((res,rej)=>{
//       setTimeout(()=>{
//         // let a=987654321
//         res("succes")
  
//       },3000)
//     })
//   }
  
//   Fetch()
//   .then((res)=>{
//     console.log(res)
//   }).catch((err)=>{
//     console.log(err)
//   })


// 2) Closures

// function outerFunction() {
//   // This variable is within the scope of outerFunction
//   let outerVar = 1

//  return function inner1(){
//   // console.log(outerVar,"1")
  
//   return function inner2(){
//     outerVar++
//     console.log(outerVar,"2")
//   }
//  }
// }

// // Calling outerFunction returns closureFunction
// const createClosure = outerFunction();

// // Calling createClosure returns innerFunction
// const myClosure = createClosure();

// // Finally, calling myClosure executes innerFunction
// myClosure(); // Outputs: "I am from outerFunction"


// const t=1
// function one(){
//   let c=0
//   function Two(){
//     // t++
//     c++
//     console.log(c,t)
//   }
//   return Two()
// }

// one()


// 3)  function Currying


// Uncurried function with three arguments
// function multiply(x, y, z) {
//   return x * y * z;
// }

// Curried version of the multiply function
// function curriedMultiply(x,t) {
//   // let t=2
//   return function(y) {
//     t++
//     return function(z) {
      
//       return x * y * z*t;
//     };
//   };
// }
// console.log(curriedMultiply(2,2)(2)(4))
// Usage of the curried function
// const multiplyBy2 = curriedMultiply(2,2); // Partial application with the first argument
// const multiplyBy2And3 = multiplyBy2(3); // Partial application with the second argument
// console.log(multiplyBy2And3(4)); // Outputs: 24



// 4) .call() , .apply() , .bind()
// let obj={
//   name:"saif",
//   age:23
// }

// function one(...a){
// console.log(a)
//   console.log(`${this.name} and ${this.age} is after one year ${this.age+a}`)
// }

// one.call(obj,1)


// one.apply(obj,1)

// let res=one.bind(obj,1)
// res()


// SQL Many to Many
// Create Cutomer  Table(
//     CustomerId INT PRIMARY KEY,
//     CustomerName varchar(255)

// )

// Create Order  Table(
//     OrderId INT PRIMARY KEY,
//     CustomerId INT,

//     Foreign Key (CustomerId) References Cutomer(CustomerId)

// )


// MongoDB Many to Many

// const StudentSchema= new Scheama({
//     name:String,
//     email:String,
//     contact:String
// })

// const courseSchema= new Schema({
//     title:String,
//     description:String,
//     duration:Number
// })

// const EnrollmentSchema= new Schema({
//     students:{
//         type: Scheama.Types.objectId,
//         ref:"Students"
//     },
//     course:{
//         type: Scheama.Types.objectId,
//         ref:"Course"
//     }
// })

// Write a SQL query to retrieve all orders made by a specific customer.

// select * from orders

// inner join customers on orders.customerid=customers.customerid
// where customers.customerid=12

//dsa question reverse str with stack
function reverse2(str){
    let st=[]

    for(let i=0;i<str.length;i++){
        st.push(str[i])
    }
    let reverseStr=""

    while(st.length>0){
        reverseStr+=st.pop()
    }

    return reverseStr

}

console.log(reverse2("abcd"))


// search with mongodb query pipeline
const search=async(req,res)=>{
    try {
      let {keyword}=req.body
  
      let data= await productModel.find({
        $or:[{title:{regex:keyword,Options:"i"}},{description:{regex:keyword,options:"i"}}]
      })
  
      return res.send(data)
      
    } catch (error) {
      return res.send(error)
    }
  }


// search with sql query pipeline
router.get('/search', async (req, res) => {
    try {
      const { keyword } = req.query;
  
      // Implement search logic using SQL queries
      const query = `
        SELECT title, description
        FROM Products
        WHERE title LIKE ? OR description LIKE ?;
      `;
  
      const searchResults = await queryDatabase(query, [`%${keyword}%`, `%${keyword}%`]);
  
      res.json({ results: searchResults });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });
 

