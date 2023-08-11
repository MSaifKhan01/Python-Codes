const container = document.getElementById("append")
const idinp=document.getElementById('id')
const selectel=document.getElementById('selectel')
const formel=document.querySelector('form')

formel.addEventListener('submit',(e)=>{
    e.preventDefault()
    fetch(`https://zomato-postgresql-db.onrender.com/order/update/${idinp.value}`,{
        method:"PATCH",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({id:idinp.value,status:selectel.value})
    })
    .then((res)=>{
        return res.json()
    })
    .then((data)=>{
        DisplayData()
    })
    .catch((err)=>{
        console.log(err)
    })
})
function DisplayData() {
    fetch(`https://zomato-postgresql-db.onrender.com/order/get`)
        .then((res) => res.json())
        .then((data) => {
            fetchAndRender(data.data)
        })
        .catch((err) => console.log(err))
}
DisplayData()
function fetchAndRender(data) {
    container.innerHTML = ""
    data.forEach((ele) => {
        const div = document.createElement("div")
        div.classList.add("newdiv")
        let id = document.createElement("p")
        id.innerText = ` ID : ${ele.id}`
        let dishname = document.createElement('p')
        dishname.innerText = ` DISHNAME : ${ele.foodname}`
        let price = document.createElement('p')
        price.innerText = `Customername : ${ele.name}`
        let available = document.createElement('p')
        available.innerText = `Status : ${ele.status}`
        let deletebutton=document.createElement('button')
        deletebutton.innerText="Delete"
        deletebutton.addEventListener('click',()=>{
            fetch(`https://zomato-postgresql-db.onrender.com/order/delete/${ele.id}`,{
                method:"DELETE",
                headers:{
                    "Content-Type":"application/json"
                }
            
            })
            .then((res)=>{
                return res.json()
            })
            .then((data)=>{
                DisplayData()
            })
            .catch((err)=>{
                console.log(err)
            })
        })
        div.append(id, dishname, price, available,deletebutton)
        container.append(div)

    });

}