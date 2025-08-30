document.addEventListener('DOMContentLoaded', function() {
    // Get CSRF token function
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');
    
    // Add event listeners to all quantity buttons
    document.querySelectorAll('.increase-btn, .decrease-btn').forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            const isAdd = this.classList.contains('increase-btn');
            
            updateQuantity(itemId, isAdd);
        });
    });
    
    function updateQuantity(itemId, isAdd) {
        const url = `/cart/update-quantity/${itemId}/`;
        
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `is_add=${isAdd}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Update quantity
                document.getElementById(`quantity-${itemId}`).textContent = data.quantity;
                
                // Update subtotal
                document.getElementById(`subtotal-${itemId}`).textContent = `₹${data.sub_total}`;
                
                // Update total price
                document.getElementById('total-price').textContent = data.overall_total;
            } else if (data.status === 'removed') {
                // Remove item from DOM
                document.getElementById(`item-${itemId}`).remove();
                
                // Update total price
                document.getElementById('total-price').textContent = data.overall_total;
                
                // Check if cart is empty
                if (document.querySelectorAll('.cart-row').length === 0) {
                    window.location.reload();
                }
            } else if (data.status === 'error') {
                console.error('Error:', data.message);
                alert('An error occurred: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    }
});