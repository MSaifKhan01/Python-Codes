const idinp=document.getElementById('id')
const foodinp=document.getElementById('food')
const nameinp=document.getElementById('customer')
const formel=document.querySelector('form')

formel.addEventListener("submit", (e) => {
    e.preventDefault()
    const obj = {
        id: idinp.value,
        foodname:foodinp.value,
        name:nameinp.value,
        status:"pending"    
    }
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(obj)
    }
    fetch(`https://zomato-postgresql-db.onrender.com/order/create`, options)
        .then(res => res.json())
        .then((data) => {
            console.log(data);
        })
        .catch(e => console.log(e))
})