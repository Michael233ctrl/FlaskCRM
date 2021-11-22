const deleteBtns = document.getElementsByClassName('delete-item')

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', function () {
        const customerId = this.dataset.customer
        deleteCustomer(customerId)
    })
}

function deleteCustomer(customerId) {
    const url = '/delete-customer/' + customerId

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