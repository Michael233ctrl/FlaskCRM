const deleteCustomer = document.querySelector('.delete-customer')
const deleteProduct = document.querySelector('.delete-product')
const deleteOrder = document.querySelector('.delete-order')

if (deleteCustomer) {
    deleteCustomer.addEventListener('click', function () {
        const customerId = this.dataset.customer
        const url = '/delete-customer/' + customerId
        deleteItem(url)
    })
}

if (deleteProduct) {
    deleteProduct.addEventListener('click', function () {
        const productId = this.dataset.product
        const url = '/delete-product/' + productId
        deleteItem(url)
    })
}

if (deleteOrder){
    deleteOrder.addEventListener('click', function () {
        console.log("clicked")
        // const orderId = this.dataset.order
        // const url = '/api/orders/' + orderId
        // deleteItem(url)
    })
}

function deleteItem(url) {
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(r => {
        return r.json();
    }).then((data) => {
        console.log('data:', data)
        window.location.href = '/'
    })
}