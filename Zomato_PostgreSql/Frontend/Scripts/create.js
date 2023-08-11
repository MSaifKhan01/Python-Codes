const ids = document.getElementById("id")
const dishnameele = document.getElementById("DishName")
const price = document.getElementById("price")
const availablityele = document.getElementById("available")
const formele = document.querySelector("form")

formele.addEventListener("submit", (e) => {
    e.preventDefault()
    const obj = {
        id: ids.value,
        foodname: dishnameele.value,
        price: price.value,
        available: availablityele.value,
    }
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(obj)
    }
    fetch(`https://zomato-postgresql-db.onrender.com/crud/create`, options)
        .then(res => res.json())
        .then((data) => {
            console.log(data);
        })
        .catch(e => console.log(e))
})