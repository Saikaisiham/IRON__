console.log('test')

function updateCartCount(count) {
    console.log('Updating cart count:', count);
    document.getElementById('cart-count').textContent = count;
}


  document.addEventListener('DOMContentLoaded', function () {
      let addButtons = document.querySelectorAll('.add-to-cart-button');

      addButtons.forEach(btn => {
          btn.addEventListener('click', addToCart);
      });

      function addToCart(e) {
          e.preventDefault(); 
          let product_id = e.target.dataset.product_id;
          let url = `/add_to_cart/${product_id}/`;

          fetch(url, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': csrftoken
              }
          })
          .then(res => res.json())
          .then(data => {
              console.log(data);
              // Update the cart count based on the response
              updateCartCount(data.cart_count);
          })
          .catch(error => {
              console.error(error);
          });
      }
  });

    


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

    document.addEventListener('DOMContentLoaded', function () {
    let btns = document.querySelectorAll('.productContainer button');

    btns.forEach(btn => {
        btn.addEventListener('click', addToCart);
    });

    function addToCart(e) {
        let product_id = e.target.value;
        let url = 'http://localhost:8000/cart/add_to_cart/';

        let data = {id:product_id};

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
    }
})




      const searchInputDropdown = document.getElementById('search-input-dropdown');
      const dropdownOptions = document.querySelectorAll('.input-group-dropdown-item');
      searchInputDropdown.addEventListener('input', () => {
      const filter = searchInputDropdown.value.toLowerCase();
      showOptions();
      const valueExist = !!filter.length;
      if (valueExist) {
        dropdownOptions.forEach((el) => {
          const elText = el.textContent.trim().toLowerCase();
          const isIncluded = elText.includes(filter);
          if (!isIncluded) {
            el.style.display = 'none';
          }
        });
      }
    });

    const showOptions = () => {
      dropdownOptions.forEach((el) => {
        el.style.display = 'flex';
      });
    };