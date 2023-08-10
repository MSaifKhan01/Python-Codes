const container = document.getElementById("append")

function DisplayData() {
    fetch(`http://127.0.0.1:8000/crud/get`)
        .then((res) => res.json())
        .then((data) => {
            fetchAndRender(data.data)
        })
        .catch((err) => console.log(err))
}
DisplayData()
function fetchAndRender(data) {

    data.forEach((ele) => {
        container.innerHTML = ""
        const div = document.createElement("div")
        div.classList.add("newdiv")
        let id = document.createElement("p")
        id.innerText = ` ID : ${ele.id}`
        let dishname = document.createElement('p')
        dishname.innerText = ` DISHNAME : ${ele.dishname}`
        let price = document.createElement('p')
        price.innerText = `PRICE : ${ele.price}`
        let available = document.createElement('p')
        available.innerText = `AVAILABLITY : ${ele.available}`

        div.append(id, dishname, price, available)
        container.append(div)

    });

}