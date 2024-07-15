const plusCartButtons = document.querySelectorAll('.plus-cart');
const minusCartButtons = document.querySelectorAll('.minus-cart');
const removeCartButtons = document.querySelectorAll('.remove-cart');

// Function to handle click events for adding items to cart
function addToCart(id) {
    fetch('/pluscart', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prod_id: id }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("data = ", data);
        const eml = document.querySelector(`.plus-cart[data-pid="${id}"] + * + * + *`);
        eml.textContent = data.quantity;
        document.getElementById("amount").textContent = data.amount;
        document.getElementById("totalamount").textContent = data.totalamount;
    });
}

// Function to handle click events for removing items from cart
function removeFromCart(id) {
    fetch('/removecart', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prod_id: id }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById("amount").textContent = data.amount;
        document.getElementById("totalamount").textContent = data.totalamount;
        const emlParent = document.querySelector(`.remove-cart[data-pid="${id}"] + * + * + *`);
        emlParent.parentNode.parentNode.parentNode.parentNode.remove();
    });
}

plusCartButtons.forEach(button => {
    button.addEventListener('click', () => addToCart(button.getAttribute('data-pid')));
});

minusCartButtons.forEach(button => {
    button.addEventListener('click', () => removeFromCart(button.getAttribute('data-pid')));
});

removeCartButtons.forEach(button => {
    button.addEventListener('click', () => removeFromCart(button.getAttribute('data-pid')));
});
