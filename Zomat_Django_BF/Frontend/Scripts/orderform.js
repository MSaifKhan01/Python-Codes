const idinp=document.getElementById('id')
const foodinp=document.getElementById('food')
const nameinp=document.getElementById('customer')
const formel=document.querySelector('form')

formel.addEventListener("submit", (e) => {
    e.preventDefault()
    const obj = {
        id: idinp.value,
        food:foodinp.value,
        customername:nameinp.value,
        status:"pending"    
    }
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(obj)
    }
    fetch(`https://test-app-3ece.onrender.com/order/create`, options)
        .then(res => res.json())
        .then((data) => {
            console.log(data);
        })
        .catch(e => console.log(e))
})